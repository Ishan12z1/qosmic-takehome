# Eval Results: tentree_20260611_72bf40

Generated: 2026-06-11 21:40

## Layers 1–8 (Deterministic)

| Layer | Name | Result | Detail |
|---|---|---|---|
| 1 | Required sections present | Pass | All required sections found |
| 2 | Exec summary quality | Pass | 3 paragraphs with diagnosis language |
| 3 | Exactly 10 experiments | Pass | Exactly 10 experiments found |
| 4 | All experiment fields present | Pass | All 10 experiments have required fields |
| 5 | All 5 pillars covered | Pass | All 5 pillars present: ['acquisition', 'aov', 'conversion', 'performance', 'retention'] |
| 6 | Evidence paths valid (no cross-run contamination) | Pass | All 26 artifact citations valid and under correct run_id |
| 7 | Technical checks match JSON | Pass | All 17 technical checks match technical_checks.json |
| 8 | Competitor table quality | Pass | 4 competitors found, section present |

**8/8 layers passed**

## Layer 9: Quality Rubric

| Dimension | Score (1–5) | Notes |
|---|---|---|
| Diagnosis sharpness | 4 | OG tags diagnosis is specific and cited (empty strings on every crawled page); minor knock for leading with a technical/acquisition failure rather than a direct conversion funnel constraint |
| Hypothesis quality | 4 | 9/10 follow "X will improve Y because Z (evidence)" precisely; EXP-10 bundles two unrelated changes (cookie consent + Lighthouse) diluting the structure |
| Evidence grounding | 5 | Layer 6 verified all 26 artifact citations are real and under the correct run_id; exec summary claims all grounded in specific crawled data |
| Pillar balance | 5 | Exactly 2 experiments per pillar — perfect distribution |
| Competitor relevance | 5 | Patagonia, Allbirds, Pact, Girlfriend Collective all in sustainable apparel; each connected to 2 specific experiments |
| Experiment specificity | 4 | Primary changes are developer-briefable (specific Shopify admin paths, exact copy, schema field names); EXP-10 is the only weak spot (bundles two unrelated tasks) |
| Technical integration | 4 | 6/7 Warn checks addressed by an experiment; Mobile-Friendly Warn has no experiment and is not acknowledged as out-of-scope |
| Exec summary quality | 4 | Tight and store-specific; paragraph 1 leads with strengths rather than diagnosis (rubric specifies "leads with diagnosis"); paragraphs 2–3 are strong |
| AOV/Retention depth | 5 | AOV: outfit-pairing framing is apparel-specific; urgency-in-cart experiment grounded in observed homepage/cart contradiction. Retention: targets tentree-specific pages; trees-per-purchase mechanic unique to this brand |
| Overall actionability | 4 | 9/10 experiments actionable in one sprint; EXP-06 (cumulative trees counter on thank-you page) requires backend data integration across purchase history |

**Total: 44/50**
**Verdict: Good — minor fixes before shipping**

### Suggested fixes

1. **EXP-10**: Split into two separate experiments — EXP-10a (cookie consent banner) under Performance, EXP-10b (Lighthouse baseline) under Performance. As combined, the hypothesis has two different KPIs and two unrelated changes.
2. **Exec summary paragraph 1**: Open with the diagnosis rather than the strengths. Move the "operational foundation is sound" framing to paragraph 3 as contrast, not paragraph 1 as context.
3. **Mobile-Friendly Warn**: Add one sentence in the Technical Checks section or EXP-10 acknowledging it is a desktop-only audit limitation — not fixable in the current pipeline.
