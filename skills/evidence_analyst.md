# /evidence-analyst

Synthesize all per-page evidence cards into one store-level analysis. This file
is the writer's main source of truth. Its job is not to sound persuasive; its
job is to be precise, quantified, and hard to misread.

## Input

- All `artifacts/<run_id>/evidence_cards/*.json` (including `shopping_journey.json`)
- `artifacts/<run_id>/technical_checks.json`

## Output

Save to `artifacts/<run_id>/evidence_summary.md`.

Complete all required sections below. Do not stop after `Findings by pillar`.

---

## Required sections (in order)

### 1. Store identity

```
store_category: <inferred from product/content evidence>
primary_use_cases:
  - <use case 1>
  - <use case 2>
  - <use case 3>
main_diagnosis: <one sharp sentence identifying the single biggest conversion constraint>
```

If `store_category` cannot be determined from the evidence, write `store_category: unknown`
and note that competitor selection in the audit writer will be low-confidence.

### 2. Findings by pillar

For each of the 5 pillars, write 3-6 bullet points:
- Conversion
- AOV
- Retention
- Acquisition
- Performance

Each bullet must:
- cite at least one artifact path
- use scoped language such as `observed on PDP1`, `observed on 2/3 sampled PDPs`, `journey JSON`, or `technical check`
- avoid universal language unless fully supported

### 3. Cross-page patterns

Only list patterns that have been checked across multiple relevant pages.

For each pattern, use this structure:

```markdown
- Pattern: <short claim>
  Support:
  - <page 1>: present/absent/unclear - artifact path
  - <page 2>: present/absent/unclear - artifact path
  - <page 3>: present/absent/unclear - artifact path
  Verdict: consistent / mixed / low-confidence
```

If the evidence is mixed, say `Verdict: mixed` and do not collapse it into a universal claim.

### 4. Purchase path constraints

Summarize the shopping journey outcome, friction score, and key blockers or strengths.
Reference `evidence_cards/shopping_journey.json` and the journey screenshots.
Distinguish empty-cart evidence from populated-cart journey evidence.

### 5. Content commercialization opportunities

Blog posts or about pages that could be converted to purchase funnels.
Note whether each surface has:
- product CTAs
- email capture
- trust/story content
- commercial dead ends

### 6. Candidate experiments (pre-draft)

List 10-15 candidate experiment ideas, each with:
- `pillar`
- one-sentence hypothesis
- expected impact: Low / Medium / High
- support scope: `single page`, `cross-page consistent`, `mixed but important`, or `technical check`

These are candidates; the audit writer selects the final 10.

### 7. Technical findings summary

Summarize the 17 technical checks from `technical_checks.json`. Group by:
- Critical failures (status = Fail)
- Warnings (status = Warn)
- Passing checks

### 8. Evidence gaps and uncertainty

List anything that could not be assessed:
- blocked pages
- missing artifacts
- low-confidence inferences
- mixed evidence that prevented a strong claim
- places where one sampled page contradicted another

Be explicit about what is unknown rather than guessing.

---

## Analysis rules

- No hallucination. Every claim must be traceable to an artifact in `artifacts/<run_id>/`.
- No competitor naming here. That belongs to the audit writer.
- Cross-page patterns are the gold standard, but mixed evidence must stay mixed.
- Never use `all`, `every`, `none`, `always`, or `never` unless all sampled relevant pages were checked and listed.
- If a PDP shows reviews, stars, subscriptions, bundles, or another proof element, do not summarize it as missing. Describe the real issue precisely:
  - below the fold
  - not near CTA
  - empty on some PDPs only
  - present but weak
  - inconsistent across sampled pages
- If a homepage or content page contains email capture, do not say `no email capture`. Describe whether the issue is no incentive, low prominence, footer-only placement, or no modal.
- When evidence conflicts, record the conflict in `Cross-page patterns` and `Evidence gaps and uncertainty`. Do not smooth it away.
- Shopping journey friction is always a Conversion finding. Even a perfect 5.0/5 score should be noted with citations.
- Technical checks feed Acquisition and Performance findings. Always connect technical results to business impact.
