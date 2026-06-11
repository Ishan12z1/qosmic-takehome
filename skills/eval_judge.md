# /eval-judge

Layer 9 quality rubric judge. Scores the audit report on 10 dimensions (1–5 each).
Invoked after `run_eval.py` outputs a pre-filled prompt for this skill.

## Input

Paste the pre-filled prompt output from `python evals/run_eval.py <run_id>`.
It will contain the audit report text and the rubric dimensions to score.

## Output

Append scores to `eval_results/<run_id>_eval.md` under a `## Layer 9: Quality Rubric` section.

```markdown
## Layer 9: Quality Rubric

| Dimension | Score (1–5) | Notes |
|---|---|---|
| Diagnosis sharpness | 4 | Main diagnosis is specific but misses the cart upsell gap |
| Hypothesis quality | 3 | 6/10 hypotheses follow the required structure; 4 are vague |
| Evidence grounding | 5 | All claims cite real artifact paths |
| Pillar balance | 4 | Conversion over-represented (5 exp); AOV has only 1 |
| Competitor relevance | 3 | One competitor is off-category |
| Experiment specificity | 4 | Primary changes are concrete; 2 are still too broad |
| Technical integration | 5 | All Fail/Warn checks mapped to experiments |
| Exec summary quality | 4 | Clear diagnosis; third paragraph too generic |
| AOV/Retention depth | 3 | Only surface-level observations for retention |
| Overall actionability | 4 | Most experiments are immediately testable |

**Total: 39/50**
**Verdict: Good — address hypothesis quality and AOV depth before shipping**
```

---

## Scoring rubric

### 1. Diagnosis sharpness (1–5)
- 5: Main diagnosis names a specific, measurable constraint with supporting evidence
- 3: Diagnosis is correct but generic ("needs more social proof")
- 1: No diagnosis, or diagnosis contradicts the evidence

### 2. Hypothesis quality (1–5)
- 5: All 10 hypotheses follow "X will improve Y because Z (evidence)" — specific change, specific metric, evidence-grounded reason
- 3: At least 6/10 follow the structure; others are directionally correct but vague
- 1: Fewer than 4 hypotheses are specific; most are generic improvement statements

### 3. Evidence grounding (1–5)
- 5: Every claim in the report cites a real artifact path or URL; no invented citations
- 3: Most claims cited; 2–3 observations lack citations
- 1: Multiple uncited claims; fabricated or non-existent paths present

### 4. Pillar balance (1–5)
- 5: All 5 pillars present, no pillar has fewer than 1 or more than 4 experiments
- 3: All pillars present but Conversion dominates (5+) or a pillar has only token coverage
- 1: One or more pillars missing entirely

### 5. Competitor relevance (1–5)
- 5: All 3–4 competitors are directly in the store's category or adjacent, each connected to ≥1 experiment
- 3: 2/3–4 competitors are relevant; one is generic/off-category
- 1: Competitors are generic (e.g., "Amazon, Shopify stores") with no connection to store category

### 6. Experiment specificity (1–5)
- 5: Every "Primary change" describes what to build/add/remove with enough detail to brief a developer
- 3: At least 7/10 are specific; 3 are high-level directions
- 1: Fewer than 5 have actionable primary changes

### 7. Technical integration (1–5)
- 5: All Fail-status checks from technical_checks.json are addressed by ≥1 experiment or acknowledged as out-of-scope with reason
- 3: Most Fail checks addressed; 1–2 ignored without explanation
- 1: Technical failures are listed but not connected to any experiment or recommendation

### 8. Exec summary quality (1–5)
- 5: 2–3 tight paragraphs; leads with diagnosis; no generic statements; cites specific evidence
- 3: Diagnosis present but one paragraph is generic or repeats experiment list
- 1: Generic, could apply to any store; no specific diagnosis

### 9. AOV/Retention depth (1–5)
- 5: AOV and Retention experiments are grounded in store-specific evidence (e.g., product catalog structure, content assets); not just "add upsell widget"
- 3: AOV/Retention experiments present but generic — not tied to observed store specifics
- 1: AOV/Retention covered only by token experiments with no evidence connection

### 10. Overall actionability (1–5)
- 5: A conversion team could begin A/B testing ≥8/10 experiments within one sprint without further research
- 3: 5–7 experiments are immediately testable; others need scoping
- 1: Fewer than 5 experiments are ready to implement; most require additional discovery

---

## Verdict thresholds

| Total | Verdict |
|---|---|
| 45–50 | Excellent — ship |
| 38–44 | Good — minor fixes before shipping |
| 28–37 | Needs work — address weak dimensions and re-eval |
| < 28 | Rework required — re-run /audit-writer after strengthening evidence_summary |
