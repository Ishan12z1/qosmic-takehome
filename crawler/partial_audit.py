"""Deterministic partial-audit report for non-auditable crawls.

When a crawl is Blocked or Non-ecommerce (or otherwise has no product/commerce
surface), no full CRO audit can honestly be produced. This module writes a clearly
labeled "Partial Audit — Crawl Issues" report to sample_output/ so the reports
folder still has an honest entry that states what went wrong — and so the run goes
end-to-end (crawl → report → eval in degraded mode) without any fabrication.
"""

import json
import re
from pathlib import Path

ARTIFACTS_ROOT = Path(__file__).parent.parent / "artifacts"
SAMPLE_OUTPUT_ROOT = Path(__file__).parent.parent / "sample_output"


def _load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _verdict_and_issues(summary_text: str):
    verdict = "Blocked"
    m = re.search(r"crawl health:\s*([A-Za-z\-]+)", summary_text, re.IGNORECASE)
    if m:
        verdict = m.group(1)
    issues = []
    block = re.search(r"## Issues a reader should know\s*(.*?)\Z", summary_text, re.DOTALL)
    if block:
        for line in block.group(1).splitlines():
            line = line.strip()
            if line.startswith("- "):
                issues.append(line[2:].strip())
    return verdict, issues


def write_partial_audit(run_id: str,
                        artifacts_root: Path = ARTIFACTS_ROOT,
                        sample_output_root: Path = SAMPLE_OUTPUT_ROOT) -> Path:
    run_dir = artifacts_root / run_id
    summary_text = (run_dir / "summary.md").read_text(encoding="utf-8") \
        if (run_dir / "summary.md").exists() else ""
    discovered = _load_json(run_dir / "discovered_links.json")
    checks = _load_json(run_dir / "technical_checks.json")

    verdict, issues = _verdict_and_issues(summary_text)
    base_url = discovered.get("base_url", run_id)

    intro = {
        "Blocked": "The storefront could not be crawled (bot protection, timeouts, or "
                   "errors on the core pages), so there is not enough evidence to produce "
                   "experiments, competitor analysis, or a reliable technical assessment.",
        "Non-ecommerce": "The pages loaded, but no retail purchase surface was found — no "
                         "product catalog with a working add-to-cart/checkout flow. This does "
                         "not appear to be a retail ecommerce store (it may still be a SaaS or "
                         "product site), so a storefront CRO audit (experiments, competitor "
                         "benchmarks, checkout checks) does not apply.",
    }.get(verdict,
          "The crawl did not yield enough commerce evidence to produce a full CRO audit.")

    lines = [
        f"# Partial Audit - Crawl Issues: {base_url}",
        "",
        f"Run ID: `{run_id}`  ",
        f"Crawl health: **{verdict}**",
        "",
        "> This is **not** a full CRO audit. " + intro,
        f"> See `artifacts/{run_id}/summary.md` for the full machine record.",
        "",
        "## Issues a reader should know",
        "",
    ]
    if issues:
        lines += [f"- {i}" for i in issues]
    else:
        lines.append("- The crawl did not complete enough pages to audit.")
    lines.append("")

    # Technical checks that *did* run (honest subset — never invented)
    if checks:
        lines += ["## Technical checks captured", "",
                  "| Check | Status | Detail |", "|---|---|---|"]
        for key, c in checks.items():
            if not isinstance(c, dict):
                continue
            detail = " ".join(str(c.get("detail", "")).split())[:90]
            lines.append(f"| {c.get('label', key)} | {c.get('status', '?')} | {detail} |")
        lines.append("")

    lines += [
        "## What is NOT claimed",
        "",
        "No experiments, competitor benchmarks, or pass/fail purchase-path verdicts are "
        "asserted — the evidence to support them was not captured. "
        + ("Re-run from a non-blocked network/IP to attempt a full audit."
           if verdict == "Blocked" else
           "A storefront CRO audit is not applicable to this site type."),
        "",
        f"Evidence: `artifacts/{run_id}/summary.md`, `artifacts/{run_id}/discovered_links.json`",
        "",
    ]

    sample_output_root.mkdir(exist_ok=True)
    out_path = sample_output_root / f"{run_id}_audit.md"
    out_path.write_text("\n".join(lines), encoding="utf-8")
    return out_path


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python -m crawler.partial_audit <run_id>")
        sys.exit(1)
    print(write_partial_audit(sys.argv[1]))
