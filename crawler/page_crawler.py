"""Browser-based page crawling for the Qosmic crawler."""

import asyncio
import json
from pathlib import Path
from urllib.parse import urlparse, urljoin

from bs4 import BeautifulSoup
from markdownify import markdownify as md
from playwright.async_api import BrowserContext, Page
from playwright_stealth import Stealth

from .utils import (
    safe_name, is_valid_page, is_soft_404, extract_page_metadata, normalize_host)
from .technical_checks import update_from_html, _pass, _warn, _fail
from .url_discovery import discover_urls

_stealth = Stealth()

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)


async def make_stealth_context(browser, viewport: dict | None = None) -> BrowserContext:
    """Create a new browser context with stealth applied."""
    ctx = await browser.new_context(
        viewport=viewport or {"width": 1280, "height": 900},
        user_agent=USER_AGENT,
        locale="en-US",
        timezone_id="America/New_York",
        extra_http_headers={
            "Accept-Language": "en-US,en;q=0.9",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        },
    )
    await _stealth.apply_stealth_async(ctx)
    return ctx


def _is_same_store(url: str, base_netloc: str) -> bool:
    """True if url belongs to same store (exact domain or www. prefix only)."""
    if not url.startswith("http"):
        return False
    return normalize_host(urlparse(url).netloc) == normalize_host(base_netloc)


async def _crawl_with_page(
    page,
    url: str,
    page_type: str,
    index: int,
    run_dir: Path,
    checks: dict,
) -> dict:
    """Crawl using an existing page object (session/cookies preserved)."""
    name = safe_name(url, page_type, index)
    screenshot_path = run_dir / "screenshots" / f"{name}.png"
    html_path = run_dir / "pages" / f"{name}.html"
    md_path = run_dir / "pages" / f"{name}.md"
    json_path = run_dir / "pages" / f"{name}.json"

    print(f"  [{page_type}] {url}")

    try:
        response = await page.goto(url, wait_until="domcontentloaded", timeout=35000)
        await asyncio.sleep(2)
        try:
            await page.wait_for_load_state("networkidle", timeout=8000)
        except Exception:
            pass

        # Hard HTTP failure — do not treat as a loaded page
        http_status = response.status if response else None
        if http_status in {401, 403, 429}:
            print(f"    [BLOCKED] HTTP {http_status}")
            return {"url": url, "page_type": page_type,
                    "status": "blocked", "reason": f"http_{http_status}"}
        if http_status is not None and http_status >= 400:
            print(f"    [HTTP {http_status}] not loaded")
            return {"url": url, "page_type": page_type,
                    "status": "error", "reason": f"http_{http_status}"}

        html = await page.content()
        title = await page.title()
        body_text = await page.evaluate(
            "() => document.body ? document.body.innerText : ''"
        )

        valid, reason = is_valid_page(title, body_text)
        # One retry for JS-heavy pages that need extra render time
        if not valid and reason == "body_too_short":
            await asyncio.sleep(3)
            body_text = await page.evaluate(
                "() => document.body ? document.body.innerText : ''"
            )
            html = await page.content()
            valid, reason = is_valid_page(title, body_text)

        if not valid:
            print(f"    [BLOCKED] ({reason})")
            return {"url": url, "page_type": page_type, "status": "blocked", "reason": reason}

        # Soft-404: HTTP 200 but a branded "page not found" (e.g. canonical → /404)
        canonical = await page.evaluate(
            "() => { const l = document.querySelector('link[rel=canonical]');"
            " return l ? l.href : ''; }"
        )
        if is_soft_404(title, canonical, body_text):
            print(f"    [SOFT-404] {url}")
            return {"url": url, "page_type": page_type,
                    "status": "soft_404", "reason": "soft_404", "title": title}

        await page.screenshot(path=str(screenshot_path), full_page=True, timeout=15000)
        html_path.write_text(html, encoding="utf-8")
        md_path.write_text(md(html, strip=["script", "style"]), encoding="utf-8")

        soup = BeautifulSoup(html, "lxml")
        metadata = extract_page_metadata(soup, url, page_type)
        json_path.write_text(
            json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8"
        )

        update_from_html(
            checks, soup,
            f"artifacts/{run_dir.name}/screenshots/{name}.png",
            html, page_type,
        )

        print(f"    [OK] {name}")
        return {
            "url": url,
            "page_type": page_type,
            "name": name,
            "status": "ok",
            "screenshot": f"artifacts/{run_dir.name}/screenshots/{name}.png",
            "html": f"artifacts/{run_dir.name}/pages/{name}.html",
            "markdown": f"artifacts/{run_dir.name}/pages/{name}.md",
            "json": f"artifacts/{run_dir.name}/pages/{name}.json",
            "title": title,
        }
    except Exception as e:
        print(f"    [FAIL] {str(e)[:100]}")
        return {"url": url, "page_type": page_type, "status": "error", "reason": str(e)[:120]}


async def discover_and_crawl(
    browser,
    base_url: str,
    selected_pages_fn,
    run_dir: Path,
    checks: dict,
) -> tuple[list[dict], list[dict], list[dict], set[str]]:
    """
    Single-context session: discover URLs then crawl pages.
    Returns (crawled_results, selected_pages, rejected_pages, guessed_links).

    guessed_links is the set of *probed* standard Shopify paths (e.g. /cart,
    /collections/all) — URLs the crawler invented to test, not links the site
    actually publishes. Callers use it to avoid counting a 404 on a guessed
    probe as a real broken link on a non-store.
    """
    parsed = urlparse(base_url)
    origin = f"https://{parsed.netloc}"
    base_netloc = parsed.netloc.lower()

    context = await make_stealth_context(browser)
    page = await context.new_page()
    links: set[str] = set()

    # ------------------------------------------------------------------
    # Phase A: Homepage - single load, extract links + save artifact
    # ------------------------------------------------------------------
    print("  Loading homepage...")
    homepage_result = None
    try:
        hp_response = await page.goto(origin + "/", wait_until="domcontentloaded", timeout=35000)
        await asyncio.sleep(3)

        # Extract nav links - strict same-store filter (no subdomains)
        hrefs = await page.eval_on_selector_all("a[href]", "els => els.map(e => e.href)")
        for href in hrefs:
            if not href.startswith("http"):
                continue
            clean = href.split("?")[0].split("#")[0]
            if _is_same_store(clean, base_netloc):
                links.add(clean)

        html = await page.content()
        title = await page.title()
        body_text = await page.evaluate("() => document.body ? document.body.innerText : ''")

        valid, reason = is_valid_page(title, body_text)
        # Retry once for JS-heavy homepages
        if not valid and reason == "body_too_short":
            await asyncio.sleep(3)
            body_text = await page.evaluate("() => document.body ? document.body.innerText : ''")
            html = await page.content()
            valid, reason = is_valid_page(title, body_text)

        # Hard HTTP failure or branded 404 on the homepage = site is unusable
        hp_status = hp_response.status if hp_response else None
        if valid and hp_status in {401, 403, 429}:
            valid, reason = False, f"http_{hp_status}"
        if valid and hp_status is not None and hp_status >= 400:
            valid, reason = False, f"http_{hp_status}"
        if valid:
            hp_canonical = await page.evaluate(
                "() => { const l = document.querySelector('link[rel=canonical]');"
                " return l ? l.href : ''; }"
            )
            if is_soft_404(title, hp_canonical, body_text):
                valid, reason = False, "soft_404"

        if valid:
            name = "homepage_0_home"
            (run_dir / "screenshots" / f"{name}.png").parent.mkdir(parents=True, exist_ok=True)
            await page.screenshot(
                path=str(run_dir / "screenshots" / f"{name}.png"),
                full_page=True, timeout=15000,
            )
            (run_dir / "pages" / f"{name}.html").write_text(html, encoding="utf-8")
            (run_dir / "pages" / f"{name}.md").write_text(
                md(html, strip=["script", "style"]), encoding="utf-8"
            )
            soup = BeautifulSoup(html, "lxml")
            metadata = extract_page_metadata(soup, origin + "/", "homepage")
            (run_dir / "pages" / f"{name}.json").write_text(
                json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8"
            )
            update_from_html(
                checks, soup,
                f"artifacts/{run_dir.name}/screenshots/{name}.png", html, "homepage",
            )
            homepage_result = {
                "url": origin + "/", "page_type": "homepage", "name": name,
                "status": "ok",
                "screenshot": f"artifacts/{run_dir.name}/screenshots/{name}.png",
                "html": f"artifacts/{run_dir.name}/pages/{name}.html",
                "markdown": f"artifacts/{run_dir.name}/pages/{name}.md",
                "json": f"artifacts/{run_dir.name}/pages/{name}.json",
                "title": title,
            }
            print(f"    [OK] homepage saved")
        else:
            print(f"    [BLOCKED] homepage ({reason})")
            homepage_result = {
                "url": origin + "/", "page_type": "homepage",
                "status": "blocked", "reason": reason,
            }

    except Exception as e:
        print(f"  [WARN] Homepage error: {str(e)[:80]}")
        homepage_result = {
            "url": origin + "/", "page_type": "homepage",
            "status": "error", "reason": str(e)[:120],
        }

    # Homepage-linked URLs are the representative/featured surfaces — keep them
    # separate so product/collection selection can prioritise them.
    nav_links = set(links)

    # Union in sitemap/homepage-discovered URLs before adding guessed standard
    # paths so selection can prioritize observed links over guesses.
    try:
        for u in discover_urls(base_url):
            links.add(u)
    except Exception as e:
        print(f"  [WARN] Sitemap discovery failed: {str(e)[:60]}")

    guessed_links = {
        urljoin(origin, path)
        for path in ["/", "/cart", "/collections", "/collections/all",
                     "/pages/about", "/pages/faq", "/pages/shipping",
                     "/pages/returns", "/pages/where-to-buy", "/blogs/news"]
    }
    links.update(guessed_links)

    all_urls = list(links)
    print(f"  Found {len(all_urls)} URLs")

    selected_pages, rejected_pages = selected_pages_fn(
        all_urls, base_url, nav_links, guessed_links)
    print(f"  Selected {len(selected_pages)} pages")
    for entry in selected_pages:
        print(f"    [{entry['page_type']}] {entry['url']}")

    # ------------------------------------------------------------------
    # Phase B: Crawl remaining pages (homepage already saved above)
    # ------------------------------------------------------------------
    print("\nCrawling remaining pages...")
    results = []
    if homepage_result:
        results.append(homepage_result)

    fallback_by_type: dict[str, list[dict]] = {}
    for rejected in rejected_pages:
        fallback_by_type.setdefault(rejected["page_type"], []).append(rejected)
    dropped_indices: list[int] = []
    optional_guessed_types = {
        "where_to_buy", "faq_shipping_returns", "about_page", "blog_or_content_page",
    }

    for i, entry in enumerate(list(selected_pages)):
        if entry["page_type"] == "homepage":
            continue
        result = await _crawl_with_page(
            page, entry["url"], entry["page_type"], i, run_dir, checks
        )

        # A guessed or stale URL should not consume the page-type quota when a
        # discovered same-type candidate is available.
        if result.get("status") != "ok":
            fallbacks = fallback_by_type.get(entry["page_type"], [])
            while fallbacks:
                fallback = fallbacks.pop(0)
                if fallback in rejected_pages:
                    rejected_pages.remove(fallback)
                fallback_result = await _crawl_with_page(
                    page, fallback["url"], fallback["page_type"], i, run_dir, checks
                )
                await asyncio.sleep(1.0)
                if fallback_result.get("status") == "ok":
                    rejected_pages.append({
                        **entry,
                        "reason": f"selected_page_failed:{result.get('reason', result.get('status'))}",
                    })
                    selected_pages[i] = {
                        "url": fallback["url"],
                        "page_type": fallback["page_type"],
                    }
                    result = fallback_result
                    break
                rejected_pages.append({
                    "url": fallback["url"],
                    "page_type": fallback["page_type"],
                    "reason": f"fallback_failed:{fallback_result.get('reason', fallback_result.get('status'))}",
                })

        if (
            result.get("status") != "ok"
            and entry["url"] in guessed_links
            and entry["page_type"] in optional_guessed_types
        ):
            rejected_pages.append({
                **entry,
                "reason": f"optional_guessed_path_unavailable:{result.get('reason', result.get('status'))}",
            })
            dropped_indices.append(i)
            print("    [SKIP] Optional guessed path unavailable; excluded from crawl health")
            continue

        results.append(result)
        await asyncio.sleep(2.0)

    for index in reversed(dropped_indices):
        del selected_pages[index]

    await context.close()
    return results, selected_pages, rejected_pages, guessed_links


# ---------------------------------------------------------------------------
# Real mobile-friendly + page-speed checks (replace hardcoded Warns)
# ---------------------------------------------------------------------------

_NAV_TIMING_JS = """() => {
  const n = performance.getEntriesByType('navigation')[0];
  if (!n) return null;
  return {
    dcl: Math.round(n.domContentLoadedEventEnd),
    load: Math.round(n.loadEventEnd),
    resp: Math.round(n.responseEnd)
  };
}"""

_MOBILE_LAYOUT_JS = """() => {
  const vp = document.querySelector('meta[name=viewport]');
  return {
    hasViewport: !!vp,
    scrollWidth: document.documentElement.scrollWidth,
    innerWidth: window.innerWidth
  };
}"""


def _speed_status(load_ms: int, dcl_ms: int) -> tuple[str, int]:
    """Map a load time to Pass/Warn/Fail. Falls back to DCL if load is 0."""
    metric = load_ms if load_ms and load_ms > 0 else dcl_ms
    if metric <= 0:
        return "Warn", metric
    if metric < 2500:
        return "Pass", metric
    if metric < 5000:
        return "Warn", metric
    return "Fail", metric


async def _measure(page, url: str) -> dict | None:
    try:
        await page.goto(url, wait_until="load", timeout=30000)
    except Exception:
        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=30000)
        except Exception:
            return None
    await asyncio.sleep(1)
    try:
        return await page.evaluate(_NAV_TIMING_JS)
    except Exception:
        return None


async def check_mobile_and_speed(browser, base_url: str) -> dict:
    """Run a genuine (single-run) mobile-friendly check and page-speed proxy.

    Page speed is navigation timing from one load — explicitly NOT Lighthouse —
    but it is measured, not hardcoded. Returns a dict of the three checks.
    """
    parsed = urlparse(base_url)
    origin = f"https://{parsed.netloc}"
    out: dict = {}

    # Desktop speed
    desk_ctx = await make_stealth_context(browser, viewport={"width": 1280, "height": 900})
    try:
        dpage = await desk_ctx.new_page()
        desk = await _measure(dpage, origin + "/")
    finally:
        await desk_ctx.close()

    if desk:
        status, metric = _speed_status(desk.get("load", 0), desk.get("dcl", 0))
        out["page_speed_desktop"] = {"label": "Page Speed Desktop", "status": status,
            "detail": f"Navigation timing (single run, not Lighthouse): load {metric}ms, "
                      f"DCL {desk.get('dcl', 0)}ms.", "evidence": origin + "/"}
    else:
        out["page_speed_desktop"] = _warn("Page Speed Desktop",
            "Navigation timing unavailable for desktop load.")

    # Mobile speed + layout
    mob_ctx = await make_stealth_context(browser, viewport={"width": 375, "height": 812})
    try:
        mpage = await mob_ctx.new_page()
        mob = await _measure(mpage, origin + "/")
        try:
            layout = await mpage.evaluate(_MOBILE_LAYOUT_JS)
        except Exception:
            layout = None
    finally:
        await mob_ctx.close()

    if mob:
        status, metric = _speed_status(mob.get("load", 0), mob.get("dcl", 0))
        out["page_speed_mobile"] = {"label": "Page Speed Mobile", "status": status,
            "detail": f"Navigation timing (single run, not Lighthouse): load {metric}ms, "
                      f"DCL {mob.get('dcl', 0)}ms at 375px viewport.", "evidence": origin + "/"}
    else:
        out["page_speed_mobile"] = _warn("Page Speed Mobile",
            "Navigation timing unavailable for mobile load.")

    if layout:
        has_vp = layout.get("hasViewport")
        overflow = layout.get("scrollWidth", 0) - layout.get("innerWidth", 0)
        if not has_vp:
            out["mobile_friendly"] = _fail("Mobile-Friendly",
                "No <meta name=viewport> tag — page will not adapt to mobile screens.",
                origin + "/")
        elif overflow > 4:
            out["mobile_friendly"] = _warn("Mobile-Friendly",
                f"Viewport meta present but content overflows {overflow}px horizontally "
                f"at 375px (scrollWidth {layout.get('scrollWidth')}px).", origin + "/")
        else:
            out["mobile_friendly"] = _pass("Mobile-Friendly",
                "Viewport meta present and no horizontal overflow at 375px.", origin + "/")
    else:
        out["mobile_friendly"] = _warn("Mobile-Friendly",
            "Could not evaluate mobile layout.")

    return out
