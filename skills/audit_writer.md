# /audit-writer

Writes the final CRO audit report. Exactly 10 experiments, all 5 pillars, every
claim cited to an artifact under `artifacts/<run_id>/`.

## Input

- `artifacts/<run_id>/evidence_summary.md` — store category, primary use cases, findings by pillar, candidate experiments
- `artifacts/<run_id>/technical_checks.json` — 17 checks, read verbatim for the technical table

## Output

Save to `sample_output/<run_id>_audit.md`

---

## Report structure (required sections in this order)

### 1. Title

```
# CRO Audit: <Store Name>
Run ID: <run_id>
Date: <YYYY-MM-DD>
```

### 2. Executive Summary

2–3 paragraphs. Must contain:
- The single biggest conversion constraint (from `main_diagnosis` in evidence_summary)
- 2–3 supporting observations with artifact citations
- One sentence on the biggest AOV or retention opportunity
- One sentence on technical health (summarize Fail/Warn counts)

Do not write a bullet list here. Prose paragraphs only.

### 3. Store Overview

Short table:
| Field | Value |
|---|---|
| Store URL | |
| Category | `store_category` from evidence_summary |
| Primary use cases | from evidence_summary |
| Pages crawled | count from discovered_links.json |
| Friction score | from shopping_journey.json |
| Shopping journey outcome | from shopping_journey.json |

### 4. Competitor Benchmarks

Table with 3–4 competitors. Select competitors based on `store_category` and
`primary_use_cases` from evidence_summary — **never hardcode a list**. For each:

| Competitor | Category | Notable CRO strength | Relevant to |
|---|---|---|---|

Pick competitors that illuminate the gaps found in the evidence. Each competitor
should relate to at least one experiment recommendation.

### 5. Experiments (exactly 10)

One H3 block per experiment. **Exactly 10 — no more, no fewer.** All 5 pillars
must appear at least once:
- Conversion (2)
- AOV (2)
- Retention (2)
- Acquisition (2)
- Performance (2)

Each experiment block:

```markdown
### EXP-01: <Short title>

| Field | Value |
|---|---|
| Pillar | Conversion |
| Surface | PDP — above fold |
| URL | https://... |
| Evidence | artifacts/<run_id>/screenshots/<name>.png |
| Hypothesis | Adding star ratings above the fold on PDPs will increase add-to-cart rate because users currently see no social proof before the fold. |
| Primary change | Add review summary widget (star count + rating) directly below product title |
| Secondary change | (optional) |
| Primary KPI | Add-to-cart rate |
| Decision rule | +5% relative lift in add-to-cart rate over 2-week test |
| Expected lift | Medium |
| Confidence | Medium |
```

**Field rules:**
- `Evidence` — must be a real path under `artifacts/<run_id>/`. Never invent a path.
- `Hypothesis` — must follow "doing X will improve Y because Z" structure. No vague hypotheses.
- `Primary KPI` — must be a measurable metric, not a description.
- `Expected lift` — Low / Medium / High only.
- `Confidence` — Low / Medium / High only. Use Low if the evidence base is thin.

Select experiments from the candidate list in evidence_summary, prioritizing:
1. Cross-page patterns (observed on 2+ pages)
2. High-friction journey steps
3. Technical failures that affect revenue (Fail status)

### 6. Technical Checks

Read **all 17 checks** from `technical_checks.json`. Reproduce them exactly — do not
change any status, do not omit any check.

```markdown
| Check | Status | Detail |
|---|---|---|
| SSL Certificate | Pass | ... |
| HTTPS Redirect | Pass | ... |
| ...all 17 rows... |
```

Statuses must match the JSON exactly. A `Warn` in JSON is `Warn` in the report —
never upgrade it to `Pass`.

### 7. Evidence Summary

Brief section (3–5 bullets per pillar) summarizing the strongest signals from
evidence_summary.md. Each bullet must cite an artifact path.

---

## Writing rules

**No hardcoded competitors.** Use `store_category` and `primary_use_cases` to infer
relevant competitors. If category is `unknown`, note low confidence in the competitor table.

**No invented evidence.** If you didn't see it in the crawled artifacts, don't write it.
Screenshots that don't exist cannot be cited.

**Hypothesis quality bar.** Every hypothesis must name a specific change, a specific
metric, and a reason grounded in observed evidence. "We hypothesize that improving the
UX will increase conversions" fails this bar.

**Pillar balance.** Conversion-heavy reports miss AOV and Retention opportunities.
Ensure at least 1 experiment per non-Conversion pillar.

**Friction score must match.** The friction score in the Store Overview must equal the
value in `pages/shopping_journey.json`. Do not paraphrase or round it.
