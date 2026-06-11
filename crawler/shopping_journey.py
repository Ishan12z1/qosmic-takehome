"""Shopping journey simulation for the Qosmic crawler."""

import asyncio
from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from .page_crawler import make_stealth_context
from .utils import detect_payment_methods, is_valid_page

FRICTION_DEDUCTIONS = {
    "add_to_cart_failed": 2.0,
    "cart_load_failed": 1.0,
    "checkout_load_failed": 1.0,
    "popup_blocked_flow": 1.0,
    "no_guest_checkout": 0.5,
    "no_payment_methods": 0.5,
}

RETAILER_SIGNALS = [
    "find a retailer", "find a store", "where to buy", "buy in store",
    "find near me", "store locator", "available at",
]

ADD_TO_CART_SELECTORS = [
    "[name='add']",
    "button[type='submit'].product-form__submit",
    ".product-form__submit",
    "[data-testid='add-to-cart']",
    "button:has-text('Add to cart')",
    "button:has-text('Add to Cart')",
    "button:has-text('ADD TO CART')",
    "button:has-text('Add To Cart')",
    "input[type='submit'][value*='cart' i]",
    "input[type='submit'][value*='Cart' i]",
]

_EMPTY_OBSERVATIONS = {
    "click_count_to_checkout": 0,
    "trust_badges_at_checkout": False,
    "cart_upsell_present": False,
    "urgency_elements_present": False,
    "error_messages_detected": False,
}


def _score_from_flags(flags: list[str]) -> float:
    score = 5.0
    for flag in flags:
        score -= FRICTION_DEDUCTIONS.get(flag, 0)
    return max(1.0, round(score, 1))


def _detail_from_flags(score: float, flags: list[str]) -> str:
    if not flags:
        return f"Score {score}/5 - no blockers detected"
    notes = [f"{f.replace('_', ' ')} (-{FRICTION_DEDUCTIONS.get(f, 0)})" for f in flags]
    return f"Score {score}/5 - " + ", ".join(notes)


async def _try_add_to_cart(page) -> bool:
    """Attempt add-to-cart using all known selectors. Returns True on success."""
    for selector in ADD_TO_CART_SELECTORS:
        try:
            btn = page.locator(selector).first
            if await btn.is_visible(timeout=2000):
                await btn.click(timeout=5000)
                await asyncio.sleep(2)
                print(f"  [OK] Add-to-cart via: {selector}")
                return True
        except Exception:
            continue
    return False


async def run_shopping_journey(
    browser,
    base_url: str,
    selected_pages: list[dict],
    run_dir: Path,
    checks: dict,
) -> dict:
    """Run the shopping journey and return journey dict."""
    print("\n--- Shopping Journey ---")

    parsed = urlparse(base_url)
    origin = f"https://{parsed.netloc}"

    journey = {
        "outcome": "unknown",
        "retailer_routed": False,
        "friction_score": 5.0,
        "friction_flags": [],
        "friction_detail": "Score 5.0/5 - journey not attempted",
        "journey_observations": dict(_EMPTY_OBSERVATIONS),
        "payment_methods_detected": [],
    }

    # Collect all product pages (try up to 3 for add-to-cart)
    pdp_entries = [p for p in selected_pages if p["page_type"] == "product_page"]
    if not pdp_entries:
        print("  No product page found - skipping journey")
        journey["outcome"] = "no_product_found"
        journey["friction_score"] = 1.0
        journey["friction_flags"] = ["no_product_found"]
        checks["shopping_journey"] = {
            "label": "Shopping Journey", "status": "Warn",
            "detail": "No product page found to start journey.", "evidence": "",
        }
        return journey

    context = await make_stealth_context(browser)
    page = await context.new_page()
    friction_flags = []
    click_count = 0
    payment_methods: list[str] = []

    try:
        # ------------------------------------------------------------------
        # Step 1 + 2: Try PDPs until add-to-cart succeeds
        # ------------------------------------------------------------------
        atc_success = False
        pdp_url = pdp_entries[0]["url"]  # default for screenshot/retailer check

        for pdp_entry in pdp_entries:
            pdp_url = pdp_entry["url"]
            print(f"  -> PDP: {pdp_url}")
            await page.goto(pdp_url, wait_until="domcontentloaded", timeout=30000)
            await asyncio.sleep(2)
            click_count += 1

            pdp_html = await page.content()
            body_text = await page.evaluate("() => document.body ? document.body.innerText : ''")
            lower_text = body_text.lower()

            if not payment_methods:
                payment_methods = detect_payment_methods(pdp_html)

            # Check for retailer routing on first PDP
            if pdp_entry == pdp_entries[0]:
                retailer_detected = (
                    any(sig in lower_text for sig in RETAILER_SIGNALS)
                    and "add to cart" not in lower_text
                    and "add to bag" not in lower_text
                )
                if retailer_detected:
                    print("  [RETAILER-ROUTED] No direct cart path found")
                    await page.screenshot(
                        path=str(run_dir / "screenshots" / "shopping_journey_retailer.png"),
                        full_page=False, timeout=10000,
                    )
                    journey.update({
                        "outcome": "retailer_routed",
                        "retailer_routed": True,
                        "friction_score": 2.0,
                        "friction_flags": ["retailer_routed"],
                        "friction_detail": "Score 2.0/5 - retailer-routed store, no direct purchase path",
                        "payment_methods_detected": payment_methods,
                    })
                    checks["checkout_reachable"] = {
                        "label": "Checkout Reachable", "status": "Warn",
                        "detail": "Retailer-routed store - no direct cart/checkout path.",
                        "evidence": f"artifacts/{run_dir.name}/screenshots/shopping_journey_retailer.png",
                    }
                    checks["shopping_journey"] = {
                        "label": "Shopping Journey", "status": "Warn",
                        "detail": "Retailer-routed. Score 2.0/5.",
                        "evidence": f"artifacts/{run_dir.name}/screenshots/shopping_journey_retailer.png",
                    }
                    _update_payment_check(checks, payment_methods, run_dir)
                    await context.close()
                    return journey

            # Screenshot PDP (first successful one)
            if not atc_success:
                await page.screenshot(
                    path=str(run_dir / "screenshots" / "shopping_journey_pdp.png"),
                    full_page=False, timeout=10000,
                )

            print("  -> Add to cart...")
            atc_success = await _try_add_to_cart(page)
            if atc_success:
                break
            else:
                print(f"  [WARN] Add-to-cart failed on {pdp_url} - trying next PDP")

        if not atc_success:
            friction_flags.append("add_to_cart_failed")
            print("  [FAIL] Add-to-cart failed on all PDPs")

        # ------------------------------------------------------------------
        # Step 3: Cart
        # ------------------------------------------------------------------
        print(f"  -> Cart: {origin}/cart")
        await page.goto(f"{origin}/cart", wait_until="domcontentloaded", timeout=20000)
        await asyncio.sleep(1.5)
        click_count += 1

        cart_html = await page.content()
        cart_title = await page.title()
        cart_body = await page.evaluate("() => document.body ? document.body.innerText : ''")
        cart_lower = cart_body.lower()

        cart_ok = not ("404" in cart_title or "page not found" in cart_lower)
        if not cart_ok:
            friction_flags.append("cart_load_failed")
            print("  [FAIL] Cart page returned 404 or not found")
            checks["checkout_reachable"] = {
                "label": "Checkout Reachable", "status": "Fail",
                "detail": "/cart returned 404 or no usable cart page.",
                "evidence": f"artifacts/{run_dir.name}/screenshots/shopping_journey_cart.png",
            }
        else:
            print("  [OK] Cart loaded")
            journey["journey_observations"]["cart_upsell_present"] = any(
                kw in cart_lower for kw in
                ["you might also", "frequently bought", "complete the look", "add on", "bundle"]
            )
            journey["journey_observations"]["urgency_elements_present"] = any(
                kw in cart_lower for kw in
                ["limited", "only", "left in stock", "selling fast", "hurry", "low stock"]
            )
            journey["journey_observations"]["error_messages_detected"] = any(
                kw in cart_lower for kw in ["error", "sorry", "unavailable", "out of stock"]
            )
            if not payment_methods:
                payment_methods = detect_payment_methods(cart_html)

        await page.screenshot(
            path=str(run_dir / "screenshots" / "shopping_journey_cart.png"),
            full_page=True, timeout=10000,
        )

        # ------------------------------------------------------------------
        # Step 4: Checkout entry (STOP here - never fill forms)
        # ------------------------------------------------------------------
        print(f"  -> Checkout entry: {origin}/checkout")
        try:
            await page.goto(f"{origin}/checkout", wait_until="domcontentloaded", timeout=20000)
            await asyncio.sleep(1.5)
            click_count += 1

            checkout_html = await page.content()
            checkout_body = await page.evaluate("() => document.body ? document.body.innerText : ''")
            checkout_lower = checkout_body.lower()

            if "404" in checkout_lower or "page not found" in checkout_lower:
                friction_flags.append("checkout_load_failed")
                print("  [FAIL] Checkout entry returned 404")
            else:
                print("  [OK] Checkout entry reached - STOPPING here (no form filling)")

                has_guest = any(kw in checkout_lower for kw in
                                ["guest", "continue as guest", "continue without account", "email"])
                if not has_guest:
                    friction_flags.append("no_guest_checkout")

                journey["journey_observations"]["trust_badges_at_checkout"] = any(
                    kw in checkout_lower for kw in
                    ["secure", "ssl", "encrypted", "safe", "protected", "guarantee", "256"]
                )

                if not payment_methods:
                    payment_methods = detect_payment_methods(checkout_html)

                if "cart_load_failed" not in friction_flags and "checkout_load_failed" not in friction_flags:
                    checks["checkout_reachable"] = {
                        "label": "Checkout Reachable", "status": "Pass",
                        "detail": "Cart loaded and checkout entry reached. Journey stopped before payment entry.",
                        "evidence": f"artifacts/{run_dir.name}/screenshots/shopping_journey_checkout.png",
                    }

            await page.screenshot(
                path=str(run_dir / "screenshots" / "shopping_journey_checkout.png"),
                full_page=False, timeout=10000,
            )

        except Exception as e:
            friction_flags.append("checkout_load_failed")
            print(f"  [FAIL] Checkout navigation: {str(e)[:80]}")

        # ------------------------------------------------------------------
        # Finalize
        # ------------------------------------------------------------------
        if not payment_methods:
            friction_flags.append("no_payment_methods")

        journey["payment_methods_detected"] = payment_methods
        journey["journey_observations"]["click_count_to_checkout"] = click_count

        score = _score_from_flags(friction_flags)
        journey["friction_score"] = score
        journey["friction_flags"] = friction_flags
        journey["friction_detail"] = _detail_from_flags(score, friction_flags)
        journey["outcome"] = "full_journey" if not friction_flags else "partial_journey"

        status = "Pass" if score >= 4.0 else ("Warn" if score >= 2.5 else "Fail")
        pm_str = ", ".join(payment_methods) if payment_methods else "none detected"
        checks["shopping_journey"] = {
            "label": "Shopping Journey",
            "status": status,
            "detail": f"{journey['friction_detail']}. Payment: {pm_str}.",
            "evidence": f"artifacts/{run_dir.name}/screenshots/shopping_journey_cart.png",
        }
        _update_payment_check(checks, payment_methods, run_dir)

    except Exception as e:
        print(f"  [FAIL] Journey error: {str(e)[:120]}")
        journey["outcome"] = "error"
        journey["friction_flags"] = ["journey_error"]
        journey["friction_score"] = 1.0
    finally:
        try:
            await context.close()
        except Exception:
            pass

    return journey


def _update_payment_check(checks: dict, payment_methods: list[str], run_dir: Path) -> None:
    pm_str = ", ".join(payment_methods) if payment_methods else "none detected"
    screenshot = f"artifacts/{run_dir.name}/screenshots/shopping_journey_cart.png"
    checks["payment_methods"] = {
        "label": "Payment Methods",
        "status": "Pass" if payment_methods else "Warn",
        "detail": f"Detected: {pm_str}." if payment_methods else "No payment method icons detected.",
        "evidence": screenshot,
    }
