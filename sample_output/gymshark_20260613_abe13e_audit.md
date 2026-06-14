# CRO Audit: gymshark

Run ID: `gymshark_20260613_abe13e`  
Date: 2026-06-13

## Executive Summary

Gymshark does not have a weak merchandising or content problem. The homepage is packed with campaign content, category routing, and training-intent navigation, while the sampled PDP shows specific fit and fabric claims, a size guide, color options, and payment-method visibility (`artifacts/gymshark_20260613_abe13e/screenshots/homepage_0_home.png`, `artifacts/gymshark_20260613_abe13e/screenshots/shopping_journey_pdp.png`, `artifacts/gymshark_20260613_abe13e/pages/product_page_1_products_gymshark-x-bratz-shorts-shorts-.md`). The main conversion constraint is purchase-path reliability because this Degraded run could not verify add-to-cart on any sampled PDP, the bag stayed empty, and checkout redirected back to the homepage instead of continuing the transaction, which means high-intent shoppers may be leaking before the actual sale can happen (`artifacts/gymshark_20260613_abe13e/summary.md`, `artifacts/gymshark_20260613_abe13e/pages/shopping_journey.json`, `artifacts/gymshark_20260613_abe13e/screenshots/shopping_journey_cart.png`, `artifacts/gymshark_20260613_abe13e/screenshots/shopping_journey_checkout.png`).

The next issue is focus and evidence quality. This run over-sampled one Bratz shorts product across three color variants and then paired it with caps and bags collections, which means the site’s broader assortment is richer than the PDP sample alone suggests (`artifacts/gymshark_20260613_abe13e/discovered_links.json`). Even so, the captured experience still shows a real browse problem: the homepage gives heavy weight to one campaign, the cookie banner blocks early product discovery, and the bags collection becomes a long, placeholder-heavy grid that feels more exhaustive than curated (`artifacts/gymshark_20260613_abe13e/screenshots/homepage_0_home.png`, `artifacts/gymshark_20260613_abe13e/screenshots/collection_page_6_collections_bags.png`). Technical health is otherwise decent on speed and link integrity, but shopping journey and checkout reachability failed and image alt coverage is poor, so the report should prioritize transaction confidence and tighter collection curation over generic storefront cleanup (`artifacts/gymshark_20260613_abe13e/technical_checks.json`).

## Proposed Experiments

### EXP-01: Verify and harden add-to-bag plus checkout handoff on top PDPs

| Field | Value |
|---|---|
| Pillar | Conversion |
| Surface | PDP to bag to checkout transition |
| URL | https://www.gymshark.com/products/gymshark-x-bratz-shorts-shorts-pink-ss26 |
| Evidence | artifacts/gymshark_20260613_abe13e/summary.md |
| Hypothesis | Hardening add-to-bag and checkout handoff will improve checkout-start rate because this run could not keep any sampled item in bag and checkout redirected away from the purchase flow. |
| Primary change | Instrument size-selection, add-to-bag, and checkout redirect events on top PDPs, then add explicit error handling and success-state confirmation when bag creation or checkout handoff fails. |
| Primary KPI | Checkout-start rate |
| Decision rule | Ship if checkout-start rate improves by at least 10% relative with a measurable drop in failed bag or redirect events over 3 weeks. |
| Expected lift | +10-18% |
| Confidence | 89% |

### EXP-02: Reduce single-campaign dominance on the homepage and surface broader shop-entry paths

| Field | Value |
|---|---|
| Pillar | Conversion |
| Surface | Homepage hero and first-scroll entry modules |
| URL | https://www.gymshark.com/ |
| Evidence | artifacts/gymshark_20260613_abe13e/screenshots/homepage_0_home.png |
| Hypothesis | Reducing single-campaign dominance will improve homepage-to-PDP click-through because the homepage currently gives disproportionate space to the Bratz launch while broader catalog entry and first product rails are partially blocked or delayed. |
| Primary change | Shrink or rotate the hero faster into evergreen category selectors like leggings, shorts, lifting, and running, and remove the cookie obstruction from the first product shelf. |
| Primary KPI | Homepage-to-PDP click-through rate |
| Decision rule | Ship if homepage-to-PDP click-through improves by at least 7% relative without lowering session depth. |
| Expected lift | +7-12% |
| Confidence | 81% |

### EXP-03: Add outfit-building logic to bag and mini-bag once core bag creation works

| Field | Value |
|---|---|
| Pillar | AOV |
| Surface | Bag and mini-bag recommendations |
| URL | https://gymshark.com/cart |
| Evidence | artifacts/gymshark_20260613_abe13e/screenshots/shopping_journey_cart.png |
| Hypothesis | Introducing outfit-building logic in bag will improve average order value because the captured journey never showed a populated bag, leaving Gymshark’s strong category breadth underused at the highest-intent moment. |
| Primary change | When a shopper adds leggings or shorts, recommend one matching bra or top plus one accessory such as a bag or cap rather than relying on empty-state bag recovery. |
| Primary KPI | Average order value |
| Decision rule | Ship if average order value improves by at least 9% relative while checkout-start rate stays flat or better. |
| Expected lift | +9-15% |
| Confidence | 74% |

### EXP-04: Curate accessories into tighter use-case bundles instead of long exhaustive grids

| Field | Value |
|---|---|
| Pillar | AOV |
| Surface | Bags and caps collections |
| URL | https://www.gymshark.com/collections/bags |
| Evidence | artifacts/gymshark_20260613_abe13e/screenshots/collection_page_6_collections_bags.png |
| Hypothesis | Curating accessories into tighter use-case bundles will improve collection conversion because the current bags page becomes a very long and repetitive grid that feels more like inventory exposure than a guided purchase path. |
| Primary change | Add curated blocks such as "gym commute setup," "lifting essentials," and "weekend training kit" above or within the accessories grid. |
| Primary KPI | Collection-to-PDP click-through rate |
| Decision rule | Ship if collection-to-PDP click-through improves by at least 8% relative without reducing pages per session. |
| Expected lift | +8-13% |
| Confidence | 73% |

### EXP-05: Move loyalty and student benefits into active purchase moments

| Field | Value |
|---|---|
| Pillar | Retention |
| Surface | PDP, bag, and checkout-adjacent messaging |
| URL | https://www.gymshark.com/ |
| Evidence | artifacts/gymshark_20260613_abe13e/screenshots/homepage_0_home.png |
| Hypothesis | Surfacing loyalty and student benefits earlier in the purchase flow will improve signup and repeat-purchase participation because these programs currently appear more clearly in footer or support surfaces than in active shopping moments. |
| Primary change | Add concise loyalty and student-benefit callouts near the purchase card and bag, tied to first-order value and future savings. |
| Primary KPI | Loyalty or student-program attach rate |
| Decision rule | Ship if program attach improves by at least 10% relative without lowering first-order conversion. |
| Expected lift | +10-16% |
| Confidence | 76% |

### EXP-06: Build post-purchase training-category progression flows

| Field | Value |
|---|---|
| Pillar | Retention |
| Surface | Post-purchase lifecycle for apparel buyers |
| URL | https://www.gymshark.com/pages/leggings-guide |
| Evidence | inferred - journey stops at checkout entry |
| Hypothesis | Guiding first-order buyers into adjacent training categories will improve repeat purchase rate because Gymshark’s site architecture already organizes the brand around lifting, running, HIIT, leggings, and matching sets. |
| Primary change | Create lifecycle journeys that recommend the next category based on first purchase type, such as leggings to sports bras, shorts to tops, or apparel to accessories. |
| Primary KPI | 60-day repeat purchase rate |
| Decision rule | Ship if 60-day repeat purchase improves by at least 7% relative among first-order buyers over 8 weeks. |
| Expected lift | +7-12% |
| Confidence | 70% |

### EXP-07: Replicate the leggings-guide merchandising model across more category guides

| Field | Value |
|---|---|
| Pillar | Acquisition |
| Surface | Category guide pages and search-entry landers |
| URL | https://www.gymshark.com/pages/leggings-guide |
| Evidence | artifacts/gymshark_20260613_abe13e/screenshots/blog_or_content_page_10_pages_leggings-guide.png |
| Hypothesis | Extending the leggings-guide model to other categories will improve content-assisted conversion because this guide already combines bestsellers, training intent, fit, color, and related education in a highly shoppable format. |
| Primary change | Launch parallel guides for shorts, sports bras, and men’s training tops using the same blend of education and direct shopping paths. |
| Primary KPI | Guide-page-to-PDP click-through rate |
| Decision rule | Ship if guide-page-to-PDP click-through improves by at least 10% relative versus standard collection entry pages. |
| Expected lift | +8-14% |
| Confidence | 82% |

### EXP-08: Surface training-mode routing earlier across home and evergreen navigation

| Field | Value |
|---|---|
| Pillar | Acquisition |
| Surface | Homepage mid-page routing and navigation handoffs |
| URL | https://www.gymshark.com/ |
| Evidence | artifacts/gymshark_20260613_abe13e/screenshots/homepage_0_home.png |
| Hypothesis | Bringing training-mode routing earlier will improve entry-page conversion because Gymshark clearly knows how shoppers think by activity, but that logic appears lower in the homepage than the big collab launch does. |
| Primary change | Move "How do you train?" style routing higher and make it a primary home-entry decision instead of a lower-page module. |
| Primary KPI | Homepage-to-category click-through rate |
| Decision rule | Ship if homepage-to-category click-through improves by at least 8% relative without lowering hero engagement. |
| Expected lift | +8-13% |
| Confidence | 78% |

### EXP-09: Reduce placeholder-heavy fatigue on long accessory collection pages

| Field | Value |
|---|---|
| Pillar | Performance |
| Surface | Bags and accessories collection rendering |
| URL | https://www.gymshark.com/collections/bags |
| Evidence | artifacts/gymshark_20260613_abe13e/screenshots/collection_page_6_collections_bags.png |
| Hypothesis | Reducing placeholder-heavy fatigue on long collections will improve collection engagement because the current bags page stretches into many low-information or partially loaded product states. |
| Primary change | Paginate or chunk very long collections, prioritize the best-converting items first, and lazy-load later rows only after intentful scrolling. |
| Primary KPI | Collection-page bounce rate |
| Decision rule | Ship if collection bounce improves and PDP click-through stays flat or better after the leaner rendering change. |
| Expected lift | +4-9% |
| Confidence | 75% |

### EXP-10: Improve image-alt coverage and transaction-state resilience together

| Field | Value |
|---|---|
| Pillar | Performance |
| Surface | PDP media, collection cards, and bag state transitions |
| URL | https://www.gymshark.com/products/gymshark-x-bratz-shorts-shorts-pink-ss26 |
| Evidence | artifacts/gymshark_20260613_abe13e/technical_checks.json |
| Hypothesis | Improving image-alt coverage and transaction-state resilience will improve perceived quality because the site is fast overall but still shows major alt gaps and a purchase state that failed before checkout. |
| Primary change | Audit product and collection media alt text, then simplify bag-state transitions and confirmation feedback after size selection and add-to-bag attempts. |
| Primary KPI | PDP add-to-bag rate |
| Decision rule | Ship if PDP add-to-bag improves by at least 6% relative with reduced state-failure events over 3 weeks. |
| Expected lift | +6-10% |
| Confidence | 80% |

## Competitor Analysis

These benchmarks focus on performance-apparel brands that make category routing, outfit-building, or training-intent shopping easier than the current Gymshark purchase path does on this run (`artifacts/gymshark_20260613_abe13e/evidence_summary.md`).

| Competitor | Domain | Positioning | What they make easier | gymshark edge | Pattern to adapt |
|---|---|---|---|---|---|
| lululemon | https://shop.lululemon.com/ | Premium performance-apparel leader with strong activity-based shopping and wardrobe-building | Activity-led routing, fit education, and polished cross-category outfit logic | Stronger creator/community energy and a more youth-coded training identity | Bring training-mode and fit routing earlier while improving outfit-building from bag and guides (EXP-03, EXP-08) |
| Vuori | https://vuoriclothing.com/ | Performance-lifestyle apparel brand with calmer merchandising and broad everyday versatility | Cleaner category curation and less campaign-heavy entry flows | More explicit gym-performance credibility and stronger training-specific identity | Tighten campaign focus and simplify path to first product (EXP-02, EXP-09) |
| Alo Yoga | https://www.aloyoga.com/ | Style-driven activewear brand with strong set-building and accessory merchandising | Matching-set logic, accessory pairing, and high-visual cross-sells | Broader training segmentation and stronger gym-specific product claims | Expand outfit and accessory bundling once bag creation is reliable (EXP-03, EXP-04) |

## Technical Checks

| Check | Status | Detail |
|---|---|---|
| SSL Certificate | Pass | HTTPS storefront loaded successfully. |
| HTTPS Redirect | Pass | HTTP redirected to HTTPS. |
| Sitemap | Pass | sitemap.xml found with ~15 entries. |
| Robots.txt | Pass | robots.txt accessible. |
| Critical Pages Loading | Pass | 9/9 selected pages loaded successfully. |
| Meta Tags & Social Previews | Warn | Title+meta description present on 8/9 pages. OG tags missing on 3/9 pages. |
| Structured Data | Pass | JSON-LD found on 4/9 pages: WebSite, Organization, ProductGroup. Product JSON-LD on 3/3 PDPs. |
| Favicon | Pass | Favicon link tag found. |
| Mobile-Friendly | Pass | Viewport meta present and no horizontal overflow at 375px. |
| Page Speed Mobile | Pass | Navigation timing (single run, not Lighthouse): load 2339ms, DCL 916ms at 375px viewport. |
| Page Speed Desktop | Pass | Navigation timing (single run, not Lighthouse): load 2136ms, DCL 994ms. |
| Broken Links | Pass | No broken links in 39 sampled links. |
| Image Optimization | Warn | 644/1349 images missing alt text (47%) across 9 crawled pages. Byte-level audit not run. |
| Cookie/Privacy | Pass | Privacy Policy and Terms found. Cookie policy also present. |
| Checkout Reachable | Fail | Checkout entry not reachable - redirected away from checkout (https://www.gymshark.com/). |
| Payment Methods | Pass | Detected: Visa, Mastercard, Amex, PayPal, Apple Pay, Klarna, Afterpay. |
| Shopping Journey | Fail | Score 2.0/5 - add to cart failed (-2.0), checkout load failed (-1.0). Payment: Visa, Mastercard, Amex, PayPal, Apple Pay, Klarna, Afterpay. |
