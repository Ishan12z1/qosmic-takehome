# CRO Audit: MUD\WTR
Run ID: mudwtr_20260611_df56a4
Date: 2026-06-11

---

## Executive Summary

MUD\WTR has built the strongest cart experience of any store in this audit cohort: the shopping journey achieves a 5.0/5 friction score with a live cart upsell, confirmed urgency elements, trust badges at checkout, and 8 payment methods in 4 clicks — the only store where all three cart-level CRO mechanisms (upsell, urgency, trust) are simultaneously active. The starter kit bundling model, which makes every first purchase a curated kit rather than a single unit, structurally elevates AOV from the product architecture level. Subscription login is always visible in the nav, the Help Center FAQ dedicates a full section to subscription management, and the recipe content library builds habitual product use that counteracts churn. For a brand asking health-conscious buyers to permanently replace their coffee routine, the operational infrastructure is mature.

The most significant gap is the inversion between the brand's social proof and its visibility on product pages. MUD\WTR claims 60,000 5-star reviews in its site-level meta, yet no reviews section heading appears on any of the three crawled PDPs — the social proof exists in the database but is not surfaced at the decision moment for new visitors comparing adaptogenic blends against a $40+ starter kit purchase. This is the highest-leverage single fix in the store: health product buyers require review validation before converting, and every PDP currently asks them to take it on faith. A secondary gap is that content pages with high discovery intent — the recipe library, the brand origin story on /pages/about, and the ingredient FAQ on /pages/help-center — have no email capture or product CTAs in their visible heading structure, meaning engaged visitors exit without being captured for the email retention channel.

On the technical side, cookie consent is absent (a GDPR/CCPA compliance exposure), image alt text is missing on 20% of product images (the highest rate of the four stores tested), and the collection page H1 is the generic word "Shop" rather than a keyword-rich heading that would strengthen organic ranking for the core 'coffee alternative' category query. A where-to-buy page returns 404 despite retail distribution being implied by a 'Find in Stores' CTA visible on multiple pages. These are all fixable within a sprint.

---

## Store Overview

| Field | Value |
|---|---|
| Store URL | https://mudwtr.com |
| Category | Functional mushroom wellness / adaptogenic coffee alternative subscription brand |
| Primary use cases | Daily coffee replacement ritual (Original, Hot Cacao, Coffee, Matcha, Turmeric starter kits); calm and sleep support (Rest Starter Kit); protein nutrition with functional mushrooms; subscription recurring ritual |
| Pages crawled | 11/11 |
| Friction score | 5.0/5 |
| Shopping journey outcome | full_journey |

---

## Competitor Benchmarks

| Competitor | Category | Notable CRO strength | Relevant to |
|---|---|---|---|
| Four Sigmatic (foursigmatic.com) | Functional mushroom coffee alternative | Star-rating review count displayed above-fold on every PDP; subscription savings percentage shown inline with add-to-cart | EXP-01, EXP-06 |
| RYZE Superfoods (ryze.com) | Mushroom coffee alternative subscription | Quiz-driven product recommendation funnel on homepage; bundle builder with morning + evening ritual pairing | EXP-04, EXP-07 |
| Laird Superfood (lairdsuperfood.com) | Functional beverage alternative (creamer, matcha, mushroom) | Email capture with recipe-specific discount on content pages; Afterpay on all orders | EXP-03, EXP-05 |
| Clevr Blends (clevrblends.com) | Adaptogenic lattes (chai, matcha, golden milk) | Collection H1 targets 'adaptogenic latte' keyword; recipe blog posts with inline 'Shop this blend' CTAs | EXP-07, EXP-08 |

---

## Experiments

### EXP-01: Surface 60,000 Reviews Above Fold on All PDPs

| Field | Value |
|---|---|
| Pillar | Conversion |
| Surface | All product pages — hero section |
| URL | https://mudwtr.com/products/hot-cacao-bag |
| Evidence | artifacts/mudwtr_20260611_df56a4/evidence_cards/product_page_1_products_hot-cacao-bag.json |
| Hypothesis | Moving the 60,000 5-star reviews count into a visible star-rating badge above the fold on all PDPs will increase PDP-to-cart conversion rate because the review count exists in site meta but no reviews section heading appears on any of the 3 crawled PDPs, meaning health-conscious buyers evaluating a $40+ first-time purchase currently see no social validation at the moment of decision. |
| Primary change | Add a review count and star-rating badge (e.g. '60,000+ 5-star reviews ★★★★★') immediately below the product title on all PDPs, visible without scrolling |
| Secondary change | Add a 'Most helpful reviews' section showing 2–3 highlighted reviews near the top of the page rather than only at the bottom |
| Primary KPI | PDP-to-cart conversion rate |
| Decision rule | +10% relative lift in PDP-to-cart conversion rate over 3-week A/B test |
| Expected lift | High |
| Confidence | High |

---

### EXP-02: Implement Cookie Consent Banner

| Field | Value |
|---|---|
| Pillar | Conversion |
| Surface | Site-wide — entry point for all visitors |
| URL | https://mudwtr.com/ |
| Evidence | artifacts/mudwtr_20260611_df56a4/technical_checks.json |
| Hypothesis | Implementing a GDPR/CCPA-compliant cookie consent banner will close the current compliance gap and maintain analytics tracking consent for EU and California visitors because Cookie/Privacy is currently Warn with no consent popup detected. |
| Primary change | Install a Shopify-compatible cookie consent app (e.g. Pandectes GDPR, Consentmo, or CookieYes) and configure for GDPR + CCPA compliance |
| Secondary change | Configure granular consent categories (functional, analytics, marketing) with regional opt-in defaults |
| Primary KPI | Cookie consent compliance rate (% of visitors accepting analytics cookies) |
| Decision rule | Zero compliance violations; analytics tracking restored for consenting visitors within 1 week |
| Expected lift | High |
| Confidence | High |

---

### EXP-03: Add BNPL Payment Option (Afterpay or Klarna)

| Field | Value |
|---|---|
| Pillar | AOV |
| Surface | Cart and checkout |
| URL | https://mudwtr.com/cart |
| Evidence | artifacts/mudwtr_20260611_df56a4/evidence_cards/shopping_journey.json |
| Hypothesis | Adding a buy-now-pay-later option (Afterpay or Klarna) will increase starter kit conversion rate and average order value because no BNPL option is currently available — the starter kits start at $40+ and BNPL removes the price barrier for first-time buyers who want to try a subscription wellness product before committing to recurring spend. Competitor Laird Superfood offers Afterpay on all orders. |
| Primary change | Enable Afterpay or Klarna via Shopify Payments or the respective Shopify app |
| Secondary change | Display 'Pay in 4 interest-free payments of $X' messaging on PDP hero sections next to the price to surface the option before checkout |
| Primary KPI | Average order value + checkout completion rate for first-time buyers |
| Decision rule | +6% relative lift in checkout completion rate for first-time visitors over 4-week test |
| Expected lift | Medium |
| Confidence | Medium |

---

### EXP-04: Add Morning + Evening Ritual Bundle Cross-Sell

| Field | Value |
|---|---|
| Pillar | AOV |
| Surface | Rest Starter Kit PDP and all Energy blend PDPs |
| URL | https://mudwtr.com/products/rest-starter-kit |
| Evidence | artifacts/mudwtr_20260611_df56a4/evidence_cards/product_page_3_products_rest-starter-kit.json |
| Hypothesis | Adding a 'Complete your ritual' bundle widget on the Rest PDP pairing Rest (zero caffeine, nighttime) with the Original or Coffee starter kit (morning energy) will increase multi-SKU order rate because Rest and Original serve complementary use-cases in a morning/evening wellness routine, yet no cross-sell between them is currently surfaced on either PDP. |
| Primary change | Add a 'Frequently bought together' or 'Build your daily ritual' section on the Rest PDP showing Original + Rest as a bundle with a 10–15% bundle discount |
| Secondary change | Mirror the cross-sell on Original/Coffee PDPs pointing to Rest: 'Complete the ritual — add Rest for your evenings' |
| Primary KPI | Multi-SKU order rate from Rest PDP |
| Decision rule | +12% relative lift in units per transaction from Rest and Original PDP visitors over 3-week test |
| Expected lift | Medium |
| Confidence | Medium |

---

### EXP-05: Add Email Capture to Recipes, About, and Help Center Pages

| Field | Value |
|---|---|
| Pillar | Retention |
| Surface | /pages/recipes, /pages/about, /pages/help-center |
| URL | https://mudwtr.com/pages/recipes |
| Evidence | artifacts/mudwtr_20260611_df56a4/evidence_cards/blog_or_content_page_10_pages_recipes.json |
| Hypothesis | Adding a contextually relevant email capture offer at the bottom of the recipes page ('Get new MUD\WTR recipes weekly — subscribe free'), the about page ('Join the movement — get the starter ritual guide'), and the help center ('Get tips for your MUD\WTR ritual') will increase email list growth because no email capture heading is detected on any of these three content-rich pages, meaning all content-engaged visitors currently exit without being captured for the retention funnel. |
| Primary change | Add an email capture section (matching the format used on comparable pages across the site, if any exist) to /pages/recipes, /pages/about, and /pages/help-center with a content-specific incentive for each |
| Secondary change | Trigger a secondary offer for visitors who reach the bottom of /pages/about ('Ready to start your ritual? Get 15% off your first order') |
| Primary KPI | Email capture rate from content pages |
| Decision rule | >3% of content page visitors subscribing to email list over 4-week measurement period |
| Expected lift | High |
| Confidence | High |

---

### EXP-06: Add Post-Purchase Subscription Upsell for One-Time Buyers

| Field | Value |
|---|---|
| Pillar | Retention |
| Surface | Order confirmation page |
| URL | https://mudwtr.com/products/30-servings-tin |
| Evidence | artifacts/mudwtr_20260611_df56a4/evidence_cards/product_page_2_products_30-servings-tin.json |
| Hypothesis | Offering a subscribe-and-save upgrade on the order confirmation page for one-time starter kit buyers ('Love your first tin? Subscribe and save 15% — never run out') will increase subscription conversion rate because buyers who just completed a purchase have maximum product confidence and are most receptive to a recurring commitment, and the subscription toggle state on PDPs was not confirmed as prominently visible in the crawled structure. |
| Primary change | Add a post-purchase upsell via Shopify's thank-you page customization or a ReConvert-style post-purchase app, offering the subscription version of the SKU just purchased at the standard save percentage |
| Secondary change | Test 'save 15%' vs. 'free shipping on every subscription order' as the subscription incentive framing |
| Primary KPI | Subscription conversion rate from one-time starter kit buyers |
| Decision rule | >8% of one-time buyers clicking Subscribe upsell over 4-week test |
| Expected lift | High |
| Confidence | Medium |

---

### EXP-07: Optimize Collection H1 from 'Shop' to Category Keyword

| Field | Value |
|---|---|
| Pillar | Acquisition |
| Surface | /collections/shop (canonical collection page) |
| URL | https://mudwtr.com/collections/shop |
| Evidence | artifacts/mudwtr_20260611_df56a4/evidence_cards/collection_page_5_collections_all.json |
| Hypothesis | Changing the collection H1 from the generic 'Shop' to a keyword-rich heading such as 'Coffee Alternatives & Adaptogenic Mushroom Blends' will improve organic ranking for the core category query 'best coffee alternative' because the current H1 provides zero keyword signal while the meta description correctly targets 'coffee alternatives designed with adaptogens' — fixing this H1/meta mismatch will fully unlock the SEO signal the meta description is already pointing at. |
| Primary change | Update the H1 on /collections/shop from 'Shop' to a keyword-rich heading targeting the primary category search query |
| Secondary change | Run the same H1 optimization audit across any sub-collection pages (Energy, Calm, Protein) to ensure consistent keyword targeting at the category level |
| Primary KPI | Organic impressions for 'coffee alternative' and related queries (Google Search Console) |
| Decision rule | Measurable improvement in organic impressions for collection-level queries within 6 weeks of deployment |
| Expected lift | Medium |
| Confidence | High |

---

### EXP-08: Fix Recipes Page H1 (CSS Artifact → Real Text Heading)

| Field | Value |
|---|---|
| Pillar | Acquisition |
| Surface | /pages/recipes |
| URL | https://mudwtr.com/pages/recipes |
| Evidence | artifacts/mudwtr_20260611_df56a4/evidence_cards/blog_or_content_page_10_pages_recipes.json |
| Hypothesis | Replacing the CSS-class-artifact H1 'SpecialtyRecipes' (a concatenated text string from an image-replacement CSS technique) with a real text H1 ('Coffee Alternative Recipes — Lattes, Smoothies & More') will improve SEO ranking for recipe-intent queries because the page currently has no actual text H1 and therefore provides no keyword signal for 'mudwtr latte recipe', 'adaptogenic smoothie recipe', and related long-tail queries. |
| Primary change | Replace the CSS image-replacement heading technique on /pages/recipes with an actual H1 text element matching the page's meta title: 'Coffee Alternative Recipes' |
| Secondary change | Add H2 sub-sections for each recipe category (Lattes, Smoothies, Protein Shakes) to improve topical depth and internal linking structure |
| Primary KPI | Organic impressions for recipe-intent queries (Google Search Console) |
| Decision rule | Measurable improvement in organic impressions for recipe queries within 6 weeks |
| Expected lift | Medium |
| Confidence | High |

---

### EXP-09: Fix Alt Text on 21 Missing Product Images

| Field | Value |
|---|---|
| Pillar | Performance |
| Surface | Site-wide — product and content images |
| URL | https://mudwtr.com/collections/shop |
| Evidence | artifacts/mudwtr_20260611_df56a4/technical_checks.json |
| Hypothesis | Adding descriptive alt text to the 21/101 product images currently missing it will improve image search indexing and accessibility compliance because 20% of images are without alt text — the highest rate of the four stores in this audit cohort — and Google cannot interpret unlabelled product images for image search or accessibility tools. |
| Primary change | Add alt text to all 21 identified images in Shopify admin (Products → each image → alt text field) |
| Secondary change | Establish a standard alt text format: '[Product name] — [flavour/blend] — MUD\\WTR coffee alternative' for product images; '[Ingredient name] — adaptogenic mushroom' for ingredient imagery |
| Primary KPI | Image search impressions (Google Search Console) |
| Decision rule | All 21 images have alt text within 1 week |
| Expected lift | Low |
| Confidence | High |

---

### EXP-10: Run Lighthouse to Establish Page Speed Baseline

| Field | Value |
|---|---|
| Pillar | Performance |
| Surface | Homepage and primary PDP |
| URL | https://mudwtr.com/ |
| Evidence | artifacts/mudwtr_20260611_df56a4/technical_checks.json |
| Hypothesis | Running Lighthouse on the homepage and the Original Starter Kit PDP will establish a quantified page speed baseline that identifies the specific rendering bottlenecks (e.g., unoptimized hero video, third-party scripts, LCP image not preloaded) causing the current Page Speed Mobile and Desktop Warn status, enabling prioritized performance improvements. |
| Primary change | Run Lighthouse CI on mudwtr.com homepage and /products/30-servings-tin — capture Core Web Vitals (LCP, CLS, FID/INP), identify the top 3 bottlenecks |
| Secondary change | If LCP > 2.5s on mobile: preload the hero image/video; if CLS > 0.1: audit layout shift sources in the ingredient section and recipe image grid |
| Primary KPI | Lighthouse Performance score (mobile) — target > 70 |
| Decision rule | Lighthouse mobile Performance score established within 1 week; improvement plan based on top 3 bottlenecks scoped and prioritized |
| Expected lift | Medium |
| Confidence | Medium |

---

## Technical Checks

| Check | Status | Detail |
|---|---|---|
| SSL Certificate | Pass | HTTPS storefront loaded successfully. |
| HTTPS Redirect | Pass | HTTP redirected to HTTPS. |
| Sitemap | Pass | sitemap.xml found with ~5 entries. |
| Robots.txt | Pass | robots.txt accessible. |
| Meta Tags & Social Previews | Pass | Title and meta description found. OG tags present. |
| Structured Data | Pass | JSON-LD found: Organization. |
| Favicon | Pass | Favicon link tag found. |
| Cookie/Privacy | Warn | Privacy and Terms found but cookie consent policy not detected. |
| Broken Links | Warn | 5 non-critical broken links in 29 sampled. |
| Image Optimization | Warn | 21/101 images missing alt text (20%). Byte-level audit not run. |
| Mobile-Friendly | Warn | Desktop-only audit. Mobile viewport not tested. |
| Page Speed Mobile | Warn | No Lighthouse run performed. |
| Page Speed Desktop | Warn | No Lighthouse run performed. |
| Critical Pages Loading | Pass | 11/11 selected pages loaded successfully. |
| Checkout Reachable | Pass | Cart loaded and checkout entry reached. Journey stopped before payment entry. |
| Shopping Journey | Pass | Score 5.0/5 — no blockers detected. Payment: Visa, Mastercard, Amex, PayPal, Apple Pay, Shop Pay, Discover, JCB. |
| Payment Methods | Pass | Detected: Visa, Mastercard, Amex, PayPal, Apple Pay, Shop Pay, Discover, JCB. |

---

## Evidence Summary

**Conversion**
- 5.0/5 friction score — 4 clicks to checkout, trust badges confirmed, live cart upsell and urgency; best cart experience of all 4 stores tested (`artifacts/mudwtr_20260611_df56a4/pages/shopping_journey.json`)
- No reviews section heading on any of 3 crawled PDPs despite 60,000 5-star reviews in site meta — social proof invisible at the decision moment (`artifacts/mudwtr_20260611_df56a4/evidence_cards/product_page_1_products_hot-cacao-bag.json`)
- Cookie consent absent — GDPR/CCPA compliance gap (`artifacts/mudwtr_20260611_df56a4/technical_checks.json`)
- 'Buy now' CTA sitewide links to coffee-starter-kit, not the current product — potential UX issue on Rest and Hot Cacao PDPs (`artifacts/mudwtr_20260611_df56a4/evidence_cards/product_page_3_products_rest-starter-kit.json`)

**AOV**
- Cart upsell confirmed live — only store of 4 tested where cart recommendations actively populate (`artifacts/mudwtr_20260611_df56a4/pages/shopping_journey.json`)
- Starter kit bundling as default SKU structure elevates baseline AOV across all product lines (`artifacts/mudwtr_20260611_df56a4/pages/homepage_0_home.json`)
- No BNPL option — deathwishcoffee has Afterpay; starter kits at $40+ would benefit from installment payment options (`artifacts/mudwtr_20260611_df56a4/evidence_cards/shopping_journey.json`)
- No morning + evening bundle cross-sell on Rest PDP (`artifacts/mudwtr_20260611_df56a4/evidence_cards/product_page_3_products_rest-starter-kit.json`)

**Retention**
- Subscription login in nav + Accounts & Subscriptions FAQ section — subscriber management infrastructure is accessible and well-supported (`artifacts/mudwtr_20260611_df56a4/pages/homepage_0_home.json`)
- Recipe content at /pages/recipes builds habitual use — smoothies, lattes, protein shakes extend the ritual beyond a simple morning beverage (`artifacts/mudwtr_20260611_df56a4/evidence_cards/blog_or_content_page_10_pages_recipes.json`)
- No email capture detected on recipes, about, or help center pages — content-engaged visitors exit without being captured (`artifacts/mudwtr_20260611_df56a4/evidence_cards/about_page_9_pages_about.json`)

**Acquisition**
- Collection meta description targets 'coffee alternative' keyword with adaptogen and superfood signals — good meta foundation (`artifacts/mudwtr_20260611_df56a4/evidence_cards/collection_page_5_collections_all.json`)
- Collection H1 is generic 'Shop' — H1/meta keyword mismatch undercuts collection-level organic ranking (`artifacts/mudwtr_20260611_df56a4/evidence_cards/collection_page_5_collections_all.json`)
- Recipes page H1 is a CSS class artifact 'SpecialtyRecipes' — effectively no text H1 for recipe-intent SEO (`artifacts/mudwtr_20260611_df56a4/evidence_cards/blog_or_content_page_10_pages_recipes.json`)
- Where-to-buy page is 404 despite implied retail distribution (`artifacts/mudwtr_20260611_df56a4/evidence_cards/where_to_buy_7_pages_where-to-buy.json`)

**Performance**
- 21/101 images (20%) missing alt text — highest rate of all 4 stores tested (`artifacts/mudwtr_20260611_df56a4/technical_checks.json`)
- Page speed unverified — Lighthouse not run; Core Web Vitals unknown (`artifacts/mudwtr_20260611_df56a4/technical_checks.json`)
