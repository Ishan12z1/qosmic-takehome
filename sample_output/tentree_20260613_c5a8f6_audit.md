# CRO Audit: tentree

Run ID: `tentree_20260613_c5a8f6`  
Date: 2026-06-13

## Executive Summary

Tentree's purchase path is healthy, so the biggest near-term constraint is not checkout friction. The fresh journey completed end to end at 5.0/5 with cart and checkout entry both reachable (`artifacts/tentree_20260613_c5a8f6/pages/shopping_journey.json`, `artifacts/tentree_20260613_c5a8f6/screenshots/shopping_journey_cart.png`). The real gap is that Tentree's strongest decision-support assets live away from the purchase moment: PDPs already show ratings, but the fit guidance is isolated on a separate fit-guide page (`artifacts/tentree_20260613_c5a8f6/screenshots/product_page_2_products_m-atlas-sweatpant.png`, `artifacts/tentree_20260613_c5a8f6/screenshots/blog_or_content_page_10_pages_fit-guide.png`), and the catalog still leans on broad browsing rather than strong shop-by-fit or shop-by-activity guidance (`artifacts/tentree_20260613_c5a8f6/screenshots/collection_page_5_collections_mens.png`, `artifacts/tentree_20260613_c5a8f6/screenshots/homepage_0_home.png`).

This run is also `Degraded`, not because core shopping broke, but because discovery quality is capped by technical and catalog issues that should be treated as real business drag. The crawler found six critical broken product links, all OG tags were missing, no JSON-LD was detected, and 56% of sampled images lacked alt text (`artifacts/tentree_20260613_c5a8f6/summary.md`, `artifacts/tentree_20260613_c5a8f6/technical_checks.json`). Tentree already has strong mission and loyalty assets on-site — Rewards, Tree Planting Auto Pilot, and impact storytelling on the homepage — so the strongest upside is to connect those existing advantages to shopping, basket-building, and repeat behavior instead of adding generic CRO widgets (`artifacts/tentree_20260613_c5a8f6/screenshots/homepage_0_home.png`).

## Proposed Experiments

### EXP-01: Pull fit-guide cues into apparel PDPs

| Field | Value |
|---|---|
| Pillar | Conversion |
| Surface | PDP size and silhouette selection |
| URL | https://tentree.com/products/m-atlas-sweatpant |
| Evidence | artifacts/tentree_20260613_c5a8f6/screenshots/blog_or_content_page_10_pages_fit-guide.png |
| Hypothesis | Bringing fit-guide cues into PDPs will improve add-to-bag rate because the store already has strong fit education, but shoppers currently have to leave the product decision moment to use it. |
| Primary change | Add inline silhouette, stretch, rise, and inseam guidance beside size selection on key apparel PDPs, with a compact fit-guide drawer. |
| Primary KPI | PDP add-to-bag rate |
| Decision rule | Ship if PDP add-to-bag rate improves by at least 5% relative without increasing returns over 4 weeks. |
| Expected lift | +5-10% |
| Confidence | 82% |

### EXP-02: Add shop-by-fit and shop-by-activity collection entry points

| Field | Value |
|---|---|
| Pillar | Conversion |
| Surface | Homepage and men's collection |
| URL | https://www.tentree.com/collections/mens |
| Evidence | artifacts/tentree_20260613_c5a8f6/screenshots/collection_page_5_collections_mens.png |
| Hypothesis | Adding guided collection entry points for fit, activity, and climate will improve collection-to-PDP click-through because shoppers currently enter a broad apparel assortment with limited decision scaffolding beyond filters. |
| Primary change | Add curated entry blocks such as "Travel layers," "Relaxed fit," "Trail-ready," and "Warm-weather essentials" above collection grids and on the homepage. |
| Primary KPI | Collection-to-PDP click-through rate |
| Decision rule | Ship if collection-to-PDP click-through improves by at least 8% relative without increasing exits. |
| Expected lift | +8-14% |
| Confidence | 77% |

### EXP-03: Add outfit-completion recommendations in cart

| Field | Value |
|---|---|
| Pillar | AOV |
| Surface | Cart |
| URL | https://tentree.com/cart |
| Evidence | artifacts/tentree_20260613_c5a8f6/screenshots/shopping_journey_cart.png |
| Hypothesis | Adding outfit-completion recommendations in cart will improve average order value because the current cart is visually sparse and offers no complementary product path before checkout. |
| Primary change | Add a cart recommendation block keyed to category, fit, and gender with one-click add-ons such as socks, tops, or layers. |
| Primary KPI | Average order value |
| Decision rule | Ship if average order value improves by at least 7% relative with checkout-start rate decreasing by less than 2%. |
| Expected lift | +7-13% |
| Confidence | 85% |

### EXP-04: Build mission-led seasonal bundles

| Field | Value |
|---|---|
| Pillar | AOV |
| Surface | Homepage and collection merchandising |
| URL | https://www.tentree.com/ |
| Evidence | artifacts/tentree_20260613_c5a8f6/screenshots/homepage_0_home.png |
| Hypothesis | Packaging seasonal apparel and accessories into mission-led bundles will improve multi-item order rate because Tentree already merchandises categories and impact storytelling strongly, but not as explicit bundled outfits or seasonal packs. |
| Primary change | Launch themed bundles such as "Summer trail set" or "Travel capsule" with a visible impact and savings summary on homepage and collection entry points. |
| Primary KPI | Multi-item order rate |
| Decision rule | Ship if multi-item order rate improves by at least 10% relative while gross margin stays within target. |
| Expected lift | +9-16% |
| Confidence | 73% |

### EXP-05: Surface Rewards Program and Tree Planting Auto Pilot near purchase

| Field | Value |
|---|---|
| Pillar | Retention |
| Surface | PDP and cart |
| URL | https://www.tentree.com/ |
| Evidence | artifacts/tentree_20260613_c5a8f6/screenshots/homepage_0_home.png |
| Hypothesis | Merchandising Rewards and Tree Planting Auto Pilot near purchase moments will improve repeat-purchase intent because those programs are already present on the homepage but are not reinforcing value when shoppers are ready to buy. |
| Primary change | Add a compact rewards/auto-pilot module on PDPs and in cart that explains points, impact accrual, and the monthly tree-planting option. |
| Primary KPI | 90-day repeat purchase rate |
| Decision rule | Ship if 90-day repeat purchase improves by at least 6% relative without hurting first-order conversion. |
| Expected lift | +6-12% |
| Confidence | 69% |

### EXP-06: Connect fit-guide engagement to lifecycle follow-up

| Field | Value |
|---|---|
| Pillar | Retention |
| Surface | Fit guide and email/SMS capture flow |
| URL | https://tentree.com/pages/fit-guide |
| Evidence | artifacts/tentree_20260613_c5a8f6/screenshots/blog_or_content_page_10_pages_fit-guide.png |
| Hypothesis | Turning fit-guide engagement into a personalized lifecycle trigger will improve repeat engagement because Tentree already captures email/SMS on fit and shopping surfaces but does not visibly use fit intent to tailor follow-up. |
| Primary change | Capture fit-guide usage signals and trigger personalized follow-up around silhouettes, inseams, and category recommendations. |
| Primary KPI | Email/SMS-assisted repeat purchase rate |
| Decision rule | Ship if assisted repeat purchase improves by at least 5% relative among fit-guide engagers over 8 weeks. |
| Expected lift | +5-10% |
| Confidence | 62% |

### EXP-07: Repair critical broken product links

| Field | Value |
|---|---|
| Pillar | Acquisition |
| Surface | Product discovery and internal linking |
| URL | https://tentree.com/ |
| Evidence | artifacts/tentree_20260613_c5a8f6/technical_checks.json |
| Hypothesis | Repairing the six critical broken product links will improve organic and internal-navigation efficiency because shoppers and crawlers are currently hitting dead-end PDPs on a degraded run. |
| Primary change | Fix or redirect the broken product URLs and add a broken-link regression check to product publishing workflows. |
| Primary KPI | Broken-link incidence on sampled product URLs |
| Decision rule | Ship when broken-link incidence falls to zero on the sampled product set and PDP exits decline on repaired routes. |
| Expected lift | +4-9% |
| Confidence | 88% |

### EXP-08: Add OG tags and product schema sitewide

| Field | Value |
|---|---|
| Pillar | Acquisition |
| Surface | Theme head and product templates |
| URL | https://www.tentree.com/ |
| Evidence | artifacts/tentree_20260613_c5a8f6/technical_checks.json |
| Hypothesis | Adding OG tags and Product/Organization JSON-LD will improve social-share quality and organic eligibility because OG tags are missing on all crawled pages and no JSON-LD was detected anywhere on the site. |
| Primary change | Add complete OG metadata and inject Product, Organization, and BreadcrumbList JSON-LD across key templates. |
| Primary KPI | Social referral sessions and rich-result coverage |
| Decision rule | Ship when metadata and schema validate sitewide and social referral / rich-result coverage improve over 6 weeks. |
| Expected lift | +6-12% |
| Confidence | 78% |

### EXP-09: Set homepage and collection speed budgets

| Field | Value |
|---|---|
| Pillar | Performance |
| Surface | Homepage and collection templates |
| URL | https://www.tentree.com/ |
| Evidence | artifacts/tentree_20260613_c5a8f6/technical_checks.json |
| Hypothesis | Reducing homepage and collection load times will improve bounce and browsing depth because both mobile and desktop page-speed checks warn on this run and the storefront is image-heavy. |
| Primary change | Set performance budgets for hero, carousel, and collection templates; defer non-critical scripts; and lazy-load below-fold modules. |
| Primary KPI | Homepage bounce rate |
| Decision rule | Ship if mobile load drops below 2.5s and desktop load below 3.0s with improved bounce and no conversion regression. |
| Expected lift | +4-9% |
| Confidence | 70% |

### EXP-10: Improve catalog image hygiene and accessibility coverage

| Field | Value |
|---|---|
| Pillar | Performance |
| Surface | Collection and PDP image system |
| URL | https://www.tentree.com/collections/mens |
| Evidence | artifacts/tentree_20260613_c5a8f6/screenshots/collection_page_5_collections_mens.png |
| Hypothesis | Tightening image handling and alt-text coverage will improve page efficiency and crawl quality because 208 of 368 sampled images are missing alt text and the catalog relies heavily on media. |
| Primary change | Backfill missing alt text, standardize responsive image sizing, and compress large collection/PDP assets. |
| Primary KPI | Mobile LCP and missing-alt rate |
| Decision rule | Ship if missing-alt coverage drops below 5% and mobile LCP improves without reducing collection engagement. |
| Expected lift | +3-7% |
| Confidence | 68% |

## Competitor Analysis

These benchmarks focus on sustainable apparel and eco-fashion patterns relevant to Tentree's discovery, fit-confidence, and mission-led retention opportunities (`artifacts/tentree_20260613_c5a8f6/evidence_summary.md`).

| Competitor | Domain | Positioning | What they make easier | tentree edge | Pattern to adapt |
|---|---|---|---|---|---|
| Pact | https://wearpact.com/ | Sustainable basics and apparel | Simpler essentials-led apparel shopping | Stronger environmental storytelling and impact branding | Sharper guided assortment and bundle entry points (EXP-02, EXP-04) |
| Kotn | https://kotn.com/ | Elevated essentials with social impact | Clean product discovery and fit-confidence basics | More visible on-site impact programs and loyalty hooks | Simpler fit-guided collection journeys (EXP-01, EXP-02) |
| Patagonia | https://www.patagonia.com/ | Outdoor apparel with mission leadership | Activity-led navigation and product-use clarity | Stronger explicit tree-planting program and rewards surfaces | Better mission-to-shopping integration (EXP-05, EXP-09) |
| Allbirds | https://www.allbirds.com/ | Sustainability-led lifestyle apparel and footwear | Lightweight browse flows and product discovery | Deeper impact ecosystem and broader loyalty story | Cleaner social/share metadata and category discovery (EXP-07, EXP-08) |

## Technical Checks

| Check | Status | Detail |
|---|---|---|
| SSL Certificate | Pass | HTTPS storefront loaded successfully. |
| HTTPS Redirect | Pass | HTTP redirected to HTTPS. |
| Sitemap | Pass | sitemap.xml found with ~7 entries. |
| Robots.txt | Pass | robots.txt accessible. |
| Critical Pages Loading | Pass | 11/11 selected pages loaded successfully. |
| Meta Tags & Social Previews | Warn | Title+meta description present on 8/11 pages. OG tags missing on 11/11 pages. |
| Structured Data | Warn | No JSON-LD detected across 11 crawled pages. |
| Favicon | Pass | Favicon link tag found. |
| Mobile-Friendly | Pass | Viewport meta present and no horizontal overflow at 375px. |
| Page Speed Mobile | Warn | Navigation timing (single run, not Lighthouse): load 3205ms, DCL 1307ms at 375px viewport. |
| Page Speed Desktop | Warn | Navigation timing (single run, not Lighthouse): load 4013ms, DCL 1477ms. |
| Broken Links | Fail | 6 broken links found. Critical: https://tentree.com/products/grove-romper-meteorite-black, https://www.tentree.com/products/denim-cascades-short-light-wash, https://www.tentree.com/products/westin-hybrid-short-lakeside-blue |
| Image Optimization | Warn | 208/368 images missing alt text (56%) across 11 crawled pages. Byte-level audit not run. |
| Cookie/Privacy | Pass | Privacy Policy and Terms found. Cookie policy also present. |
| Checkout Reachable | Pass | Cart loaded and checkout entry reached. Journey stopped before payment entry. |
| Payment Methods | Pass | Detected: Visa, Mastercard, Amex, PayPal, Apple Pay, Google Pay, Shop Pay, Klarna, Diners Club, JCB. |
| Shopping Journey | Pass | Score 5.0/5 - no blockers detected. Payment: Visa, Mastercard, Amex, PayPal, Apple Pay, Google Pay, Shop Pay, Klarna, Diners Club, JCB. |
