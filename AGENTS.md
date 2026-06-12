# AGENTS.md — Qosmic Audit Harness

Entry point for Codex and other OpenAI-compatible coding agents.

## Goal

Given any Shopify store URL, produce a full CRO audit report matching
`docs/target_report.md` quality. The output is `sample_output/<run_id>_audit.md`.

## Quick start

```bash
pip install -r requirements.txt
playwright install chromium
python -m crawler.crawl_store https://example-store.com
```

Then follow the pipeline in sequence:

```
1. python -m crawler.crawl_store <url>   → artifacts/<run_id>/
2. /page-evidence-extractor (per page)  → artifacts/<run_id>/evidence_cards/
3. /evidence-analyst                    → artifacts/<run_id>/evidence_summary.md
4. /audit-writer                        → sample_output/<run_id>_audit.md
5. python evals/run_eval.py <run_id>    → eval_results/<run_id>_eval.md
```

For a single command that orchestrates all steps: `/audit <url>`

## Key files

| File | Purpose |
|---|---|
| `CLAUDE.md` | Full pipeline reference (primary) |
| `docs/plan.md` | Architecture decisions |
| `docs/target_report.md` | Calibration anchor for output quality |
| `skills/audit.md` | `/audit` orchestrator spec |
| `skills/page_evidence_extractor.md` | Per-page evidence extraction spec |
| `skills/evidence_analyst.md` | Store-level synthesis spec |
| `skills/audit_writer.md` | Final report writing spec |
| `skills/eval_judge.md` | Layer 9 rubric judge spec |
| `evals/run_eval.py` | Deterministic eval layers 1–8 + Layer 9 prompt |
| `evals/rubric.md` | Scoring criteria |

## Critical constraints

1. **Never go past `/checkout` entry** — do not fill payment forms, do not place orders.
2. **Never invent artifact paths** — only cite paths that exist under `artifacts/<run_id>/`.
3. **Never change a technical check status** — copy from `technical_checks.json` verbatim.
4. **Exactly 10 experiments, all 5 pillars** — Conversion, AOV, Retention, Acquisition, Performance.
5. **run_id from `discovered_links.json`** — never construct it manually.
6. **No store-specific hardcoding** — competitors derived from `store_category` in evidence_summary, not hardcoded.

## Artifact structure

```
artifacts/<slug>_<YYYYMMDD>_<6char-uuid>/
  screenshots/          ← one per page + shopping journey steps
  pages/                ← html, md, json per page + shopping_journey.json
  evidence_cards/       ← one json per page + shopping_journey.json
  technical_checks.json ← 17 checks
  discovered_links.json ← selected_pages, run_id
  evidence_summary.md   ← store_category, primary_use_cases, findings by pillar
```

## Eval layers

| Layer | Check |
|---|---|
| 1 | Required sections present |
| 2 | Exec summary: 2–3 paragraphs with diagnosis |
| 3 | Exactly 10 experiments |
| 4 | All required fields per experiment |
| 5 | All 5 pillars present |
| 6 | Evidence paths exist on disk, all under `artifacts/<run_id>/` |
| 7 | Technical checks table matches `technical_checks.json` |
| 8 | Competitor table has 3–4 rows relevant to store_category |
| 9 | Quality rubric — paste pre-filled prompt to `/eval-judge` |
