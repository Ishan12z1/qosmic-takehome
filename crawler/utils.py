"""Shared utilities for the Qosmic crawler."""

import json
import re
import uuid
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup


# ---------------------------------------------------------------------------
# Naming
# ---------------------------------------------------------------------------

def normalize_host(host: str) -> str:
    """Normalize a hostname without stripping legitimate leading characters."""
    normalized = host.lower()
    return normalized[4:] if normalized.startswith("www.") else normalized


def derive_slug(url: str) -> str:
    hostname = urlparse(url).hostname or url
    for prefix in ["www.", "shop.", "store.", "m."]:
        if hostname.startswith(prefix):
            hostname = hostname[len(prefix):]
    return re.sub(r"[^a-z0-9]", "", hostname.split(".")[0].lower())


def generate_run_id(slug: str) -> str:
    date_str = datetime.now().strftime("%Y%m%d")
    uid = uuid.uuid4().hex[:6]
    return f"{slug}_{date_str}_{uid}"


def safe_name(url: str, page_type: str, index: int) -> str:
    path = urlparse(url).path.strip("/").replace("/", "_") or "home"
    path = re.sub(r"[^a-z0-9_-]", "", path.lower())[:40]
    return f"{page_type}_{index}_{path}" if path else f"{page_type}_{index}"


# ---------------------------------------------------------------------------
# Bot detection
# ---------------------------------------------------------------------------

BLOCKED_SIGNALS = [
    "checking your browser",
    "cf-browser-verification",
    "just a moment",
    "ddos-guard",
    "ray id",
    "enable javascript and cookies",
    "please wait",
    "attention required",
    # Geo-routing / interstitial walls that serve placeholder content on every
    # URL instead of the real storefront (e.g. patagonia "Hang Tight!").
    "hang tight",
    "routing to checkout",
    "sit tight",
]


def is_blocked(text: str) -> bool:
    lower = text.lower()
    return any(sig in lower for sig in BLOCKED_SIGNALS)


def is_valid_page(title: str, body_text: str) -> tuple[bool, str]:
    if not title or len(title.strip()) == 0:
        return False, "missing_title"
    if len(body_text.strip()) < 300:
        return False, "body_too_short"
    if is_blocked(title + " " + body_text[:500]):
        return False, "bot_challenge_detected"
    return True, "ok"


# ---------------------------------------------------------------------------
# Soft-404 detection (branded 404 pages that return HTTP 200)
# ---------------------------------------------------------------------------

_SOFT_404_TITLE_SIGNALS = ["404", "page not found", "not found"]


def is_soft_404(title: str, canonical: str, body_text: str) -> bool:
    """True if a page is a branded/soft 404 despite a 200 status.

    Detected via the document title ("404 Not Found"), a canonical URL that
    resolves to a /404 path, or an explicit not-found message in a short body.
    """
    t = (title or "").lower()
    if any(sig in t for sig in _SOFT_404_TITLE_SIGNALS):
        return True
    canon_path = urlparse(canonical or "").path.rstrip("/").lower()
    if canon_path.endswith("/404"):
        return True
    body = (body_text or "").lower()
    if len(body.strip()) < 1200 and ("page not found" in body or "page you requested" in body):
        return True
    return False


# ---------------------------------------------------------------------------
# Cart content detection (verify add-to-cart actually populated the cart)
# ---------------------------------------------------------------------------

_EMPTY_CART_SIGNALS = [
    "your cart is empty",
    "your shopping cart is empty",
    "cart is empty",
    "no items in your cart",
    "your bag is empty",
]


def cart_has_items(cart_body_text: str) -> bool:
    """True if the cart page shows at least one line item.

    Returns False when the cart page explicitly states it is empty. This guards
    against treating a successful add-to-cart *click* as a successful add when
    the item never actually landed in the cart.
    """
    body = (cart_body_text or "").lower()
    if any(sig in body for sig in _EMPTY_CART_SIGNALS):
        return False
    # Heuristic positive signals of a populated cart.
    return any(sig in body for sig in ["subtotal", "checkout", "remove", "quantity"])


# ---------------------------------------------------------------------------
# Payment method detection
# ---------------------------------------------------------------------------

_PAYMENT_PATTERNS = {
    "Visa": [
        r"\bvisa\b",
        r"visa(?:\.svg|\.png|\.webp|\.jpg)",
    ],
    "Mastercard": [
        r"\bmastercard\b",
        r"master[-_ ]?card(?:\.svg|\.png|\.webp|\.jpg)?",
    ],
    "Amex": [
        r"\bamex\b",
        r"american[-_ ]?express",
    ],
    "PayPal": [
        r"\bpaypal\b",
        r"pay[-_ ]?pal",
    ],
    "Apple Pay": [
        r"apple[-_ ]?pay",
    ],
    "Google Pay": [
        r"google[-_ ]?pay",
        r"\bgpay\b",
    ],
    "Shop Pay": [
        r"shop(?:ify)?[-_ ]?pay",
    ],
    "Klarna": [
        r"\bklarna\b",
    ],
    "Afterpay": [
        r"\bafterpay\b",
        r"\bclearpay\b",
    ],
    "Stripe": [
        r"\bstripe\b",
    ],
    "Discover": [
        r"discover[-_ ]card",
        r"card[-_ ]discover",
        r"discover(?:\.svg|\.png|\.webp|\.jpg)",
    ],
    "Amazon Pay": [
        r"amazon[-_ ]?pay",
    ],
    "Diners Club": [
        r"\bdiners\b",
        r"diners[-_ ]club",
    ],
    "JCB": [
        r"\bjcb\b",
    ],
}


def detect_payment_methods(html: str) -> list[str]:
    lower = html.lower()
    found = []
    for label, patterns in _PAYMENT_PATTERNS.items():
        if any(re.search(pattern, lower, re.IGNORECASE) for pattern in patterns):
            found.append(label)
    return found


# ---------------------------------------------------------------------------
# Page metadata extraction
# ---------------------------------------------------------------------------

def extract_page_metadata(soup: BeautifulSoup, url: str, page_type: str) -> dict:
    title = soup.find("title")
    meta_desc = soup.find("meta", attrs={"name": "description"})
    canonical = soup.find("link", rel="canonical")
    og_title = soup.find("meta", property="og:title")
    og_desc = soup.find("meta", property="og:description")

    headings = []
    for tag in ["h1", "h2", "h3"]:
        for h in soup.find_all(tag)[:5]:
            text = h.get_text(strip=True)
            if text:
                headings.append({"tag": tag, "text": text})

    cta_keywords = ["add", "buy", "shop", "get", "find", "checkout",
                    "cart", "order", "purchase", "subscribe", "learn", "explore"]
    ctas = []
    for btn in soup.find_all(["button", "a"], limit=40):
        text = btn.get_text(strip=True)
        if text and 2 < len(text) < 60:
            if any(kw in text.lower() for kw in cta_keywords):
                ctas.append(text)
    ctas = list(dict.fromkeys(ctas))[:10]

    links = []
    for a in soup.find_all("a", href=True)[:50]:
        href = a.get("href", "")
        text = a.get_text(strip=True)
        if href and not href.startswith("#") and text:
            links.append({"text": text[:60], "href": href[:120]})

    return {
        "url": url,
        "page_type": page_type,
        "title": title.get_text(strip=True) if title else "",
        "meta_description": meta_desc.get("content", "") if meta_desc else "",
        "canonical": canonical.get("href", "") if canonical else "",
        "og_title": og_title.get("content", "") if og_title else "",
        "og_description": og_desc.get("content", "") if og_desc else "",
        "headings": headings,
        "ctas": ctas,
        "important_links": links[:20],
    }


# ---------------------------------------------------------------------------
# Artifact helpers
# ---------------------------------------------------------------------------

def find_existing_run(slug: str, artifacts_root: Path) -> str | None:
    if not artifacts_root.exists():
        return None

    candidates: list[tuple[int, datetime, str]] = []
    required = [
        "discovered_links.json",
        "technical_checks.json",
        "summary.md",
        "pages/shopping_journey.json",
    ]

    for folder in artifacts_root.iterdir():
        if not folder.is_dir() or not folder.name.startswith(f"{slug}_"):
            continue
        if not all((folder / relative).exists() for relative in required):
            continue

        discovered = folder / "discovered_links.json"
        try:
            data = json.loads(discovered.read_text(encoding="utf-8"))
            crawled_at = datetime.fromisoformat(data["crawled_at"])
        except (KeyError, TypeError, ValueError, json.JSONDecodeError):
            crawled_at = datetime.fromtimestamp(folder.stat().st_mtime)

        summary = (folder / "summary.md").read_text(encoding="utf-8", errors="replace")
        verdict_match = re.search(r"crawl health:\s*([A-Za-z]+)", summary, re.IGNORECASE)
        verdict = verdict_match.group(1).lower() if verdict_match else "unknown"
        usability = {"healthy": 2, "degraded": 1, "blocked": 0}.get(verdict, 0)
        candidates.append((usability, crawled_at, folder.name))

    if not candidates:
        return None

    # Prefer the newest Healthy/Degraded crawl. Blocked-only runs should be retried
    # by default rather than silently reused, because they are often transient.
    usable = [candidate for candidate in candidates if candidate[0] > 0]
    if not usable:
        return None
    return max(usable, key=lambda candidate: candidate[1])[2]


def make_run_dirs(run_dir: Path) -> None:
    for subdir in ["screenshots", "pages", "evidence_cards"]:
        (run_dir / subdir).mkdir(parents=True, exist_ok=True)
