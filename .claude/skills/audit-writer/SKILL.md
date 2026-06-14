---
name: audit-writer
description: Write the final CRO audit report (exec summary, 10 experiments across 5 pillars, 6-column competitor table, 17 technical checks) from evidence_summary.md. Use after evidence_summary.md exists.
---

# /audit-writer

Write `sample_output/<run_id>_audit.md` from `artifacts/<run_id>/evidence_summary.md`
and `technical_checks.json`. Follow the full structure and field rules in
`skills/audit_writer.md`.

Contract (must match `docs/target_report.md`):
- The report contains exactly four H2 sections in this order: Executive Summary,
  Proposed Experiments, Competitor Analysis, Technical Checks.
- Executive summary is prose and contains ≥1 inline citation backing the diagnosis.
- Exactly 10 experiments spanning all 5 pillars (Conversion, AOV, Retention,
  Acquisition, Performance).
- `Expected lift` is a numeric range (e.g. `+8–15%`); `Confidence` is a percentage
  (e.g. `72%`). Never Low/Medium/High.
- Competitor table uses the 6-column schema:
  `Competitor | Domain | Positioning | What they make easier | <Store> edge | Pattern to adapt`.
- All 17 technical checks reproduced verbatim from `technical_checks.json` (never
  upgrade a Warn/Fail to Pass).
- Never assert the state of an un-crawled surface (post-purchase / thank-you /
  account). Such experiments use `Evidence: inferred — journey stops at checkout entry`.
