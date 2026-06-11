"""Deterministic technical checks (requests-based, no browser) for the Qosmic crawler."""

import json
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

from .utils import detect_payment_methods

_SESSION = requests.Session()
_SESSION.headers.update({"User-Agent": "Mozilla/5.0 (compatible; QosmicAuditBot/1.0)"})


def _warn(label: str, detail: str, evidence=None) -> dict:
    return {"label": label, "status": "Warn", "detail": detail, "evidence": evidence}


def _pass(label: str, detail: str, evidence=None) -> dict:
    return {"label": label, "status": "Pass", "detail": detail, "evidence": evidence}


def _fail(label: str, detail: str, evidence=None) -> dict:
    return {"label": label, "status": "Fail", "detail": detail, "evidence": evidence}


# ---------------------------------------------------------------------------
# Individual checks
# ---------------------------------------------------------------------------

def check_ssl(netloc: str) -> dict:
    try:
        r = _SESSION.get(f"https://{netloc}", timeout=10, allow_redirects=True)
        return _pass("SSL Certificate", "HTTPS storefront loaded successfully.", f"https://{netloc}")
    except Exception as e:
        return _fail("SSL Certificate", f"HTTPS failed: {str(e)[:80]}")


def check_https_redirect(netloc: str) -> dict:
    try:
        r = _SESSION.get(f"http://{netloc}", timeout=10, allow_redirects=True)
        if r.url.startswith("https://"):
            return _pass("HTTPS Redirect", "HTTP redirected to HTTPS.", f"http://{netloc}")
        return _fail("HTTPS Redirect", "HTTP did not redirect to HTTPS.", f"http://{netloc}")
    except Exception as e:
        return _warn("HTTPS Redirect", f"Could not verify redirect: {str(e)[:80]}")


def check_sitemap(netloc: str) -> dict:
    url = f"https://{netloc}/sitemap.xml"
    try:
        r = _SESSION.get(url, timeout=10)
        if r.status_code == 200 and ("<urlset" in r.text or "<sitemapindex" in r.text):
            count = r.text.count("<loc>")
            return _pass("Sitemap", f"sitemap.xml found with ~{count} entries.", url)
        return _warn("Sitemap", f"sitemap.xml returned status {r.status_code}.", url)
    except Exception:
        return _warn("Sitemap", "sitemap.xml could not be fetched.")


def check_robots(netloc: str) -> dict:
    url = f"https://{netloc}/robots.txt"
    try:
        r = _SESSION.get(url, timeout=10)
        if r.status_code == 200:
            return _pass("Robots.txt", "robots.txt accessible.", url)
        return _warn("Robots.txt", f"robots.txt returned status {r.status_code}.", url)
    except Exception:
        return _warn("Robots.txt", "robots.txt could not be fetched.")


def check_broken_links(urls: list[str]) -> dict:
    sample = urls[:40]
    broken = []
    critical_paths = ["/cart", "/checkout", "/collections", "/products"]
    critical_broken = []

    for url in sample:
        try:
            r = _SESSION.head(url, timeout=8, allow_redirects=True)
            if r.status_code >= 400:
                broken.append({"url": url, "status": r.status_code})
                path = urlparse(url).path
                if any(cp in path for cp in critical_paths):
                    critical_broken.append(url)
        except Exception:
            pass

    if critical_broken:
        return _fail("Broken Links",
                     f"{len(broken)} broken links found. Critical: {', '.join(critical_broken[:3])}")
    if broken:
        return _warn("Broken Links",
                     f"{len(broken)} non-critical broken links in {len(sample)} sampled.")
    return _pass("Broken Links", f"No broken links in {len(sample)} sampled links.")


# ---------------------------------------------------------------------------
# HTML-based checks (run after browser crawl)
# ---------------------------------------------------------------------------

def update_from_html(checks: dict, soup: BeautifulSoup,
                     screenshot_path: str, page_html: str) -> None:
    """Update browser-dependent checks from a crawled page's soup + HTML."""

    # Meta tags & social previews
    title = soup.find("title")
    meta_desc = soup.find("meta", attrs={"name": "description"})
    og_title = soup.find("meta", property="og:title")
    if title and meta_desc:
        checks["meta_tags_social"] = _pass(
            "Meta Tags & Social Previews",
            "Title and meta description found." + (" OG tags present." if og_title else " OG tags missing."),
            screenshot_path,
        )
    elif title:
        checks["meta_tags_social"] = _warn(
            "Meta Tags & Social Previews",
            "Title found but meta description missing.",
            screenshot_path,
        )

    # Structured data
    ld_scripts = soup.find_all("script", type="application/ld+json")
    if ld_scripts:
        types_found = []
        for block in ld_scripts:
            try:
                data = json.loads(block.string or "{}")
                t = data.get("@type", "")
                if t:
                    types_found.append(t)
            except Exception:
                pass
        checks["structured_data"] = _pass(
            "Structured Data",
            f"JSON-LD found: {', '.join(types_found[:5]) or 'present'}.",
            screenshot_path,
        )

    # Favicon
    favicon = (soup.find("link", rel="icon") or
               soup.find("link", rel="shortcut icon") or
               soup.find("link", rel=lambda v: v and "icon" in (v if isinstance(v, str) else " ".join(v))))
    if favicon:
        checks["favicon"] = _pass("Favicon", "Favicon link tag found.", screenshot_path)

    # Cookie / Privacy
    text = soup.get_text(separator=" ", strip=True).lower()
    has_privacy = "privacy" in text
    has_terms = "terms" in text
    has_cookie = "cookie" in text
    if has_privacy and has_terms:
        checks["cookie_privacy"] = (
            _pass("Cookie/Privacy",
                  "Privacy Policy and Terms links found. Cookie policy also present." if has_cookie
                  else "Privacy Policy and Terms found. Cookie policy not detected.",
                  screenshot_path)
            if has_cookie else
            _warn("Cookie/Privacy",
                  "Privacy and Terms found but cookie consent policy not detected.",
                  screenshot_path)
        )

    # Image optimization
    imgs = soup.find_all("img")
    if imgs:
        missing_alt = sum(1 for img in imgs if not img.get("alt"))
        alt_pct = int(missing_alt / len(imgs) * 100)
        checks["image_optimization"] = _warn(
            "Image Optimization",
            f"{missing_alt}/{len(imgs)} images missing alt text ({alt_pct}%). Byte-level audit not run.",
            screenshot_path,
        )

    # Payment methods from HTML
    methods = detect_payment_methods(page_html)
    if methods:
        checks["payment_methods"] = _pass(
            "Payment Methods",
            f"Detected: {', '.join(methods)}.",
            screenshot_path,
        )


# ---------------------------------------------------------------------------
# Build initial checks dict (all set to Warn until browser data arrives)
# ---------------------------------------------------------------------------

def build_initial_checks(base_url: str) -> dict:
    parsed = urlparse(base_url)
    netloc = parsed.netloc

    checks: dict = {}

    print("  SSL certificate...")
    checks["ssl_certificate"] = check_ssl(netloc)

    print("  HTTPS redirect...")
    checks["https_redirect"] = check_https_redirect(netloc)

    print("  Sitemap...")
    checks["sitemap"] = check_sitemap(netloc)

    print("  Robots.txt...")
    checks["robots_txt"] = check_robots(netloc)

    # Browser-dependent checks — initialized as Warn
    browser_checks = {
        "critical_pages_loading": "Critical Pages Loading",
        "meta_tags_social": "Meta Tags & Social Previews",
        "structured_data": "Structured Data",
        "favicon": "Favicon",
        "mobile_friendly": "Mobile-Friendly",
        "page_speed_mobile": "Page Speed Mobile",
        "page_speed_desktop": "Page Speed Desktop",
        "broken_links": "Broken Links",
        "image_optimization": "Image Optimization",
        "cookie_privacy": "Cookie/Privacy",
        "checkout_reachable": "Checkout Reachable",
        "payment_methods": "Payment Methods",
        "shopping_journey": "Shopping Journey",
    }

    details = {
        "mobile_friendly": "Desktop-only audit. Mobile viewport not tested.",
        "page_speed_mobile": "No Lighthouse run performed.",
        "page_speed_desktop": "No Lighthouse run performed.",
    }

    for key, label in browser_checks.items():
        checks[key] = _warn(label, details.get(key, "Updated after browser crawl."))

    return checks


def finalize_critical_pages(checks: dict, crawled_results: list[dict],
                              selected_count: int) -> None:
    ok = sum(1 for r in crawled_results if r.get("status") == "ok")
    blocked = sum(1 for r in crawled_results if r.get("status") == "blocked")

    if ok >= selected_count * 0.8:
        first_ok = next((r["screenshot"] for r in crawled_results if r.get("status") == "ok"), None)
        checks["critical_pages_loading"] = _pass(
            "Critical Pages Loading",
            f"{ok}/{selected_count} selected pages loaded successfully.",
            first_ok,
        )
    elif blocked > selected_count * 0.3:
        checks["critical_pages_loading"] = _warn(
            "Critical Pages Loading",
            f"{blocked}/{selected_count} pages blocked by bot protection.",
        )
    else:
        checks["critical_pages_loading"] = _warn(
            "Critical Pages Loading",
            f"{ok}/{selected_count} pages loaded. {blocked} blocked.",
        )
