# /eval-judge

Layer 9 quality rubric judge. Score the audit report on 10 dimensions (1-5 each).
This layer should judge evidence truthfulness, not just evidence presence.

## Input

Paste the pre-filled prompt output from `python evals/run_eval.py <run_id>`.
It will contain the audit report text and the rubric dimensions to score.

## Output

Append scores to `eval_results/<run_id>_eval.md` under a `## Layer 9: Quality Rubric` section.

## Scoring procedure

Before assigning scores, check for:
- claims contradicted by their own cited artifact
- universal claims supported by only one sampled page
- better available evidence ignored in favor of a weaker artifact
- URL/evidence mismatches
- mixed evidence presented as consistent

If any of those occur, reduce `Evidence grounding`, and reduce any other affected dimension such as `Diagnosis sharpness` or `Exec summary quality`.

## Scoring rubric

### 1. Diagnosis sharpness (1-5)
- 5: Main diagnosis names a specific, measurable constraint with supporting evidence.
- 3: Diagnosis is directionally right but generic.
- 1: Diagnosis contradicts the evidence or overstates a mixed pattern.

### 2. Hypothesis quality (1-5)
- 5: All 10 hypotheses follow "X will improve Y because Z (evidence)" with specific change, metric, and reason.
- 3: At least 6/10 follow the structure; others are vague.
- 1: Fewer than 4 are specific.

### 3. Evidence grounding (1-5)
- 5: Every major claim cites a real artifact or URL, and the cited evidence actually supports the claim.
- 3: Citations mostly exist, but some claims overgeneralize, use weaker-than-necessary evidence, or rely on mixed evidence without saying so.
- 1: Claims are uncited, fabricated, contradicted by the cited artifact, or clearly mismatched to the referenced page.

### 4. Pillar balance (1-5)
- 5: All 5 pillars present, no pillar has fewer than 1 or more than 4 experiments.
- 3: All pillars present but one pillar dominates or one has only token coverage.
- 1: One or more pillars missing entirely.

### 5. Competitor relevance (1-5)
- 5: All 3-4 competitors are directly in the store's category or adjacent, each connected to at least one experiment.
- 3: Most are relevant but one is generic or off-category.
- 1: Competitors are generic or disconnected from the store category.

### 6. Experiment specificity (1-5)
- 5: Every `Primary change` is concrete enough to brief a developer or growth engineer.
- 3: At least 7/10 are specific; the rest are high-level directions.
- 1: Fewer than 5 are actionable.

### 7. Technical integration (1-5)
- 5: All Fail checks and material Warn checks are addressed by experiments or explicitly scoped out.
- 3: Most are addressed; 1-2 are ignored without explanation.
- 1: Technical findings are listed but not connected to recommendations.

### 8. Exec summary quality (1-5)
- 5: 2-3 tight paragraphs; leads with diagnosis; specific, cited, and free of contradicted claims.
- 3: Diagnosis present but one paragraph is generic, overbroad, or too dependent on weaker evidence.
- 1: Generic or contradicted by sampled evidence.

### 9. AOV/Retention depth (1-5)
- 5: AOV and Retention experiments are grounded in store-specific evidence.
- 3: Present but somewhat generic or supported by weaker evidence.
- 1: Token coverage only.

### 10. Overall actionability (1-5)
- 5: A team could start A/B testing at least 8/10 experiments within one sprint without further research.
- 3: 5-7 experiments are immediately testable; others need more scoping.
- 1: Fewer than 5 are implementation-ready.

## Verdict thresholds

| Total | Verdict |
|---|---|
| 45-50 | Excellent - ship |
| 38-44 | Good - minor fixes before shipping |
| 28-37 | Needs work - address weak dimensions and re-eval |
| < 28 | Rework required - strengthen `evidence_summary.md` and re-run `/audit-writer` |
