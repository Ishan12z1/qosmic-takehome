# EVAL_LOOP.md — Autonomy Plan

How the Qosmic Audit Harness improves itself over time using a failure taxonomy
feedback loop.

---

## Core mechanism

Every eval failure is tagged with a failure type and appended to
`evals/failure_log.jsonl`. The most common failure types drive automatic
tightening of the relevant skill instructions.

```
eval run → failures tagged → failure_log.jsonl → top failure types → skill instructions tightened
```

---

## Failure taxonomy

| Tag | What it means | Skill to tighten |
|---|---|---|
| `weak_hypothesis` | Hypothesis doesn't follow "X→Y because Z (evidence)" | `audit_writer.md` |
| `missing_evidence_citation` | Observation has no artifact path | `page_evidence_extractor.md`, `audit_writer.md` |
| `generic_experiment` | Primary change is vague ("improve UX", "add social proof") | `audit_writer.md` |
| `wrong_pillar` | Experiment tagged to wrong pillar | `audit_writer.md`, `evidence_analyst.md` |
| `technical_mismatch` | Report status differs from `technical_checks.json` | `audit_writer.md` |
| `competitor_mismatch` | Competitors don't match store_category | `evidence_analyst.md`, `audit_writer.md` |
| `pillar_missing` | One of 5 pillars absent from experiments | `audit_writer.md` |
| `exec_summary_generic` | Exec summary could apply to any store | `audit_writer.md` |
| `cross_run_contamination` | Evidence paths reference a different run_id | `audit.md`, `audit_writer.md` |
| `missing_section` | Required report section absent | `audit_writer.md` |

---

## Month 1 — Baseline

- Run deterministic eval (Layers 1–8) + manual Layer 9 rubric on all audit outputs.
- Human reviews all low-scoring audits (total < 35/50).
- Build failure taxonomy by tagging every failure in `failure_log.jsonl`.
- Identify the top 3 most common failure types across all runs.

---

## Month 2 — Auto-tighten

- Read `failure_log.jsonl` to count failure type frequency.
- For any failure type that fires 5+ times: update the relevant skill's instruction
  with a stricter rule or additional example.

Example tightening triggers:
- `generic_experiment` fires 8× → `audit_writer.md` gets: "Every 'Primary change' must
  name the exact element (e.g. 'star rating widget below product title'), not a category
  ('improve social proof')."
- `weak_hypothesis` fires 6× → `audit_writer.md` gets a required template with a
  filled example.
- `cross_run_contamination` fires 3× → `audit.md` gets an explicit cross-check step
  before saving the report.

For any section that failed Layer 1–8 deterministic checks: auto-regenerate only that
section (not the full report). Re-run eval to confirm fix.

Track skill instruction versions in git — each tightening is a separate commit with
the failure count that triggered it.

---

## Month 3 — Confidence calibration

- Merchant A/B test outcomes feed back as ground truth where available.
- Experiment types that consistently underperform expected lift get downweighted
  in the `Expected lift` field guidance.
- Human review scope shrinks: only audits with confidence < 70% or novel
  `store_category` values require review.
- Novel categories (not seen in prior runs) flag for human review automatically
  since competitor selection is untested.

---

## Human review surface over time

| Stage | What humans review |
|---|---|
| Month 1 | All audits scoring < 35/50 on Layer 9 |
| Month 2 | Audits with 2+ deterministic layer failures |
| Month 3 | Only low-confidence audits and novel store categories |

---

## failure_log.jsonl format

Each line is one JSON object:

```json
{
  "run_id": "zenrojas_20260611_e275e3",
  "timestamp": "2026-06-11T14:23:01",
  "layer": 4,
  "failure_type": "missing_exp_fields",
  "detail": "EXP-07: missing ['decision rule', 'confidence']"
}
```

Used by: human reviewers, future auto-tighten scripts, confidence calibration.
