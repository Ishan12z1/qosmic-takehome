"""End-to-end driver for the full eval website list.

For every site: crawl -> (if non-auditable) write a deterministic partial audit
-> run the eval. Auditable Shopify stores are crawled and flagged for a full
agent-written audit (the only non-scriptable step). Writes scripts/run_all_results.md.
"""

import asyncio
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))
from crawler.crawl_store import run_crawl  # noqa: E402
from crawler.partial_audit import write_partial_audit  # noqa: E402

ARTIFACTS = ROOT / "artifacts"
RESULTS = Path(__file__).parent / "run_all_results.md"

SITES = [
    ("A", "https://zenrojas.com"),
    ("A", "https://beardbrand.com"),
    ("A", "https://deathwishcoffee.com"),
    ("A", "https://mudwtr.com"),
    ("A", "https://tentree.com"),
    ("B", "https://graza.co"),
    ("B", "https://puravidabracelets.com"),
    ("B", "https://chubbiesshorts.com"),
    ("C", "https://gingerpeople.com"),
    ("C", "https://allbirds.com"),
    ("C", "https://gymshark.com"),
    ("D", "https://patagonia.com"),
    ("D", "https://warbyparker.com"),
    ("D", "https://rei.com"),
    ("E", "https://stripe.com"),
    ("E", "https://wikipedia.org"),
    ("E", "https://vercel.com"),
]


def _read(run_id: str, *parts) -> dict:
    p = ARTIFACTS / run_id
    for part in parts:
        p = p / part
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _verdict(run_id: str) -> str:
    p = ARTIFACTS / run_id / "summary.md"
    if not p.exists():
        return "?"
    for line in p.read_text(encoding="utf-8").splitlines():
        if line.lower().startswith("**crawl health:"):
            return line.split(":", 1)[1].strip().rstrip("*").strip()
    return "?"


def _run_eval(run_id: str) -> str:
    try:
        out = subprocess.run(
            [sys.executable, "evals/run_eval.py", run_id],
            cwd=str(ROOT), capture_output=True, text=True, timeout=180,
        ).stdout
    except Exception as e:
        return f"eval error: {e}"
    for line in out.splitlines():
        if "layers passed" in line:
            return line.strip()
    return "eval ran (no summary line)"


async def main():
    rows = []
    full_audit_needed = []
    for typ, url in SITES:
        print(f"\n########## [{typ}] {url} ##########", flush=True)
        try:
            run_id = await run_crawl(url, force=True)
        except Exception as e:
            rows.append((typ, url, "CRAWL-ERROR", "-", str(e)[:50]))
            continue

        verdict = _verdict(run_id)
        journey = _read(run_id, "pages", "shopping_journey.json")
        outcome = journey.get("outcome", "?")

        if verdict in ("Blocked", "Non-ecommerce"):
            write_partial_audit(run_id)
            eval_line = _run_eval(run_id)
            rows.append((typ, url, run_id, verdict, f"partial -> {eval_line}"))
        else:
            # Auditable Shopify store: needs the agent-written full audit.
            full_audit_needed.append((typ, url, run_id, verdict, outcome))
            rows.append((typ, url, run_id, verdict, "AUDITABLE - full audit pending"))

    lines = ["# Run-all results", "",
             "| Type | URL | Run ID | Verdict | Status |", "|---|---|---|---|---|"]
    for r in rows:
        lines.append("| " + " | ".join(str(x) for x in r) + " |")
    lines += ["", "## Full audits needed (auditable Shopify stores)", ""]
    for typ, url, run_id, verdict, outcome in full_audit_needed:
        lines.append(f"- [{typ}] {url} -> `{run_id}` (verdict {verdict}, journey {outcome})")
    RESULTS.write_text("\n".join(lines), encoding="utf-8")
    print("\n" + "\n".join(lines), flush=True)


if __name__ == "__main__":
    asyncio.run(main())
