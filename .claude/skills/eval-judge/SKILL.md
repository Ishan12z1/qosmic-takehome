---
name: eval-judge
description: Score a completed audit report on the 10-dimension Layer 9 quality rubric (1–5 each) and append the result to the eval file. Use after run_eval.py prints the pre-filled Layer 9 prompt.
---

# /eval-judge

Score the audit report on the 10-dimension Layer 9 quality rubric. Follow
`skills/eval_judge.md` and `evals/rubric.md`.

- Input: the pre-filled prompt printed by `python evals/run_eval.py <run_id>`
  (it contains the full report and the rubric).
- Output: append a `## Layer 9: Quality Rubric` table (Dimension | Score | Notes),
  a Total /50, and a Verdict to `eval_results/<run_id>_eval.md`.
- Penalise any experiment that asserts the state of an un-crawled surface
  (post-purchase / thank-you) as if observed, and any qualitative (non-numeric)
  expected-lift or confidence value.
