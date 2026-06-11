# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Qosmic Audit Harness — a generic Shopify CRO audit agent. Given any Shopify URL, produce a full audit report (executive summary, 10 experiments across 5 pillars, competitor analysis, 17 technical checks) matching `docs/target_report.md` quality.

**Reference files:**
- `docs/plan.md` — full build plan with all architecture decisions
- `docs/README.md` — original assignment brief
- `docs/target_report.md` — calibration anchor for output quality

## Current State

Completed phases:
- [x] Phase 0 — CLAUDE.md + repo structure
- [x] Phase 1 — Crawler (modular: `crawler/crawl_store.py`, `utils.py`, `url_discovery.py`, `technical_checks.py`, `page_crawler.py`, `shopping_journey.py`) — tested on 4 stores, 5 bugs fixed
- [x] Phase 2 — Skills (`skills/audit.md`, `skills/page_evidence_extractor.md`, `skills/evidence_analyst.md`, `skills/audit_writer.md`, `skills/eval_judge.md`)
- [x] Phase 3 — Eval (`evals/run_eval.py`, `evals/rubric.md`)
- [x] Phase 4 — Agent docs (`AGENTS.md`, `EVAL_LOOP.md`)
- [ ] Phase 5 — Sample runs (in progress — see below)

## Phase 5 Status (Resume Here)

Testing each phase on 4 diverse stores: zenrojas.com, beardbrand.com, deathwishcoffee.com, mudwtr.com

### Phase 1 test: COMPLETE (all 4 stores crawled, bugs fixed, committed)

Crawl artifacts exist at:
- `artifacts/zenrojas_20260611_e275e3/` — tea/beverages, 11/11 pages, 5.0/5 friction
- `artifacts/beardbrand_20260611_fbafd8/` — men's grooming, 11/11 pages, 4.5/5 friction
- `artifacts/deathwishcoffee_20260611_5362ac/` — coffee, 10/11 pages, 5.0/5 friction
- `artifacts/mudwtr_20260611_df56a4/` — wellness/subscription, 11/11 pages, 5.0/5 friction

### Phase 2 test: IN PROGRESS

Evidence cards written for zenrojas (`artifacts/zenrojas_20260611_e275e3/evidence_cards/` — 12 cards):
- [x] homepage_0_home.json
- [x] product_page_1_products_tea-bags.json
- [x] product_page_2_products_blacktea.json
- [x] product_page_3_products_tea-seeper.json
- [x] cart_page_4_cart.json
- [x] collection_page_5_collections_all.json
- [x] collection_page_6_collections_teas.json
- [x] where_to_buy_7_pages_where-to-buy.json
- [x] faq_shipping_returns_8_pages_faq.json
- [x] about_page_9_pages_about.json
- [x] blog_or_content_page_10_blogs_weekly-blog_building-a-family-lega.json
- [x] shopping_journey.json

**Next step:** Run `/evidence-analyst` on zenrojas → write `artifacts/zenrojas_20260611_e275e3/evidence_summary.md`
**Then:** Run `/audit-writer` → write `sample_output/zenrojas_20260611_e275e3_audit.md`
**Then:** Run `python evals/run_eval.py zenrojas_20260611_e275e3`
**Then:** Repeat Phase 2 pipeline for beardbrand, deathwishcoffee, mudwtr

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
| cookie_privacy | Cookie/Privacy |
| broken_links | Broken Links |
| image_optimization | Image Optimization |
| mobile_friendly | Mobile-Friendly |
| page_speed_mobile | Page Speed Mobile |
| page_speed_desktop | Page Speed Desktop |
| critical_pages_loading | Critical Pages Loading |
| checkout_reachable | Checkout Reachable |
| shopping_journey | Shopping Journey |
| payment_methods | Payment Methods |

## Phase 1 Bug Fixes (committed)

Five bugs found during multi-store testing and fixed:
1. `mailto:` links being selected as pages — now filtered in url_discovery.py
2. www/non-www duplicate URLs — deduplicated by path key
3. Subdomain leakage (careers.mudwtr.com) — exact netloc match now enforced
4. body_too_short blocking JS-heavy pages — one retry with +3s wait added
5. Add-to-cart fails on non-buyable first PDP — now tries all PDPs before flagging failure

## Known Limitations

- **Allbirds-class stores** (heavy SPA + bot protection like Imperva) block all pages — not fixable at crawler level
- **Gingerpeople.com** blocks non-homepage pages with Cloudflare — revisit later

## claude-mem Plugin Issue

The claude-mem plugin hooks are registered in **global** settings at `C:\Users\sharm\.claude\settings.json` (not project settings). To remove: open that file, delete hook entries referencing `thedotmack/claude-mem` or `bun-runner.js`. These hooks were causing the Read tool to be blocked during this session.
