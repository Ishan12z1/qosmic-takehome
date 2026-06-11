"""Browser-based page crawling for the Qosmic crawler."""

import asyncio
import json
from pathlib import Path
from urllib.parse import urlparse, urljoin

from bs4 import BeautifulSoup
from markdownify import markdownify as md
from playwright.async_api import BrowserContext, Page
from playwright_stealth import Stealth

from .utils import safe_name, is_valid_page, extract_page_metadata
from .technical_checks import update_from_html

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
    clean = base_netloc.lower().lstrip("www.")
    url_netloc = urlparse(url).netloc.lower()
    return url_netloc == clean or url_netloc == "www." + clean


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


async def discover_and_crawl(
    browser,
    base_url: str,
    selected_pages_fn,
    run_dir: Path,
    checks: dict,
) -> tuple[list[dict], list[dict], list[dict]]:
    """
    Single-context session: discover URLs then crawl pages.
    Returns (crawled_results, selected_pages, rejected_pages).
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
        await page.goto(origin + "/", wait_until="domcontentloaded", timeout=35000)
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
                f"artifacts/{run_dir.name}/screenshots/{name}.png", html,
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

    # Add standard Shopify paths
    for path in ["/", "/cart", "/collections", "/collections/all",
                 "/pages/about", "/pages/faq", "/pages/shipping",
                 "/pages/returns", "/pages/where-to-buy", "/blogs/news"]:
        links.add(urljoin(origin, path))

    all_urls = list(links)
    print(f"  Found {len(all_urls)} URLs")

    selected_pages, rejected_pages = selected_pages_fn(all_urls, base_url)
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

    for i, entry in enumerate(selected_pages):
        if entry["page_type"] == "homepage":
            continue
        result = await _crawl_with_page(
            page, entry["url"], entry["page_type"], i, run_dir, checks
        )
        results.append(result)
        await asyncio.sleep(2.0)

    await context.close()
    return results, selected_pages, rejected_pages
