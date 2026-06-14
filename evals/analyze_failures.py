#!/usr/bin/env python3
"""Summarize unique cross-run eval failures into skill-tightening candidates."""

import argparse
import json
from collections import defaultdict
from pathlib import Path


SKILL_BY_FAILURE = {
    "weak_hypothesis": "skills/audit_writer.md",
    "missing_evidence_citation": "skills/page_evidence_extractor.md + skills/audit_writer.md",
    "generic_experiment": "skills/audit_writer.md",
    "wrong_pillar": "skills/audit_writer.md + skills/evidence_analyst.md",
    "technical_mismatch": "skills/audit_writer.md",
    "competitor_mismatch": "skills/audit_writer.md",
    "pillar_missing": "skills/audit_writer.md",
    "exec_summary_generic": "skills/audit_writer.md",
    "cross_run_contamination": "skills/audit.md + skills/audit_writer.md",
    "missing_section": "skills/audit_writer.md",
    "uncited_section": "skills/audit_writer.md",
    "uncrawled_surface_claim": "skills/audit_writer.md",
}


def unique_failures(path: Path) -> list[dict]:
    seen = set()
    failures = []
    if not path.exists():
        return failures

    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            failure = json.loads(line)
        except json.JSONDecodeError:
            continue
        key = (
            failure.get("run_id"),
            failure.get("layer"),
            failure.get("failure_type"),
            failure.get("detail"),
        )
        if key not in seen:
            seen.add(key)
            failures.append(failure)
    return failures


def build_candidates(failures: list[dict], min_runs: int) -> list[dict]:
    grouped: dict[str, set[str]] = defaultdict(set)
    examples: dict[str, list[str]] = defaultdict(list)

    for failure in failures:
        failure_type = failure.get("failure_type", "unknown")
        grouped[failure_type].add(failure.get("run_id", "unknown"))
        detail = failure.get("detail", "")
        if detail and detail not in examples[failure_type]:
            examples[failure_type].append(detail)

    candidates = []
    for failure_type, runs in grouped.items():
        if len(runs) < min_runs:
            continue
        candidates.append({
            "failure_type": failure_type,
            "distinct_runs": len(runs),
            "skill": SKILL_BY_FAILURE.get(failure_type, "manual triage"),
            "example": examples[failure_type][0] if examples[failure_type] else "",
        })
    return sorted(candidates, key=lambda item: (-item["distinct_runs"], item["failure_type"]))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Find recurring eval failures across distinct store runs.")
    parser.add_argument(
        "--log", type=Path, default=Path(__file__).parent / "failure_log.jsonl")
    parser.add_argument("--min-runs", type=int, default=3)
    args = parser.parse_args()

    failures = unique_failures(args.log)
    candidates = build_candidates(failures, args.min_runs)

    print("# Skill-tightening candidates")
    print()
    print(f"Unique failures: {len(failures)}")
    print(f"Threshold: {args.min_runs} distinct runs")
    print()
    print("| Failure type | Distinct runs | Candidate skill | Example |")
    print("|---|---:|---|---|")
    for candidate in candidates:
        example = candidate["example"].replace("|", "\\|")[:140]
        print(
            f"| {candidate['failure_type']} | {candidate['distinct_runs']} | "
            f"{candidate['skill']} | {example} |"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
