# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Qosmic Audit Harness — a generic Shopify CRO audit agent. Given any Shopify URL, produce a full audit report (executive summary, 10 experiments across 5 pillars, competitor analysis, 17 technical checks) matching `docs/target_report.md` quality.

**Reference files:**
- `docs/plan.md` — full build plan with all architecture decisions
- `docs/README.md` — original assignment brief
- `docs/target_report.md` — calibration anchor for output quality

## Current State

Planning complete. Implementation in progress.

Completed phases:
- [x] Phase 0 — CLAUDE.md + repo structure
- [x] Phase 1 — Crawler (modular: `crawler/crawl_store.py`, `utils.py`, `url_discovery.py`, `technical_checks.py`, `page_crawler.py`, `shopping_journey.py`)
- [x] Phase 2 — Skills (`skills/audit.md`, `skills/page_evidence_extractor.md`, `skills/evidence_analyst.md`, `skills/audit_writer.md`, `skills/eval_judge.md`)
- [x] Phase 3 — Eval (`evals/run_eval.py`, `evals/rubric.md`)
- [x] Phase 4 — Agent docs (`AGENTS.md`, `EVAL_LOOP.md`)
- [ ] Phase 5 — Sample runs (zenrojas full pipeline, gingerpeople if CF resolved)

## How to Run an Audit

```bash
# Install dependencies (once)
pip install -r requirements.txt
playwright install chromium

# Step 1 — Crawl (creates artifacts/<slug>_<YYYYMMDD>_<uuid>/)
python crawler/crawl_store.py https://example-store.com

# Step 2 — Full pipeline (in Claude Code)
/audit https://example-store.com

# Step 3 — Deterministic eval
python evals/run_eval.py <run_id>
```

Re-running is safe — completed artifacts are skipped. Use `--force` to overwrite everything.

## Pipeline

```
/audit <url>
  ↓
crawler/crawl_store.py       → artifacts/<run_id>/
  ↓
/page-evidence-extractor     → evidence_cards/<page>.json  (one per page + shopping_journey.json)
  ↓
/evidence-analyst            → evidence_summary.md  (includes store_category + primary_use_cases)
  ↓
/audit-writer                → sample_output/<run_id>_audit.md
  ↓
evals/run_eval.py            → eval_results/<run_id>_eval.md  (+ Layer 9 pre-filled prompt)
  ↓
/eval-judge (Layer 9)        → quality rubric scores appended to eval result
  ↓
Fix only failed sections → re-eval
```

## Artifact Structure

Every run creates: `artifacts/<slug>_<YYYYMMDD>_<6char-uuid>/`

```
artifacts/<run_id>/
  screenshots/           ← one per crawled page + shopping journey screens
  pages/                 ← <name>.html, <name>.md, <name>.json per page
  evidence_cards/        ← <name>.json per page + shopping_journey.json
  technical_checks.json  ← 17 checks: 15 standard + shopping_journey + payment_methods
  discovered_links.json  ← all links, selected_pages, run_id, blocked pages
  evidence_summary.md    ← store_category, primary_use_cases, findings by pillar
```

## Skills Reference

| Skill | When to invoke |
|---|---|
| `/audit <url>` | Start a full audit run |
| `/page-evidence-extractor` | After crawl, for each page in `selected_pages` |
| `/evidence-analyst` | After all evidence cards exist |
| `/audit-writer` | After `evidence_summary.md` exists |
| `/eval-judge` | After `run_eval.py` outputs the Layer 9 prompt |

## Critical Rules

**Citations:** Every audit claim must cite `artifacts/<run_id>/...` path or a URL. No exceptions.

**No hallucination:** Never invent screenshots or technical check results. If a check was not performed, mark `Warn` — never `Pass`.

**No hardcoding:** No store names, competitor names, or category-specific logic in skills or scripts. `store_category` is extracted by the evidence analyst from crawled evidence.

**Retry safety:** Each pipeline step checks if its output artifact already exists and skips if present. `--force` overwrites.

**Shopping journey limit:** Never go past `/checkout` entry. Never fill forms. Never place orders.

**17 technical checks:** 15 standard + `shopping_journey` + `payment_methods`. Report table must match `technical_checks.json` exactly.

**Exactly 10 experiments:** All 5 pillars required — Conversion, AOV, Retention, Acquisition, Performance.

**Modular code:** No single file should exceed 500 lines. Split at logical boundaries when approaching that limit.

## Eval Layers

| Layer | Check |
|---|---|
| 1 | Required sections present |
| 2 | Exec summary is 2–3 paragraphs with diagnosis |
| 3 | Exactly 10 experiments |
| 4 | All required fields in every experiment |
| 5 | All 5 pillars present |
| 6 | Evidence paths exist on disk and under `artifacts/<run_id>/` (cross-run contamination check) |
| 7 | Technical checks table matches `technical_checks.json` (all 17) |
| 8 | Competitor table has 3–4 rows relevant to `store_category` |
| 9 | Quality rubric — pre-filled prompt output, paste to `/eval-judge` |

## 17 Technical Checks

| Key | Label |
|---|---|
| ssl_certificate | SSL Certificate |
| https_redirect | HTTPS Redirect |
| sitemap | Sitemap |
| robots_txt | Robots.txt |
| meta_tags_social | Meta Tags & Social Previews |
| structured_data | Structured Data |
| favicon | Favicon |
| cookie_privacy | Cookie / Privacy |
| broken_links | Broken Links |
| image_optimization | Image Optimization |
| mobile_friendly | Mobile-Friendly |
| page_speed_mobile | Page Speed Mobile |
| page_speed_desktop | Page Speed Desktop |
| critical_pages_loading | Critical Pages Loading |
| checkout_reachable | Checkout Reachable |
| shopping_journey | Shopping Journey |
| payment_methods | Payment Methods |
