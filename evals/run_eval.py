#!/usr/bin/env python3
"""
run_eval.py — Deterministic eval layers 1–8 + Layer 9 pre-filled prompt output.

Usage:
    python evals/run_eval.py <run_id>

Output:
    eval_results/<run_id>_eval.md
    Prints Layer 9 pre-filled prompt to stdout at the end.
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path

ARTIFACTS_ROOT = Path(__file__).parent.parent / "artifacts"
SAMPLE_OUTPUT_ROOT = Path(__file__).parent.parent / "sample_output"
EVAL_RESULTS_ROOT = Path(__file__).parent.parent / "eval_results"
RUBRIC_PATH = Path(__file__).parent / "rubric.md"

REQUIRED_SECTIONS = [
    "executive summary",
    "store overview",
    "competitor",
    "experiment",
    "technical check",
]

ALL_PILLARS = {"conversion", "aov", "retention", "acquisition", "performance"}

REQUIRED_EXP_FIELDS = [
    "pillar", "surface", "url", "evidence", "hypothesis",
    "primary change", "primary kpi", "decision rule", "expected lift", "confidence",
]

FAILURE_LOG = Path(__file__).parent / "failure_log.jsonl"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _load_json(path: Path) -> dict | None:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def _load_text(path: Path) -> str | None:
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


def _result(layer: int, name: str, passed: bool, detail: str) -> dict:
    return {"layer": layer, "name": name, "passed": passed, "detail": detail}


def _log_failure(run_id: str, layer: int, failure_type: str, detail: str) -> None:
    entry = {
        "run_id": run_id,
        "timestamp": datetime.now().isoformat(),
        "layer": layer,
        "failure_type": failure_type,
        "detail": detail,
    }
    with FAILURE_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")


# ---------------------------------------------------------------------------
# Layer checks
# ---------------------------------------------------------------------------

def layer1_required_sections(report: str, run_id: str) -> dict:
    lower = report.lower()
    missing = [s for s in REQUIRED_SECTIONS if s not in lower]
    if missing:
        _log_failure(run_id, 1, "missing_section", f"Missing: {missing}")
        return _result(1, "Required sections present", False,
                       f"Missing sections: {missing}")
    return _result(1, "Required sections present", True,
                   "All required sections found")


def layer2_exec_summary(report: str, run_id: str) -> dict:
    lower = report.lower()
    # Find exec summary block
    match = re.search(r"executive summary.*?(?=\n#{1,3} |\Z)", lower, re.DOTALL | re.IGNORECASE)
    if not match:
        _log_failure(run_id, 2, "exec_summary_missing", "Exec summary section not found")
        return _result(2, "Exec summary quality", False, "Executive summary section not found")

    section = match.group(0)
    paragraphs = [p.strip() for p in section.split("\n\n") if len(p.strip()) > 80]

    issues = []
    if len(paragraphs) < 2:
        issues.append(f"only {len(paragraphs)} paragraph(s) — needs 2–3")
        _log_failure(run_id, 2, "exec_summary_generic",
                     f"Too few paragraphs: {len(paragraphs)}")

    # Check for diagnosis keywords
    diag_keywords = ["because", "due to", "constraint", "friction", "gap", "lack", "missing", "no "]
    has_diagnosis = any(kw in section for kw in diag_keywords)
    if not has_diagnosis:
        issues.append("no diagnostic reasoning detected (missing 'because', 'constraint', etc.)")
        _log_failure(run_id, 2, "exec_summary_generic", "No diagnosis found in exec summary")

    if issues:
        return _result(2, "Exec summary quality", False, "; ".join(issues))
    return _result(2, "Exec summary quality", True,
                   f"{len(paragraphs)} paragraphs with diagnosis language")


def layer3_experiment_count(report: str, run_id: str) -> dict:
    # Count EXP-NN headings
    exp_matches = re.findall(r"EXP-\d{2}", report, re.IGNORECASE)
    count = len(set(exp_matches))
    if count != 10:
        _log_failure(run_id, 3, "wrong_experiment_count", f"Found {count} experiments")
        return _result(3, "Exactly 10 experiments", False,
                       f"Found {count} experiment(s) — exactly 10 required")
    return _result(3, "Exactly 10 experiments", True, "Exactly 10 experiments found")


def layer4_experiment_fields(report: str, run_id: str) -> dict:
    # Find all experiment blocks
    blocks = re.findall(
        r"(### EXP-\d{2}.*?)(?=### EXP-\d{2}|\Z)", report, re.DOTALL | re.IGNORECASE
    )
    missing_by_exp = {}
    for block in blocks:
        exp_id_match = re.search(r"EXP-\d{2}", block)
        exp_id = exp_id_match.group(0) if exp_id_match else "unknown"
        lower_block = block.lower()
        missing = [f for f in REQUIRED_EXP_FIELDS if f not in lower_block]
        if missing:
            missing_by_exp[exp_id] = missing

    if missing_by_exp:
        details = "; ".join(f"{k}: missing {v}" for k, v in missing_by_exp.items())
        _log_failure(run_id, 4, "missing_exp_fields", details)
        return _result(4, "All experiment fields present", False, details)
    return _result(4, "All experiment fields present", True,
                   f"All {len(blocks)} experiments have required fields")


def layer5_pillar_coverage(report: str, run_id: str) -> dict:
    lower = report.lower()
    # Find pillar values within experiment blocks only
    blocks = re.findall(
        r"### EXP-\d{2}.*?(?=### EXP-\d{2}|\Z)", report, re.DOTALL | re.IGNORECASE
    )
    found_pillars = set()
    for block in blocks:
        for pillar in ALL_PILLARS:
            if f"| pillar | {pillar}" in block.lower() or f"pillar | {pillar}" in block.lower():
                found_pillars.add(pillar)

    # Fallback: search full report for pillar mentions near "pillar" keyword
    if len(found_pillars) < 5:
        for pillar in ALL_PILLARS:
            if re.search(rf"\|\s*pillar\s*\|\s*{pillar}", lower):
                found_pillars.add(pillar)

    missing = ALL_PILLARS - found_pillars
    if len(found_pillars) < 5:
        _log_failure(run_id, 5, "pillar_missing", f"Missing pillars: {missing}")
        return _result(5, "All 5 pillars covered", False,
                       f"Missing pillars: {missing}. Found: {found_pillars}")
    return _result(5, "All 5 pillars covered", True,
                   f"All 5 pillars present: {sorted(found_pillars)}")


def layer6_evidence_paths(report: str, run_id: str, run_dir: Path) -> dict:
    # Find all artifact path citations in the report
    cited_paths = re.findall(r"artifacts/[^\s\)\"']+", report)
    issues = []
    cross_run = []

    for raw_path in cited_paths:
        # Strip trailing punctuation
        clean = raw_path.rstrip(".,;)")

        # Cross-run contamination: path must be under this run_id
        if not clean.startswith(f"artifacts/{run_id}/"):
            cross_run.append(clean)
            continue

        # File existence check
        abs_path = run_dir.parent / clean.replace(f"artifacts/{run_id}/", "")
        if not abs_path.exists():
            issues.append(clean)

    if cross_run:
        detail = f"Cross-run contamination — paths from other runs: {cross_run[:3]}"
        _log_failure(run_id, 6, "cross_run_contamination", detail)
        return _result(6, "Evidence paths valid (no cross-run contamination)", False, detail)

    if issues:
        detail = f"{len(issues)} cited path(s) do not exist on disk: {issues[:3]}"
        _log_failure(run_id, 6, "missing_evidence_citation", detail)
        return _result(6, "Evidence paths valid (no cross-run contamination)", False, detail)

    return _result(6, "Evidence paths valid (no cross-run contamination)", True,
                   f"All {len(cited_paths)} artifact citations valid and under correct run_id")


def layer7_technical_checks(report: str, checks: dict, run_id: str) -> dict:
    issues = []

    for key, check in checks.items():
        label = check.get("label", key)
        json_status = check.get("status", "")
        lower_report = report.lower()

        # Check label appears in report
        if label.lower() not in lower_report:
            issues.append(f"'{label}' missing from report")
            continue

        # Check status matches (look for label + status proximity)
        # Find the row containing this label
        label_pos = lower_report.find(label.lower())
        surrounding = lower_report[label_pos:label_pos + 120]
        if json_status.lower() not in surrounding:
            issues.append(f"'{label}': JSON says '{json_status}' but not found in report row")
            _log_failure(run_id, 7, "technical_mismatch",
                         f"{label}: expected {json_status}")

    if issues:
        return _result(7, "Technical checks match JSON", False,
                       f"{len(issues)} mismatch(es): " + "; ".join(issues[:3]))
    return _result(7, "Technical checks match JSON", True,
                   f"All {len(checks)} technical checks match technical_checks.json")


def layer8_competitor_table(report: str, evidence_summary: str | None, run_id: str) -> dict:
    lower = report.lower()

    # Count competitor table rows (look for table rows after "competitor" heading)
    comp_section = re.search(
        r"competitor.*?(?=\n#{1,3} |\Z)", lower, re.DOTALL | re.IGNORECASE
    )
    if not comp_section:
        _log_failure(run_id, 8, "competitor_mismatch", "Competitor section not found")
        return _result(8, "Competitor table quality", False, "Competitor section not found")

    section_text = comp_section.group(0)
    # Count table rows (lines starting with |, skip header and separator)
    rows = [l for l in section_text.split("\n")
            if l.strip().startswith("|") and "---" not in l and "competitor" not in l.lower()]

    if len(rows) < 3:
        _log_failure(run_id, 8, "competitor_mismatch",
                     f"Only {len(rows)} competitor rows — need 3–4")
        return _result(8, "Competitor table quality", False,
                       f"Only {len(rows)} competitor row(s) found — need 3–4")

    # Check store_category alignment (best-effort)
    if evidence_summary:
        cat_match = re.search(r"store_category:\s*(.+)", evidence_summary)
        if cat_match:
            category = cat_match.group(1).strip().lower()
            if category and category != "unknown":
                # Very loose check: at least some category keyword in competitor section
                cat_words = [w for w in re.split(r"[/\s,]+", category) if len(w) > 3]
                category_aligned = any(w in section_text for w in cat_words)
                if not category_aligned:
                    _log_failure(run_id, 8, "competitor_mismatch",
                                 f"Competitors don't reflect store_category: {category}")
                    return _result(8, "Competitor table quality", False,
                                   f"Competitors may not match store_category '{category}'")

    return _result(8, "Competitor table quality", True,
                   f"{len(rows)} competitors found, section present")


# ---------------------------------------------------------------------------
# Layer 9 pre-filled prompt builder
# ---------------------------------------------------------------------------

def build_layer9_prompt(report: str, run_id: str) -> str:
    rubric = _load_text(RUBRIC_PATH) or "(rubric.md not found)"
    # Truncate report to ~4000 chars to keep prompt manageable
    report_preview = report[:4000] + ("\n\n[...truncated...]" if len(report) > 4000 else "")
    return f"""# /eval-judge — Layer 9 Quality Rubric

Run ID: {run_id}

## Rubric

{rubric}

## Audit Report (to evaluate)

{report_preview}

## Instructions

Score the audit report above on all 10 rubric dimensions (1–5 each).
Output a markdown table with Score and Notes columns, a Total, and a Verdict.
Append results to eval_results/{run_id}_eval.md under ## Layer 9: Quality Rubric
"""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run_eval(run_id: str) -> None:
    run_dir = ARTIFACTS_ROOT / run_id
    report_path = SAMPLE_OUTPUT_ROOT / f"{run_id}_audit.md"
    eval_path = EVAL_RESULTS_ROOT / f"{run_id}_eval.md"

    EVAL_RESULTS_ROOT.mkdir(exist_ok=True)

    print(f"\n{'='*60}")
    print(f"Qosmic Eval — {run_id}")
    print(f"{'='*60}\n")

    # Load artifacts
    report = _load_text(report_path)
    if not report:
        print(f"[FAIL] Audit report not found: {report_path}")
        print("       Run /audit-writer first.")
        sys.exit(1)

    checks = _load_json(run_dir / "technical_checks.json")
    if not checks:
        print(f"[WARN] technical_checks.json not found — Layer 7 will be skipped")
        checks = {}

    evidence_summary = _load_text(run_dir / "evidence_summary.md")

    # Run layers 1–8
    results = [
        layer1_required_sections(report, run_id),
        layer2_exec_summary(report, run_id),
        layer3_experiment_count(report, run_id),
        layer4_experiment_fields(report, run_id),
        layer5_pillar_coverage(report, run_id),
        layer6_evidence_paths(report, run_id, run_dir),
        layer7_technical_checks(report, checks, run_id),
        layer8_competitor_table(report, evidence_summary, run_id),
    ]

    # Print results
    passed = sum(1 for r in results if r["passed"])
    failed = [r for r in results if not r["passed"]]

    for r in results:
        status = "[PASS]" if r["passed"] else "[FAIL]"
        print(f"  {status} Layer {r['layer']}: {r['name']}")
        if not r["passed"]:
            print(f"         {r['detail']}")

    print(f"\n  {passed}/8 deterministic layers passed")

    # Build eval report
    lines = [
        f"# Eval Results: {run_id}",
        f"",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"",
        f"## Layers 1–8 (Deterministic)",
        f"",
        f"| Layer | Name | Result | Detail |",
        f"|---|---|---|---|",
    ]
    for r in results:
        status_md = "Pass" if r["passed"] else "**Fail**"
        detail = r["detail"].replace("|", "\\|")
        lines.append(f"| {r['layer']} | {r['name']} | {status_md} | {detail} |")

    lines += [
        f"",
        f"**{passed}/8 layers passed**",
        f"",
    ]

    if failed:
        lines += [
            f"## Failures and suggested fixes",
            f"",
        ]
        for r in failed:
            lines.append(f"### Layer {r['layer']}: {r['name']}")
            lines.append(f"")
            lines.append(f"**Detail:** {r['detail']}")
            lines.append(f"")
            lines.append(f"**Fix:** See `evals/rubric.md` failure patterns for `{r['name'].lower().replace(' ', '_')}`")
            lines.append(f"")

    lines += [
        f"## Layer 9: Quality Rubric",
        f"",
        f"_(Paste the pre-filled prompt below into /eval-judge to complete Layer 9)_",
        f"",
    ]

    eval_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\n  Eval report saved: {eval_path}")

    # Always output Layer 9 pre-filled prompt
    layer9_prompt = build_layer9_prompt(report, run_id)
    print(f"\n{'='*60}")
    print("Layer 9 — paste this prompt to /eval-judge:")
    print(f"{'='*60}\n")
    print(layer9_prompt)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python evals/run_eval.py <run_id>")
        sys.exit(1)
    run_eval(sys.argv[1])
