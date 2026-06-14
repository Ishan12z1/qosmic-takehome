# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Qosmic Audit Harness — a generic Shopify CRO audit agent. Given any Shopify URL, produce a full audit report (executive summary, 10 experiments across 5 pillars, competitor analysis, 17 technical checks) matching `docs/target_report.md` quality.

**Reference files:**
- `docs/plan.md` — full build plan with all architecture decisions
- `docs/README.md` — original assignment brief
- `docs/target_report.md` — calibration anchor for output quality

## Current State

Runtime and evaluator hardening is implemented, with regression tests under
`tests/`. The project is not submission-ready until fresh required-target reports
and their cited verification artifacts are packaged, and the user-authored
deliverables are completed.

Health policy:
- Healthy and Degraded crawls continue to a full audit; Degraded reports must
  label evidence gaps and cite `summary.md`.
- Blocked crawls produce only an honest partial crawl-issues report.

Current submission runs:

| Store | Run ID | Crawl health | Eval |
|---|---|---|---|
| zenrojas.com | `zenrojas_20260613_b07d01` | Healthy, 10/10 observed pages | 9/9 deterministic, Layer 9 48/50 |
| gingerpeople.com | `gingerpeople_20260613_5bcc0b` | Blocked by bot protection | 3/3 Blocked-site checks |

Completed phases:
- [x] Phase 0 — CLAUDE.md + repo structure
- [x] Phase 1 — Crawler (modular: `crawler/crawl_store.py`, `utils.py`, `url_discovery.py`, `technical_checks.py`, `page_crawler.py`, `shopping_journey.py`) — tested on 5 stores, 5 bugs fixed
- [x] Phase 2 — Skills (`skills/audit.md`, `skills/page_evidence_extractor.md`, `skills/evidence_analyst.md`, `skills/audit_writer.md`, `skills/eval_judge.md`)
- [x] Phase 3 — Eval (`evals/run_eval.py`, `evals/rubric.md`) — 4 bugs fixed
- [x] Phase 4 — Agent docs (`AGENTS.md`, `EVAL_LOOP.md`) — crawler command bug fixed in 4 doc files
- [x] Phase 5 — Sample runs (5 stores, 8/8 eval layers each)
- [x] Phase 6 — Layer 9 quality rubric scored (tentree: 44/50 — Good)
- [x] Phase 7 — Eval website list (17 sites across 4 types, `docs/eval_website_list.md`)

## Historical Run History

These are historical calibration records. Re-run the current evaluator before
using any score as a submission claim.

| Store | run_id | Pages | Friction | Layer 1–8 | Layer 9 |
|---|---|---|---|---|---|
| zenrojas.com | zenrojas_20260611_e275e3 | 11/11 | 5.0/5 | 8/8 Pass | not scored |
| beardbrand.com | beardbrand_20260611_fbafd8 | 11/11 | 4.5/5 | 8/8 Pass | not scored |
| deathwishcoffee.com | deathwishcoffee_20260611_5362ac | 10/11 | 5.0/5 | 8/8 Pass | not scored |
| mudwtr.com | mudwtr_20260611_df56a4 | 11/11 | 5.0/5 | 8/8 Pass | not scored |
| tentree.com | tentree_20260611_72bf40 | 11/11 | 5.0/5 | 8/8 Pass | **44/50 Good** |
| gingerpeople.com | gingerpeople_20260611_5f1b85 | 1/10 | 2.0/5 | blocked | n/a |

## Layer 9 Score Detail (tentree — 44/50)

`eval_results/tentree_20260611_72bf40_eval.md` contains full scored rubric.

| Dimension | Score | Issue |
|---|---|---|
| Diagnosis sharpness | 4/5 | Leads with technical gap not funnel constraint |
| Hypothesis quality | 4/5 | EXP-10 bundles two unrelated changes |
| Evidence grounding | 5/5 | All 26 citations verified |
| Pillar balance | 5/5 | Exactly 2 per pillar |
| Competitor relevance | 5/5 | All 4 in sustainable apparel, tied to experiments |
| Experiment specificity | 4/5 | EXP-10 bundles two unrelated tasks |
| Technical integration | 4/5 | Mobile-Friendly Warn not acknowledged |
| Exec summary quality | 4/5 | Para 1 leads with strengths, not diagnosis |
| AOV/Retention depth | 5/5 | Store-specific throughout |
| Overall actionability | 4/5 | EXP-06 needs backend data integration |

### 3 fixes to reach 45+ (not yet applied to tentree audit)

1. **Split EXP-10** into EXP-10a (cookie consent) and EXP-10b (Lighthouse) — fixes Hypothesis quality + Experiment specificity (+2 pts)
2. **Flip exec summary para 1** to lead with OG tag diagnosis, move strengths to para 3 — fixes Exec summary quality (+1 pt)
3. **Acknowledge Mobile-Friendly Warn** in EXP-10b or Technical Checks section — fixes Technical integration (+1 pt)

Applying all 3 would bring tentree to ~48/50 (Excellent).

## Gingerpeople Status (confirmed)

`artifacts/gingerpeople_20260611_5f1b85/` — Cloudflare blocks everything except homepage.
- 1/10 pages crawled, 9 `bot_challenge_detected`
- Retailer-routed, friction 2.0/5, 0 payment methods detected
- **No audit producible** — insufficient evidence (only homepage)
- Document this as a known limitation in submission: "gingerpeople.com blocked by Cloudflare; zenrojas.com serves as the calibration generalization run"

## Eval Website List (`docs/eval_website_list.md`)

17 sites across 4 types for ongoing harness validation:
- **Type A (5):** zenrojas, beardbrand, deathwishcoffee, mudwtr, tentree — all validated baselines
- **Type B (3):** graza.co, puravidabracelets.com, chubbiesshorts.com — new Shopify targets
- **Type C (3):** gingerpeople.com (confirmed blocked), allbirds.com, gymshark.com — edge cases
- **Type D (3):** patagonia.com, warbyparker.com, rei.com — non-Shopify ecommerce
- **Type E (3):** stripe.com, wikipedia.org, vercel.com — non-ecommerce adversarial

## Submission Readiness

### Completed (harness)
- [x] Runtime harness with explicit Healthy / Degraded / Blocked policy
- [x] Safe shopping journey that stops at checkout entry
- [x] Fail-closed deterministic eval + Layer 9 rubric
- [x] Regression tests for critical crawler/evaluator behavior
- [x] `EVAL_LOOP.md` — autonomy plan written
- [x] `evals/failure_log.jsonl` — deduplicated live failure accumulation
- [x] `docs/eval_website_list.md` — 17-site test matrix

### Required before submission
- [ ] Generate fresh Zen Rojas evidence cards, evidence summary, exact four-section
  audit, deterministic eval, and Layer 9 score.
- [ ] Package every artifact cited by submitted reports.
- [ ] Re-run every submitted sample with the current evaluator and remove stale reports.

### User still needs to write/record
- [ ] `AGENT_LOG.md` — time per part, prompts fed, where Claude drove vs. you took the wheel
- [ ] `WORKFLOWS.md` — how you use coding agents day-to-day (tool stack, delegation patterns)
- [ ] Loom video (3–5 min) — walk through harness + eval loop; one decision you'd reverse; one unmeasured dimension that matters. Email link to trustin@qosmic.ai

### Current output contract
- Exactly four H2 sections: Executive Summary, Proposed Experiments, Competitor
  Analysis, Technical Checks.
- Expected lift and confidence are numeric.
- Competitor analysis uses the six-column target schema.

## Bug Fixes Log

**Phase 1 — Crawler (5 bugs):**
1. `mailto:` links selected as pages → filtered in url_discovery.py
2. www/non-www duplicate URLs → deduplicated by path key
3. Subdomain leakage (careers.mudwtr.com) → exact netloc match enforced
4. body_too_short blocking JS-heavy pages → retry with +3s wait
5. Add-to-cart fails on non-buyable first PDP → tries all PDPs before flagging

**Phase 3 — Eval (4 bugs):**
1. Layer 6 path resolution: `run_dir.parent` → `run_dir`
2. Layer 6 backtick stripping: added backtick to rstrip
3. Layer 7 first-occurrence: search only within `## Technical Checks` section
4. Layer 9 Unicode crash on Windows cp1252: use `sys.stdout.buffer.write` with utf-8

**Phase 4 — Doc fixes (4 files, same bug):**
- `python crawler/crawl_store.py` → `python -m crawler.crawl_store` (ImportError on direct invocation)
- Fixed in: CLAUDE.md (2 places), AGENTS.md (2 places), skills/audit.md (1 place)
- Also fixed: `skills/audit_writer.md` pillar distribution ("minimum 3 Conversion" → "2 per pillar")

## How to Run an Audit

```bash
# Install dependencies (once)
pip install -r requirements.txt
playwright install chromium

# Step 1 — Crawl (creates artifacts/<slug>_<YYYYMMDD>_<uuid>/)
python -m crawler.crawl_store https://example-store.com

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
python -m crawler.crawl_store → artifacts/<run_id>/
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

**Retry safety:** The crawler reuses the newest usable complete crawl. `--force`
creates a fresh run.

**Shopping journey limit:** Never go past `/checkout` entry. Never fill forms. Never place orders.

**17 technical checks:** 15 standard + `shopping_journey` + `payment_methods`. Report table must match `technical_checks.json` exactly.

**Exactly 10 experiments:** All 5 pillars required — Conversion, AOV, Retention, Acquisition, Performance.

**Modular code:** No single file should exceed 500 lines. Split at logical boundaries when approaching that limit.

## Eval Layers

| Layer | Check |
|---|---|
| 1 | Exactly four required sections, in order |
| 2 | Exec summary is 2–3 paragraphs with diagnosis |
| 3 | Exactly 10 experiments |
| 4 | All required fields in every experiment |
| 5 | All 5 pillars present |
| 6 | Evidence paths exist on disk and under `artifacts/<run_id>/` (cross-run contamination check) |
| 7 | All 17 technical statuses and details match `technical_checks.json` |
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
