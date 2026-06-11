#!/usr/bin/env python3
"""
crawl_store.py — Qosmic Audit Harness entry point

Usage:
    python crawler/crawl_store.py <url>          # skips completed artifacts
    python crawler/crawl_store.py <url> --force  # overwrites everything

Output: artifacts/<slug>_<YYYYMMDD>_<uuid>/
"""

import argparse
import asyncio
import json
import sys
from datetime import datetime
from pathlib import Path

from playwright.async_api import async_playwright

from .url_discovery import select_pages
from .technical_checks import build_initial_checks, check_broken_links, finalize_critical_pages
from .page_crawler import discover_and_crawl
from .shopping_journey import run_shopping_journey
from .utils import derive_slug, generate_run_id, find_existing_run, make_run_dirs


ARTIFACTS_ROOT = Path(__file__).parent.parent / "artifacts"


async def run_crawl(url: str, force: bool) -> str:
    if not url.startswith("http"):
        url = "https://" + url

    slug = derive_slug(url)
    ARTIFACTS_ROOT.mkdir(exist_ok=True)

    # Retry safety: reuse existing complete run unless --force
    if not force:
        existing = find_existing_run(slug, ARTIFACTS_ROOT)
        if existing:
            print(f"[OK] Existing run found: {existing}  (use --force to re-crawl)")
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

        crawled_results, selected_pages, rejected_pages = await discover_and_crawl(
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

        await browser.close()

    # ------------------------------------------------------------------
    # Post-crawl checks
    # ------------------------------------------------------------------
    all_sample_urls = [p["url"] for p in selected_pages] + [p["url"] for p in rejected_pages[:30]]
    checks["broken_links"] = check_broken_links(all_sample_urls)
    finalize_critical_pages(checks, crawled_results, len(selected_pages))

    # ------------------------------------------------------------------
    # Save final artifacts
    # ------------------------------------------------------------------
    _save_json(run_dir / "technical_checks.json", checks)
    _save_json(run_dir / "discovered_links.json", discovered)
    _save_json(run_dir / "pages" / "shopping_journey.json", journey)

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
    print(f"  Artifacts:       artifacts/{run_id}/")
    print(f"{'='*60}")
    print(f"\nNext: /audit {url}  or  python evals/run_eval.py {run_id}")

    return run_id


def _save_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Qosmic Audit Harness Crawler")
    parser.add_argument("url", help="Shopify store URL to crawl")
    parser.add_argument("--force", action="store_true", help="Overwrite existing artifacts")
    args = parser.parse_args()

    run_id = asyncio.run(run_crawl(args.url, args.force))
    print(run_id)
