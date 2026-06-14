"""Always-on crawl-health summary for the Qosmic crawler.

Every crawl writes `artifacts/<run_id>/summary.md`. When a site is blocked,
partially broken, or otherwise degraded, this file states the issues in plain
language so a person reading the reports knows the crawler hit problems on that
site — even when no full audit can be produced.
"""

from pathlib import Path


# Verdict thresholds
_BLOCKED_RATIO = 0.30      # >30% pages blocked/errored -> Blocked
_HEALTHY_OK_RATIO = 0.80   # <80% pages ok -> Degraded


def _count(results: list[dict], status: str) -> int:
    return sum(1 for r in results if r.get("status") == status)


def is_non_ecommerce(journey: dict, crawled_results: list[dict]) -> bool:
    """True when pages load but there is no real retail purchase surface.

    Single source of truth for the "this isn't a store" decision, shared by the
    health verdict and by the technical-check gating in crawl_store (so a SaaS
    site's guessed /cart probe is never counted as a broken link, and brand or
    processor names in page copy are never counted as accepted payment methods).
    """
    outcome = journey.get("outcome", "unknown")
    flags = journey.get("friction_flags", [])
    payments = journey.get("payment_methods_detected", [])
    product_ok = any(r.get("status") == "ok" and r.get("page_type") == "product_page"
                     for r in crawled_results)
    no_payments = not payments
    # Pages classified as "product" but neither add-to-cart nor checkout works and
    # there is no real payment coverage → not a real store (e.g. a SaaS /products/).
    fake_commerce = ("add_to_cart_failed" in flags and "checkout_load_failed" in flags
                     and len(payments) <= 1)
    return (outcome == "no_product_found") or (not product_ok and no_payments) or fake_commerce


def compute_health(discovered: dict, checks: dict, journey: dict,
                   crawled_results: list[dict]) -> tuple[str, list[str]]:
    """Return (verdict, issues). verdict is Healthy / Degraded / Blocked."""
    selected = discovered.get("selected_pages", [])
    selected_count = max(1, len(selected))

    ok = _count(crawled_results, "ok")
    blocked = _count(crawled_results, "blocked")
    soft404 = _count(crawled_results, "soft_404")
    errored = _count(crawled_results, "error")

    homepage_ok = any(
        r.get("page_type") == "homepage" and r.get("status") == "ok"
        for r in crawled_results
    )

    issues: list[str] = []

    # --- blocked-level signals ---
    homepage_down = not homepage_ok and any(
        r.get("page_type") == "homepage" for r in crawled_results
    )
    blocked_ratio = (blocked + errored) / selected_count
    is_blocked = homepage_down or blocked_ratio > _BLOCKED_RATIO

    if homepage_down:
        issues.append("Homepage could not be crawled — the site may be down or bot-protected.")
    if blocked > 0:
        issues.append(f"{blocked}/{selected_count} pages were blocked by bot protection.")
    if errored > 0:
        issues.append(f"{errored}/{selected_count} pages returned an HTTP error (4xx/5xx).")
    if soft404 > 0:
        issues.append(f"{soft404}/{selected_count} selected pages were branded 404s "
                      f"(returned 'page not found' despite a 200 status).")
    if ok < selected_count * _HEALTHY_OK_RATIO:
        issues.append(f"Only {ok}/{selected_count} pages loaded cleanly.")

    # --- journey signals ---
    outcome = journey.get("outcome", "unknown")
    friction = journey.get("friction_score", 5.0)
    flags = journey.get("friction_flags", [])
    if outcome in ("error", "no_product_found"):
        issues.append(f"Shopping journey could not complete (outcome: {outcome}).")
    elif outcome == "retailer_routed":
        issues.append("Store is retailer-routed — no direct cart/checkout path to test.")
    if "add_to_cart_failed" in flags:
        issues.append("Add-to-cart could not be verified (cart remained empty).")
    if "api_add_to_cart_fallback" in flags:
        issues.append(
            "Customer-facing add-to-cart was not verified; the journey required an API fallback.")
    if "checkout_load_failed" in flags or "cart_load_failed" in flags:
        issues.append("Cart or checkout entry was not reachable.")
    if not journey.get("payment_methods_detected"):
        issues.append("No payment methods were detected.")

    # --- technical Fail signals ---
    fails = [c.get("label", k) for k, c in checks.items()
             if isinstance(c, dict) and c.get("status") == "Fail"]
    for label in fails:
        issues.append(f"Technical check failed: {label}.")

    # --- non-ecommerce detection ---
    # Pages load fine, but there is no retail purchase surface to audit. This is
    # distinct from Blocked (can't crawl) — the site simply isn't a store.
    no_commerce = is_non_ecommerce(journey, crawled_results)

    # --- verdict ---
    if homepage_down or (is_blocked and not (homepage_ok and no_commerce)):
        verdict = "Blocked"
    elif homepage_ok and no_commerce:
        verdict = "Non-ecommerce"
        issues.insert(0, "No retail purchase surface found — no product catalog with a "
                         "working add-to-cart/checkout flow. This does not appear to be a "
                         "retail ecommerce store (it may still be a SaaS or product site).")
    elif issues:
        verdict = "Degraded"
    else:
        verdict = "Healthy"

    return verdict, issues


def write_crawl_summary(run_dir: Path, discovered: dict, checks: dict,
                        journey: dict, crawled_results: list[dict]) -> str:
    """Write artifacts/<run_id>/summary.md. Returns the verdict."""
    verdict, issues = compute_health(discovered, checks, journey, crawled_results)

    selected = discovered.get("selected_pages", [])
    selected_count = len(selected)
    ok = _count(crawled_results, "ok")
    blocked = _count(crawled_results, "blocked")
    soft404 = _count(crawled_results, "soft_404")
    errored = _count(crawled_results, "error")

    banner = {
        "Healthy": "✅ Healthy — full audit can be produced.",
        "Degraded": "⚠️ Degraded — an audit can be produced but some evidence is missing or unreliable.",
        "Blocked": "⛔ Blocked — the site could not be crawled; no full audit is possible.",
        "Non-ecommerce": "🛈 Non-ecommerce — pages load but no retail purchase/checkout surface was found; a storefront CRO audit does not apply (the site may still be a SaaS or product site).",
    }[verdict]

    lines = [
        f"# Crawl Summary — {run_dir.name}",
        "",
        f"**Crawl health: {verdict}**",
        "",
        banner,
        "",
        f"- Base URL: {discovered.get('base_url', '')}",
        f"- Pages selected: {selected_count}",
        f"- Pages loaded cleanly (ok): {ok}",
        f"- Blocked (bot protection): {blocked}",
        f"- Branded 404 (soft-404): {soft404}",
        f"- HTTP errors: {errored}",
        "",
    ]

    # Per-page problems
    problem_rows = [r for r in crawled_results
                    if r.get("status") in ("blocked", "soft_404", "error")]
    if problem_rows:
        lines += ["## Pages with problems", "",
                  "| URL | Status | Reason |", "|---|---|---|"]
        for r in problem_rows:
            # Collapse multi-line reasons (e.g. Playwright call logs) to one cell.
            reason = " ".join(str(r.get("reason", "")).split())[:80]
            lines.append(f"| {r.get('url','')} | {r.get('status','')} | {reason} |")
        lines.append("")

    # Journey
    lines += [
        "## Shopping journey",
        "",
        f"- Outcome: {journey.get('outcome', 'unknown')}",
        f"- Friction score: {journey.get('friction_score', 'n/a')}/5",
        f"- Friction flags: {', '.join(journey.get('friction_flags', [])) or 'none'}",
        f"- Payment methods: {', '.join(journey.get('payment_methods_detected', [])) or 'none detected'}",
        "",
    ]

    # Technical Fail/Warn
    fails = [(k, c) for k, c in checks.items()
             if isinstance(c, dict) and c.get("status") == "Fail"]
    warns = [(k, c) for k, c in checks.items()
             if isinstance(c, dict) and c.get("status") == "Warn"]
    if fails or warns:
        lines += ["## Technical issues", ""]
        for _, c in fails:
            lines.append(f"- **Fail** — {c.get('label')}: {c.get('detail')}")
        for _, c in warns:
            lines.append(f"- Warn — {c.get('label')}: {c.get('detail')}")
        lines.append("")

    # The headline: issues a reader should know
    lines += ["## Issues a reader should know", ""]
    if issues:
        for issue in issues:
            lines.append(f"- {issue}")
    else:
        lines.append("- None. The crawl was clean and a full audit can be trusted.")
    lines.append("")

    summary_path = run_dir / "summary.md"
    summary_path.write_text("\n".join(lines), encoding="utf-8")
    return verdict
