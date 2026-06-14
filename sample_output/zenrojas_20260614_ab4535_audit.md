# CRO Audit - Zen Rojas (zenrojas.com)

**Run ID:** `zenrojas_20260614_ab4535`  
**Date:** 2026-06-14  
**Crawl health:** Healthy - 10/10 pages loaded, full shopping journey, friction 5.0/5

## Executive Summary

The biggest conversion constraint is purchase reassurance placement, not purchase-path friction. The journey itself is clean: the crawler reached checkout in 3 clicks with no friction flags, and checkout shows express checkout plus 9 detected payment methods (`artifacts/zenrojas_20260614_ab4535/pages/shopping_journey.json`, `artifacts/zenrojas_20260614_ab4535/screenshots/shopping_journey_checkout.png`). But on all 3 sampled PDPs, no rating summary is visible near the primary CTA. Review depth is mixed below the fold instead: `/products/blacktea` shows a real reviews block with 1 review, while `/products/tea-bags` and `/products/tea-seeper` show empty review states (`artifacts/zenrojas_20260614_ab4535/screenshots/product_page_2_products_blacktea.png`, `artifacts/zenrojas_20260614_ab4535/screenshots/product_page_1_products_tea-bags.png`, `artifacts/zenrojas_20260614_ab4535/screenshots/product_page_3_products_tea-seeper.png`). The brand's strongest trust story also lives on the About page rather than the populated cart surface where shoppers commit (`artifacts/zenrojas_20260614_ab4535/screenshots/about_page_9_pages_aboutus.png`, `artifacts/zenrojas_20260614_ab4535/screenshots/shopping_journey_cart.png`).

The largest revenue opportunity is the gap between strong PDP merchandising and weak cart merchandising. PDP1 and PDP2 both show a visible "Frequently bought together" module, and all 3 sampled PDPs show "Complete Your Ritual" cross-sells (`artifacts/zenrojas_20260614_ab4535/screenshots/product_page_1_products_tea-bags.png`, `artifacts/zenrojas_20260614_ab4535/screenshots/product_page_2_products_blacktea.png`, `artifacts/zenrojas_20260614_ab4535/screenshots/product_page_3_products_tea-seeper.png`). That momentum disappears in the populated cart: no upsell is visible, no free-shipping progress reinforces the "$50+ orders" threshold, and the journey JSON records `cart_upsell_present: false` (`artifacts/zenrojas_20260614_ab4535/screenshots/shopping_journey_cart.png`, `artifacts/zenrojas_20260614_ab4535/pages/shopping_journey.json`). Retention has the same pattern: checkout captures marketing consent, and the homepage footer has email capture, but no first-order incentive or subscription option was observed on the sampled tea PDPs (`artifacts/zenrojas_20260614_ab4535/screenshots/shopping_journey_checkout.png`, `artifacts/zenrojas_20260614_ab4535/screenshots/homepage_0_home.png`, `artifacts/zenrojas_20260614_ab4535/screenshots/product_page_1_products_tea-bags.png`).

Technical health is solid but not complete. The run passed 12 of 17 checks, including mobile-friendly, page-speed timing, and checkout reachability (`artifacts/zenrojas_20260614_ab4535/technical_checks.json`). The 5 warnings are the more strategic cleanup list: no JSON-LD across the crawl, weak metadata on key discovery surfaces, no favicon link tag, 4 non-critical broken links, and 31/92 sampled images missing alt text (`artifacts/zenrojas_20260614_ab4535/technical_checks.json`, `artifacts/zenrojas_20260614_ab4535/pages/homepage_0_home.json`, `artifacts/zenrojas_20260614_ab4535/pages/blog_or_content_page_10_blogs_weekly-blog_building-a-family-lega.json`). None of these block checkout, but they do hold back discovery quality and polish for a brand with real story depth.

## Proposed Experiments

### EXP-01: Move tea PDP proof into the buy box

| Field | Value |
|---|---|
| Pillar | Conversion |
| Surface | PDP - buy box |
| URL | https://zenrojas.com/products/blacktea |
| Evidence | artifacts/zenrojas_20260614_ab4535/screenshots/product_page_2_products_blacktea.png |
| Hypothesis | Showing a rating summary and review count directly near the tea PDP CTA will lift add-to-cart rate, because the sampled PDPs keep review proof below the fold or in an empty state instead of at the decision point. |
| Primary change | Add a compact star-rating summary with review count beneath the product title and above the primary CTA on tea PDPs; keep the full reviews section lower on the page. |
| Primary KPI | PDP add-to-cart rate |
| Decision rule | Ship if add-to-cart rate improves by at least 5% relative over 3 weeks with no drop in checkout-start rate. |
| Expected lift | +5-11% |
| Confidence | 76% |

### EXP-02: Add a trust strip to the populated cart

| Field | Value |
|---|---|
| Pillar | Conversion |
| Surface | Cart - above checkout CTA |
| URL | https://zenrojas.com/cart |
| Evidence | artifacts/zenrojas_20260614_ab4535/screenshots/shopping_journey_cart.png |
| Hypothesis | Adding a trust strip above checkout will increase cart-to-checkout continuation, because the populated cart currently shows price and subtotal but not the veteran-owned, organic, or guarantee reassurance visible elsewhere in the brand story. |
| Primary change | Add a compact cart reassurance band above the Checkout button with veteran-owned, secure-checkout, and guarantee messaging pulled from existing brand copy. |
| Primary KPI | Cart-to-checkout rate |
| Decision rule | Ship if cart-to-checkout rate improves by at least 3% relative over 3 weeks. |
| Expected lift | +3-7% |
| Confidence | 67% |

### EXP-03: Add free-shipping progress in the populated cart

| Field | Value |
|---|---|
| Pillar | AOV |
| Surface | Cart - summary area |
| URL | https://zenrojas.com/cart |
| Evidence | artifacts/zenrojas_20260614_ab4535/screenshots/shopping_journey_cart.png |
| Hypothesis | Showing a dynamic progress cue toward the visible "$50+ orders" threshold will raise AOV, because the populated cart currently gives shoppers no reminder of how close they are to qualifying for free shipping. |
| Primary change | Add a subtotal-aware progress bar with remaining-dollar messaging and a link to relevant add-ons. |
| Primary KPI | Average order value |
| Decision rule | Ship if AOV improves by at least 4% relative with no decrease in checkout-start rate over 3 weeks. |
| Expected lift | +5-10% |
| Confidence | 78% |

### EXP-04: Continue "Complete Your Ritual" inside the cart

| Field | Value |
|---|---|
| Pillar | AOV |
| Surface | Cart - below line items |
| URL | https://zenrojas.com/cart |
| Evidence | artifacts/zenrojas_20260614_ab4535/pages/shopping_journey.json |
| Hypothesis | Extending product recommendations into the cart will increase units per order, because the sampled PDPs already use cross-sells well while the journey cart records `cart_upsell_present: false`. |
| Primary change | Add a 2-3 item cart recommendation module tied to cart contents, prioritizing tea-and-teaware pairings and sampler add-ons. |
| Primary KPI | Units per order |
| Decision rule | Ship if units per order improve by at least 4% relative over 3 weeks. |
| Expected lift | +4-9% |
| Confidence | 72% |

### EXP-05: Add subscribe-and-save on consumable tea PDPs

| Field | Value |
|---|---|
| Pillar | Retention |
| Surface | Tea PDP - buy box |
| URL | https://zenrojas.com/products/tea-bags |
| Evidence | artifacts/zenrojas_20260614_ab4535/screenshots/product_page_1_products_tea-bags.png |
| Hypothesis | Adding a recurring purchase option on consumable tea PDPs will grow repeat revenue, because the sampled tea PDPs currently offer one-time purchase only despite the product category being replenishable. |
| Primary change | Add a one-time vs subscription selector with 30/45/60-day cadence options and a modest recurring-order discount on tea PDPs. |
| Primary KPI | Subscription attach rate / 90-day repeat revenue |
| Decision rule | Ship if at least 8% of tea orders choose subscription within 4 weeks with no decrease in primary conversion. |
| Expected lift | +8-18% |
| Confidence | 70% |

### EXP-06: Upgrade homepage capture from footer signup to incentivized lead capture

| Field | Value |
|---|---|
| Pillar | Retention |
| Surface | Homepage |
| URL | https://zenrojas.com/ |
| Evidence | artifacts/zenrojas_20260614_ab4535/screenshots/homepage_0_home.png |
| Hypothesis | Adding a clearer value exchange to homepage email capture will grow the list faster, because the current homepage already captures email in the footer but does not offer a first-order incentive or stronger prominence. |
| Primary change | Add an entry or exit-intent capture that offers a first-order incentive and keep the footer signup as a secondary capture point. |
| Primary KPI | Email capture rate |
| Decision rule | Ship if email capture rate reaches at least 2% of sessions with no meaningful bounce-rate increase over 3 weeks. |
| Expected lift | +1.5-3.5% |
| Confidence | 75% |

### EXP-07: Add Product and FAQPage structured data

| Field | Value |
|---|---|
| Pillar | Acquisition |
| Surface | PDPs + FAQ page |
| URL | https://zenrojas.com/products/blacktea |
| Evidence | artifacts/zenrojas_20260614_ab4535/technical_checks.json |
| Hypothesis | Adding Product and FAQPage JSON-LD will improve organic result quality and CTR, because the current crawl found no JSON-LD across the 10 sampled pages. |
| Primary change | Implement Product schema on PDPs and FAQPage schema on `/pages/faqs`, validating the output in Search Console and rich-results testing. |
| Primary KPI | Organic CTR / rich-result coverage |
| Decision rule | Ship and keep if rich-result eligibility is validated and organic CTR improves over 6 weeks. |
| Expected lift | +4-10% |
| Confidence | 66% |

### EXP-08: Turn founder content into a product-discovery surface

| Field | Value |
|---|---|
| Pillar | Acquisition |
| Surface | Blog article body |
| URL | https://zenrojas.com/blogs/weekly-blog/building-a-family-legacy-through-wellness-community-and-purpose-driven-growth |
| Evidence | artifacts/zenrojas_20260614_ab4535/screenshots/blog_or_content_page_10_blogs_weekly-blog_building-a-family-lega.png |
| Hypothesis | Adding contextual product cards and a stronger next-step CTA to founder-led blog content will increase content-assisted sessions into PDPs, because the sampled article builds trust today but does not place product CTAs inside the body. |
| Primary change | Add an in-content module with 1-2 relevant teas, a ritual CTA, and a supporting newsletter prompt near the middle and end of the article. |
| Primary KPI | Blog-to-PDP click-through rate |
| Decision rule | Ship if article-to-PDP click-through exceeds 3% and assisted add-to-cart rate rises over 6 weeks. |
| Expected lift | +3-8% |
| Confidence | 69% |

### EXP-09: Fix image accessibility coverage across the catalog

| Field | Value |
|---|---|
| Pillar | Performance |
| Surface | Sitewide image library |
| URL | https://zenrojas.com/ |
| Evidence | artifacts/zenrojas_20260614_ab4535/technical_checks.json |
| Hypothesis | Closing the current image-alt coverage gap will improve crawl cleanliness and content accessibility, because the technical audit found 31 of 92 sampled images missing alt text. |
| Primary change | Add descriptive alt text to missing catalog and content images, then add an image-publishing QA check so new assets cannot ship blank. |
| Primary KPI | Image-alt coverage / crawl cleanliness |
| Decision rule | Ship if alt coverage reaches at least 98% on the next crawl with no net-new missing-alt regressions. |
| Expected lift | +20-33% |
| Confidence | 73% |

### EXP-10: Add a crawl-clean release checklist for favicon and broken-link hygiene

| Field | Value |
|---|---|
| Pillar | Performance |
| Surface | Sitewide release QA |
| URL | https://zenrojas.com/ |
| Evidence | artifacts/zenrojas_20260614_ab4535/technical_checks.json |
| Hypothesis | A lightweight technical QA checklist will reduce polish leaks that hurt perceived quality, because the current crawl still flags 4 non-critical broken links and no favicon link tag. |
| Primary change | Add favicon-tag verification and broken-link scanning to the release checklist, then fix the current flagged issues before the next crawl. |
| Primary KPI | Warning-count reduction in technical crawl |
| Decision rule | Ship if the next crawl clears both the favicon and broken-link warnings with no new regressions. |
| Expected lift | +40-100% |
| Confidence | 64% |

## Competitor Analysis

Selected from `store_category: tea / organic wellness beverages and teaware` and the store's ritual/wellness use cases in `artifacts/zenrojas_20260614_ab4535/evidence_summary.md`.

| Competitor | Domain | Positioning | What they make easier | Zen Rojas edge | Pattern to adapt |
|---|---|---|---|---|---|
| Vahdam Teas | https://www.vahdam.com | Premium global tea brand with strong tea-category merchandising | Review density and rating visibility on PDPs; subscription mechanics are easier to understand | Zen Rojas has a more personal veteran-owned story | Surface proof near the buy box and test subscriptions (EXP-01, EXP-05) |
| Art of Tea | https://www.artoftea.com | Organic tea and gifting brand with ritual positioning | Bundles and giftable attach flows are more explicit across tea and teaware | Zen Rojas has a simpler, less crowded visual language | Extend ritual merchandising into cart and attach surfaces (EXP-03, EXP-04) |
| Rishi Tea | https://rishi-tea.com | Botanical and wellness-forward tea authority | Discovery surfaces and education content connect more directly back to product exploration | Zen Rojas has founder-led local-community storytelling | Commercialize content and improve organic discovery hygiene (EXP-07, EXP-08) |
| Tea Drops | https://www.myteadrop.com | Modern tea ritual brand with a broader lifestyle/lift-the-routine angle | List-growth and starter-funnel patterns are more assertive at session entry | Zen Rojas has stronger veteran-owned trust storytelling | Upgrade lead capture beyond footer-only value exchange (EXP-06) |

## Technical Checks

All 17 checks reproduced from `artifacts/zenrojas_20260614_ab4535/technical_checks.json`.

| Check | Status | Detail |
|---|---|---|
| SSL Certificate | Pass | HTTPS storefront loaded successfully. |
| HTTPS Redirect | Pass | HTTP redirected to HTTPS. |
| Sitemap | Pass | sitemap.xml found with ~5 entries. |
| Robots.txt | Pass | robots.txt accessible. |
| Critical Pages Loading | Pass | 10/10 selected pages loaded successfully. |
| Meta Tags & Social Previews | Warn | Title+meta description present on 9/10 pages. OG tags present on all pages. |
| Structured Data | Warn | No JSON-LD detected across 10 crawled pages. |
| Favicon | Warn | No favicon link tag detected across 10 crawled pages. |
| Mobile-Friendly | Pass | Viewport meta present and no horizontal overflow at 375px. |
| Page Speed Mobile | Pass | Navigation timing (single run, not Lighthouse): load 1733ms, DCL 970ms at 375px viewport. |
| Page Speed Desktop | Pass | Navigation timing (single run, not Lighthouse): load 1978ms, DCL 1033ms. |
| Broken Links | Warn | 4 non-critical broken links in 40 sampled. |
| Image Optimization | Warn | 31/92 images missing alt text (33%) across 10 crawled pages. Byte-level audit not run. |
| Cookie/Privacy | Pass | Privacy Policy and Terms found. Cookie policy also present. |
| Checkout Reachable | Pass | Cart loaded and checkout entry reached. Journey stopped before payment entry. |
| Payment Methods | Pass | Detected: Visa, Mastercard, Amex, PayPal, Apple Pay, Google Pay, Shop Pay, Diners Club, JCB. |
| Shopping Journey | Pass | Score 5.0/5 - no blockers detected. Payment: Visa, Mastercard, Amex, PayPal, Apple Pay, Google Pay, Shop Pay, Diners Club, JCB. |
