# CRO Audit: allbirds

Run ID: `allbirds_20260613_24b222`  
Date: 2026-06-13

## Executive Summary

Allbirds already looks credible, premium, and easy to trust. The sampled PDPs show a clean purchase card with fit-guide access, clear pricing, free-shipping messaging, and size selection, while the cart and checkout entry both look polished once an item is present (`artifacts/allbirds_20260613_24b222/screenshots/shopping_journey_pdp.png`, `artifacts/allbirds_20260613_24b222/screenshots/shopping_journey_cart.png`, `artifacts/allbirds_20260613_24b222/screenshots/shopping_journey_checkout.png`). The sharper conversion constraint is purchase-path certainty because this Degraded run could not verify customer-facing add-to-cart on any of the three sampled PDPs and only reached a real cart after an API fallback, which means otherwise high-intent traffic may be leaking before the shopper gets a confirmed success state (`artifacts/allbirds_20260613_24b222/summary.md`, `artifacts/allbirds_20260613_24b222/pages/shopping_journey.json`).

The second issue is that Allbirds’ brand calm is stronger than its product-direction urgency. The homepage, Our Story, and The Perch all reinforce sustainability, comfort, and materials quality, but the collection page does a much better job than the homepage at helping shoppers compare real silhouettes and move toward a first purchase (`artifacts/allbirds_20260613_24b222/screenshots/homepage_0_home.png`, `artifacts/allbirds_20260613_24b222/screenshots/about_page_9_pages_our-story.png`, `artifacts/allbirds_20260613_24b222/screenshots/blog_or_content_page_10_blogs_the-perch.png`, `artifacts/allbirds_20260613_24b222/screenshots/collection_page_5_collections_mens.png`). Technical health is mostly good: metadata, broken links, privacy, payment methods, and checkout reachability all passed, but page speed, image alt coverage, and the add-to-cart fallback warning still matter because they create subtle friction on a site that otherwise signals precision and simplicity (`artifacts/allbirds_20260613_24b222/technical_checks.json`).

## Proposed Experiments

### EXP-01: Verify and harden UI add-to-cart on core shoe PDPs

| Field | Value |
|---|---|
| Pillar | Conversion |
| Surface | Core shoe PDP purchase-card interaction |
| URL | https://www.allbirds.com/products/mens-runner-nz-slip-on |
| Evidence | artifacts/allbirds_20260613_24b222/summary.md |
| Hypothesis | Hardening customer-facing add-to-cart on core PDPs will improve checkout-start rate because this run only succeeded after an API fallback even though the visible purchase card looked clean and complete. |
| Primary change | Instrument size-selection and add-to-cart state changes on top PDPs, then add explicit confirmation, loading, and retry handling whenever a shopper tries to add a shoe to cart. |
| Primary KPI | Checkout-start rate |
| Decision rule | Ship if checkout-start rate improves by at least 8% relative with a measurable drop in cart-state error events over 3 weeks. |
| Expected lift | +8-14% |
| Confidence | 86% |

### EXP-02: Bring clearer first-shoe guidance earlier into home and PDP experiences

| Field | Value |
|---|---|
| Pillar | Conversion |
| Surface | Homepage hero and PDP comparison guidance |
| URL | https://www.allbirds.com/ |
| Evidence | artifacts/allbirds_20260613_24b222/screenshots/homepage_0_home.png |
| Hypothesis | Giving shoppers clearer first-shoe guidance earlier will improve homepage-to-PDP click-through because the homepage currently sells the brand mood more strongly than it explains which silhouette fits which use case. |
| Primary change | Add "best for commute," "best for everyday walk," "best slip-on," and "best lightweight runner" guidance near the hero and major entry modules. |
| Primary KPI | Homepage-to-PDP click-through rate |
| Decision rule | Ship if homepage-to-PDP click-through improves by at least 7% relative without reducing session depth. |
| Expected lift | +7-12% |
| Confidence | 80% |

### EXP-03: Upgrade cart recommendations from accessory add-ons to second-pair logic

| Field | Value |
|---|---|
| Pillar | AOV |
| Surface | Cart drawer recommendations |
| URL | https://allbirds.com/cart |
| Evidence | artifacts/allbirds_20260613_24b222/screenshots/shopping_journey_cart.png |
| Hypothesis | Replacing narrow accessory-focused recommendations with second-pair logic will improve average order value because the sampled cart drawer mostly recommends socks rather than a higher-value adjacent silhouette or category step-up. |
| Primary change | Add one stronger cross-sell rule in cart such as "add a second everyday pair," "pair with apparel," or "add care essentials" based on the first item in cart. |
| Primary KPI | Average order value |
| Decision rule | Ship if average order value improves by at least 8% relative while checkout-start rate stays flat or better. |
| Expected lift | +8-13% |
| Confidence | 76% |

### EXP-04: Introduce wardrobe-building paths from collections, not just single-SKU browsing

| Field | Value |
|---|---|
| Pillar | AOV |
| Surface | Men’s and women’s collection pages |
| URL | https://www.allbirds.com/collections/mens |
| Evidence | artifacts/allbirds_20260613_24b222/screenshots/collection_page_5_collections_mens.png |
| Hypothesis | Building clearer second-item pathways from collection pages will improve multi-item order rate because collections already help shoppers compare silhouettes, but they do not strongly escalate those shoppers into a broader wardrobe or seasonal kit. |
| Primary change | Add curated collection modules such as "travel pair + casual pair," "office + weekend rotation," or "shoe + sock + apparel" bundles below the first product grid. |
| Primary KPI | Multi-item order rate |
| Decision rule | Ship if multi-item order rate improves by at least 7% relative without lowering PDP click-through. |
| Expected lift | +7-12% |
| Confidence | 72% |

### EXP-05: Build post-purchase progression from first pair to adjacent silhouette

| Field | Value |
|---|---|
| Pillar | Retention |
| Surface | Post-purchase lifecycle for first-pair buyers |
| URL | https://www.allbirds.com/products/mens-cruiser-medium-grey |
| Evidence | inferred - journey stops at checkout entry |
| Hypothesis | Guiding first-pair buyers into an adjacent silhouette will improve repeat purchase rate because the assortment supports natural progression from one comfort use case into another without needing a subscription model. |
| Primary change | Send a lifecycle sequence that recommends the next best pair based on first purchase type, such as commuter, slip-on, lounge, or seasonal rotation. |
| Primary KPI | 90-day repeat purchase rate |
| Decision rule | Ship if 90-day repeat purchase improves by at least 6% relative among first-time buyers over 10 weeks. |
| Expected lift | +6-11% |
| Confidence | 69% |

### EXP-06: Turn sustainability affinity into retention and reactivation messaging

| Field | Value |
|---|---|
| Pillar | Retention |
| Surface | Email and account lifecycle tied to materials and impact story |
| URL | https://allbirds.com/pages/our-story |
| Evidence | artifacts/allbirds_20260613_24b222/screenshots/about_page_9_pages_our-story.png |
| Hypothesis | Connecting sustainability affinity to reactivation messaging will improve returning-customer engagement because the brand story is strong across About and content pages but not obviously linked to a repeat-purchase cadence. |
| Primary change | Create a lifecycle stream that pairs product-use education with materials, care, and impact storytelling tied to the buyer’s first product category. |
| Primary KPI | Reactivation click-through rate |
| Decision rule | Ship if reactivation CTR improves by at least 10% relative without lowering conversion from those campaigns. |
| Expected lift | +8-14% |
| Confidence | 71% |

### EXP-07: Turn The Perch into a stronger product-entry content engine

| Field | Value |
|---|---|
| Pillar | Acquisition |
| Surface | The Perch blog hub and article cards |
| URL | https://www.allbirds.com/blogs/the-perch |
| Evidence | artifacts/allbirds_20260613_24b222/screenshots/blog_or_content_page_10_blogs_the-perch.png |
| Hypothesis | Adding stronger product handoffs from The Perch will improve content-assisted conversion because the blog already has high-quality editorial cards but weak visible pathways into matching shoes or categories. |
| Primary change | Add "shop this article" modules that map each story to the most relevant silhouette, weather use case, or apparel pairing. |
| Primary KPI | Content-assisted product click-through rate |
| Decision rule | Ship if content-assisted product clicks improve by at least 10% relative without reducing article engagement depth. |
| Expected lift | +8-13% |
| Confidence | 77% |

### EXP-08: Convert story and sustainability pages into clearer shop-entry paths

| Field | Value |
|---|---|
| Pillar | Acquisition |
| Surface | Our Story and materials-led brand pages |
| URL | https://allbirds.com/pages/our-story |
| Evidence | artifacts/allbirds_20260613_24b222/screenshots/about_page_9_pages_our-story.png |
| Hypothesis | Converting story pages into clearer shop-entry paths will improve assisted conversion because the brand narrative is memorable, but the current page does more to inspire values alignment than to help a shopper choose a specific product. |
| Primary change | Add material- and use-case-based shop blocks such as "shop breathable tree styles," "shop everyday commuters," and "shop lighter impact favorites." |
| Primary KPI | Story-page-to-PDP click-through rate |
| Decision rule | Ship if story-page-to-PDP click-through improves by at least 12% relative without reducing time on page. |
| Expected lift | +9-15% |
| Confidence | 75% |

### EXP-09: Reduce page-weight friction on key browse and PDP surfaces

| Field | Value |
|---|---|
| Pillar | Performance |
| Surface | Homepage, collections, and PDP media loading |
| URL | https://www.allbirds.com/ |
| Evidence | artifacts/allbirds_20260613_24b222/technical_checks.json |
| Hypothesis | Reducing page-weight friction will improve browse depth because both mobile and desktop timing checks warned on a site that depends on large photography and long visual layouts. |
| Primary change | Compress non-critical media, prioritize above-the-fold assets, and defer lower-priority imagery on home and collection pages. |
| Primary KPI | Homepage bounce rate |
| Decision rule | Ship if mobile load time drops below 3.0s with improved bounce and no conversion regression. |
| Expected lift | +4-8% |
| Confidence | 74% |

### EXP-10: Improve image-alt and interaction-state quality on product cards and PDP media

| Field | Value |
|---|---|
| Pillar | Performance |
| Surface | Product media and purchase-card state changes |
| URL | https://www.allbirds.com/products/womens-runner-nz-slip-on |
| Evidence | artifacts/allbirds_20260613_24b222/technical_checks.json |
| Hypothesis | Improving image-alt coverage and interaction-state quality will improve accessibility confidence and reduce subtle purchase friction because the sampled site still has meaningful alt gaps and an add-to-cart path that was not reliably customer-verified. |
| Primary change | Audit product-card and PDP media alt text, then simplify purchase-card state transitions so size selection and add-to-cart confirmation are more obvious and resilient. |
| Primary KPI | PDP add-to-cart rate |
| Decision rule | Ship if PDP add-to-cart improves by at least 5% relative with reduced interaction-failure events over 3 weeks. |
| Expected lift | +5-9% |
| Confidence | 78% |

## Competitor Analysis

These benchmarks focus on premium footwear and comfort-first apparel brands that make product-choice clarity, category progression, or content commercialization easier than the current Allbirds purchase path does on this run (`artifacts/allbirds_20260613_24b222/evidence_summary.md`).

| Competitor | Domain | Positioning | What they make easier | allbirds edge | Pattern to adapt |
|---|---|---|---|---|---|
| Rothy's | https://rothys.com/ | Sustainable footwear brand with strong material story and polished ecommerce merchandising | Product-choice clarity and cleaner shopper routing from brand promise into purchase | Broader comfort and performance story across men’s and women’s categories | Add more direct product-selection guidance without losing calm brand presentation (EXP-02, EXP-08) |
| Cariuma | https://www.cariuma.com/ | Sustainability-led casual footwear brand with lifestyle positioning and broad sneaker assortment | Story-to-product transition and silhouette comparison | Stronger B Corp credibility and more refined checkout/cart experience | Turn sustainability and comfort story into more explicit product-entry paths (EXP-07, EXP-08) |
| On | https://www.on.com/ | Performance-led footwear brand with sharper use-case and activity framing | Easier activity-based product comparison and stronger first-shoe orientation | Softer brand tone, more approachable aesthetics, and stronger sustainability trust | Bring clearer use-case routing earlier in home and collection flows (EXP-02, EXP-04) |

## Technical Checks

| Check | Status | Detail |
|---|---|---|
| SSL Certificate | Pass | HTTPS storefront loaded successfully. |
| HTTPS Redirect | Pass | HTTP redirected to HTTPS. |
| Sitemap | Pass | sitemap.xml found with ~6 entries. |
| Robots.txt | Pass | robots.txt accessible. |
| Critical Pages Loading | Pass | 11/11 selected pages loaded successfully. |
| Meta Tags & Social Previews | Pass | Title, meta description, and OG tags present on all 11 crawled pages. |
| Structured Data | Pass | JSON-LD found on 4/11 pages: ProductGroup, Blog. Product JSON-LD on 3/3 PDPs. |
| Favicon | Pass | Favicon link tag found. |
| Mobile-Friendly | Pass | Viewport meta present and no horizontal overflow at 375px. |
| Page Speed Mobile | Warn | Navigation timing (single run, not Lighthouse): load 3776ms, DCL 1340ms at 375px viewport. |
| Page Speed Desktop | Warn | Navigation timing (single run, not Lighthouse): load 3748ms, DCL 1529ms. |
| Broken Links | Pass | No broken links in 40 sampled links. |
| Image Optimization | Warn | 74/336 images missing alt text (22%) across 11 crawled pages. Byte-level audit not run. |
| Cookie/Privacy | Pass | Privacy Policy and Terms found. Cookie policy also present. |
| Checkout Reachable | Pass | Cart loaded and checkout entry reached. Journey stopped before payment entry. |
| Payment Methods | Pass | Detected: Visa, Mastercard, Amex, PayPal, Apple Pay, Google Pay, Shop Pay, Stripe, Amazon Pay, Diners Club, JCB. |
| Shopping Journey | Warn | Score 4.0/5 - api add to cart fallback (-1.0). Payment: Visa, Mastercard, Amex, PayPal, Apple Pay, Google Pay, Shop Pay, Stripe, Amazon Pay, Diners Club, JCB. |
