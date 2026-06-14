"""Temp driver: crawl a representative slice of docs/eval_website_list.md and
record crawl-health / journey / page outcomes for each. Not part of the harness."""

import asyncio
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from crawler.crawl_store import run_crawl  # noqa: E402

ARTIFACTS = Path(__file__).parent.parent / "artifacts"
RESULTS = Path(__file__).parent / "sweep_results.md"

SITES = [
    ("A", "https://tentree.com"),
    ("C", "https://allbirds.com"),
    ("C", "https://gymshark.com"),
    ("D", "https://warbyparker.com"),
    ("D", "https://rei.com"),
    ("E", "https://wikipedia.org"),
    ("E", "https://vercel.com"),
    ("E", "https://stripe.com"),
]


def _verdict(run_id: str) -> str:
    p = ARTIFACTS / run_id / "summary.md"
    if not p.exists():
        return "?"
    for line in p.read_text(encoding="utf-8").splitlines():
        if line.lower().startswith("**crawl health:"):
            return line.split(":")[1].strip().rstrip("*").strip()
    return "?"


def _journey(run_id: str) -> tuple:
    p = ARTIFACTS / run_id / "pages" / "shopping_journey.json"
    if not p.exists():
        return ("?", "?")
    j = json.loads(p.read_text(encoding="utf-8"))
    return (j.get("outcome", "?"), j.get("friction_score", "?"))


def _pages(run_id: str) -> tuple:
    p = ARTIFACTS / run_id / "discovered_links.json"
    if not p.exists():
        return ("?", "?")
    d = json.loads(p.read_text(encoding="utf-8"))
    return (len(d.get("selected_pages", [])), d.get("total_discovered", "?"))


async def main():
    rows = []
    for typ, url in SITES:
        print(f"\n########## [{typ}] {url} ##########", flush=True)
        try:
            run_id = await run_crawl(url, force=True)
            verdict = _verdict(run_id)
            outcome, friction = _journey(run_id)
            sel, total = _pages(run_id)
            rows.append((typ, url, run_id, verdict, f"{outcome} ({friction}/5)", f"{sel} sel"))
        except Exception as e:
            rows.append((typ, url, "ERROR", "ERROR", str(e)[:60], "-"))
            print(f"  [ERROR] {e}", flush=True)

    lines = ["# Sweep results", "",
             "| Type | URL | Run ID | Crawl health | Journey | Pages |",
             "|---|---|---|---|---|---|"]
    for typ, url, run_id, verdict, journey, pages in rows:
        lines.append(f"| {typ} | {url} | {run_id} | {verdict} | {journey} | {pages} |")
    RESULTS.write_text("\n".join(lines), encoding="utf-8")
    print("\n" + "\n".join(lines), flush=True)


if __name__ == "__main__":
    asyncio.run(main())
