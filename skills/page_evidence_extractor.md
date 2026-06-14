# /page-evidence-extractor

Extract CRO evidence from a single crawled page into one
`evidence_cards/<name>.json` file. Stay at page scope. This skill should make
later reasoning easier by recording normalized page facts, not just prose.

## Input

For a regular page, provide:
- `artifacts/<run_id>/pages/<name>.json` - structured metadata (title, headings, CTAs, links)
- `artifacts/<run_id>/pages/<name>.md` - rendered page text
- `artifacts/<run_id>/screenshots/<name>.png` - visual screenshot

For the shopping journey card, provide:
- `artifacts/<run_id>/pages/shopping_journey.json`
- `artifacts/<run_id>/screenshots/shopping_journey_pdp.png`
- `artifacts/<run_id>/screenshots/shopping_journey_cart.png`
- `artifacts/<run_id>/screenshots/shopping_journey_checkout.png` or `shopping_journey_retailer.png`

## Output

Save to `artifacts/<run_id>/evidence_cards/<name>.json`.

### Required shape

```json
{
  "page_url": "https://...",
  "page_type": "product_page",
  "name": "<artifact name>",
  "run_id": "<run_id>",
  "primary_visual_evidence": "artifacts/<run_id>/screenshots/<name>.png",
  "facts": [
    {
      "key": "reviews_visible",
      "state": "present",
      "scope": "below_fold",
      "evidence": "artifacts/<run_id>/screenshots/<name>.png",
      "note": "Reviews block visible near bottom of PDP"
    }
  ],
  "observed_strengths": [
    {
      "observation": "Frequently bought together bundle is visible and actionable",
      "evidence": "artifacts/<run_id>/screenshots/<name>.png",
      "pillar": "AOV"
    }
  ],
  "missing_or_weak": [
    {
      "observation": "No review summary is visible near the primary CTA",
      "evidence": "artifacts/<run_id>/screenshots/<name>.png",
      "pillar": "Conversion"
    }
  ],
  "purchase_path_notes": "Bundle and cross-sell are present on the PDP.",
  "pillar_tags": ["Conversion", "AOV"]
}
```

### `facts` state vocabulary

Use only:
- `present`
- `absent`
- `mixed`
- `unclear`
- `not_applicable`

### Preferred evidence source

- Use screenshots for visible UI claims.
- Use page JSON/MD for metadata, hidden text, headings, links, or copy not legible in the screenshot.
- Use shopping journey JSON only for machine-recorded journey facts such as `cart_upsell_present`.

## Required facts by page type

Record only the fields that are relevant and observable for that page type.

### Product page

- `reviews_visible`
- `review_count_visible`
- `rating_summary_near_cta`
- `bundle_present`
- `cross_sell_present`
- `subscription_present`
- `trust_reassurance_present`
- `express_checkout_present`

### Collection page

- `sort_control_present`
- `filter_control_present`
- `proof_badges_present`
- `sold_out_state_visible`

### Cart page

- `empty_cart_state`
- `cart_upsell_present`
- `free_shipping_progress_present`
- `trust_reassurance_present`
- `express_checkout_present`

### Homepage / content / about

- `email_capture_present`
- `email_incentive_present`
- `social_proof_present`
- `product_cta_present`
- `trust_story_present`

### Shopping journey

- Copy `friction_score`, `friction_flags`, `friction_detail`, `journey_observations`, and
  `payment_methods_detected` verbatim from `pages/shopping_journey.json`.
- Add screenshot-based facts for the journey surfaces when visible.

## Extraction rules

- Only observe what is present in the artifacts. Do not infer, assume, or add anything not supported by the screenshot, HTML, or metadata.
- Cite every observation. Each item in `facts`, `observed_strengths`, and `missing_or_weak` must include a real artifact path.
- Stay at page scope. Do not draw store-level conclusions here.
- If an element exists, do not mark it as missing. Describe the real issue precisely:
  - `below_fold`
  - `not_adjacent_to_cta`
  - `low_prominence`
  - `empty_state`
  - `inconsistent_copy`
- If the evidence is ambiguous, mark the fact `unclear` and explain why.
- If a screenshot and metadata disagree, trust the screenshot for visible UI and mention the conflict in `note`.
- If the page is an empty cart or fallback state, say so explicitly in `facts`; do not let later stages confuse it with a populated cart.
