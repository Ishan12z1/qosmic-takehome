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
# Payment method detection
# ---------------------------------------------------------------------------

_PAYMENT_LABEL_MAP = {
    "visa": "Visa",
    "mastercard": "Mastercard",
    "amex": "Amex",
    "american-express": "Amex",
    "paypal": "PayPal",
    "apple-pay": "Apple Pay",
    "apple_pay": "Apple Pay",
    "applepay": "Apple Pay",
    "google-pay": "Google Pay",
    "google_pay": "Google Pay",
    "googlepay": "Google Pay",
    "shop-pay": "Shop Pay",
    "shop_pay": "Shop Pay",
    "shopify-pay": "Shop Pay",
    "shopifypay": "Shop Pay",
    "klarna": "Klarna",
    "afterpay": "Afterpay",
    "clearpay": "Afterpay",
    "stripe": "Stripe",
    "discover": "Discover",
    "amazon-pay": "Amazon Pay",
    "diners": "Diners Club",
    "jcb": "JCB",
}


def detect_payment_methods(html: str) -> list[str]:
    lower = html.lower()
    seen: set[str] = set()
    found = []
    for pattern, label in _PAYMENT_LABEL_MAP.items():
        if pattern in lower and label not in seen:
            found.append(label)
            seen.add(label)
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
    for folder in sorted(artifacts_root.iterdir(), reverse=True):
        if folder.is_dir() and folder.name.startswith(f"{slug}_"):
            if (folder / "discovered_links.json").exists() and (folder / "technical_checks.json").exists():
                return folder.name
    return None


def make_run_dirs(run_dir: Path) -> None:
    for subdir in ["screenshots", "pages", "evidence_cards"]:
        (run_dir / subdir).mkdir(parents=True, exist_ok=True)
