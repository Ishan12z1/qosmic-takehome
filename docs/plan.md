# Qosmic Audit Harness — Build Plan (v2, refined)

## Goal

Build a generic Shopify CRO audit agent harness. Any coding agent (Claude Code, Codex, or future agents) handed this repo and a Shopify URL should produce a full audit report matching `docs/target_report.md` quality.

**Input:** any Shopify storefront URL  
**Output:** one markdown audit report per run containing — executive summary, 10 proposed experiments (all 5 pillars), competitor analysis, technical checks table  

Validated on two example runs:
- `gingerpeople.com` — calibration target (output should approach `target_report.md`)
- `zenrojas.com` — generalization target (zero gingerpeople assumptions)

The harness must generalize to **any** Shopify store. No store-specific logic anywhere.

---

## Architecture Decisions (locked)

| Decision | Answer |
|---|---|
| Reasoning stages | Agent-driven — Claude Code skills (markdown prompt files), no programmatic LLM API calls |
| Browser automation | Playwright + `playwright-stealth` (one extra line; legally sound for public page auditing) |
| Shopping journey | PDP → add-to-cart → cart → `/checkout` entry → stop. Never fill forms or enter payment details |
| Page discovery | `/sitemap.xml` + Shopify standard paths + homepage nav link extraction |
| Page selection | Type-quota sampling, priority order, 12-page hard cap |
| Artifact naming | `artifacts/<slug>_<YYYYMMDD>_<6char-uuid>/` — unique per run, never overwrites |
| Retry safety | File-existence checks — skip completed artifacts on re-run. `--force` flag overwrites all |
| Eval LLM judge | `run_eval.py` outputs a pre-filled Layer 9 prompt — agent or human pastes it, never silently skipped |
| Technical checks | 17 total: 15 standard + `shopping_journey` + `payment_methods` |
| Generalization | Fully generic — `store_category` and `primary_use_cases` extracted by evidence analyst and used by audit writer for competitor selection |
| Entry point | `/audit <url>` orchestrator skill + `CLAUDE.md` |

---

## Repo Structure

```
takehome/                                  ← harness at root; docs/ is reference material only
  CLAUDE.md                                ← pipeline reference + rules for any agent
  AGENTS.md                                ← same, Codex entry-point format
  README.md
  EVAL_LOOP.md                             ← autonomy plan (agent drafts)
  requirements.txt

  crawler/
    crawl_store.py                         ← Playwright + stealth + requests; deterministic only

  skills/
    audit.md                               ← /audit <url> — orchestrator
    page_evidence_extractor.md             ← /page-evidence-extractor
    evidence_analyst.md                    ← /evidence-analyst
    audit_writer.md                        ← /audit-writer
    eval_judge.md                          ← /eval-judge (Layer 9 rubric)

  evals/
    run_eval.py                            ← deterministic Layers 1–8 + pre-filled Layer 9 prompt
    rubric.md                              ← scoring criteria for /eval-judge
    failure_log.jsonl                      ← accumulates failure tags across all runs

  artifacts/
    <slug>_<YYYYMMDD>_<uuid>/              ← one folder per run, any store
      screenshots/
        homepage.png
        product_1.png
        ...
        shopping_journey_pdp.png
        shopping_journey_cart.png
        shopping_journey_checkout.png      ← or shopping_journey_retailer.png if retailer-routed
      pages/
        homepage.md
        homepage.html
        homepage.json
        ...
        shopping_journey.json              ← journey metadata, friction score, observations
      evidence_cards/
        homepage.json
        product_1.json
        ...
        shopping_journey.json              ← special journey evidence card
      technical_checks.json               ← 17 checks
      discovered_links.json               ← all links, selected_pages, run_id, blocked pages

  sample_output/
    <run_id>_audit.md                      ← one per run

  eval_results/
    <run_id>_eval.md                       ← one per run
```

---

## Phase 1 — Crawler (`crawler/crawl_store.py`)

### Invocation

```bash
python crawler/crawl_store.py <url>          # skips completed artifacts
python crawler/crawl_store.py <url> --force  # overwrites everything
```

### Startup

1. Derive slug from URL hostname — strip `www.`, `shop.`, extract root domain  
   (`https://www.gingerpeople.com` → `gingerpeople`)
2. Generate `run_id = <slug>_<YYYYMMDD>_<6char-uuid>`
3. Create `artifacts/<run_id>/` directory tree
4. Write `run_id` to `discovered_links.json` immediately
5. If artifacts exist and no `--force`: skip any step whose output file already exists (retry-safe)

### Dependencies (`requirements.txt`)

```
playwright
playwright-stealth
beautifulsoup4
lxml
requests
markdownify
```

After install: `playwright install chromium`

### Technical Checks (deterministic, via `requests`)

Run these first — no browser needed.

| Check | Method |
|---|---|
| SSL Certificate | Load `https://<store>` — Pass if succeeds |
| HTTPS Redirect | Load `http://<store>` — Pass if redirects to HTTPS |
| Sitemap | Fetch `/sitemap.xml` — Pass/Warn/Fail |
| Robots.txt | Fetch `/robots.txt` — Pass/Warn/Fail |
| Meta Tags & Social Previews | Inspect sampled page HTML for `<title>`, `<meta name="description">`, `og:title`, `og:description`, `canonical` |
| Structured Data | Inspect HTML for `application/ld+json`, Product/Organization/Breadcrumb schema |
| Favicon | Check `<link rel="icon">` or `/favicon.ico` |
| Broken Links | Sample 30–50 internal links; Pass = none broken, Warn = minor, Fail = /cart or nav broken |
| Image Optimization | Basic: large assets (>500KB), missing alt text — Warn if not deeply measured |
| Cookie/Privacy | Check footer/header for Privacy Policy, Terms, CCPA/Do Not Sell |
| Mobile-Friendly | Warn if only desktop checked |
| Page Speed Mobile | Warn if no Lighthouse run |
| Page Speed Desktop | Warn if no Lighthouse run |
| Critical Pages Loading | Based on sampled pages — Warn/Fail if key surfaces broken |

**Payment methods detection (passive — no extra navigation):**  
Scrape footer + cart page HTML for payment icon patterns: Visa, Mastercard, Amex, PayPal, Apple Pay, Google Pay, Shop Pay, Klarna, Afterpay, etc. Save as `payment_methods` check in `technical_checks.json`.

All 17 checks use exactly: `Pass` / `Warn` / `Fail`  
Rule: **never mark Pass if the check was not performed. Use Warn.**

### Page Discovery + Type-Quota Sampling

1. Fetch `/sitemap.xml` — extract all URLs
2. Extract nav links from homepage HTML
3. Try Shopify standard paths: `/cart`, `/collections`, `/pages/about`, `/blogs`
4. Classify every URL by page type:
   - `homepage`, `product_page`, `collection_page`, `cart_page`, `where_to_buy`, `faq_shipping_returns`, `about_page`, `blog_or_content_page`, `other`
5. Select pages by priority quota (12-page hard cap):

```
Priority 1 — Always crawl:
  homepage          × 1  (required)
  product_page      × 3  (first 3 from /products/ in sitemap)
  cart_page         × 1  (via shopping journey)

Priority 2 — Crawl if exists:
  collection_page   × 2  (top-level collections only, not sub-collections)
  where_to_buy      × 1
  faq_shipping      × 1

Priority 3 — Fill remaining slots:
  about_page        × 1
  blog_content      × 1  (pick by keyword relevance: health, guide, routine, recipe)
```

Save all URLs considered (selected + rejected with reason + blocked) to `discovered_links.json`.

### Per-Page Artifacts

For each selected page:

1. Launch Playwright with `playwright-stealth` applied
2. Navigate to URL
3. **Page sanity check** — before saving anything, verify:
   - Page `<title>` is present
   - Body text length > 500 chars
   - Body does NOT contain: "Checking your browser" / "cf-browser-verification" / "Just a moment"
   - If check fails: log as `blocked` in `discovered_links.json`, mark `Critical Pages Loading` → `Warn`, skip. Never save a Cloudflare challenge page as evidence.
4. Take screenshot → `screenshots/<name>.png`
5. Save rendered HTML → `pages/<name>.html`
6. Extract to `pages/<name>.md` (via markdownify)
7. Save `pages/<name>.json`:
   ```json
   {
     "url": "...",
     "page_type": "product_page",
     "title": "...",
     "meta_description": "...",
     "headings": [],
     "ctas": [],
     "important_links": []
   }
   ```

### Shopping Journey

Three possible outcomes — all produce a valid `shopping_journey.json`:

| Outcome | Trigger | Friction score |
|---|---|---|
| **Full journey** | Add-to-cart → cart → `/checkout` entry all succeed | Computed from deduction flags |
| **Partial journey** | Add-to-cart blocked/failed, but `/cart` loads | Computed from deduction flags |
| **Retailer-routed** | No cart found; "Find a Retailer" / "Where to Buy" CTA detected | Fixed 2.0 + `retailer_routed: true` |

Steps:
1. Navigate to first PDP
2. Attempt add-to-cart (handle variant selector requirement gracefully; log popup/modal blocks)
3. Screenshot cart → `screenshots/shopping_journey_cart.png`
4. Navigate to `/checkout` entry → screenshot → `screenshots/shopping_journey_checkout.png`
5. **Stop. Do not fill any forms. Do not enter payment details.**
6. If no cart path: detect retailer handoff CTA, screenshot → `screenshots/shopping_journey_retailer.png`

**Friction score (deterministic — computed by crawler from boolean flags):**

| Event | Deduction |
|---|---|
| Add-to-cart failed entirely | −2 |
| Cart page failed to load | −1 |
| Checkout entry failed to load | −1 |
| Popup / modal blocked the flow | −1 |
| No guest checkout option detected | −0.5 |
| No payment methods detected | −0.5 |

Start at 5, deduct per flag, floor at 1. No LLM involved.

Save `pages/shopping_journey.json`:
```json
{
  "outcome": "full_journey | partial_journey | retailer_routed",
  "retailer_routed": false,
  "friction_score": 3.5,
  "friction_flags": ["no_guest_checkout_detected"],
  "friction_detail": "Score 3.5/5 — no guest checkout visible (−0.5), popup blocked flow (−1)",
  "journey_observations": {
    "click_count_to_checkout": 4,
    "trust_badges_at_checkout": false,
    "cart_upsell_present": false,
    "urgency_elements_present": false,
    "error_messages_detected": false
  },
  "payment_methods_detected": ["Visa", "Mastercard", "Shop Pay", "PayPal"]
}
```

Add `shopping_journey` as the 16th check in `technical_checks.json` using friction_score and outcome.

---

## Phase 2 — Skills

### `skills/audit.md` — `/audit <url>`

Orchestrator. Explicit checklist — before each step, check if output artifact exists and skip if present.

```
[ ] 1. Run: python crawler/crawl_store.py <url>
        Read run_id from artifacts/<run_id>/discovered_links.json
[ ] 2. For each page in selected_pages: apply /page-evidence-extractor
        → artifacts/<run_id>/evidence_cards/<page>.json
[ ] 3. Apply /page-evidence-extractor to shopping journey artifacts
        → artifacts/<run_id>/evidence_cards/shopping_journey.json
[ ] 4. Apply /evidence-analyst
        → artifacts/<run_id>/evidence_summary.md
[ ] 5. Apply /audit-writer
        → sample_output/<run_id>_audit.md
[ ] 6. Run: python evals/run_eval.py <run_id>
        → eval_results/<run_id>_eval.md
[ ] 7. Review eval failures → fix only failed sections → re-run eval
        (Do not regenerate passing sections)
```

### `skills/page_evidence_extractor.md`

Per-page CRO evidence extraction. Input: page artifacts (screenshot path, page .md, page .json, URL).  
Output: `evidence_cards/<name>.json`

Schema:
```json
{
  "page_type": "product_page",
  "url": "...",
  "screenshot": "artifacts/<run_id>/screenshots/<name>.png",
  "text_artifact": "artifacts/<run_id>/pages/<name>.md",
  "page_summary": "...",
  "observed_strengths": [
    { "pillar": "Conversion", "claim": "...", "evidence": "artifacts/...", "confidence": 0.85 }
  ],
  "missing_or_weak": [
    { "pillar": "AOV", "claim": "...", "evidence": "artifacts/...", "severity": "high", "confidence": 0.82 }
  ],
  "purchase_path_notes": [],
  "content_commercialization_notes": [],
  "evidence_gaps": []
}
```

Rules:
- Page-level claims only — no store-level conclusions
- Missing claims must be scoped: "Reviews not visible near buy box on this PDP" not "The store has no reviews"
- Every claim cites a screenshot path or URL
- Pillar: Conversion / AOV / Retention / Acquisition / Performance

For `shopping_journey.json` evidence card: synthesize full journey findings. Cite `friction_score`, `friction_flags`, `journey_observations`. The `retailer_routed` flag is a primary diagnosis signal — if true, purchase handoff is the main finding.

### `skills/evidence_analyst.md`

Store-level synthesis. Input: all evidence cards (including `shopping_journey.json`) + `technical_checks.json`.  
Output: `evidence_summary.md`

Required fields in output:
- `store_category` — inferred from product/content evidence (e.g. "ginger candy / natural health snacks")  
  If cannot determine: mark `unknown` → audit writer flags competitor section as low-confidence
- `primary_use_cases` — list inferred from page content
- One sharp main diagnosis sentence
- Findings grouped by pillar with evidence paths
- Cross-page patterns (e.g. "no reviews above fold across all 3 PDPs")
- Purchase path constraints (friction_score + retailer_routed findings prominent)
- Content commercialization opportunities
- Candidate experiments with evidence
- Technical findings summary
- Evidence gaps + uncertainty

### `skills/audit_writer.md`

Final report generation. Input: `evidence_summary.md` + `technical_checks.json`.  
Output: `sample_output/<run_id>_audit.md`

Rules:
- Competitors inferred from `store_category` + `primary_use_cases` — **no hardcoded competitor lists**
- If `store_category = unknown`: write competitor section as low-confidence, say so
- Exactly 10 experiments, all 5 pillars covered
- All experiment fields required: exp-id, pillar, affected surface, URL, evidence, hypothesis, primary change, primary KPI, decision rule, expected lift, confidence
- Suggested pillar distribution: 3 Conversion, 2 AOV, 2 Retention, 1 Acquisition, 2 Performance
- Technical checks table from `technical_checks.json` only — all 17 checks — never guess or upgrade a status
- Every experiment evidence path must be under `artifacts/<run_id>/`

Report structure:
```markdown
# <Store> audit — <sharp diagnosis>

## Executive summary
(2–3 paragraphs, evidence-backed, no generic CRO language)

## Proposed experiments
### exp-<id> — <title>
**Pillar:** ...
**Affected surface:** ...
**URL:** ...
**Evidence:** artifacts/<run_id>/...
**Hypothesis:** ...
**Primary change:** ...
**Primary KPI:** ...
**Decision rule:** ...
**Expected lift:** +X–Y%
**Confidence:** XX%

## Competitor analysis
| Competitor | Domain | Positioning | What they make easier | Store edge | Pattern to adapt |

## Technical checks
| Check | Status | Detail |
```

### `skills/eval_judge.md`

Layer 9 rubric quality judge. Uses `evals/rubric.md`. Scores 10 dimensions 1–5 each (50 points total, reported as /100 by doubling). Dimensions: evidence grounding, experiment specificity, business usefulness, hypothesis quality, KPI quality, decision rule quality, confidence calibration, competitor usefulness, technical honesty, non-generic reasoning.

---

## Phase 3 — Eval (`evals/run_eval.py`)

### Invocation

```bash
python evals/run_eval.py <run_id>
```

### Layers

| Layer | Type | Check |
|---|---|---|
| 1 | Deterministic | Required sections present: title, exec summary, experiments, competitor table, technical checks |
| 2 | Heuristic | Exec summary: 2–3 paragraphs, contains diagnosis keyword, not a bullet list |
| 3 | Deterministic | Exactly 10 experiments (count `### exp-` headers) |
| 4 | Deterministic | All required fields present in every experiment |
| 5 | Deterministic | All 5 pillars present (5/5 Pass, 4/5 Warn, <4 Fail) |
| 6 | Deterministic | Evidence citations: artifact paths exist on disk OR are valid URLs. **All artifact paths must be under `artifacts/<run_id>/` — cross-run contamination Fail** |
| 7 | Deterministic | Technical checks table matches `technical_checks.json`: all 17 checks present, status matches JSON, no uninspected check marked Pass |
| 8 | Heuristic | Competitor table: 3–4 rows exist; competitors plausibly match `store_category` from `evidence_summary.md` |
| 9 | LLM | Output pre-filled prompt for `/eval-judge` rubric scoring — never silently skip |

**Failure tagging:** Every failure is tagged with a type and appended to `evals/failure_log.jsonl`:
```jsonl
{"run_id": "...", "layer": 6, "tag": "missing_evidence_citation", "detail": "EXP-CVR-002 cites missing file ..."}
```

### Output: `eval_results/<run_id>_eval.md`

```markdown
# Eval result — <run_id>

Overall score: XX/100

| Category | Score | Status |
|---|---:|---|
| Required sections | 10/10 | Pass |
| Exec summary | 8/10 | Pass |
| Experiment count | 10/10 | Pass |
| Required fields | 18/20 | Warn |
| Pillar coverage | 10/10 | Pass |
| Evidence citations | 28/30 | Warn |
| Technical checks | 10/10 | Pass |
| Competitor analysis | 8/10 | Pass |

## Failures
- ...

## Suggested fixes
- ...

---
## Layer 9 — Quality Judge Prompt
Paste the following into Claude Code to run /eval-judge:

> [pre-filled prompt with report content, evidence summary, rubric dimensions]
```

---

## Phase 4 — Agent Docs

### `CLAUDE.md` and `AGENTS.md`

Full generic pipeline reference. No store-specific logic. Must include:
- Project goal and how to run `/audit <url>` end-to-end
- What each skill does and when to invoke it
- `run_id` naming convention and artifact folder structure
- Citation rules: every audit claim must cite `artifacts/<run_id>/...` path or URL
- No-hallucination rules: never invent screenshots, never invent technical checks
- Technical check rules: Warn if not checked, never fake Pass
- No-hardcoding rules: no store names, competitor names, or category assumptions in skills
- Pillar definitions and experiment quality bar
- Retry safety: file-existence checks, `--force` flag
- Shopping journey: never go past `/checkout` entry, never fill payment forms

### `EVAL_LOOP.md`

How the eval system becomes autonomous and self-learning. Core mechanism: **failure taxonomy feedback loop.**

**Current loop:**
```
Audit generated
  ↓
run_eval.py — deterministic Layers 1–8
  ↓
/eval-judge — Layer 9 rubric scoring
  ↓
Failures tagged → failure_log.jsonl
  ↓
Fix only failed sections → re-eval
```

**Month 1:**
- Deterministic schema/citation/pillar evals running on every audit
- Rubric judge (Layer 9) run on sampled audits with human review
- Failure taxonomy built: tag every failure type, measure frequency
- Identify top 3 recurring failure patterns

**Month 2:**
- System reads `failure_log.jsonl` → top failure types automatically tighten relevant skill instructions
  (e.g. `generic_experiment` fires 8× → `audit_writer.md` gets stronger specificity rule appended)
- Auto-regeneration for failed sections — no full re-run
- Prompt version tracking: each skill change is versioned, eval scores tracked per version
- Store-category-specific rubric additions

**Month 3:**
- Merchant experiment outcomes feed back as ground truth
- Underperforming experiment types get downweighted in confidence calibration
- Automated prompt improvements from failure clusters
- Human review only for: confidence < 70%, novel store categories, eval disagreements

**Human review surface shrinks:**
- Early: all low-scoring audits, unsupported claims, new store categories
- Later: only low-confidence audits, eval disagreements, high-value merchants

---

## Phase 5 — Run Both Example Stores

```bash
# Gingerpeople (calibration)
python crawler/crawl_store.py https://gingerpeople.com
# Then in Claude Code: /audit https://gingerpeople.com
python evals/run_eval.py <gingerpeople_run_id>

# ZenRojas (generalization)
python crawler/crawl_store.py https://zenrojas.com
# Then in Claude Code: /audit https://zenrojas.com
python evals/run_eval.py <zenrojas_run_id>
```

ZenRojas run: zero reuse of gingerpeople artifacts, paths, competitors, or assumptions.  
Verified automatically by Layer 6 cross-run contamination check.

---

## Verification Checklist

- [ ] `python crawler/crawl_store.py <url>` runs on any Shopify URL without error
- [ ] `artifacts/<run_id>/` folder created with correct `<slug>_<YYYYMMDD>_<uuid>` naming
- [ ] Screenshots exist in `artifacts/<run_id>/screenshots/` for each selected page
- [ ] `technical_checks.json` has all 17 checks for both runs
- [ ] `shopping_journey.json` exists with `friction_score`, `friction_flags`, `journey_observations`
- [ ] Evidence cards exist for 6+ pages per run (including `shopping_journey.json`)
- [ ] `evidence_summary.md` contains `store_category` + `primary_use_cases` for both runs
- [ ] Both `sample_output/<run_id>_audit.md` exist with exactly 10 experiments and all 5 pillars
- [ ] All experiment evidence paths are under `artifacts/<run_id>/`
- [ ] `python evals/run_eval.py <run_id>` — Layers 1–5 pass for both runs
- [ ] Layer 6: no run cites another run's artifacts
- [ ] Layer 7: technical checks table matches JSON for both runs (17 checks)
- [ ] `eval_results/<run_id>_eval.md` exists for both runs with Layer 9 pre-filled prompt
- [ ] ZenRojas report cites no gingerpeople artifacts (verified by Layer 6)
- [ ] `evals/failure_log.jsonl` populated after both eval runs

---

## Out of Scope

- `AGENT_LOG.md` — user writes (personal time tracking per assignment requirements)
- `WORKFLOWS.md` — user writes (personal AI usage patterns per assignment requirements)
- Lighthouse speed checks — mark Page Speed checks as `Warn`
- Competitor page screenshots
- UI or web interface
- Going past `/checkout` entry — no payment page, no form filling
- Programmatic LLM API calls in eval script
