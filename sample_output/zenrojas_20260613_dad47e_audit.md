# CRO Audit: zenrojas

Run ID: `zenrojas_20260613_dad47e`  
Date: 2026-06-13

## Executive Summary

Zen Rojas can sell cleanly once a shopper decides to buy, so the main near-term constraint is not checkout friction. The fresh shopping journey reached cart and checkout entry without blockers (`artifacts/zenrojas_20260613_dad47e/pages/shopping_journey.json`, `artifacts/zenrojas_20260613_dad47e/screenshots/shopping_journey_cart.png`, `artifacts/zenrojas_20260613_dad47e/screenshots/shopping_journey_checkout.png`). The bigger issue is that the store's strongest positioning lives in the brand story and wellness framing, while the shopping surfaces are thinner and less decisive: the homepage sells sleep, immunity, energy, and digestion use cases (`artifacts/zenrojas_20260613_dad47e/screenshots/homepage_0_home.png`), but the first captured tea collection view is led by sold-out products (`artifacts/zenrojas_20260613_dad47e/screenshots/collection_page_5_collections_teas.png`), and PDPs lean on long copy more than crisp buying guidance (`artifacts/zenrojas_20260613_dad47e/screenshots/product_page_1_products_blacktea.png`).

Trust and AOV friction also show up in concrete customer-facing details. The sitewide announcement promises free shipping at `$50+`, while the FAQ says orders over `$30` ship free (`artifacts/zenrojas_20260613_dad47e/screenshots/homepage_0_home.png`, `artifacts/zenrojas_20260613_dad47e/screenshots/faq_shipping_returns_8_pages_faqs.png`), which is the kind of mismatch that can quietly reduce checkout confidence. Zen Rojas already has the ingredients for stronger basket building - teaware, samplers, "Frequently bought together" modules, and a strong ritual-based brand story (`artifacts/zenrojas_20260613_dad47e/screenshots/product_page_1_products_blacktea.png`, `artifacts/zenrojas_20260613_dad47e/screenshots/collection_page_6_collections_teaware.png`, `artifacts/zenrojas_20260613_dad47e/screenshots/about_page_9_pages_aboutus.png`) - but the cart still leaves a shopper with an `$8` basket mostly on their own (`artifacts/zenrojas_20260613_dad47e/screenshots/shopping_journey_cart.png`). Technical health is broadly good, but JSON-LD is missing, favicon detection failed, 4 sampled links were broken, and 33% of images were missing alt text (`artifacts/zenrojas_20260613_dad47e/technical_checks.json`).

## Proposed Experiments

### EXP-01: Rebuild the tea collection around available wellness needs

| Field | Value |
|---|---|
| Pillar | Conversion |
| Surface | Tea collection above the fold |
| URL | https://zenrojas.com/collections/teas |
| Evidence | artifacts/zenrojas_20260613_dad47e/screenshots/collection_page_5_collections_teas.png |
| Hypothesis | Replacing a sold-out-dominated first collection view with available need-led entries will improve collection-to-PDP click-through because the current above-fold catalog opens with multiple sold-out teas, which weakens shopping momentum immediately. |
| Primary change | Reorder the teas collection so in-stock products lead, add "Shop Sleep," "Shop Immunity," "Shop Energy," and "Shop Digestion" entry cards above the grid, and demote sold-out products behind an "Email me when available" state. |
| Primary KPI | Collection-to-PDP click-through rate |
| Decision rule | Ship if collection-to-PDP click-through improves by at least 10% relative without increasing exits over 3 weeks. |
| Expected lift | +10-18% |
| Confidence | 84% |

### EXP-02: Fix shipping-threshold messaging everywhere shoppers see it

| Field | Value |
|---|---|
| Pillar | Conversion |
| Surface | Announcement bar, FAQ, PDP, and cart |
| URL | https://zenrojas.com/pages/faqs |
| Evidence | artifacts/zenrojas_20260613_dad47e/screenshots/faq_shipping_returns_8_pages_faqs.png |
| Hypothesis | Aligning the free-shipping threshold across trust surfaces will improve checkout-start rate because the store currently tells shoppers two different thresholds: `$50+` in the announcement bar and `$30+` in the FAQ. |
| Primary change | Standardize the free-shipping threshold across theme copy, FAQ, cart, and PDP messaging, then repeat the same threshold in cart progress and PDP reassurance text. |
| Primary KPI | Checkout-start rate |
| Decision rule | Ship if checkout-start rate improves by at least 5% relative and support contacts about shipping policy decline over 4 weeks. |
| Expected lift | +5-9% |
| Confidence | 88% |

### EXP-03: Add threshold-closing recommendations in cart

| Field | Value |
|---|---|
| Pillar | AOV |
| Surface | Cart |
| URL | https://zenrojas.com/cart |
| Evidence | artifacts/zenrojas_20260613_dad47e/screenshots/shopping_journey_cart.png |
| Hypothesis | Adding threshold-closing recommendations in cart will improve average order value because the captured cart shows a low-value `$8` basket with no visible help toward a larger ritual purchase or free-shipping goal. |
| Primary change | Add a cart module that recommends samplers, teaware, or complementary teas with one-click add buttons and a live "You're $X away from free shipping" bar once the policy is standardized. |
| Primary KPI | Average order value |
| Decision rule | Ship if average order value improves by at least 12% relative while checkout-start rate stays flat or better. |
| Expected lift | +12-20% |
| Confidence | 86% |

### EXP-04: Package tea-plus-teaware starter kits

| Field | Value |
|---|---|
| Pillar | AOV |
| Surface | PDPs and teaware collection |
| URL | https://zenrojas.com/collections/teaware |
| Evidence | artifacts/zenrojas_20260613_dad47e/screenshots/collection_page_6_collections_teaware.png |
| Hypothesis | Packaging clear starter kits will improve multi-item order rate because the store already sells tea bags, loose tea, samplers, mugs, and infusers, but shoppers have to assemble the ritual themselves. |
| Primary change | Launch named bundles such as "Sleep Ritual Starter Set," "Morning Energy Set," and "Tea Basics Kit" that combine tea, infuser, and mug with a visible savings summary. |
| Primary KPI | Multi-item order rate |
| Decision rule | Ship if multi-item order rate improves by at least 10% relative without lowering product-page conversion. |
| Expected lift | +9-16% |
| Confidence | 78% |

### EXP-05: Launch replenishment around daily ritual teas

| Field | Value |
|---|---|
| Pillar | Retention |
| Surface | Core tea PDPs |
| URL | https://zenrojas.com/products/blacktea |
| Evidence | artifacts/zenrojas_20260613_dad47e/screenshots/product_page_1_products_blacktea.png |
| Hypothesis | Introducing replenishment for core tea SKUs will improve repeat purchase rate because the brand repeatedly frames tea as a daily ritual, but the captured buying surfaces do not visibly convert that routine language into a repeat-purchase offer. |
| Primary change | Add a simple recurring-delivery option for core teas with cadence choices such as every 2, 4, or 6 weeks and a small subscriber benefit. |
| Primary KPI | 60-day repeat purchase rate |
| Decision rule | Ship if 60-day repeat purchase improves by at least 8% relative among exposed shoppers without hurting first-order conversion. |
| Expected lift | +8-14% |
| Confidence | 67% |

### EXP-06: Build a stronger review and routine follow-up loop

| Field | Value |
|---|---|
| Pillar | Retention |
| Surface | PDP review coverage and post-purchase follow-up |
| URL | https://zenrojas.com/products/tea-bags |
| Evidence | inferred - journey stops at checkout entry |
| Hypothesis | Prompting routine-based review requests and usage follow-up will improve both review coverage and repeat engagement because sampled PDP proof is uneven, with Black Tea showing one review while Tea Bags shows none. |
| Primary change | Trigger post-purchase emails and SMS that ask for a review after the first brewing window, include brewing tips, and suggest the next tea or teaware add-on based on what was purchased. |
| Primary KPI | Review submission rate |
| Decision rule | Ship if review submission rate improves by at least 20% relative and repeat purchase rate among recipients also trends upward over 8 weeks. |
| Expected lift | +15-25% |
| Confidence | 72% |

### EXP-07: Create real shop-by-benefit landing pages

| Field | Value |
|---|---|
| Pillar | Acquisition |
| Surface | Homepage use-case modules and new benefit landing pages |
| URL | https://zenrojas.com/ |
| Evidence | artifacts/zenrojas_20260613_dad47e/screenshots/homepage_0_home.png |
| Hypothesis | Turning the homepage's sleep, immunity, energy, and digestion stories into dedicated shop-by-benefit landing pages will improve landing-page conversion because the current modules mostly route to single products instead of helping shoppers compare options by need. |
| Primary change | Build dedicated benefit pages with 2-4 matching products, brewing guidance, ingredient explanation, and a "start your ritual" CTA for each wellness goal. |
| Primary KPI | Landing-page conversion rate |
| Decision rule | Ship if benefit-page conversion beats the current homepage-to-PDP path by at least 10% relative over 4 weeks. |
| Expected lift | +10-17% |
| Confidence | 81% |

### EXP-08: Commercialize story pages with linked products and routines

| Field | Value |
|---|---|
| Pillar | Acquisition |
| Surface | About page and editorial content |
| URL | https://zenrojas.com/blogs/weekly-blog/building-a-family-legacy-through-wellness-community-and-purpose-driven-growth |
| Evidence | artifacts/zenrojas_20260613_dad47e/screenshots/blog_or_content_page_10_blogs_weekly-blog_building-a-family-lega.png |
| Hypothesis | Adding contextual product and routine modules to story pages will improve assisted conversion because the current trust-building content is credible but weakly connected to shopping actions. |
| Primary change | Add in-article product cards, "shop the ritual" blocks, and related wellness pathways on the blog and About page. |
| Primary KPI | Content-assisted product click-through rate |
| Decision rule | Ship if content-assisted product clicks improve by at least 15% relative without reducing time on page. |
| Expected lift | +8-15% |
| Confidence | 74% |

### EXP-09: Improve image hygiene and accessibility coverage

| Field | Value |
|---|---|
| Pillar | Performance |
| Surface | Homepage, collection, and PDP image system |
| URL | https://zenrojas.com/ |
| Evidence | artifacts/zenrojas_20260613_dad47e/technical_checks.json |
| Hypothesis | Cleaning up image alt coverage and media handling will improve crawl quality and template efficiency because 31 of 92 sampled images are missing alt text and the storefront relies heavily on product and lifestyle imagery. |
| Primary change | Backfill alt text, standardize responsive image sizes, and audit large lifestyle/product assets on homepage and collection templates. |
| Primary KPI | Missing-alt rate |
| Decision rule | Ship if missing-alt coverage drops below 5% and template engagement stays flat or better after the media cleanup. |
| Expected lift | +3-7% |
| Confidence | 69% |

### EXP-10: Defer non-critical third-party widgets on long pages

| Field | Value |
|---|---|
| Pillar | Performance |
| Surface | Homepage and PDP third-party script loading |
| URL | https://zenrojas.com/products/blacktea |
| Evidence | artifacts/zenrojas_20260613_dad47e/pages/product_page_1_products_blacktea.md |
| Hypothesis | Deferring non-critical chat, review, and upsell widgets until interaction will improve engagement on long pages because the captured page source shows multiple third-party widgets loading together on a relatively lightweight storefront. |
| Primary change | Move chat, review, and upsell widgets behind interaction or idle-load gates on homepage and PDP templates while keeping core cart and checkout functionality immediate. |
| Primary KPI | PDP bounce rate |
| Decision rule | Ship if PDP bounce rate improves and add-to-cart rate stays flat or better after the deferred-loading change. |
| Expected lift | +4-8% |
| Confidence | 64% |

## Competitor Analysis

These benchmarks focus on premium tea brands that make discovery, benefits-based shopping, gifting, loyalty, or ritual building easier for tea shoppers than the current Zen Rojas flow does (`artifacts/zenrojas_20260613_dad47e/evidence_summary.md`).

| Competitor | Domain | Positioning | What they make easier | zenrojas edge | Pattern to adapt |
|---|---|---|---|---|---|
| Harney & Sons | https://www.harney.com/ | Broad premium tea catalog with discovery tools | Tea-type discovery, bundles, and a "Your Perfect Tea Quiz" for guided shopping | More intimate veteran-owned family story and calmer wellness positioning | Add guided tea discovery and clearer bundle entry points (EXP-01, EXP-04) |
| Tea Forté | https://teaforte.com/ | Elevated tea gifting and wellness tea | Gift sets, wellness tea navigation, and subscription-oriented merchandising | Stronger small-brand authenticity and simpler ritual story | Package tea-plus-teaware starter sets and more premium giftable rituals (EXP-04, EXP-05) |
| DAVIDsTEA | https://davidstea.com/ | Flavor-forward tea retailer with loyalty and review scale | Bundles, ingredient education, loyalty, and visible review depth | More focused calm/wellness voice and local founder story | Scale review coverage and lifecycle programs around routines (EXP-06, EXP-07) |
| The Republic of Tea | https://www.republicoftea.com/ | Benefit-led premium tea merchandising | Shop-by-benefit navigation, samplers, rewards, and auto-ship | Cleaner emotional brand story and more personal founder narrative | Build dedicated benefit landing pages and stronger repeat-purchase paths (EXP-07, EXP-05) |

## Technical Checks

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
| Page Speed Mobile | Pass | Navigation timing (single run, not Lighthouse): load 1723ms, DCL 913ms at 375px viewport. |
| Page Speed Desktop | Pass | Navigation timing (single run, not Lighthouse): load 1809ms, DCL 995ms. |
| Broken Links | Warn | 4 non-critical broken links in 40 sampled. |
| Image Optimization | Warn | 31/92 images missing alt text (33%) across 10 crawled pages. Byte-level audit not run. |
| Cookie/Privacy | Pass | Privacy Policy and Terms found. Cookie policy also present. |
| Checkout Reachable | Pass | Cart loaded and checkout entry reached. Journey stopped before payment entry. |
| Payment Methods | Pass | Detected: Visa, Mastercard, Amex, PayPal, Apple Pay, Google Pay, Shop Pay, Diners Club, JCB. |
| Shopping Journey | Pass | Score 5.0/5 - no blockers detected. Payment: Visa, Mastercard, Amex, PayPal, Apple Pay, Google Pay, Shop Pay, Diners Club, JCB. |
