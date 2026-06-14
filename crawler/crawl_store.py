#!/usr/bin/env python3
"""
crawl_store.py — Qosmic Audit Harness entry point

Usage:
    python -m crawler.crawl_store <url>          # reuses newest usable crawl
    python -m crawler.crawl_store <url> --force  # creates a fresh crawl

Output: artifacts/<slug>_<YYYYMMDD>_<uuid>/
"""

import argparse
import asyncio
import json
import os
import sys
from datetime import datetime
from pathlib import Path

from playwright.async_api import async_playwright

from .url_discovery import select_pages, _path_key
from .technical_checks import (
    build_initial_checks, check_broken_links, finalize_critical_pages, finalize_html_checks)
from .page_crawler import discover_and_crawl, check_mobile_and_speed
from .shopping_journey import run_shopping_journey
from .crawl_summary import write_crawl_summary, is_non_ecommerce
from .utils import derive_slug, generate_run_id, find_existing_run, make_run_dirs


ARTIFACTS_ROOT = Path(__file__).parent.parent / "artifacts"


def homepage_loaded_cleanly(crawled_results: list[dict]) -> bool:
    return any(
        result.get("page_type") == "homepage" and result.get("status") == "ok"
        for result in crawled_results
    )


async def run_crawl(url: str, force: bool) -> str:
    if not url.startswith("http"):
        url = "https://" + url

    slug = derive_slug(url)
    ARTIFACTS_ROOT.mkdir(exist_ok=True)

    # Retry safety: reuse existing complete run unless --force
    if not force:
        existing = find_existing_run(slug, ARTIFACTS_ROOT)
        if existing:
            summary = (ARTIFACTS_ROOT / existing / "summary.md").read_text(
                encoding="utf-8", errors="replace")
            verdict = next(
                (line.split(":", 1)[1].strip(" *") for line in summary.splitlines()
                 if "Crawl health:" in line),
                "Unknown",
            )
            print(f"[OK] Existing complete run found: {existing} ({verdict})"
                  "  (use --force to re-crawl)")
            return existing

    run_id = generate_run_id(slug)
    run_dir = ARTIFACTS_ROOT / run_id
    make_run_dirs(run_dir)

    print(f"\n{'='*60}")
    print(f"Qosmic Audit Crawler")
    print(f"URL:    {url}")
    print(f"Run ID: {run_id}")
    print(f"{'='*60}\n")

    # ------------------------------------------------------------------
    # Technical checks (requests-based, fast)
    # ------------------------------------------------------------------
    print("Running technical checks...")
    checks = build_initial_checks(url)

    # ------------------------------------------------------------------
    # Browser session: discovery + crawl in one persistent context
    # ------------------------------------------------------------------
    print("\nStarting browser session...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        crawled_results, selected_pages, rejected_pages, guessed_links = await discover_and_crawl(
            browser, url, select_pages, run_dir, checks
        )

        # Save discovered_links (run_id written here for orchestrator)
        discovered = {
            "run_id": run_id,
            "base_url": url,
            "slug": slug,
            "crawled_at": datetime.now().isoformat(),
            "total_discovered": len(selected_pages) + len(rejected_pages),
            "selected_pages": selected_pages,
            "rejected_pages": rejected_pages[:50],
            "blocked_pages": [
                {"url": r["url"], "reason": r.get("reason")}
                for r in crawled_results if r.get("status") == "blocked"
            ],
        }
        _save_json(run_dir / "discovered_links.json", discovered)

        # Shopping journey (separate browser context, fresh session after main crawl)
        journey = await run_shopping_journey(browser, url, selected_pages, run_dir, checks)

        if homepage_loaded_cleanly(crawled_results):
            print("\nMeasuring mobile-friendliness + page speed...")
            try:
                speed_checks = await check_mobile_and_speed(browser, url)
                checks.update(speed_checks)
            except Exception as e:
                print(f"  [WARN] Mobile/speed measurement failed: {str(e)[:80]}")
        else:
            print("\nSkipping mobile/speed measurement: homepage did not load cleanly.")

        await browser.close()

    # ------------------------------------------------------------------
    # Post-crawl checks
    # ------------------------------------------------------------------
    rejected_samples = [
        page["url"] for page in rejected_pages
        if not page.get("reason", "").startswith((
            "optional_guessed_path_unavailable", "fallback_failed"))
    ][:30]
    all_sample_urls = [p["url"] for p in selected_pages] + rejected_samples

    # On a non-store, guessed standard Shopify probe paths (/cart, /collections/all)
    # 404 because the site never had them — that is not a real broken link. Only
    # count guessed probes as defects on a confirmed retail store. Links the site
    # actually publishes (sitemap/nav) are still checked everywhere.
    non_ecommerce = is_non_ecommerce(journey, crawled_results)
    if non_ecommerce:
        guessed_keys = {_path_key(u) for u in guessed_links}
        all_sample_urls = [u for u in all_sample_urls if _path_key(u) not in guessed_keys]
    checks["broken_links"] = check_broken_links(all_sample_urls)
    finalize_critical_pages(checks, crawled_results, len(selected_pages))
    finalize_html_checks(checks)

    # Payment methods are only meaningful on a real purchase surface. On a non-store,
    # brand/processor names in marketing copy (e.g. "Visa", "Klarna", "Stripe") must
    # not become an accepted-payment "Pass". Reset to an honest Warn.
    if non_ecommerce:
        checks["payment_methods"] = {
            "label": "Payment Methods",
            "status": "Warn",
            "detail": "No retail checkout surface detected; accepted payment methods were "
                      "not assessed. Brand or processor names in page copy are not treated "
                      "as accepted payments.",
            "evidence": None,
        }

    # ------------------------------------------------------------------
    # Save final artifacts
    # ------------------------------------------------------------------
    _save_json(run_dir / "technical_checks.json", checks)
    _save_json(run_dir / "discovered_links.json", discovered)
    _save_json(run_dir / "pages" / "shopping_journey.json", journey)

    # Always-on crawl-health summary (states issues for broken/blocked sites)
    health_verdict = write_crawl_summary(run_dir, discovered, checks, journey, crawled_results)

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    ok = sum(1 for r in crawled_results if r.get("status") == "ok")
    blocked = sum(1 for r in crawled_results if r.get("status") == "blocked")
    pm = ", ".join(journey.get("payment_methods_detected", [])) or "none detected"

    print(f"\n{'='*60}")
    print(f"Crawl complete")
    print(f"  run_id:          {run_id}")
    print(f"  Pages crawled:   {ok}/{len(selected_pages)}")
    print(f"  Pages blocked:   {blocked}")
    print(f"  Journey:         {journey['outcome']} (friction {journey['friction_score']}/5)")
    print(f"  Payment methods: {pm}")
    print(f"  Crawl health:    {health_verdict}")
    print(f"  Artifacts:       artifacts/{run_id}/  (see summary.md)")
    print(f"{'='*60}")
    print(f"\nNext: /audit {url}  or  python evals/run_eval.py {run_id}")

    return run_id


def _save_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Qosmic Audit Harness Crawler")
    parser.add_argument("url", help="Shopify store URL to crawl")
    parser.add_argument("--force", action="store_true", help="Create a fresh crawl")
    args = parser.parse_args()

    run_id = asyncio.run(run_crawl(args.url, args.force))
    print(run_id)

    # Playwright's node driver can leave non-daemon threads / subprocess transports
    # alive after asyncio.run() returns, which hangs interpreter shutdown on Windows
    # (observed on rei.com / vercel.com). All artifacts are already flushed to disk
    # above, so force a clean, deterministic exit instead of hanging on teardown.
    sys.stdout.flush()
    sys.stderr.flush()
    os._exit(0)
