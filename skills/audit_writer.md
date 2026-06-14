# /audit-writer

Write the final CRO audit report from the synthesized evidence. A full report
must satisfy the repo contract and must also survive an evidence-truth review,
not just a schema review.

## Input

- `artifacts/<run_id>/evidence_summary.md`
- `artifacts/<run_id>/technical_checks.json`
- `artifacts/<run_id>/summary.md`

## Output

Save to `sample_output/<run_id>_audit.md`.

## Full-report structure

Start with an H1 title plus run ID and date. Then write exactly these four H2
sections in this order:

1. `## Executive Summary`
2. `## Proposed Experiments`
3. `## Competitor Analysis`
4. `## Technical Checks`

Do not add any other H2 sections.

## Pre-write verification

Before drafting, inspect `evidence_summary.md` for:
- unsupported universal language
- mixed evidence reported as consistent
- page URL / evidence mismatches
- cart claims backed by empty-cart evidence
- homepage/email claims that confuse `present`, `prominent`, and `incentivized`

If those issues exist, do not amplify them. Rewrite the report to match the strongest verified evidence, even if `evidence_summary.md` is overconfident.

## 1. Executive Summary

Write 2-3 paragraphs containing:
- the single biggest conversion constraint from `main_diagnosis`
- 2-3 supporting observations with inline artifact citations
- the biggest AOV or retention opportunity
- a concise technical-health summary
- for a Degraded crawl, the evidence limitations from `summary.md`

Rules:
- Every factual claim must cite a real `artifacts/<run_id>/...` path or URL.
- Lead with the diagnosis, not generic praise.
- Use quantified language when evidence is partial:
  - `on PDP1`
  - `on 2/3 sampled PDPs`
  - `mixed across sampled PDPs`
- Do not use `all`, `every`, `none`, `always`, or `never` unless the summary proves it across all sampled relevant pages.

## 2. Proposed Experiments

Write exactly 10 H3 experiment blocks, with exactly two experiments per pillar:
Conversion, AOV, Retention, Acquisition, and Performance.

```markdown
### EXP-01: <Short title>

| Field | Value |
|---|---|
| Pillar | Conversion |
| Surface | PDP - above fold |
| URL | https://... |
| Evidence | artifacts/<run_id>/screenshots/<name>.png |
| Hypothesis | ... |
| Primary change | ... |
| Primary KPI | ... |
| Decision rule | ... |
| Expected lift | +8-15% |
| Confidence | 72% |
```

Field rules:
- `Evidence` must be the strongest available artifact for that claim.
- Prefer screenshots for visible UI claims.
- Prefer shopping-journey screenshots/JSON for populated cart and checkout claims.
- If the experiment references a specific URL, use evidence from that page when possible.
- `Evidence` may use `inferred - journey stops at checkout entry` only for uncrawled post-checkout surfaces.
- `Hypothesis` must name a specific change, measurable metric, and evidence-grounded reason.
- `Primary change` must be specific enough to brief an implementer.
- `Expected lift` must be a numeric percentage range.
- `Confidence` must be a numeric percentage.

Verification rules:
- Re-open the cited artifact before finalizing each experiment.
- If a feature exists anywhere in sampled evidence, do not call it simply `missing` unless the experiment is page-specific and the cited page truly lacks it.
- If the evidence is mixed, phrase the problem as inconsistency, placement, prominence, weak default state, or partial coverage.
- If the cart page screenshot is an empty-cart state, do not use it to support claims about populated-cart modules.

## 3. Competitor Analysis

Select 3-4 competitors based on `store_category` and `primary_use_cases`.
Never use a hardcoded category list.

| Competitor | Domain | Positioning | What they make easier | <Store> edge | Pattern to adapt |
|---|---|---|---|---|---|

Rules:
- Each row must include the competitor URL.
- Each row must connect to at least one proposed experiment.
- If competitor confidence is low, say so rather than inventing facts.

## 4. Technical Checks

Reproduce all 17 checks from `technical_checks.json` exactly, including both
status and detail.

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
- Separate observed evidence from uncertainty.
- Use `evidence_summary.md` as the main source, but not as an unquestioned source.
- Prefer precise weakness framing over generic absence framing.
- If a claim fails an evidence re-check, rewrite the claim; do not keep it because it sounds stronger.
