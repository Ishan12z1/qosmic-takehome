# /audit-writer

Writes the final CRO audit report from the synthesized evidence. A full report
contains exactly the four H2 sections required by `docs/README.md` and
`docs/target_report.md`.

## Input

- `artifacts/<run_id>/evidence_summary.md`
- `artifacts/<run_id>/technical_checks.json`
- `artifacts/<run_id>/summary.md`

## Output

Save to `sample_output/<run_id>_audit.md`.

## Full-report structure

Start with an H1 title plus run ID and date. Then write exactly these four H2
sections in this order. Do not add Store Overview, Evidence Summary, appendix, or
other H2 sections.

### 1. Executive Summary

Use the heading `## Executive Summary`. Write 2-3 prose paragraphs containing:

- The single biggest conversion constraint from `main_diagnosis`.
- 2-3 supporting observations with inline artifact citations.
- The biggest AOV or retention opportunity.
- A concise technical-health summary.
- For a Degraded crawl, the evidence limitations from `summary.md`.

Every factual claim must cite a real `artifacts/<run_id>/...` path or URL.
For a Degraded crawl, cite `artifacts/<run_id>/summary.md` directly and state
what evidence is missing or uncertain.

### 2. Proposed Experiments

Use the heading `## Proposed Experiments`. Write exactly 10 H3 experiment blocks,
with exactly two experiments per pillar: Conversion, AOV, Retention, Acquisition,
and Performance.

```markdown
### EXP-01: <Short title>

| Field | Value |
|---|---|
| Pillar | Conversion |
| Surface | PDP - above fold |
| URL | https://... |
| Evidence | artifacts/<run_id>/screenshots/<name>.png |
| Hypothesis | Adding star ratings above the fold will improve add-to-cart rate because the current PDP has no visible social proof. |
| Primary change | Add review summary widget directly below the product title |
| Primary KPI | Add-to-cart rate |
| Decision rule | Ship if add-to-cart rate improves by at least 5% relative after a 2-week test |
| Expected lift | +8-15% |
| Confidence | 72% |
```

Field rules:

- `Evidence` must be a real path under `artifacts/<run_id>/` or an explicit
  `inferred - journey stops at checkout entry` label for an unobserved surface.
- `Hypothesis` must name a specific change, measurable metric, and cited reason.
- `Primary change` must be specific enough to brief an implementer.
- `Expected lift` must be a numeric percentage range.
- `Confidence` must be a numeric percentage.
- Never state an un-crawled account, post-purchase, order-confirmation, or
  thank-you surface as observed.

Prioritize cross-page patterns, customer-visible journey friction, and technical
failures with measurable revenue impact. An API add-to-cart fallback is evidence
of customer-facing journey uncertainty, not a successful UI journey.

Before finalizing each experiment, re-check the cited screenshot/JSON so the
claim is not contradicted by the evidence. If the PDP already shows reviews,
ratings, subscriptions, bundles, or another UI element, do not call it
"missing"; describe the real problem more precisely (placement, prominence,
clarity, default state, cross-page inconsistency, or below-the-fold visibility).

### 3. Competitor Analysis

Use the heading `## Competitor Analysis`. Select 3-4 competitors based on
`store_category` and `primary_use_cases`; never use a hardcoded category list.
Competitor observations must include the competitor URL that supports the claim.

| Competitor | Domain | Positioning | What they make easier | <Store> edge | Pattern to adapt |
|---|---|---|---|---|---|

Each row must connect to at least one proposed experiment. If the category is
unknown or competitor research is unavailable, label the uncertainty rather than
inventing facts.

### 4. Technical Checks

Use the heading `## Technical Checks`. Reproduce all 17 checks from
`technical_checks.json` exactly, including both status and detail.

| Check | Status | Detail |
|---|---|---|
| SSL Certificate | Pass | ... |

Never upgrade a Warn or Fail to Pass. If the crawl is Degraded, keep blocked or
unmeasured checks explicit.

## Writing Rules

- Cite every factual claim.
- Never invent artifact paths or technical results.
- Do not reuse evidence from another run ID.
- Do not hardcode store names, categories, or competitors.
- The report must remain useful when some surfaces are unavailable by clearly
  separating observed evidence from uncertainty.
- Use `evidence_summary.md` as the primary source for experiment selection.
  Prefer its cross-page patterns and candidate experiments over generic fallback
  ideas.
- Avoid stock experiments unless the cited evidence makes them one of the
  strongest opportunities for this specific store.
