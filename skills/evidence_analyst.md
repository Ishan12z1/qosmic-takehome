# /evidence-analyst

Synthesizes all per-page evidence cards into a single store-level analysis.
Extracts `store_category` and `primary_use_cases` which drive competitor
selection in the audit writer.

## Input

- All `artifacts/<run_id>/evidence_cards/*.json` (including `shopping_journey.json`)
- `artifacts/<run_id>/technical_checks.json`

## Output

Save to `artifacts/<run_id>/evidence_summary.md`

This file is the writer's main source of truth. If it is thin or generic, the
final audit will also be thin or generic. Complete all required sections below;
do not stop after `Findings by pillar`.

---

## Required sections (in order)

### 1. Store identity

```
store_category: <inferred from product/content evidence, e.g. "tea / specialty beverages">
primary_use_cases:
  - <use case 1, e.g. "daily tea ritual">
  - <use case 2>
  - <use case 3>
main_diagnosis: <one sharp sentence identifying the single biggest conversion constraint>
```

**If `store_category` cannot be determined** from the evidence, write `store_category: unknown`
and note that competitor selection in the audit writer will be low-confidence.

### 2. Findings by pillar

For each of the 5 pillars, write a short section (3–6 bullet points):
- **Conversion** — friction, CTA quality, trust signals, checkout experience
- **AOV** — upsell/cross-sell opportunities, bundle visibility, subscription
- **Retention** — email capture, loyalty, post-purchase, account
- **Acquisition** — SEO signals, organic content, social proof
- **Performance** — page speed signals, image optimization, mobile layout

Each bullet must cite at least one artifact path from `artifacts/<run_id>/`.

### 3. Cross-page patterns

Observations that appear consistently across multiple pages (e.g., "no customer
reviews above fold on any of the 3 PDPs"). These are the strongest signals for
experiments. Each pattern must cite 2+ page artifact paths.

### 4. Purchase path constraints

Summarize the shopping journey outcome, friction score, and key blockers or
strengths. Reference `evidence_cards/shopping_journey.json` and its screenshots.

### 5. Content commercialization opportunities

Blog posts or about pages that could be converted to purchase funnels. Note if
content builds authority but lacks CTAs or product links.

### 6. Candidate experiments (pre-draft)

List 10–15 candidate experiment ideas, each with:
- `pillar` tag
- one-sentence hypothesis
- expected impact (Low / Medium / High)

These are candidates — the audit writer selects the final 10.

### 7. Technical findings summary

Summarize the 17 technical checks from `technical_checks.json`. Group by:
- Critical failures (status = Fail)
- Warnings (status = Warn)
- Passing checks

### 8. Evidence gaps and uncertainty

List anything that could not be assessed (blocked pages, missing artifacts,
low-confidence inferences). Be explicit about what is unknown rather than
guessing.

---

## Analysis rules

**No hallucination.** Every claim must be traceable to an artifact in
`artifacts/<run_id>/`. If you didn't see it in the crawled data, don't state it.

**No store-specific hardcoding.** Do not name competitors here — that is the
audit writer's job based on `store_category` and `primary_use_cases`.

**Cross-page patterns are the gold standard.** A weakness observed on one page
is a signal. The same weakness on three pages is a finding. Weight cross-page
patterns more heavily in candidate experiments.

**Do not contradict the screenshot.** If a PDP already shows reviews, stars,
subscriptions, bundles, or another proof element, do not summarize it as
"missing." Instead describe the real issue precisely, for example "reviews are
below the fold" or "cross-sell exists on PDP A but not PDP B."

**Candidate experiments must be store-specific.** Avoid defaulting to generic
"add stars / add cart upsell / add email capture" ideas unless the cited
evidence clearly shows the element is absent and the change is one of the
strongest cross-page opportunities.

**Shopping journey friction is always a Conversion pillar finding.** Even a
perfect 5.0/5 score should be noted (positive signal) with citations to the
journey screenshots.

**Technical checks feed Acquisition and Performance pillars.** Sitemap missing
→ Acquisition. Image optimization warnings → Performance. Always connect
technical failures to business impact in the pillar sections.
