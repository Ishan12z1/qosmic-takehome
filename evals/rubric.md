# Eval Rubric — Qosmic Audit Harness

Used by `/eval-judge` (Layer 9) to score a completed audit report.
Each dimension is scored 1–5. Total possible: 50 points.

## Dimensions

| # | Dimension | What it measures |
|---|---|---|
| 1 | Diagnosis sharpness | Is the main conversion problem named precisely with evidence? |
| 2 | Hypothesis quality | Do hypotheses follow "X will improve Y because Z (evidence)"? |
| 3 | Evidence grounding | Is every claim backed by a cited artifact path or URL? |
| 4 | Pillar balance | Are all 5 pillars represented without one dominating? |
| 5 | Competitor relevance | Do competitors reflect the store's actual category and use cases? |
| 6 | Experiment specificity | Are "Primary change" fields actionable enough to brief a developer? |
| 7 | Technical integration | Are Fail/Warn checks connected to experiments or acknowledged? |
| 8 | Exec summary quality | Does the exec summary lead with diagnosis and avoid generic statements? |
| 9 | AOV/Retention depth | Are AOV and Retention experiments store-specific, not generic? |
| 10 | Overall actionability | Can ≥8/10 experiments be A/B tested in one sprint without further research? |

## Score anchors (apply to all dimensions)

| Score | Meaning |
|---|---|
| 5 | Excellent — no meaningful gaps |
| 4 | Good — minor gap that doesn't affect usability |
| 3 | Acceptable — noticeable gap but core requirement met |
| 2 | Weak — partial coverage or significant gap |
| 1 | Failing — requirement not met or actively misleading |

## Verdict thresholds

| Total | Verdict |
|---|---|
| 45–50 | Excellent — ship |
| 38–44 | Good — minor fixes before shipping |
| 28–37 | Needs work — address weak dimensions and re-eval |
| < 28 | Rework required — re-run /audit-writer after strengthening evidence_summary |

## Common failure patterns (for triage)

| Failure type | Typical cause | Fix |
|---|---|---|
| `weak_hypothesis` | Hypothesis doesn't follow "X→Y because Z" | Rewrite using observed evidence |
| `missing_evidence_citation` | Observation has no artifact path | Add screenshot or HTML path from run artifacts |
| `generic_experiment` | Primary change is "improve UX" or "add social proof" without specifics | Name the exact widget, placement, copy change |
| `wrong_pillar` | Experiment tagged to wrong pillar | Reclassify based on primary KPI |
| `technical_mismatch` | Report status differs from technical_checks.json | Read JSON again, copy verbatim |
| `competitor_mismatch` | Competitors don't match store_category | Re-derive from evidence_summary store_category |
| `pillar_missing` | One of 5 pillars has zero experiments | Add experiment for missing pillar |
| `exec_summary_generic` | Exec summary could apply to any store | Add store-specific diagnosis with artifact citation |
| `cross_run_contamination` | Evidence paths point to a different run_id | Replace with correct run_id paths |
