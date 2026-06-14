# EVAL_LOOP.md - Autonomous Improvement Plan

The eval loop treats every audit as a traceable training example:

```text
crawl + report -> fail-closed deterministic eval -> quality judge
-> deduplicated failure taxonomy -> candidate skill change
-> held-out store evaluation -> promote or roll back
```

## Current Foundation

`evals/run_eval.py` checks the exact report contract, experiment schema, pillar
coverage, evidence existence, technical status/detail fidelity, competitor
schema, and unobserved-surface claims. Failed deterministic checks return a
non-zero exit and block Layer 9.

Each unique failure is appended once to `evals/failure_log.jsonl`. Run:

```bash
python evals/analyze_failures.py --min-runs 3
```

This proposes skill-tightening candidates only when a failure repeats across
distinct stores. Re-running one bad audit cannot inflate the signal.

## Month 1 - Establish Trusted Baselines

- Maintain a versioned suite covering normal Shopify stores, blocked stores,
  unusual domains, and non-Shopify adversarial sites.
- Store audit, artifacts, eval result, skill version, and runtime version
  together for every baseline.
- Humans review deterministic-eval changes and score a stratified sample with
  Layer 9. Disagreements become new deterministic checks or rubric examples.
- Track false-positive and false-negative rates for every evaluator layer.

## Month 2 - Candidate/Champion Loop

- A recurring cross-store failure generates a candidate skill patch and a
  focused regression test.
- Run champion and candidate skills against held-out stores not used to propose
  the patch.
- Promote only when the candidate improves the target failure without reducing
  evidence validity, contract pass rate, or Layer 9 score.
- Commit every promoted change with before/after evals. Automatically roll back
  regressions.

The system may regenerate only a failed report section after deterministic
validation. It never auto-edits crawler safety rules or promotes its own skill
change without held-out evidence.

## Month 3 - Outcome Calibration

- Join merchant A/B outcomes to experiment type, evidence pattern, expected
  lift, and confidence.
- Recalibrate confidence and expected-lift guidance from observed results.
- Route novel categories, low evidence coverage, evaluator disagreement, and
  safety-sensitive changes to humans.
- Shrink review by demonstrated reliability per category, not by elapsed time.

## Human Surface

| Stage | Human responsibility |
|---|---|
| Month 1 | Validate evaluator correctness and review low-scoring audits |
| Month 2 | Approve candidate promotion when held-out results are ambiguous |
| Month 3 | Review novel categories, safety changes, and outcome anomalies |

The target is not zero humans. It is a small, auditable approval surface around
novelty and risk, while repetitive quality failures are detected, tested, and
corrected automatically.
