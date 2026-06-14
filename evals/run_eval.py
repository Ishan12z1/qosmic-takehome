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

REQUIRED_H2_SECTIONS = [
    "executive summary",
    "proposed experiments",
    "competitor analysis",
    "technical checks",
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


def _completed_layer9(eval_text: str) -> str:
    match = re.search(r"## Layer 9: Quality Rubric\s*\n(.*)\Z", eval_text, re.DOTALL)
    if match and "**Total:" in match.group(1):
        return match.group(1).strip()
    return ""


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
    key = (run_id, layer, failure_type, detail)
    if FAILURE_LOG.exists():
        for line in FAILURE_LOG.read_text(encoding="utf-8", errors="replace").splitlines():
            try:
                previous = json.loads(line)
            except json.JSONDecodeError:
                continue
            previous_key = (
                previous.get("run_id"),
                previous.get("layer"),
                previous.get("failure_type"),
                previous.get("detail"),
            )
            if previous_key == key:
                return
    with FAILURE_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")


# ---------------------------------------------------------------------------
# Layer checks
# ---------------------------------------------------------------------------

def layer1_required_sections(report: str, run_id: str) -> dict:
    headings = [
        re.sub(r"\s+", " ", heading.strip().lower())
        for heading in re.findall(r"^##\s+(.+?)\s*$", report, re.MULTILINE)
    ]
    missing = [s for s in REQUIRED_H2_SECTIONS if s not in headings]
    extras = [s for s in headings if s not in REQUIRED_H2_SECTIONS]
    wrong_order = [s for s in headings if s in REQUIRED_H2_SECTIONS] != REQUIRED_H2_SECTIONS
    if missing or extras or wrong_order:
        detail = f"Expected exactly {REQUIRED_H2_SECTIONS}; found {headings}"
        _log_failure(run_id, 1, "missing_section", detail)
        return _result(1, "Required sections present", False,
                       detail)
    return _result(1, "Required sections present", True,
                   "Exactly four required H2 sections found in order")


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

    # Diagnostic reasoning — meaningful constraint language (not the trivial "no ").
    diag_keywords = ["because", "due to", "constraint", "friction", "leak", "leaking",
                     "costing", "losing", "suppress", "blocker", "bottleneck",
                     "drives", "driving", "gap in", "the biggest"]
    has_diagnosis = any(kw in section for kw in diag_keywords)
    if not has_diagnosis:
        issues.append("no diagnostic reasoning detected (needs constraint language: "
                      "'because', 'costing', 'leaking', 'constraint', etc.)")
        _log_failure(run_id, 2, "exec_summary_generic", "No diagnosis found in exec summary")

    # Must cite at least one piece of evidence for the diagnosis.
    has_citation = bool(re.search(r"artifacts/[^\s\)\"']+", section))
    if not has_citation:
        issues.append("executive summary contains no artifact citation")
        _log_failure(run_id, 2, "uncited_section", "Exec summary has no citation")

    if issues:
        return _result(2, "Exec summary quality", False, "; ".join(issues))
    return _result(2, "Exec summary quality", True,
                   f"{len(paragraphs)} paragraphs, diagnosis language + citation present")


def layer3_experiment_count(report: str, run_id: str) -> dict:
    # Count EXP-NN headings
    exp_matches = re.findall(r"EXP-\d{2}", report, re.IGNORECASE)
    count = len(set(exp_matches))
    if count != 10:
        _log_failure(run_id, 3, "wrong_experiment_count", f"Found {count} experiments")
        return _result(3, "Exactly 10 experiments", False,
                       f"Found {count} experiment(s) — exactly 10 required")
    return _result(3, "Exactly 10 experiments", True, "Exactly 10 experiments found")


_LIFT_RANGE_RE = re.compile(r"[+\-−]?\d+(?:\.\d+)?\s*[–\-—]\s*[+\-−]?\d+(?:\.\d+)?\s*%")
_PERCENT_RE = re.compile(r"\d+(?:\.\d+)?\s*%")
_QUALITATIVE = {"low", "medium", "high", "med"}


def _field_value(block: str, field: str) -> str:
    """Extract a markdown-table field value: | field | VALUE |."""
    m = re.search(rf"{field}\s*\|\s*([^|\n]+)", block, re.IGNORECASE)
    return m.group(1).strip() if m else ""


def layer4_experiment_fields(report: str, run_id: str) -> dict:
    # Find all experiment blocks
    blocks = re.findall(
        r"(### EXP-\d{2}.*?)(?=### EXP-\d{2}|\Z)", report, re.DOTALL | re.IGNORECASE
    )
    if not blocks:
        detail = "No experiment blocks found"
        _log_failure(run_id, 4, "missing_exp_fields", detail)
        return _result(4, "All experiment fields present", False, detail)

    missing_by_exp = {}
    bad_format = []
    for block in blocks:
        exp_id_match = re.search(r"EXP-\d{2}", block)
        exp_id = exp_id_match.group(0) if exp_id_match else "unknown"
        lower_block = block.lower()
        missing = [f for f in REQUIRED_EXP_FIELDS if f not in lower_block]
        if missing:
            missing_by_exp[exp_id] = missing
            continue

        # Enforce the numeric schema from target_report.md.
        lift = _field_value(block, "expected lift")
        conf = _field_value(block, "confidence")
        if lift.lower() in _QUALITATIVE or not _LIFT_RANGE_RE.search(lift):
            bad_format.append(f"{exp_id}: expected lift '{lift}' is not a numeric % range")
            _log_failure(run_id, 4, "non_numeric_lift", f"{exp_id}: '{lift}'")
        if conf.lower() in _QUALITATIVE or not _PERCENT_RE.search(conf):
            bad_format.append(f"{exp_id}: confidence '{conf}' is not a percentage")
            _log_failure(run_id, 4, "non_numeric_confidence", f"{exp_id}: '{conf}'")

    if missing_by_exp:
        details = "; ".join(f"{k}: missing {v}" for k, v in missing_by_exp.items())
        _log_failure(run_id, 4, "missing_exp_fields", details)
        return _result(4, "All experiment fields present", False, details)
    if bad_format:
        return _result(4, "All experiment fields present", False,
                       f"{len(bad_format)} format issue(s): " + "; ".join(bad_format[:4]))
    return _result(4, "All experiment fields present", True,
                   f"All {len(blocks)} experiments have required fields + numeric lift/confidence")


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
        # Strip trailing punctuation and markdown delimiters
        clean = raw_path.rstrip(".,;)`")

        # Cross-run contamination: path must be under this run_id
        if not clean.startswith(f"artifacts/{run_id}/"):
            cross_run.append(clean)
            continue

        # File existence check
        abs_path = run_dir / clean.replace(f"artifacts/{run_id}/", "")
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

    # Citation coverage: the exec summary and competitor sections must each carry
    # at least one citation — uncited prose is the core "trust" failure.
    def _section(name: str) -> str:
        m = re.search(rf"{name}.*?(?=\n#{{1,3}} |\Z)", report, re.DOTALL | re.IGNORECASE)
        return m.group(0) if m else ""

    def _has_artifact_citation(text: str) -> bool:
        return bool(re.search(r"artifacts/[^\s\)\"']+", text))

    uncited = []
    if not _has_artifact_citation(_section("executive summary")):
        uncited.append("executive summary")

    competitor_section = _section("competitor analysis")
    competitor_rows = [
        line for line in competitor_section.splitlines()
        if line.strip().startswith("|")
        and "---" not in line
        and "competitor" not in line.lower()
    ]
    uncited_competitors = [
        row for row in competitor_rows
        if not re.search(r"https?://|(?:www\.)?[a-z0-9-]+\.[a-z]{2,}", row, re.IGNORECASE)
    ]
    if uncited_competitors:
        uncited.append(f"{len(uncited_competitors)} competitor row(s)")

    blocks = re.findall(
        r"### EXP-\d{2}.*?(?=### EXP-\d{2}|\n## |\Z)", report, re.DOTALL | re.IGNORECASE)
    missing_evidence = []
    for block in blocks:
        evidence = _field_value(block, "evidence")
        if not evidence or ("artifacts/" not in evidence and "inferred" not in evidence.lower()):
            exp_id = re.search(r"EXP-\d{2}", block, re.IGNORECASE)
            missing_evidence.append(exp_id.group(0) if exp_id else "unknown")
    if missing_evidence:
        uncited.append(f"experiment evidence missing: {missing_evidence}")

    if uncited:
        detail = f"Sections with no citation: {uncited}"
        _log_failure(run_id, 6, "uncited_section", detail)
        return _result(6, "Evidence paths valid (no cross-run contamination)", False, detail)

    return _result(6, "Evidence paths valid (no cross-run contamination)", True,
                   f"All {len(cited_paths)} citations valid; exec summary + competitor cited")


def _normalize_cell(value: str) -> str:
    return re.sub(r"\s+", " ", value.replace("\\|", "|").strip())


def layer7_technical_checks(report: str, checks: dict | None, run_id: str) -> dict:
    if not checks:
        detail = "technical_checks.json missing or invalid"
        _log_failure(run_id, 7, "technical_mismatch", detail)
        return _result(7, "Technical checks match JSON", False, detail)
    if len(checks) != 17:
        detail = f"technical_checks.json contains {len(checks)} checks; exactly 17 required"
        _log_failure(run_id, 7, "technical_mismatch", detail)
        return _result(7, "Technical checks match JSON", False, detail)

    issues = []

    # Constrain search to the Technical Checks section to avoid false label matches elsewhere
    tech_section_match = re.search(
        r"## Technical Checks.*?(?=\n## |\Z)", report, re.DOTALL | re.IGNORECASE
    )
    if not tech_section_match:
        detail = "Technical Checks section not found"
        _log_failure(run_id, 7, "technical_mismatch", detail)
        return _result(7, "Technical checks match JSON", False, detail)

    rows: dict[str, tuple[str, str]] = {}
    for line in tech_section_match.group(0).splitlines():
        if not line.strip().startswith("|") or "---" in line:
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) >= 3 and cells[0].lower() != "check":
            rows[_normalize_cell(cells[0]).lower()] = (
                _normalize_cell(cells[1]),
                _normalize_cell("|".join(cells[2:])),
            )

    for key, check in checks.items():
        label = check.get("label", key)
        json_status = check.get("status", "")
        json_detail = check.get("detail", "")
        row = rows.get(_normalize_cell(label).lower())

        if not row:
            issues.append(f"'{label}' missing from report")
            continue

        report_status, report_detail = row
        if report_status.lower() != _normalize_cell(json_status).lower():
            issues.append(f"'{label}': JSON says '{json_status}' but not found in report row")
            _log_failure(run_id, 7, "technical_mismatch",
                         f"{label}: expected {json_status}")
        if report_detail != _normalize_cell(json_detail):
            issues.append(f"'{label}': detail does not match technical_checks.json")
            _log_failure(run_id, 7, "technical_mismatch",
                         f"{label}: detail mismatch")

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

    if len(rows) < 3 or len(rows) > 4:
        _log_failure(run_id, 8, "competitor_mismatch",
                     f"{len(rows)} competitor rows — need 3–4")
        return _result(8, "Competitor table quality", False,
                       f"{len(rows)} competitor row(s) found — need 3–4")

    # Validate the required column schema from target_report.md. The old
    # Category / Notable-CRO-strength / Relevant-to schema must fail.
    header_match = re.search(r"\|\s*competitor\s*\|[^\n]*", section_text, re.IGNORECASE)
    header = (header_match.group(0).lower() if header_match else "")
    required_cols = ["positioning", "make easier", "pattern"]
    missing_cols = [c for c in required_cols if c not in header]
    if missing_cols:
        _log_failure(run_id, 8, "competitor_mismatch",
                     f"Competitor table missing required columns: {missing_cols}")
        return _result(8, "Competitor table quality", False,
                       f"Competitor table must use the positioning / what they make easier / "
                       f"pattern-to-adapt schema. Missing: {missing_cols}")

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


_POST_PURCHASE_TERMS = [
    "order confirmation", "order-confirmation", "thank-you", "thank you",
    "post-purchase", "post purchase", "order status page", "confirmation page",
]


def layer10_uncrawled_surface(report: str, run_id: str) -> dict:
    """Flag experiments that assert post-purchase state as if observed.

    The shopping journey always stops at the checkout entry — the crawler never
    loads any order-confirmation / thank-you / post-purchase page. An experiment
    touching those surfaces is fine, but its evidence must be labeled 'inferred',
    never cited as if the surface was crawled.
    """
    blocks = re.findall(r"### EXP-\d{2}.*?(?=### EXP-\d{2}|\Z)", report, re.DOTALL | re.IGNORECASE)
    offenders = []
    for block in blocks:
        lower = block.lower()
        if any(t in lower for t in _POST_PURCHASE_TERMS):
            if "inferred" not in lower:
                exp_id = re.search(r"EXP-\d{2}", block)
                offenders.append(exp_id.group(0) if exp_id else "unknown")

    if offenders:
        detail = (f"Experiments assert post-purchase state without an 'inferred' label "
                  f"(journey stops at checkout entry): {offenders}")
        _log_failure(run_id, 10, "uncrawled_surface_claim", detail)
        return _result(10, "No claims about un-crawled surfaces", False, detail)
    return _result(10, "No claims about un-crawled surfaces", True,
                   "No experiment asserts un-crawled post-purchase state as observed")


# ---------------------------------------------------------------------------
# Crawl health (Blocked-site gating)
# ---------------------------------------------------------------------------

def _read_health_verdict(run_dir: Path) -> str:
    summary = _load_text(run_dir / "summary.md")
    if not summary:
        return "Unknown"
    m = re.search(r"crawl health:\s*([A-Za-z][A-Za-z\-]*)", summary, re.IGNORECASE)
    if not m:
        return "Unknown"
    raw = m.group(1).strip().lower()
    return {
        "healthy": "Healthy",
        "degraded": "Degraded",
        "blocked": "Blocked",
        "non-ecommerce": "Non-ecommerce",
    }.get(raw, m.group(1).strip())


def blocked_results(report: str, run_id: str, run_dir: Path) -> list[dict]:
    """Reduced eval for Blocked sites: verify an honest issues report exists
    rather than demanding a full 10-experiment audit."""
    results = []

    has_marker = any(m in report.lower() for m in
                     ["partial audit", "crawl issues", "could not be crawled",
                      "blocked", "page not found", "bot protection"])
    results.append(_result(1, "Blocked report flags the problem", has_marker,
                           "Partial-audit / crawl-issue marker " +
                           ("present" if has_marker else "MISSING")))

    summary = _load_text(run_dir / "summary.md") or ""
    lists_issues = "issues a reader should know" in summary.lower()
    results.append(_result(2, "Crawl issues documented in summary.md", lists_issues,
                           "summary.md issues section " +
                           ("present" if lists_issues else "MISSING")))

    exp_count = len(set(re.findall(r"EXP-\d{2}", report)))
    no_fab = exp_count < 10
    results.append(_result(3, "No fabricated full audit for a blocked site", no_fab,
                           f"{exp_count} experiments (a blocked site should not yield a full 10)"))

    if not has_marker:
        _log_failure(run_id, 1, "blocked_report_missing_marker",
                     "Blocked-site report does not flag the crawl problem")
    return results


# ---------------------------------------------------------------------------
# Layer 9 pre-filled prompt builder
# ---------------------------------------------------------------------------

def build_layer9_prompt(report: str, run_id: str) -> str:
    rubric = _load_text(RUBRIC_PATH) or "(rubric.md not found)"
    # Pass the FULL report — the judge must see all 10 experiments and the
    # technical section to score technical-integration and actionability.
    return f"""# /eval-judge — Layer 9 Quality Rubric

Run ID: {run_id}

## Rubric

{rubric}

## Audit Report (to evaluate)

{report}

## Instructions

Score the audit report above on all 10 rubric dimensions (1–5 each).
Output a markdown table with Score and Notes columns, a Total, and a Verdict.
Append results to eval_results/{run_id}_eval.md under ## Layer 9: Quality Rubric
"""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run_eval(run_id: str) -> int:
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
        print("[FAIL] technical_checks.json missing or invalid — Layer 7 will fail")

    evidence_summary = _load_text(run_dir / "evidence_summary.md")
    existing_eval = _load_text(eval_path) or ""
    existing_layer9 = _completed_layer9(existing_eval)

    # Crawl-health gating: only Blocked / Non-ecommerce runs get the reduced eval.
    # A Degraded run that outputs a partial report should fail the full eval.
    verdict = _read_health_verdict(run_dir)
    is_partial_report = report.lstrip().lower().startswith("# partial audit")
    blocked = verdict in ("Blocked", "Non-ecommerce") or (
        verdict == "Unknown" and is_partial_report
    )

    if blocked:
        print(f"  Crawl health: {verdict} — running reduced blocked-site eval\n")
        results = blocked_results(report, run_id, run_dir)
    else:
        results = [
            layer1_required_sections(report, run_id),
            layer2_exec_summary(report, run_id),
            layer3_experiment_count(report, run_id),
            layer4_experiment_fields(report, run_id),
            layer5_pillar_coverage(report, run_id),
            layer6_evidence_paths(report, run_id, run_dir),
            layer7_technical_checks(report, checks, run_id),
            layer8_competitor_table(report, evidence_summary, run_id),
            layer10_uncrawled_surface(report, run_id),
        ]

    # Print results
    total = len(results)
    passed = sum(1 for r in results if r["passed"])
    failed = [r for r in results if not r["passed"]]

    for r in results:
        status = "[PASS]" if r["passed"] else "[FAIL]"
        print(f"  {status} Layer {r['layer']}: {r['name']}")
        if not r["passed"]:
            print(f"         {r['detail']}")

    mode = "blocked" if blocked else "deterministic"
    print(f"\n  {passed}/{total} {mode} layers passed")

    # Build eval report
    lines = [
        f"# Eval Results: {run_id}",
        f"",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"",
        f"## Deterministic Layers" + (" (Blocked mode)" if blocked else ""),
        f"",
        f"Crawl health verdict: **{verdict}**",
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
        f"**{passed}/{total} layers passed**",
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

    if not failed and not blocked and existing_layer9:
        lines += [
            "## Layer 9: Quality Rubric",
            "",
            existing_layer9,
            "",
        ]
    elif not failed and not blocked:
        lines += [
            "## Layer 9: Quality Rubric",
            "",
            "_(Paste the pre-filled prompt below into /eval-judge to complete Layer 9)_",
            "",
        ]
    elif blocked:
        lines += [
            "## Layer 9: Quality Rubric",
            "",
            "_Not applicable to a Blocked-site partial report._",
            "",
        ]
    else:
        lines += [
            "## Layer 9: Quality Rubric",
            "",
            "_Not run because deterministic layers failed._",
            "",
        ]

    eval_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\n  Eval report saved: {eval_path}")

    if not failed and not blocked and existing_layer9:
        print("\n  Existing completed Layer 9 score preserved.")
    elif not failed and not blocked:
        layer9_prompt = build_layer9_prompt(report, run_id)
        print(f"\n{'='*60}")
        print("Layer 9 — paste this prompt to /eval-judge:")
        print(f"{'='*60}\n")
        sys.stdout.buffer.write((layer9_prompt + "\n").encode("utf-8", errors="replace"))
    elif failed:
        print("\n  Layer 9 skipped because deterministic layers failed.")
    else:
        print("\n  Layer 9 skipped for Blocked-site partial report.")

    return 1 if failed else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python evals/run_eval.py <run_id>")
        sys.exit(1)
    sys.exit(run_eval(sys.argv[1]))
