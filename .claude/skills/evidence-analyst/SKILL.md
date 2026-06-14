---
name: evidence-analyst
description: Synthesize all per-page evidence cards into a single store-level evidence_summary.md, including store_category and primary_use_cases. Use after every evidence card exists.
---

# /evidence-analyst

Synthesize all `artifacts/<run_id>/evidence_cards/*.json` + `technical_checks.json`
into `artifacts/<run_id>/evidence_summary.md`. Follow the full section spec in
`skills/evidence_analyst.md`.

Key rules:
- Extract `store_category` and `primary_use_cases` from the evidence (never hardcode).
- Every claim cites an artifact path under `artifacts/<run_id>/`.
- Cross-page patterns (a weakness on 2+ pages) are the strongest signals — weight them.
- Connect technical Fail/Warn checks to business impact in the pillar sections.
- Note evidence gaps explicitly: blocked / soft-404 pages, un-crawled surfaces
  (post-purchase), and any low-confidence inference.
