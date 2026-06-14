---
name: page-evidence-extractor
description: Extract cited CRO evidence from one crawled page's artifacts into evidence_cards/<name>.json. Use after a crawl, once per page in selected_pages plus the shopping journey.
---

# /page-evidence-extractor

Extract CRO evidence from a single crawled page's artifacts into
`artifacts/<run_id>/evidence_cards/<name>.json`. Follow the full schema and rules
in `skills/page_evidence_extractor.md`.

Key rules:
- Only observe what is present in the artifacts (screenshot / HTML / metadata).
- Every observation in `observed_strengths` and `missing_or_weak` carries an
  `evidence` path under `artifacts/<run_id>/`.
- Skip pages whose crawl status is `soft_404`, `blocked`, or `error` — note them
  as evidence gaps rather than inventing observations.
- For the shopping journey card, copy `friction_score`, `friction_flags`,
  `friction_detail`, `journey_observations`, and `payment_methods_detected`
  verbatim from `pages/shopping_journey.json`. Do not describe post-purchase
  surfaces — the journey stops at the checkout entry.
