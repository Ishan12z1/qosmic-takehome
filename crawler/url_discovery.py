"""URL discovery and page-type quota sampling for the Qosmic crawler."""

import re
from urllib.parse import urlparse, urljoin

import requests
from bs4 import BeautifulSoup

from .utils import normalize_host


# ---------------------------------------------------------------------------
# Page type classification
# ---------------------------------------------------------------------------

def classify_url(url: str) -> str:
    path = urlparse(url).path.lower().rstrip("/")
    if path in ("", "/"):
        return "homepage"
    if "/products/" in path:
        return "product_page"
    if path == "/cart":
        return "cart_page"
    if "/collections/" in path:
        return "collection_page"
    for kw in ["where-to-buy", "where_to_buy", "find-a-store", "store-locator",
               "retailers", "stockists", "find-a-retailer", "find-retailers"]:
        if kw in path:
            return "where_to_buy"
    for kw in ["faq", "shipping", "returns", "refund", "delivery", "help", "support"]:
        if kw in path:
            return "faq_shipping_returns"
    for kw in ["about", "our-story", "who-we-are", "mission", "our-brand", "our-company"]:
        if kw in path:
            return "about_page"
    for kw in ["blog", "article", "news", "recipe", "education", "guide", "learn", "journal"]:
        if kw in path:
            return "blog_or_content_page"
    return "other"


# ---------------------------------------------------------------------------
# URL validation helpers
# ---------------------------------------------------------------------------

def _is_valid_store_url(url: str, base_netloc: str) -> bool:
    """Accept only http/https on exact store domain or www. prefix.
    Rejects mailto:, tel:, subdomains, and external domains.
    """
    if not url.startswith("http"):
        return False
    url_netloc = urlparse(url).netloc.lower()
    clean_base = normalize_host(base_netloc)
    return normalize_host(url_netloc) == clean_base


def _path_key(url: str) -> str:
    """Normalized path key for deduplication - strips www and trailing slash."""
    p = urlparse(url)
    netloc = p.netloc.lower()
    if netloc.startswith("www."):
        netloc = netloc[4:]
    return netloc + p.path.rstrip("/").lower()


# ---------------------------------------------------------------------------
# Sitemap parsing (handles sitemap index + nested sitemaps)
# ---------------------------------------------------------------------------

_SESSION = requests.Session()
_SESSION.headers.update({"User-Agent": "Mozilla/5.0 (compatible; QosmicAuditBot/1.0)"})


def _fetch_sitemap_urls(sitemap_url: str, depth: int = 0) -> list[str]:
    if depth > 3:
        return []
    try:
        r = _SESSION.get(sitemap_url, timeout=10)
        if r.status_code != 200:
            return []
        soup = BeautifulSoup(r.text, "lxml-xml")

        # Sitemap index - recurse into child sitemaps
        sitemaps = soup.find_all("sitemap")
        if sitemaps:
            urls = []
            for sm in sitemaps[:8]:
                loc = sm.find("loc")
                if loc:
                    urls.extend(_fetch_sitemap_urls(loc.get_text(strip=True), depth + 1))
            return urls

        # Regular sitemap - return all <loc> entries
        return [loc.get_text(strip=True) for loc in soup.find_all("loc")]
    except Exception:
        return []


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------

def discover_urls(base_url: str) -> list[str]:
    parsed = urlparse(base_url)
    origin = f"https://{parsed.netloc}"
    found: set[str] = set()

    # 1. Sitemap
    sitemap_urls = _fetch_sitemap_urls(f"{origin}/sitemap.xml")
    for url in sitemap_urls:
        if _is_valid_store_url(url, parsed.netloc):
            found.add(url.split("?")[0])

    # 2. Homepage nav links
    try:
        r = _SESSION.get(origin, timeout=12)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, "lxml")
            for a in soup.find_all("a", href=True):
                href = a["href"].split("?")[0]
                if href.startswith("/"):
                    found.add(urljoin(origin, href))
                elif _is_valid_store_url(href, parsed.netloc):
                    found.add(href.split("?")[0])
    except Exception:
        pass

    found.add(origin + "/")
    return list(found)


# ---------------------------------------------------------------------------
# Page quota sampling
# ---------------------------------------------------------------------------

PAGE_QUOTA = {
    "homepage": 1,
    "product_page": 3,
    "cart_page": 1,
    "collection_page": 2,
    "where_to_buy": 1,
    "faq_shipping_returns": 1,
    "about_page": 1,
    "blog_or_content_page": 1,
}

MAX_PAGES = 12

_BLOG_PRIORITY_KEYWORDS = ["health", "guide", "routine", "recipe", "education",
                            "wellness", "glp", "nausea", "digest", "nutrition"]

# Product handles that are rarely representative of the catalog. These are ranked
# LAST (not excluded) so they're only chosen when nothing better exists.
_PRODUCT_DENYLIST = ["gift-card", "giftcard", "gift_card", "e-gift", "egift",
                     "membership", "donation", "subscription-gift"]


def _blog_priority(url: str) -> int:
    path = urlparse(url).path.lower()
    return sum(1 for kw in _BLOG_PRIORITY_KEYWORDS if kw in path)


def _is_denylisted_product(url: str) -> bool:
    handle = urlparse(url).path.lower()
    return any(kw in handle for kw in _PRODUCT_DENYLIST)


def select_pages(urls: list[str], base_url: str,
                 nav_links: set[str] | None = None,
                 guessed_links: set[str] | None = None) -> tuple[list[dict], list[dict]]:
    parsed = urlparse(base_url)
    base_netloc = normalize_host(parsed.netloc)

    # Classify - only accept valid store URLs, deduplicate by path key
    classified: dict[str, list[str]] = {k: [] for k in list(PAGE_QUOTA.keys()) + ["other"]}
    seen_keys: set[str] = set()

    for url in urls:
        # Reject non-http links (mailto:, tel:, javascript:, etc.)
        if not url.startswith("http"):
            continue
        # Reject subdomains and external domains
        if not _is_valid_store_url(url, base_netloc):
            continue
        # Deduplicate www vs non-www via path key
        key = _path_key(url)
        if key in seen_keys:
            continue
        seen_keys.add(key)

        ptype = classify_url(url)
        classified[ptype].append(url)

    # Rank for representativeness. Products/collections linked from the homepage
    # nav are featured/representative; gift-cards & memberships rank last. This
    # replaces the old shortest-path sort that picked mugs/gift-cards/memberships.
    nav_keys = {_path_key(u) for u in (nav_links or set())}
    guessed_keys = {_path_key(u) for u in (guessed_links or set())}

    def _source_rank(u: str) -> tuple[int, int]:
        return (
            1 if _path_key(u) in guessed_keys else 0,
            0 if _path_key(u) in nav_keys else 1,
        )

    def _product_rank(u: str):
        return (*_source_rank(u),
                0 if not _is_denylisted_product(u) else 1,
                len(urlparse(u).path))

    def _collection_rank(u: str):
        return (*_source_rank(u),
                len(urlparse(u).path))

    classified["product_page"].sort(key=_product_rank)
    classified["collection_page"].sort(key=_collection_rank)
    classified["blog_or_content_page"].sort(
        key=lambda u: (*_source_rank(u), -_blog_priority(u), len(urlparse(u).path)))

    # Real sitemap/nav URLs always outrank guessed standard Shopify paths.
    for page_type in [
        "cart_page", "where_to_buy", "faq_shipping_returns", "about_page",
    ]:
        classified[page_type].sort(key=lambda u: (*_source_rank(u), len(urlparse(u).path)))

    # Ensure homepage
    if not classified["homepage"]:
        classified["homepage"] = [f"https://{parsed.netloc}/"]

    # Apply quota in priority order
    priority_order = [
        "homepage", "product_page", "cart_page", "collection_page",
        "where_to_buy", "faq_shipping_returns", "about_page", "blog_or_content_page",
    ]

    selected: list[dict] = []
    rejected: list[dict] = []

    for ptype in priority_order:
        quota = PAGE_QUOTA.get(ptype, 1)
        pool = classified.get(ptype, [])
        take = pool[:quota]
        skip = pool[quota:]
        for u in take:
            if len(selected) < MAX_PAGES:
                selected.append({"url": u, "page_type": ptype})
        for u in skip:
            rejected.append({"url": u, "page_type": ptype, "reason": "quota_exceeded"})

    return selected, rejected
