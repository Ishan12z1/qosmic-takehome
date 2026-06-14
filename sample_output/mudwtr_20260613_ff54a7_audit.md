# CRO Audit: mudwtr

Run ID: `mudwtr_20260613_ff54a7`  
Date: 2026-06-13

## Executive Summary

MUD/WTR is not missing trust. The sampled PDPs already show strong proof, including visible review summaries, subscribe-vs-one-time purchase options, and a 30-day guarantee, while the FAQ clearly explains subscription management and refund terms (`artifacts/mudwtr_20260613_ff54a7/screenshots/product_page_1_products_hot-cacao-bag.png`, `artifacts/mudwtr_20260613_ff54a7/screenshots/product_page_2_products_30-servings-tin.png`, `artifacts/mudwtr_20260613_ff54a7/screenshots/faq_shipping_returns_8_pages_faqs.png`). The bigger conversion issue is that the store feels overbuilt for a first purchase: the homepage is extremely long, the main shop taxonomy is broad, and the starter-kit PDP stacks many modules onto an already complex choice set (`artifacts/mudwtr_20260613_ff54a7/screenshots/homepage_0_home.png`, `artifacts/mudwtr_20260613_ff54a7/screenshots/collection_page_5_collections_shop.png`, `artifacts/mudwtr_20260613_ff54a7/screenshots/product_page_2_products_30-servings-tin.png`).

The run also confirms that technical and interaction drag are part of the story. Checkout entry was reachable, but the journey degraded because customer-facing add-to-cart could not be verified and the crawler had to fall back to the cart API (`artifacts/mudwtr_20260613_ff54a7/summary.md`, `artifacts/mudwtr_20260613_ff54a7/pages/shopping_journey.json`). At the same time, mobile and desktop page speed both failed, mobile overflow warned, and the sampled page source shows a very heavy third-party script stack (`artifacts/mudwtr_20260613_ff54a7/technical_checks.json`, `artifacts/mudwtr_20260613_ff54a7/pages/product_page_1_products_hot-cacao-bag.md`). That combination points to the main diagnosis: MUD/WTR has enough proof and merchandising power already, but it needs a simpler first-purchase path and a lighter template footprint.

## Proposed Experiments

### EXP-01: Give first-time shoppers a clearer “start here” path on the homepage

| Field | Value |
|---|---|
| Pillar | Conversion |
| Surface | Homepage hero and first-scroll routing |
| URL | https://mudwtr.com/ |
| Evidence | artifacts/mudwtr_20260613_ff54a7/screenshots/homepage_0_home.png |
| Hypothesis | Replacing the homepage’s long exploratory first journey with a clearer “find your blend” and starter-kit entry path will improve homepage-to-PDP click-through because the current page asks shoppers to process many sections and product families before they know what to buy. |
| Primary change | Test a homepage variant that prioritizes one guided decision block with options like “Want focus,” “Need calm,” “Want protein,” or “Start with the Original Kit,” and move some education blocks below that decision layer. |
| Primary KPI | Homepage-to-PDP click-through rate |
| Decision rule | Ship if homepage-to-PDP click-through improves by at least 8% relative without reducing average session depth over 3 weeks. |
| Expected lift | +8-14% |
| Confidence | 82% |

### EXP-02: Simplify the PDP purchase module and verify add-to-cart more clearly

| Field | Value |
|---|---|
| Pillar | Conversion |
| Surface | Starter-kit and flagship PDP purchase module |
| URL | https://mudwtr.com/products/30-servings-tin |
| Evidence | artifacts/mudwtr_20260613_ff54a7/pages/shopping_journey.json |
| Hypothesis | Simplifying the purchase module and making add-to-cart confirmation more explicit will improve add-to-cart rate because the current journey required an API fallback and the PDP presents a dense set of options, discounts, and adjacent content. |
| Primary change | Reduce competing elements near the purchase box, default to the recommended starter option, and add a clearer post-click confirmation state before opening the cart drawer. |
| Primary KPI | Add-to-cart rate |
| Decision rule | Ship if add-to-cart rate improves by at least 6% relative and the customer-facing add-to-cart success rate reaches parity with API-cart verification. |
| Expected lift | +6-11% |
| Confidence | 84% |

### EXP-03: Turn accessories into named ritual-completion bundles

| Field | Value |
|---|---|
| Pillar | AOV |
| Surface | Shop collection and starter-kit PDPs |
| URL | https://mudwtr.com/collections/shop |
| Evidence | artifacts/mudwtr_20260613_ff54a7/screenshots/collection_page_5_collections_shop.png |
| Hypothesis | Grouping accessories into named ritual-completion bundles will improve average order value because the store sells many complements like whip, shaker, creamer, and sweetener, but shoppers must currently assemble those combinations themselves. |
| Primary change | Create one-click bundles such as “Morning Ritual Set,” “Starter Kit + Creamer,” and “Desk Setup Bundle,” surfaced on shop and PDP templates. |
| Primary KPI | Average order value |
| Decision rule | Ship if average order value improves by at least 9% relative without lowering PDP conversion over 4 weeks. |
| Expected lift | +9-16% |
| Confidence | 78% |

### EXP-04: Use the cart drawer to drive high-LTV upgrades instead of broad browsing

| Field | Value |
|---|---|
| Pillar | AOV |
| Surface | Cart drawer and cart entry flow |
| URL | https://mudwtr.com/cart |
| Evidence | artifacts/mudwtr_20260613_ff54a7/screenshots/shopping_journey_cart.png |
| Hypothesis | Focusing cart upsells on a small set of high-LTV upgrades will improve multi-item order rate because the current flow already has upsell capacity, but the best next step for a starter buyer is not always obvious. |
| Primary change | Prioritize one upgrade rail in cart for “move to 90 servings,” “add your creamer,” or “complete your ritual” based on the item already in cart, rather than presenting a wider merch mix. |
| Primary KPI | Multi-item order rate |
| Decision rule | Ship if multi-item order rate improves by at least 8% relative while checkout-start rate stays flat or better. |
| Expected lift | +8-14% |
| Confidence | 75% |

### EXP-05: Bring subscription flexibility and perks into a compact reassurance block

| Field | Value |
|---|---|
| Pillar | Retention |
| Surface | PDP purchase module and cart reassurance |
| URL | https://mudwtr.com/pages/faqs |
| Evidence | artifacts/mudwtr_20260613_ff54a7/pages/faq_shipping_returns_8_pages_faqs.md |
| Hypothesis | Bringing skip, swap, cancel, and subscriber-perk messaging into a compact reassurance block near purchase will improve subscription take rate because those benefits are clearly documented but currently live more fully in FAQ and long-form PDP content than in a tight decision aid. |
| Primary change | Add a concise “Subscription made easy” module beside the subscribe option covering flexibility, delivery cadence, and perks like app access. |
| Primary KPI | Subscription attach rate |
| Decision rule | Ship if subscription attach improves by at least 10% relative without lowering first-order conversion. |
| Expected lift | +10-17% |
| Confidence | 83% |

### EXP-06: Create a starter-kit to refill lifecycle for first-order buyers

| Field | Value |
|---|---|
| Pillar | Retention |
| Surface | Post-purchase lifecycle for starter-kit buyers |
| URL | https://mudwtr.com/products/30-servings-tin |
| Evidence | inferred - journey stops at checkout entry |
| Hypothesis | Moving starter-kit buyers into refill and recurring plans after first use will improve repeat purchase rate because the catalog is already structured around kits, 30-serving options, and larger refill formats. |
| Primary change | Build a post-purchase flow that introduces refill sizes, preferred cadence, and “graduate your ritual” offers based on the product family purchased first. |
| Primary KPI | 60-day repeat purchase rate |
| Decision rule | Ship if 60-day repeat purchase improves by at least 7% relative among starter-kit first orders over 8 weeks. |
| Expected lift | +7-13% |
| Confidence | 69% |

### EXP-07: Add benefit-led landing paths from homepage to product families

| Field | Value |
|---|---|
| Pillar | Acquisition |
| Surface | Homepage category routing and blend discovery |
| URL | https://mudwtr.com/ |
| Evidence | artifacts/mudwtr_20260613_ff54a7/screenshots/homepage_0_home.png |
| Hypothesis | Routing shoppers into benefit-led landing paths instead of broad category browsing will improve acquisition efficiency because the brand already sells around outcomes like focus, calm, and nourishment, but the current first path is still assortment-heavy. |
| Primary change | Create dedicated landing paths for goals such as focus, calm, or protein, each with one recommended starter, one alternate, and a proof block. |
| Primary KPI | Paid-landing-to-PDP click-through rate |
| Decision rule | Ship if landing-to-PDP click-through improves by at least 10% relative without worsening bounce on paid sessions. |
| Expected lift | +8-15% |
| Confidence | 77% |

### EXP-08: Commercialize the recipes page with stronger product handoffs

| Field | Value |
|---|---|
| Pillar | Acquisition |
| Surface | Recipes / content page templates |
| URL | https://mudwtr.com/pages/recipes |
| Evidence | artifacts/mudwtr_20260613_ff54a7/screenshots/blog_or_content_page_10_pages_recipes.png |
| Hypothesis | Adding stronger product pathways to recipe and educational content will improve content-assisted conversion because the sampled content helps explain ritual use but does not push shoppers decisively into the matching blends or kits. |
| Primary change | Add “shop this ritual,” “start with this kit,” and “works best with” modules to recipe and education templates. |
| Primary KPI | Content-assisted product click-through rate |
| Decision rule | Ship if content-assisted product clicks improve by at least 12% relative without lowering content engagement depth. |
| Expected lift | +7-12% |
| Confidence | 72% |

### EXP-09: Defer non-critical third-party scripts until interaction or idle time

| Field | Value |
|---|---|
| Pillar | Performance |
| Surface | Homepage and PDP script loading |
| URL | https://mudwtr.com/products/hot-cacao-bag |
| Evidence | artifacts/mudwtr_20260613_ff54a7/pages/product_page_1_products_hot-cacao-bag.md |
| Hypothesis | Deferring non-critical third-party scripts until interaction or idle time will improve responsiveness because the sampled page source shows a very large stack of chat, referral, review, quiz, retention, and marketing scripts layered onto already long templates. |
| Primary change | Move non-essential review widgets, referral scripts, chat, and certain marketing tags behind interaction or idle-load triggers while preserving checkout-critical code. |
| Primary KPI | PDP bounce rate |
| Decision rule | Ship if PDP bounce rate improves and add-to-cart rate stays flat or better after the script deferral test. |
| Expected lift | +4-9% |
| Confidence | 80% |

### EXP-10: Reduce mobile overflow and trim heavy below-fold modules on long pages

| Field | Value |
|---|---|
| Pillar | Performance |
| Surface | Homepage, FAQ, and long PDP templates |
| URL | https://mudwtr.com/ |
| Evidence | artifacts/mudwtr_20260613_ff54a7/technical_checks.json |
| Hypothesis | Reducing mobile overflow and trimming heavy below-fold modules will improve browsing depth because mobile-friendly checks warned on 4000px scroll width and both mobile and desktop page-speed checks failed on this run. |
| Primary change | Audit the bottom ticker, embedded widgets, and oversized modules causing overflow, then remove or lazy-load non-essential below-fold sections on long templates. |
| Primary KPI | Homepage bounce rate |
| Decision rule | Ship if mobile load falls below 3.5s with overflow eliminated and bounce improves without conversion regression. |
| Expected lift | +5-10% |
| Confidence | 76% |

## Competitor Analysis

These benchmarks focus on functional-beverage brands that make first-product discovery, subscription value, or ritual bundling simpler than the current MUD/WTR first-purchase journey does on this run (`artifacts/mudwtr_20260613_ff54a7/evidence_summary.md`).

| Competitor | Domain | Positioning | What they make easier | mudwtr edge | Pattern to adapt |
|---|---|---|---|---|---|
| Four Sigmatic | https://us.foursigmatic.com/ | Mainstream functional mushroom coffee and adaptogen brand | Category clarity, product education, and easier first-product choice | Darker ritual identity, deeper long-form proof, and stronger lifestyle distinctiveness | Simplify first-product discovery without losing education (EXP-01, EXP-07) |
| RYZE | https://www.ryzesuperfoods.com/ | Mushroom coffee brand built around a simpler starter conversion path | Guided starter flow, offer clarity, and recurring-plan framing | Broader assortment depth and stronger accessory ecosystem | Make the default starter path easier and reduce choice friction (EXP-02, EXP-05) |
| Clevr Blends | https://clevrblends.com/ | Functional latte brand with strong ritual and bundle positioning | Sampler logic, ritual merchandising, and lifestyle-led bundle discovery | More expansive category breadth and stronger ingredient education | Turn accessories and formats into clearer ritual bundles and content bridges (EXP-03, EXP-08) |

## Technical Checks

| Check | Status | Detail |
|---|---|---|
| SSL Certificate | Pass | HTTPS storefront loaded successfully. |
| HTTPS Redirect | Pass | HTTP redirected to HTTPS. |
| Sitemap | Pass | sitemap.xml found with ~5 entries. |
| Robots.txt | Pass | robots.txt accessible. |
| Critical Pages Loading | Pass | 11/11 selected pages loaded successfully. |
| Meta Tags & Social Previews | Warn | Title+meta description present on 10/11 pages. OG tags present on all pages. |
| Structured Data | Pass | JSON-LD found on 5/11 pages: Organization, Product. Product JSON-LD on 3/3 PDPs. |
| Favicon | Pass | Favicon link tag found. |
| Mobile-Friendly | Warn | Viewport meta present but content overflows 3625px horizontally at 375px (scrollWidth 4000px). |
| Page Speed Mobile | Fail | Navigation timing (single run, not Lighthouse): load 6526ms, DCL 1579ms at 375px viewport. |
| Page Speed Desktop | Fail | Navigation timing (single run, not Lighthouse): load 7902ms, DCL 1580ms. |
| Broken Links | Pass | No broken links in 40 sampled links. |
| Image Optimization | Warn | 268/803 images missing alt text (33%) across 11 crawled pages. Byte-level audit not run. |
| Cookie/Privacy | Pass | Privacy Policy and Terms found. Cookie policy also present. |
| Checkout Reachable | Pass | Cart loaded and checkout entry reached. Journey stopped before payment entry. |
| Payment Methods | Pass | Detected: Visa, Mastercard, Amex, PayPal, Apple Pay, Shop Pay, JCB. |
| Shopping Journey | Warn | Score 4.0/5 - api add to cart fallback (-1.0). Payment: Visa, Mastercard, Amex, PayPal, Apple Pay, Shop Pay, JCB. |
