# CRO Audit: puravidabracelets

Run ID: `puravidabracelets_20260613_38ebc0`  
Date: 2026-06-13

## Executive Summary

Pura Vida does not have a broken shopping path. The sampled journey completed cleanly from PDP to cart to checkout entry with a 5.0/5 friction score, and the sampled bracelet PDP already shows stock messaging, pair-with cross-sells, and visible review content (`artifacts/puravidabracelets_20260613_38ebc0/pages/shopping_journey.json`, `artifacts/puravidabracelets_20260613_38ebc0/screenshots/product_page_1_products_isla.png`, `artifacts/puravidabracelets_20260613_38ebc0/screenshots/shopping_journey_checkout.png`). The sharper issue is distraction: the homepage, sale collection, and PDPs all show layered interruptions that compete with product discovery, including cookie consent, a 10% capture modal, a side cart drawer, and an unrelated ring-size overlay on a bracelet PDP (`artifacts/puravidabracelets_20260613_38ebc0/screenshots/homepage_0_home.png`, `artifacts/puravidabracelets_20260613_38ebc0/screenshots/collection_page_5_collections_sale.png`, `artifacts/puravidabracelets_20260613_38ebc0/screenshots/product_page_1_products_isla.png`, `artifacts/puravidabracelets_20260613_38ebc0/screenshots/shopping_journey_cart.png`).

The second issue is that assortment breadth is stronger than purchase guidance. Pura Vida has a huge low-ticket catalog and obvious basket-building potential across bracelets, rings, sunglasses, and Bracelet Club, but the current experience often feels like endless browsing rather than guided stacking or gifting (`artifacts/puravidabracelets_20260613_38ebc0/screenshots/homepage_0_home.png`, `artifacts/puravidabracelets_20260613_38ebc0/screenshots/collection_page_5_collections_sale.png`, `artifacts/puravidabracelets_20260613_38ebc0/screenshots/collection_page_6_collections_rings.png`). This run also has one evidence-quality caveat: the intended help / FAQ path did not resolve to a normal policy page and fell back to support videos, so the report should not overclaim shipping or returns detail from that surface (`artifacts/puravidabracelets_20260613_38ebc0/screenshots/faq_shipping_returns_8_pages_support-videos.png`, `artifacts/puravidabracelets_20260613_38ebc0/discovered_links.json`).

## Proposed Experiments

### EXP-01: Remove stacked interruptions from the browse-to-buy path

| Field | Value |
|---|---|
| Pillar | Conversion |
| Surface | Homepage, sale collection, and PDP overlay behavior |
| URL | https://puravidabracelets.com/collections/sale |
| Evidence | artifacts/puravidabracelets_20260613_38ebc0/screenshots/collection_page_5_collections_sale.png |
| Hypothesis | Reducing stacked interruptions across browse and PDP surfaces will improve product engagement and add-to-cart rate because shoppers currently face multiple competing overlays before they can focus on merchandise. |
| Primary change | Suppress the 10% capture modal until later intent signals, avoid utility overlays like ring-size guidance on irrelevant product types, and sequence cookie / promo / cart surfaces more deliberately. |
| Primary KPI | Add-to-cart rate |
| Decision rule | Ship if add-to-cart rate improves by at least 6% relative without materially lowering email capture efficiency over 3 weeks. |
| Expected lift | +6-11% |
| Confidence | 87% |

### EXP-02: Curate clearer entry paths through the low-ticket catalog

| Field | Value |
|---|---|
| Pillar | Conversion |
| Surface | Homepage and key collection entry points |
| URL | https://puravidabracelets.com/ |
| Evidence | artifacts/puravidabracelets_20260613_38ebc0/screenshots/homepage_0_home.png |
| Hypothesis | Curating clearer “start here” paths through the catalog will improve homepage-to-PDP click-through because the current experience exposes a huge number of low-price SKUs before helping shoppers build a first stack or occasion-based set. |
| Primary change | Add curated entry modules such as “Best first stack,” “Under $25 favorites,” “Vacation bracelets,” and “Gift-ready picks,” then reduce the reliance on long generic product rails. |
| Primary KPI | Homepage-to-PDP click-through rate |
| Decision rule | Ship if homepage-to-PDP click-through improves by at least 8% relative without lowering average items viewed per session. |
| Expected lift | +8-14% |
| Confidence | 81% |

### EXP-03: Use cart to build stacks, not just confirm single-item orders

| Field | Value |
|---|---|
| Pillar | AOV |
| Surface | Cart drawer for low-price bracelet orders |
| URL | https://puravidabracelets.com/cart |
| Evidence | artifacts/puravidabracelets_20260613_38ebc0/screenshots/shopping_journey_cart.png |
| Hypothesis | Reframing cart as a stack-building surface will improve average order value because the sampled low-ticket cart does not strongly help a shopper move from one bracelet to a fuller styled set. |
| Primary change | Add curated stack suggestions and spend-threshold offers in cart, such as “Complete this color story,” “Add two more for free shipping,” or “Build a beach stack.” |
| Primary KPI | Average order value |
| Decision rule | Ship if average order value improves by at least 9% relative while checkout-start rate stays flat or better. |
| Expected lift | +9-16% |
| Confidence | 78% |

### EXP-04: Create occasion-led bundles for gifting and self-expression

| Field | Value |
|---|---|
| Pillar | AOV |
| Surface | Collection rails, PDP recommendations, and homepage curation |
| URL | https://www.puravidabracelets.com/collections/rings |
| Evidence | artifacts/puravidabracelets_20260613_38ebc0/screenshots/collection_page_6_collections_rings.png |
| Hypothesis | Offering occasion-led bundles will improve multi-item order rate because Pura Vida’s catalog already supports stacking and gifting, but shoppers must currently do too much of the styling and curation themselves. |
| Primary change | Launch bundles like “Beach Weekend Stack,” “Best Friend Gift Set,” and “Summer Ring + Bracelet Pairing” across collection and PDP surfaces. |
| Primary KPI | Multi-item order rate |
| Decision rule | Ship if multi-item order rate improves by at least 8% relative without lowering single-item conversion on core PDPs. |
| Expected lift | +8-15% |
| Confidence | 74% |

### EXP-05: Bring Bracelet Club into the active shopping flow

| Field | Value |
|---|---|
| Pillar | Retention |
| Surface | Homepage, PDP, and cart club messaging |
| URL | https://puravidabracelets.com/ |
| Evidence | artifacts/puravidabracelets_20260613_38ebc0/screenshots/homepage_0_home.png |
| Hypothesis | Bringing Bracelet Club into active purchase moments will improve recurring-program adoption because the homepage promotes monthly delivery, but the sampled product-to-cart flow does not strongly connect ordinary bracelet purchases to the club. |
| Primary change | Add club comparison cards on PDP and cart that explain when a shopper should buy one item versus join Bracelet Club for monthly variety and value. |
| Primary KPI | Bracelet Club click-through or signup rate |
| Decision rule | Ship if Bracelet Club signup or click-through improves by at least 12% relative without lowering first-order conversion. |
| Expected lift | +10-18% |
| Confidence | 80% |

### EXP-06: Convert one-bracelet buyers into multi-order habit shoppers

| Field | Value |
|---|---|
| Pillar | Retention |
| Surface | Post-purchase lifecycle for low-ticket bracelet buyers |
| URL | https://www.puravidabracelets.com/products/isla |
| Evidence | inferred - journey stops at checkout entry |
| Hypothesis | Following one-bracelet buyers with stack-building and club messaging will improve repeat purchase rate because the brand’s economics and category structure reward ongoing collecting rather than one-off item purchases. |
| Primary change | Send a post-purchase series that recommends matching styles, seasonal stacks, and Bracelet Club based on the first item purchased. |
| Primary KPI | 60-day repeat purchase rate |
| Decision rule | Ship if 60-day repeat purchase improves by at least 7% relative among single-item first orders over 8 weeks. |
| Expected lift | +7-13% |
| Confidence | 69% |

### EXP-07: Turn PV Scoop stories into “shop the vibe” merchandising

| Field | Value |
|---|---|
| Pillar | Acquisition |
| Surface | PV Scoop hub and related lifestyle content |
| URL | https://puravidabracelets.com/blogs/the-pv-scoop |
| Evidence | artifacts/puravidabracelets_20260613_38ebc0/screenshots/blog_or_content_page_10_blogs_the-pv-scoop.png |
| Hypothesis | Turning lifestyle stories into “shop the vibe” merchandising will improve content-assisted conversion because the current PV Scoop hub is inspirational but does not strongly route readers into matching products or looks. |
| Primary change | Add story-linked look carousels and “shop this trip / look / mood” modules to blog cards and article templates. |
| Primary KPI | Content-assisted product click-through rate |
| Decision rule | Ship if content-assisted product clicks improve by at least 12% relative without lowering content engagement depth. |
| Expected lift | +8-14% |
| Confidence | 76% |

### EXP-08: Build inspiration-led category pages instead of generic product sprawl

| Field | Value |
|---|---|
| Pillar | Acquisition |
| Surface | Homepage categories and sale / rings collection routing |
| URL | https://puravidabracelets.com/collections/sale |
| Evidence | artifacts/puravidabracelets_20260613_38ebc0/screenshots/collection_page_5_collections_sale.png |
| Hypothesis | Replacing generic product sprawl with inspiration-led category pages will improve landing-page conversion because the current assortment is large enough to feel noisy without stronger “why this set?” framing. |
| Primary change | Create curated landing pages such as “Travel-ready stacks,” “Gift under $20,” and “Top-rated rings” to route paid or organic traffic into tighter assortments. |
| Primary KPI | Collection-to-PDP click-through rate |
| Decision rule | Ship if collection-to-PDP click-through improves by at least 10% relative without reducing pages per session. |
| Expected lift | +8-15% |
| Confidence | 73% |

### EXP-09: Reduce mobile load from dense imagery and overlay scripts

| Field | Value |
|---|---|
| Pillar | Performance |
| Surface | Homepage, collection, and PDP mobile loading |
| URL | https://puravidabracelets.com/ |
| Evidence | artifacts/puravidabracelets_20260613_38ebc0/technical_checks.json |
| Hypothesis | Reducing mobile load from dense imagery and overlay scripts will improve browse depth because mobile page speed failed badly on a store that relies on long visual rails and many layered UI elements. |
| Primary change | Defer non-critical overlays and compress below-fold product-grid imagery, especially on homepage and collection pages. |
| Primary KPI | Homepage bounce rate |
| Decision rule | Ship if mobile load falls below 4.0s with improved bounce and no conversion regression. |
| Expected lift | +4-9% |
| Confidence | 79% |

### EXP-10: Simplify below-fold recommendation bloat on long pages

| Field | Value |
|---|---|
| Pillar | Performance |
| Surface | PDP and homepage recommendation sections |
| URL | https://www.puravidabracelets.com/products/isla |
| Evidence | artifacts/puravidabracelets_20260613_38ebc0/screenshots/product_page_1_products_isla.png |
| Hypothesis | Simplifying below-fold recommendation bloat will improve performance and scroll efficiency because the current pages stack multiple recommendation rails, brand blocks, and review sections on already long templates. |
| Primary change | Reduce duplicated recommendation modules and lazy-load lower-priority merchandising rails after the shopper has engaged with core product content. |
| Primary KPI | PDP bounce rate |
| Decision rule | Ship if PDP bounce improves and add-to-cart rate stays flat or better after the leaner template test. |
| Expected lift | +4-8% |
| Confidence | 72% |

## Competitor Analysis

These benchmarks focus on lifestyle jewelry and accessory brands that make stacking, gifting, or personalization easier than the current Pura Vida browse-to-buy flow does on this run (`artifacts/puravidabracelets_20260613_38ebc0/evidence_summary.md`).

| Competitor | Domain | Positioning | What they make easier | puravidabracelets edge | Pattern to adapt |
|---|---|---|---|---|---|
| BaubleBar | https://www.baublebar.com/ | Trend-led accessories and gifting brand with broad assortment | Occasion-based curation, gifting, and trend shopping | Stronger surf/lifestyle identity and lower-friction low-price entry | Add clearer occasion-led bundle and gift curation (EXP-03, EXP-04) |
| Little Words Project | https://www.littlewordsproject.com/ | Bracelet-first community and sentiment-driven jewelry brand | Emotional storytelling, collecting behavior, and bracelet-led repeat purchase | Broader accessory assortment and stronger visual merchandising range | Connect individual purchases to collecting and club behavior more directly (EXP-05, EXP-06) |
| Kendra Scott | https://www.kendrascott.com/ | Mainstream jewelry brand with polished category and gifting flows | Category clarity, gifting pathways, and guided browsing | More accessible price point and stronger friendship/community vibe | Reduce catalog sprawl by adding guided “shop the vibe” and gifting paths (EXP-02, EXP-08) |

## Technical Checks

| Check | Status | Detail |
|---|---|---|
| SSL Certificate | Pass | HTTPS storefront loaded successfully. |
| HTTPS Redirect | Pass | HTTP redirected to HTTPS. |
| Sitemap | Pass | sitemap.xml found with ~5 entries. |
| Robots.txt | Pass | robots.txt accessible. |
| Critical Pages Loading | Pass | 11/11 selected pages loaded successfully. |
| Meta Tags & Social Previews | Warn | Title+meta description present on 8/11 pages. OG tags present on all pages. |
| Structured Data | Pass | JSON-LD found on 11/11 pages: Organization, WebSite, Product. Product JSON-LD on 3/3 PDPs. |
| Favicon | Pass | Favicon link tag found. |
| Mobile-Friendly | Pass | Viewport meta present and no horizontal overflow at 375px. |
| Page Speed Mobile | Fail | Navigation timing (single run, not Lighthouse): load 9903ms, DCL 7193ms at 375px viewport. |
| Page Speed Desktop | Warn | Navigation timing (single run, not Lighthouse): load 3844ms, DCL 2703ms. |
| Broken Links | Pass | No broken links in 40 sampled links. |
| Image Optimization | Warn | 334/4957 images missing alt text (6%) across 11 crawled pages. Byte-level audit not run. |
| Cookie/Privacy | Warn | Privacy and Terms found but cookie consent policy not detected. |
| Checkout Reachable | Pass | Cart loaded and checkout entry reached. Journey stopped before payment entry. |
| Payment Methods | Pass | Detected: Visa, Mastercard, Amex, PayPal, Apple Pay, Shop Pay, Afterpay, JCB. |
| Shopping Journey | Pass | Score 5.0/5 - no blockers detected. Payment: Visa, Mastercard, Amex, PayPal, Apple Pay, Shop Pay, Afterpay, JCB. |
