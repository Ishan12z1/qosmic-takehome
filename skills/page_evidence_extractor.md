# /page-evidence-extractor

Extracts CRO evidence from a single crawled page's artifacts. Produces one
`evidence_cards/<name>.json` file per page. Run once per page in `selected_pages`,
plus once for the shopping journey.

## Input

For a regular page, provide:
- `artifacts/<run_id>/pages/<name>.json` — structured metadata (title, headings, CTAs, links)
- `artifacts/<run_id>/pages/<name>.md` — rendered page text
- `artifacts/<run_id>/screenshots/<name>.png` — visual screenshot

For the shopping journey card, provide:
- `artifacts/<run_id>/pages/shopping_journey.json`
- `artifacts/<run_id>/screenshots/shopping_journey_pdp.png`
- `artifacts/<run_id>/screenshots/shopping_journey_cart.png`
- `artifacts/<run_id>/screenshots/shopping_journey_checkout.png` or `shopping_journey_retailer.png`

## Output

Save to `artifacts/<run_id>/evidence_cards/<name>.json` (use the same `<name>` as the page artifact).

```json
{
  "page_url": "https://...",
  "page_type": "product_page",
  "name": "<artifact name>",
  "run_id": "<run_id>",
  "screenshot": "artifacts/<run_id>/screenshots/<name>.png",
  "observed_strengths": [
    {
      "observation": "Clear above-fold headline with brand promise",
      "evidence": "artifacts/<run_id>/screenshots/<name>.png",
      "pillar": "Conversion"
    }
  ],
  "missing_or_weak": [
    {
      "observation": "No social proof or star ratings above the fold",
      "evidence": "artifacts/<run_id>/screenshots/<name>.png",
      "pillar": "Conversion"
    }
  ],
  "purchase_path_notes": "Single-step add-to-cart, no variant upsell visible",
  "pillar_tags": ["Conversion", "AOV"]
}
```

For the shopping journey card, the schema extends to include journey-specific fields:

```json
{
  "page_url": "<store base url>",
  "page_type": "shopping_journey",
  "name": "shopping_journey",
  "run_id": "<run_id>",
  "outcome": "full_journey",
  "friction_score": 5.0,
  "friction_flags": [],
  "friction_detail": "Score 5.0/5 — no blockers detected",
  "journey_observations": {
    "click_count_to_checkout": 4,
    "trust_badges_at_checkout": true,
    "cart_upsell_present": false,
    "urgency_elements_present": false,
    "error_messages_detected": false
  },
  "payment_methods_detected": ["Visa", "Mastercard", "Shop Pay"],
  "observed_strengths": [...],
  "missing_or_weak": [...],
  "purchase_path_notes": "...",
  "pillar_tags": ["Conversion", "AOV", "Retention"]
}
```

## Extraction rules

**Only observe what is present in the artifacts.** Do not infer, assume, or add anything
not supported by the screenshot, HTML, or metadata.

**Cite every observation.** Each item in `observed_strengths` and `missing_or_weak` must
include an `"evidence"` field pointing to a real artifact path under `artifacts/<run_id>/`.
No citeless observations.

**Page-scope only.** This skill identifies page-level signals. Do not draw store-level
conclusions here — that is the evidence analyst's job.

**Pillar assignment** — assign each observation to its most relevant pillar:
- `Conversion` — friction, CTA clarity, trust signals, page load, checkout flow
- `AOV` — upsell, cross-sell, bundles, subscription offers
- `Retention` — loyalty programs, email capture, post-purchase flows, account benefits
- `Acquisition` — SEO (meta, headings, structured data), social proof, referral
- `Performance` — page speed signals, image weight, mobile layout issues

**Missing observations** — if the page has no obvious weaknesses in a pillar, omit that
pillar from `missing_or_weak` rather than inventing one.

**Shopping journey card specifics:**
- Copy `friction_score`, `friction_flags`, `friction_detail`, `journey_observations`, and
  `payment_methods_detected` verbatim from `pages/shopping_journey.json`.
- Add `observed_strengths` and `missing_or_weak` based on what you see in the screenshots.
- `purchase_path_notes` should summarize the full PDP → cart → checkout flow in 1–2 sentences.
