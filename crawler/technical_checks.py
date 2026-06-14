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
    inaccessible = []
    critical_paths = ["/cart", "/checkout", "/collections", "/products"]
    critical_broken = []

    for url in sample:
        try:
            r = _SESSION.head(url, timeout=8, allow_redirects=True)
            if r.status_code == 405:
                r = _SESSION.get(url, timeout=8, allow_redirects=True, stream=True)
            if r.status_code in {401, 403, 429}:
                inaccessible.append({"url": url, "status": r.status_code})
                continue
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
    if inaccessible:
        return _warn(
            "Broken Links",
            f"No broken links confirmed; {len(inaccessible)}/{len(sample)} sampled links "
            "could not be verified because the server returned 401/403/429.",
        )
    return _pass("Broken Links", f"No broken links in {len(sample)} sampled links.")


# ---------------------------------------------------------------------------
# HTML-based checks (run after browser crawl)
# ---------------------------------------------------------------------------

def update_from_html(checks: dict, soup: BeautifulSoup,
                     screenshot_path: str, page_html: str,
                     page_type: str = "other") -> None:
    """Accumulate per-page HTML signals into checks["_html_accum"].

    Called for EVERY crawled page (not just the homepage). The aggregate
    Pass/Warn/Fail statuses are computed later by finalize_html_checks, so
    sitewide claims (e.g. image alt-text coverage, OG-tag coverage) reflect all
    crawled pages rather than the homepage alone.
    """
    accum = checks.setdefault("_html_accum", [])

    title = soup.find("title")
    meta_desc = soup.find("meta", attrs={"name": "description"})
    og_title = soup.find("meta", property="og:title")

    ld_types = []
    for block in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(block.string or "{}")
            t = data.get("@type", "")
            if isinstance(t, list):
                ld_types.extend(str(x) for x in t)
            elif t:
                ld_types.append(str(t))
        except Exception:
            pass

    favicon = (soup.find("link", rel="icon") or
               soup.find("link", rel="shortcut icon") or
               soup.find("link", rel=lambda v: v and "icon" in (v if isinstance(v, str) else " ".join(v))))

    text = soup.get_text(separator=" ", strip=True).lower()
    imgs = soup.find_all("img")
    missing_alt = sum(1 for img in imgs if not img.get("alt"))

    accum.append({
        "screenshot": screenshot_path,
        "page_type": page_type,
        "has_title": bool(title),
        "has_meta_desc": bool(meta_desc),
        "has_og": bool(og_title),
        "ld_types": ld_types,
        "has_favicon": bool(favicon),
        "has_privacy": "privacy" in text,
        "has_terms": "terms" in text,
        "has_cookie": "cookie" in text,
        "img_total": len(imgs),
        "img_missing_alt": missing_alt,
    })

    # Payment methods from HTML — fallback only; the shopping journey owns the
    # authoritative payment_methods check and overwrites this later.
    methods = detect_payment_methods(page_html)
    if methods and checks.get("payment_methods", {}).get("status") != "Pass":
        checks["payment_methods"] = _pass(
            "Payment Methods",
            f"Detected: {', '.join(methods)}.",
            screenshot_path,
        )


def finalize_html_checks(checks: dict) -> None:
    """Compute aggregate HTML-based checks from accumulated per-page signals."""
    accum = checks.pop("_html_accum", [])
    if not accum:
        return

    n = len(accum)
    first_shot = accum[0]["screenshot"]

    # Meta tags & social previews — coverage across all crawled pages
    titled = sum(1 for a in accum if a["has_title"])
    described = sum(1 for a in accum if a["has_meta_desc"])
    og_missing = sum(1 for a in accum if not a["has_og"])
    if titled == n and described == n and og_missing == 0:
        checks["meta_tags_social"] = _pass(
            "Meta Tags & Social Previews",
            f"Title, meta description, and OG tags present on all {n} crawled pages.",
            first_shot)
    elif titled or described:
        og_note = (" OG tags present on all pages."
                   if og_missing == 0 else f" OG tags missing on {og_missing}/{n} pages.")
        checks["meta_tags_social"] = _warn(
            "Meta Tags & Social Previews",
            f"Title+meta description present on {min(titled, described)}/{n} pages." + og_note,
            first_shot)
    else:
        checks["meta_tags_social"] = _warn(
            "Meta Tags & Social Previews",
            f"No title or meta description detected across {n} crawled pages.",
            first_shot)

    # Structured data — present anywhere, with PDP coverage noted
    pages_with_ld = [a for a in accum if a["ld_types"]]
    if pages_with_ld:
        all_types = []
        for a in pages_with_ld:
            for t in a["ld_types"]:
                if t not in all_types:
                    all_types.append(t)
        pdps = [a for a in accum if a["page_type"] == "product_page"]
        pdps_with_ld = sum(1 for a in pdps if a["ld_types"])
        pdp_note = (f" Product JSON-LD on {pdps_with_ld}/{len(pdps)} PDPs." if pdps else "")
        checks["structured_data"] = _pass(
            "Structured Data",
            f"JSON-LD found on {len(pages_with_ld)}/{n} pages: {', '.join(all_types[:6])}." + pdp_note,
            first_shot)
    else:
        checks["structured_data"] = _warn(
            "Structured Data",
            f"No JSON-LD detected across {n} crawled pages.",
            first_shot)

    # Favicon — any page
    if any(a["has_favicon"] for a in accum):
        checks["favicon"] = _pass("Favicon", "Favicon link tag found.", first_shot)
    else:
        checks["favicon"] = _warn(
            "Favicon", f"No favicon link tag detected across {n} crawled pages.", first_shot)

    # Cookie / Privacy — any page across the crawl
    has_privacy = any(a["has_privacy"] for a in accum)
    has_terms = any(a["has_terms"] for a in accum)
    has_cookie = any(a["has_cookie"] for a in accum)
    if has_privacy and has_terms:
        checks["cookie_privacy"] = (
            _pass("Cookie/Privacy",
                  "Privacy Policy and Terms found. Cookie policy also present.", first_shot)
            if has_cookie else
            _warn("Cookie/Privacy",
                  "Privacy and Terms found but cookie consent policy not detected.", first_shot)
        )
    else:
        checks["cookie_privacy"] = _warn(
            "Cookie/Privacy",
            "Privacy Policy and Terms were not both detected across crawled pages.",
            first_shot)

    # Image optimization — sitewide aggregate across all crawled pages
    total_imgs = sum(a["img_total"] for a in accum)
    total_missing = sum(a["img_missing_alt"] for a in accum)
    if total_imgs:
        alt_pct = int(total_missing / total_imgs * 100)
        checks["image_optimization"] = _warn(
            "Image Optimization",
            f"{total_missing}/{total_imgs} images missing alt text ({alt_pct}%) across "
            f"{n} crawled pages. Byte-level audit not run.",
            first_shot)
    else:
        checks["image_optimization"] = _warn(
            "Image Optimization",
            f"No images detected across {n} crawled pages; byte-level audit not run.",
            first_shot)


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

    # Fallback details only — mobile_friendly / page_speed_* are overwritten by a
    # real measurement pass (check_mobile_and_speed). If that pass fails, these
    # honest "not measured" Warns remain.
    details = {
        "mobile_friendly": "Mobile layout not measured (measurement pass did not run).",
        "page_speed_mobile": "Page speed not measured (measurement pass did not run).",
        "page_speed_desktop": "Page speed not measured (measurement pass did not run).",
    }

    for key, label in browser_checks.items():
        checks[key] = _warn(
            label,
            details.get(key, "Not measured; no valid browser evidence was collected."),
        )

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
