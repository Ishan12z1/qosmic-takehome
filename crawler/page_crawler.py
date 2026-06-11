"""Browser-based page crawling for the Qosmic crawler."""

import asyncio
import json
from pathlib import Path

from bs4 import BeautifulSoup
from markdownify import markdownify as md
from playwright.async_api import BrowserContext, Page
from playwright_stealth import Stealth

from .utils import safe_name, is_valid_page, extract_page_metadata
from .technical_checks import update_from_html

_stealth = Stealth()

# Shared user agent
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
        await page.goto(url, wait_until="domcontentloaded", timeout=35000)
        await asyncio.sleep(2)
        try:
            await page.wait_for_load_state("networkidle", timeout=8000)
        except Exception:
            pass

        html = await page.content()
        title = await page.title()
        body_text = await page.evaluate(
            "() => document.body ? document.body.innerText : ''"
        )

        valid, reason = is_valid_page(title, body_text)
        if not valid:
            print(f"    [BLOCKED] ({reason})")
            return {"url": url, "page_type": page_type, "status": "blocked", "reason": reason}

        await page.screenshot(path=str(screenshot_path), full_page=True, timeout=15000)
        html_path.write_text(html, encoding="utf-8")
        md_path.write_text(md(html, strip=["script", "style"]), encoding="utf-8")

        soup = BeautifulSoup(html, "lxml")
        metadata = extract_page_metadata(soup, url, page_type)
        json_path.write_text(
            json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8"
        )

        if page_type == "homepage":
            update_from_html(
                checks, soup,
                f"artifacts/{run_dir.name}/screenshots/{name}.png",
                html,
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


async def crawl_page(
    context: BrowserContext,
    url: str,
    page_type: str,
    index: int,
    run_dir: Path,
    checks: dict,
) -> dict:
    """Crawl a single page. Returns result dict."""
    name = safe_name(url, page_type, index)
    screenshot_path = run_dir / "screenshots" / f"{name}.png"
    html_path = run_dir / "pages" / f"{name}.html"
    md_path = run_dir / "pages" / f"{name}.md"
    json_path = run_dir / "pages" / f"{name}.json"

    print(f"  [{page_type}] {url}")

    page = await context.new_page()
    try:
        await page.goto(url, wait_until="domcontentloaded", timeout=35000)
        # Allow JS to settle
        await asyncio.sleep(2)

        # Second wait if page is still loading
        try:
            await page.wait_for_load_state("networkidle", timeout=8000)
        except Exception:
            pass

        html = await page.content()
        title = await page.title()
        body_text = await page.evaluate(
            "() => document.body ? document.body.innerText : ''"
        )

        # Sanity check
        valid, reason = is_valid_page(title, body_text)
        if not valid:
            print(f"    [BLOCKED] ({reason})")
            await page.close()
            return {"url": url, "page_type": page_type, "status": "blocked", "reason": reason}

        # Save artifacts
        await page.screenshot(path=str(screenshot_path), full_page=True, timeout=15000)
        html_path.write_text(html, encoding="utf-8")
        md_path.write_text(
            md(html, strip=["script", "style"]), encoding="utf-8"
        )

        soup = BeautifulSoup(html, "lxml")
        metadata = extract_page_metadata(soup, url, page_type)
        json_path.write_text(
            json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8"
        )

        # Update technical checks from homepage HTML
        if page_type == "homepage":
            update_from_html(
                checks, soup,
                f"artifacts/{run_dir.name}/screenshots/{name}.png",
                html,
            )

        print(f"    [OK] saved {name}")
        await page.close()
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
        try:
            await page.close()
        except Exception:
            pass
        return {"url": url, "page_type": page_type, "status": "error", "reason": str(e)[:120]}


async def crawl_all_pages(
    browser,
    selected_pages: list[dict],
    run_dir: Path,
    checks: dict,
) -> list[dict]:
    """Crawl all selected pages using a single page object to maintain CF session."""
    context = await make_stealth_context(browser)
    # Use ONE page object for all navigations — Cloudflare cookies persist
    page = await context.new_page()
    results = []

    # Step 1: warm up on homepage first to establish cf_clearance cookie
    homepage = next((p for p in selected_pages if p["page_type"] == "homepage"), None)
    if homepage:
        result = await _crawl_with_page(
            page, homepage["url"], homepage["page_type"], 0, run_dir, checks
        )
        results.append(result)
        # Give Cloudflare JS challenge time to complete and set cookies
        await asyncio.sleep(3)

    # Step 2: crawl remaining pages on the same page/session
    for i, entry in enumerate(selected_pages):
        if entry["page_type"] == "homepage":
            continue
        result = await _crawl_with_page(
            page, entry["url"], entry["page_type"], i, run_dir, checks
        )
        results.append(result)
        await asyncio.sleep(1.5)  # human-like pacing between pages

    await context.close()
    return results


async def discover_and_crawl(
    browser,
    base_url: str,
    selected_pages_fn,  # callable(urls, base_url) -> (selected, rejected)
    run_dir: Path,
    checks: dict,
) -> tuple[list[dict], list[dict], list[dict]]:
    """
    Single-context session: discover URLs then crawl pages.
    Returns (crawled_results, selected_pages, rejected_pages).
    Keeps one browser context alive throughout so CF cookies persist.
    """
    from urllib.parse import urlparse, urljoin
    from bs4 import BeautifulSoup

    parsed = urlparse(base_url)
    origin = f"https://{parsed.netloc}"

    context = await make_stealth_context(browser)
    page = await context.new_page()
    links: set[str] = set()

    # ------------------------------------------------------------------
    # Phase A: Homepage — single load, extract links + save artifact
    # ------------------------------------------------------------------
    print("  Loading homepage...")
    homepage_result = None
    try:
        await page.goto(origin + "/", wait_until="domcontentloaded", timeout=35000)
        await asyncio.sleep(3)  # let CF JS settle

        # Extract all nav links from rendered page (no further navigations)
        hrefs = await page.eval_on_selector_all("a[href]", "els => els.map(e => e.href)")
        for href in hrefs:
            clean = href.split("?")[0].split("#")[0]
            if parsed.netloc in clean:
                links.add(clean)

        # Save homepage artifacts now (avoid loading it again later)
        html = await page.content()
        title = await page.title()
        body_text = await page.evaluate("() => document.body ? document.body.innerText : ''")
        valid, reason = is_valid_page(title, body_text)

        if valid:
            name = "homepage_0_home"
            (run_dir / "screenshots" / f"{name}.png").parent.mkdir(parents=True, exist_ok=True)
            await page.screenshot(path=str(run_dir / "screenshots" / f"{name}.png"),
                                  full_page=True, timeout=15000)
            (run_dir / "pages" / f"{name}.html").write_text(html, encoding="utf-8")
            (run_dir / "pages" / f"{name}.md").write_text(
                md(html, strip=["script", "style"]), encoding="utf-8")
            soup = BeautifulSoup(html, "lxml")
            metadata = extract_page_metadata(soup, origin + "/", "homepage")
            (run_dir / "pages" / f"{name}.json").write_text(
                json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8")
            update_from_html(checks, soup, f"artifacts/{run_dir.name}/screenshots/{name}.png", html)
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
            homepage_result = {"url": origin + "/", "page_type": "homepage",
                               "status": "blocked", "reason": reason}

    except Exception as e:
        print(f"  [WARN] Homepage error: {str(e)[:80]}")

    # Standard Shopify paths (always include)
    for path in ["/", "/cart", "/collections", "/collections/all",
                 "/pages/about", "/pages/faq", "/pages/shipping",
                 "/pages/returns", "/pages/where-to-buy", "/blogs/news"]:
        links.add(urljoin(origin, path))

    all_urls = list(links)
    print(f"  Found {len(all_urls)} URLs")

    # Page selection
    selected_pages, rejected_pages = selected_pages_fn(all_urls, base_url)
    print(f"  Selected {len(selected_pages)} pages")
    for entry in selected_pages:
        print(f"    [{entry['page_type']}] {entry['url']}")

    # ------------------------------------------------------------------
    # Phase B: Crawl remaining pages (skip homepage — already done)
    # ------------------------------------------------------------------
    print("\nCrawling remaining pages...")
    results = []
    if homepage_result:
        results.append(homepage_result)

    for i, entry in enumerate(selected_pages):
        if entry["page_type"] == "homepage":
            continue  # already crawled above
        result = await _crawl_with_page(
            page, entry["url"], entry["page_type"], i, run_dir, checks
        )
        results.append(result)
        await asyncio.sleep(2.0)  # human-like pacing

    await context.close()
    return results, selected_pages, rejected_pages
