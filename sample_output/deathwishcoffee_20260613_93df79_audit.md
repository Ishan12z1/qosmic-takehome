# CRO Audit: deathwishcoffee

Run ID: `deathwishcoffee_20260613_93df79`  
Date: 2026-06-13

## Executive Summary

Death Wish Coffee does not have a broken buy path. The fresh journey completed cleanly through cart and checkout entry with a 5.0/5 friction score (`artifacts/deathwishcoffee_20260613_93df79/pages/shopping_journey.json`, `artifacts/deathwishcoffee_20260613_93df79/screenshots/shopping_journey_cart.png`, `artifacts/deathwishcoffee_20260613_93df79/screenshots/shopping_journey_checkout.png`). The bigger issue is interruption: the same birthday/email modal visibly covers the homepage, sale collection, FAQ page, blog page, and an apparel PDP with size selection (`artifacts/deathwishcoffee_20260613_93df79/screenshots/homepage_0_home.png`, `artifacts/deathwishcoffee_20260613_93df79/screenshots/collection_page_5_collections_sale.png`, `artifacts/deathwishcoffee_20260613_93df79/screenshots/faq_shipping_returns_8_pages_help.png`, `artifacts/deathwishcoffee_20260613_93df79/screenshots/blog_or_content_page_10_pages_blog.png`, `artifacts/deathwishcoffee_20260613_93df79/screenshots/product_page_3_products_father-time-tee-1.png`). That matters more than generic "add trust" fixes because observed shopping surfaces already show strong proof, including visible review counts on merch PDPs and rated products across the mugs collection (`artifacts/deathwishcoffee_20260613_93df79/screenshots/product_page_1_products_baba-yaga-mug.png`, `artifacts/deathwishcoffee_20260613_93df79/screenshots/collection_page_6_collections_mugs.png`).

The second issue is that the brand's repeat-purchase and basket-building ecosystem is stronger in architecture than in the sampled page state. Navigation and support surfaces clearly expose subscription and Ritual Rewards (`artifacts/deathwishcoffee_20260613_93df79/pages/homepage_0_home.md`, `artifacts/deathwishcoffee_20260613_93df79/pages/faq_shipping_returns_8_pages_help.md`), but the captured cart page for a `$38` mug order is visually sparse and does not visibly push coffee add-ons, bundles, or program value (`artifacts/deathwishcoffee_20260613_93df79/screenshots/shopping_journey_cart.png`). Technical health is mostly good - structured data, favicon, and broken-link hygiene all pass (`artifacts/deathwishcoffee_20260613_93df79/technical_checks.json`) - but mobile and desktop speed both warn, and the captured page source shows a heavy third-party script stack (`artifacts/deathwishcoffee_20260613_93df79/technical_checks.json`, `artifacts/deathwishcoffee_20260613_93df79/pages/product_page_1_products_baba-yaga-mug.md`).

## Proposed Experiments

### EXP-01: Delay the birthday modal until real buying intent is clearer

| Field | Value |
|---|---|
| Pillar | Conversion |
| Surface | Homepage, collection, FAQ, blog, and PDP modal trigger |
| URL | https://deathwishcoffee.com/collections/sale |
| Evidence | artifacts/deathwishcoffee_20260613_93df79/screenshots/collection_page_5_collections_sale.png |
| Hypothesis | Delaying the birthday/email modal until a second pageview or exit intent will improve product engagement and add-to-cart rate because the current modal blocks primary shopping and support content across multiple surface types. |
| Primary change | Show the modal only after deeper engagement signals such as second pageview, 30 seconds on site, or exit intent, and suppress it entirely on product pages with size/variant selection. |
| Primary KPI | Add-to-cart rate |
| Decision rule | Ship if add-to-cart rate improves by at least 6% relative without lowering email capture efficiency over 3 weeks. |
| Expected lift | +6-11% |
| Confidence | 87% |

### EXP-02: Rebalance the homepage toward coffee discovery and subscription entry

| Field | Value |
|---|---|
| Pillar | Conversion |
| Surface | Homepage hero and first-scroll merchandising |
| URL | https://deathwishcoffee.com/ |
| Evidence | artifacts/deathwishcoffee_20260613_93df79/screenshots/homepage_0_home.png |
| Hypothesis | Giving core coffee choice and subscription entry equal or greater prominence than limited merch hero content will improve homepage-to-PDP click-through because the current first impression is dominated by a mug campaign even though the brand's repeat value comes from coffee and recurring purchase. |
| Primary change | Test a hero variant with coffee-first entry points such as "Shop Coffee," "Start a Subscription," and "Find Your Roast," while moving merch campaigns below the fold. |
| Primary KPI | Homepage-to-PDP click-through rate |
| Decision rule | Ship if homepage-to-PDP click-through improves by at least 8% relative without reducing merch revenue contribution. |
| Expected lift | +8-14% |
| Confidence | 79% |

### EXP-03: Add visible coffee and gift add-ons to the cart page

| Field | Value |
|---|---|
| Pillar | AOV |
| Surface | `/cart` page |
| URL | https://deathwishcoffee.com/cart |
| Evidence | artifacts/deathwishcoffee_20260613_93df79/screenshots/shopping_journey_cart.png |
| Hypothesis | Adding visible coffee and gift add-ons to the actual cart page will improve average order value because the captured `$38` mug cart is clean but under-merchandised, with no visible path to coffee, bundles, or free-shipping progress. |
| Primary change | Add a cart-page module for one-click coffee, pods, and gift add-ons plus a visible free-shipping / free-gift progress bar that mirrors the brand's broader cart incentives. |
| Primary KPI | Average order value |
| Decision rule | Ship if average order value improves by at least 10% relative while checkout-start rate stays flat or better. |
| Expected lift | +10-18% |
| Confidence | 84% |

### EXP-04: Bundle merch with coffee and subscription starters

| Field | Value |
|---|---|
| Pillar | AOV |
| Surface | Merch PDPs and sale/mugs collections |
| URL | https://deathwishcoffee.com/products/baba-yaga-mug |
| Evidence | artifacts/deathwishcoffee_20260613_93df79/screenshots/product_page_1_products_baba-yaga-mug.png |
| Hypothesis | Packaging merch with coffee or subscription starters will improve multi-item order rate because sampled merch PDPs attract shoppers with strong design and reviews, but they do not visibly convert that interest into a larger coffee basket. |
| Primary change | Launch bundles such as "Mug + Dark Roast Starter," "Giftable Mug + Pods," and "Society Starter Kit" with one-click add on merch PDPs and merch collections. |
| Primary KPI | Multi-item order rate |
| Decision rule | Ship if multi-item order rate improves by at least 9% relative without reducing merch PDP conversion. |
| Expected lift | +9-15% |
| Confidence | 76% |

### EXP-05: Bring subscription and Ritual Rewards into the purchase module

| Field | Value |
|---|---|
| Pillar | Retention |
| Surface | Product-page purchase module and cart reassurance |
| URL | https://deathwishcoffee.com/pages/help |
| Evidence | artifacts/deathwishcoffee_20260613_93df79/pages/faq_shipping_returns_8_pages_help.md |
| Hypothesis | Surfacing subscription and Ritual Rewards next to purchase actions will improve repeat-purchase participation because those programs clearly exist in the site's architecture but are not doing enough visible work during the sampled shopping flow. |
| Primary change | Add a compact module near add-to-cart and in cart that explains subscription perks, rewards accrual, and member-only benefits in plain language. |
| Primary KPI | Subscription or rewards-program opt-in rate |
| Decision rule | Ship if program opt-in rate improves by at least 12% relative without hurting first-order conversion. |
| Expected lift | +12-20% |
| Confidence | 81% |

### EXP-06: Convert merch buyers into recurring coffee customers

| Field | Value |
|---|---|
| Pillar | Retention |
| Surface | Post-purchase lifecycle for merch-led orders |
| URL | https://deathwishcoffee.com/products/father-time-tee-1 |
| Evidence | inferred - journey stops at checkout entry |
| Hypothesis | Following merch-first orders with coffee and subscription education will improve repeat purchase rate because this run skewed toward mugs and apparel, which are high-brand-affinity but often lower-repeat entry points than coffee. |
| Primary change | Send a post-purchase sequence for merch orders that introduces core roasts, subscription value, and a first-coffee offer tied to the purchased item theme. |
| Primary KPI | 60-day repeat purchase rate |
| Decision rule | Ship if 60-day repeat purchase improves by at least 7% relative among merch-first buyers over 8 weeks. |
| Expected lift | +7-13% |
| Confidence | 68% |

### EXP-07: Turn help content into a stronger trust-to-purchase bridge

| Field | Value |
|---|---|
| Pillar | Acquisition |
| Surface | Help and FAQ pages |
| URL | https://deathwishcoffee.com/pages/help |
| Evidence | artifacts/deathwishcoffee_20260613_93df79/screenshots/faq_shipping_returns_8_pages_help.png |
| Hypothesis | Adding stronger product and program handoffs to help content will improve assisted conversion because the page contains valuable shipping and discount reassurance but currently behaves more like a support dead end than a purchase bridge. |
| Primary change | Add contextual CTAs on key FAQ sections for "Shop Coffee," "Start a Subscription," "Apply Military Discount," and "Best Sellers" based on the topic being read. |
| Primary KPI | Help-page assisted product click-through rate |
| Decision rule | Ship if help-page assisted product clicks improve by at least 15% relative without reducing FAQ satisfaction metrics. |
| Expected lift | +8-15% |
| Confidence | 73% |

### EXP-08: Commercialize the blog hub with product and category pathways

| Field | Value |
|---|---|
| Pillar | Acquisition |
| Surface | Blog hub and article templates |
| URL | https://deathwishcoffee.com/pages/blog |
| Evidence | artifacts/deathwishcoffee_20260613_93df79/screenshots/blog_or_content_page_10_pages_blog.png |
| Hypothesis | Adding clearer product and category pathways to content surfaces will improve content-assisted conversion because the captured blog experience is heavy on social and editorial browsing but light on shopping entry points. |
| Primary change | Add "shop the post," "start with these roasts," and category rails to blog hub and article templates. |
| Primary KPI | Content-assisted product click-through rate |
| Decision rule | Ship if content-assisted product clicks improve by at least 12% relative without reducing blog engagement depth. |
| Expected lift | +7-13% |
| Confidence | 70% |

### EXP-09: Defer non-critical modal, chat, and marketing scripts

| Field | Value |
|---|---|
| Pillar | Performance |
| Surface | Homepage and PDP script loading |
| URL | https://deathwishcoffee.com/products/baba-yaga-mug |
| Evidence | artifacts/deathwishcoffee_20260613_93df79/pages/product_page_1_products_baba-yaga-mug.md |
| Hypothesis | Deferring modal, chat, and marketing scripts until interaction or idle time will improve page responsiveness because the captured page source shows a large third-party script stack layered onto already media-heavy templates. |
| Primary change | Defer Klaviyo modal, chat, and selected marketing pixels behind interaction or idle-load gates while keeping checkout-critical code immediate. |
| Primary KPI | PDP bounce rate |
| Decision rule | Ship if PDP bounce rate improves and add-to-cart rate stays flat or better after the script deferral test. |
| Expected lift | +4-8% |
| Confidence | 74% |

### EXP-10: Reduce template weight on homepage and long merch pages

| Field | Value |
|---|---|
| Pillar | Performance |
| Surface | Homepage and merch templates |
| URL | https://deathwishcoffee.com/ |
| Evidence | artifacts/deathwishcoffee_20260613_93df79/technical_checks.json |
| Hypothesis | Reducing template weight on homepage and long merch pages will improve browsing depth because both mobile and desktop navigation timing warn on this run despite otherwise strong technical hygiene. |
| Primary change | Optimize hero/carousel assets, trim below-fold embeds, and lazy-load non-essential review or content modules on long merch templates. |
| Primary KPI | Homepage bounce rate |
| Decision rule | Ship if mobile load falls below 3.0s and desktop load below 3.5s with improved bounce and no conversion regression. |
| Expected lift | +4-9% |
| Confidence | 71% |

## Competitor Analysis

These benchmarks focus on coffee brands that balance repeat coffee purchase, discovery, merch, or loyalty better than the current Death Wish flow does on this run (`artifacts/deathwishcoffee_20260613_93df79/evidence_summary.md`).

| Competitor | Domain | Positioning | What they make easier | deathwishcoffee edge | Pattern to adapt |
|---|---|---|---|---|---|
| Black Rifle Coffee Company | https://www.blackriflecoffee.com/ | Veteran-led coffee and merch brand with a strong club/rewards layer | Coffee-club discovery, merch integration, and loyalty visibility | Darker, more distinctive gothic brand identity and stronger observed merch reviews | Make subscription and loyalty more visible during the purchase flow (EXP-02, EXP-05) |
| Bones Coffee Company | https://www.bonescoffee.com/ | Flavor-forward coffee brand with bundles, subscriptions, and merch | Sample packs, bundles, flavor finding, and merch-to-coffee crossover | Stronger hardcore brand voice and bolder community feel | Use curated bundles and clearer coffee discovery to grow AOV and first-order confidence (EXP-03, EXP-04) |
| Stumptown Coffee | https://www.stumptowncoffee.com/ | Coffee-first specialty DTC with quiz and subscription clarity | Coffee quiz, bundle framing, and transparent subscribe-vs-one-time choices | Stronger lifestyle/merch identity and broader community-program potential | Route more shoppers into coffee choice and recurring purchase paths earlier (EXP-02, EXP-10) |

## Technical Checks

| Check | Status | Detail |
|---|---|---|
| SSL Certificate | Pass | HTTPS storefront loaded successfully. |
| HTTPS Redirect | Pass | HTTP redirected to HTTPS. |
| Sitemap | Pass | sitemap.xml found with ~5 entries. |
| Robots.txt | Pass | robots.txt accessible. |
| Critical Pages Loading | Pass | 10/10 selected pages loaded successfully. |
| Meta Tags & Social Previews | Warn | Title+meta description present on 7/10 pages. OG tags present on all pages. |
| Structured Data | Pass | JSON-LD found on 10/10 pages: Organization, WebSite, Product, FAQPage, Article. Product JSON-LD on 3/3 PDPs. |
| Favicon | Pass | Favicon link tag found. |
| Mobile-Friendly | Pass | Viewport meta present and no horizontal overflow at 375px. |
| Page Speed Mobile | Warn | Navigation timing (single run, not Lighthouse): load 4048ms, DCL 1451ms at 375px viewport. |
| Page Speed Desktop | Warn | Navigation timing (single run, not Lighthouse): load 4373ms, DCL 2100ms. |
| Broken Links | Pass | No broken links in 40 sampled links. |
| Image Optimization | Warn | 62/493 images missing alt text (12%) across 10 crawled pages. Byte-level audit not run. |
| Cookie/Privacy | Pass | Privacy Policy and Terms found. Cookie policy also present. |
| Checkout Reachable | Pass | Cart loaded and checkout entry reached. Journey stopped before payment entry. |
| Payment Methods | Pass | Detected: Visa, Mastercard, Amex, PayPal, Apple Pay, Shop Pay, Afterpay, JCB. |
| Shopping Journey | Pass | Score 5.0/5 - no blockers detected. Payment: Visa, Mastercard, Amex, PayPal, Apple Pay, Shop Pay, Afterpay, JCB. |
