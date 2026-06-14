# CRO Audit — Zen Rojas (zenrojas.com)

**Run ID:** `zenrojas_20260614_ab4535`
**Date:** 2026-06-14
**Crawl health:** Healthy — 10/10 pages loaded, full shopping journey, friction 5.0/5

## Executive Summary

Zen Rojas has solved the hard part of ecommerce and left the easy money on the table. The storefront is technically clean and the purchase path is frictionless — the crawler completed a full PDP → cart → checkout journey in three clicks with no errors, scored friction 5.0/5, and detected nine payment methods including Apple Pay, Google Pay, and Shop Pay (`artifacts/zenrojas_20260614_ab4535/pages/shopping_journey.json`). The single biggest constraint is not friction; it is **trust and basket size at the moment of decision.** Every product page renders its reviews widget empty ("No reviews yet"), so qualified shoppers reach the buy box with zero social proof (`artifacts/zenrojas_20260614_ab4535/screenshots/product_page_1_products_tea-bags.png`), and the brand's strongest credibility cue — "Veteran owned," organic, ethically sourced — is stranded on the About page, never echoed on the cart or checkout where doubt peaks (`artifacts/zenrojas_20260614_ab4535/pages/about_page_9_pages_aboutus.md`, `artifacts/zenrojas_20260614_ab4535/screenshots/cart_page_4_cart.png`).

The largest AOV opportunity is a structural mismatch between the PDP and the cart. The product pages actively grow baskets with a working "Frequently bought together" bundle and a "Complete Your Ritual" cross-sell row (`artifacts/zenrojas_20260614_ab4535/screenshots/product_page_1_products_tea-bags.png`), yet the cart abandons that momentum entirely: there is no in-cart upsell and no free-shipping progress bar, even though the store advertises free shipping over $50 (`artifacts/zenrojas_20260614_ab4535/screenshots/cart_page_4_cart.png`, `artifacts/zenrojas_20260614_ab4535/pages/shopping_journey.json`). For a repeat-purchase consumable category, the absence of any subscribe-and-save option is the corresponding retention gap (`artifacts/zenrojas_20260614_ab4535/pages/product_page_1_products_tea-bags.json`).

Technical health is solid with no critical failures: 12 of 17 checks pass, including SSL, HTTPS redirect, sitemap, mobile-friendliness, and page speed (mobile load 1733ms, desktop 1978ms) (`artifacts/zenrojas_20260614_ab4535/technical_checks.json`). The five warnings are acquisition-and-performance drags rather than blockers — no JSON-LD structured data on any page, generic/truncated metadata, no favicon link tag, four non-critical broken links, and 33% of images missing alt text. None of these stop a sale, but together they cap organic discovery and rich-result eligibility for a brand whose blog and story are genuine acquisition assets.

## Proposed Experiments

### EXP-01: Populate and surface PDP social proof

| Field | Value |
|---|---|
| Pillar | Conversion |
| Surface | PDP — buy box |
| URL | https://zenrojas.com/products/tea-bags |
| Evidence | artifacts/zenrojas_20260614_ab4535/screenshots/product_page_1_products_tea-bags.png |
| Hypothesis | Seeding the existing (empty) review widget via automated review-request emails to past buyers and displaying a rating summary beside the product title will raise add-to-cart rate, because the PDP currently shows "No reviews yet" and offers no social proof at the decision point. |
| Primary change | Launch automated review-request emails to past buyers; render the star-rating summary directly under the H1 and a reviews section above "Complete Your Ritual" |
| Primary KPI | PDP add-to-cart rate |
| Decision rule | Ship if add-to-cart rate improves ≥5% relative over a 3-week test at 95% significance |
| Expected lift | +6–12% |
| Confidence | 70% |

### EXP-02: Trust strip on cart and checkout

| Field | Value |
|---|---|
| Pillar | Conversion |
| Surface | Cart page + checkout entry |
| URL | https://zenrojas.com/cart |
| Evidence | artifacts/zenrojas_20260614_ab4535/screenshots/cart_page_4_cart.png |
| Hypothesis | Adding a trust strip ("Veteran owned · 100% organic · 30-day guarantee · secure checkout") to the cart will reduce cart abandonment, because these credibility cues currently exist only on the About/PDP copy and are absent where final purchase doubt occurs. |
| Primary change | Add a compact trust/reassurance band above the Checkout button on the cart, reusing existing About-page claims |
| Primary KPI | Cart-to-checkout continuation rate |
| Decision rule | Ship if cart→checkout rate improves ≥3% relative over a 3-week test |
| Expected lift | +3–8% |
| Confidence | 65% |

### EXP-03: Free-shipping progress bar in cart

| Field | Value |
|---|---|
| Pillar | AOV |
| Surface | Cart page |
| URL | https://zenrojas.com/cart |
| Evidence | artifacts/zenrojas_20260614_ab4535/screenshots/cart_page_4_cart.png |
| Hypothesis | Showing a dynamic "You're $X away from free shipping" progress bar tied to the existing $50 threshold will increase average order value, because the threshold is advertised in the announcement bar but never reinforced in the cart where the add-on decision is made. |
| Primary change | Add a free-shipping progress meter to the cart that updates with subtotal and links to recommended add-ons |
| Primary KPI | Average order value |
| Decision rule | Ship if AOV improves ≥4% relative with no drop in checkout rate over a 3-week test |
| Expected lift | +5–10% |
| Confidence | 74% |

### EXP-04: In-cart cross-sell

| Field | Value |
|---|---|
| Pillar | AOV |
| Surface | Cart page |
| URL | https://zenrojas.com/cart |
| Evidence | artifacts/zenrojas_20260614_ab4535/pages/shopping_journey.json |
| Hypothesis | Adding a "Complete your ritual" recommended-add-ons module to the cart will lift units per order, because the journey data confirms no cart upsell exists (cart_upsell_present: false) while the same mechanic already converts on the PDP. |
| Primary change | Render 2–3 complementary recommendations (teaware for tea carts, sampler for single-SKU carts) with one-tap add, below the line items |
| Primary KPI | Units per order |
| Decision rule | Ship if units-per-order improves ≥4% relative over a 3-week test |
| Expected lift | +4–9% |
| Confidence | 68% |

### EXP-05: Subscribe-and-save on consumable teas

| Field | Value |
|---|---|
| Pillar | Retention |
| Surface | PDP — buy box |
| URL | https://zenrojas.com/products/blacktea |
| Evidence | artifacts/zenrojas_20260614_ab4535/pages/product_page_1_products_tea-bags.json |
| Hypothesis | Offering a subscribe-and-save option (e.g. 10–15% off recurring) on consumable teas will increase repeat-purchase revenue, because the PDPs currently sell only one-time purchases despite tea being an inherently replenishable category. |
| Primary change | Add a subscription toggle (one-time vs. deliver every 30/45/60 days) to tea PDP buy boxes |
| Primary KPI | Subscription attach rate / 90-day repeat revenue |
| Decision rule | Ship if ≥8% of tea orders select subscription within 4 weeks with no drop in overall conversion |
| Expected lift | +8–18% (90-day repeat revenue) |
| Confidence | 66% |

### EXP-06: Homepage email capture with first-order incentive

| Field | Value |
|---|---|
| Pillar | Retention |
| Surface | Homepage |
| URL | https://zenrojas.com/ |
| Evidence | artifacts/zenrojas_20260614_ab4535/pages/homepage_0_home.md |
| Hypothesis | Adding a homepage email-capture offering a first-order incentive will grow the marketing list and recover non-buyers, because newsletter signup currently exists only in the footer with no incentive and there is no homepage capture. |
| Primary change | Add a delayed/exit-intent email modal (and inline footer form) offering 10% off the first order |
| Primary KPI | Email capture rate (% of sessions) |
| Decision rule | Ship if capture rate reaches ≥2% of sessions with no measurable bounce increase over a 3-week test |
| Expected lift | +1.5–3% (sessions capturing email) |
| Confidence | 72% |

### EXP-07: Add Product and FAQPage structured data

| Field | Value |
|---|---|
| Pillar | Acquisition |
| Surface | PDPs + FAQ page (sitewide) |
| URL | https://zenrojas.com/products/tea-bags |
| Evidence | artifacts/zenrojas_20260614_ab4535/technical_checks.json |
| Hypothesis | Adding Product JSON-LD (name, price, availability, rating once EXP-01 lands) and FAQPage JSON-LD will increase organic CTR via rich results, because no JSON-LD was detected on any of the 10 crawled pages. |
| Primary change | Inject Product schema on PDPs and FAQPage schema on /pages/faqs through the theme |
| Primary KPI | Organic impressions and CTR for product/FAQ queries |
| Decision rule | Ship and keep if rich results validate in Search Console and organic CTR rises over 6 weeks |
| Expected lift | +5–12% (organic CTR) |
| Confidence | 64% |

### EXP-08: Fix templated metadata and commercialize content

| Field | Value |
|---|---|
| Pillar | Acquisition |
| Surface | Homepage, blog, collections |
| URL | https://zenrojas.com/blogs/weekly-blog/building-a-family-legacy-through-wellness-community-and-purpose-driven-growth |
| Evidence | artifacts/zenrojas_20260614_ab4535/pages/blog_or_content_page_10_blogs_weekly-blog_building-a-family-lega.json |
| Hypothesis | Replacing generic/truncated metadata (homepage OG title "Home Page", blog title cut at "Purpose-Driv") and adding contextual product cards to blog posts will improve organic CTR and content-assisted conversion, because the blog builds authority today but contains no product links or tuned metadata. |
| Primary change | Author unique title/meta/OG per template; insert in-content product cards + a newsletter block into blog posts |
| Primary KPI | Organic CTR + content-assisted conversion rate |
| Decision rule | Ship if organic CTR improves and blog→PDP click-through exceeds 3% over 6 weeks |
| Expected lift | +4–9% (organic CTR) |
| Confidence | 60% |

### EXP-09: Next-gen image compression and lazy-loading

| Field | Value |
|---|---|
| Pillar | Performance |
| Surface | Sitewide (PDP, collections, homepage) |
| URL | https://zenrojas.com/collections/teas |
| Evidence | artifacts/zenrojas_20260614_ab4535/technical_checks.json |
| Hypothesis | Serving responsive WebP/AVIF images and lazy-loading below-the-fold media will protect and improve mobile LCP as the catalog grows, because 92 images were crawled with no byte-level optimization audited and image weight is the most common cause of mobile slowdown. |
| Primary change | Enable responsive next-gen image formats and native lazy-loading for below-fold images across templates |
| Primary KPI | Mobile LCP / page load time |
| Decision rule | Ship if mobile LCP improves ≥10% with no layout regressions |
| Expected lift | +5–12% (LCP improvement) |
| Confidence | 67% |

### EXP-10: Defer non-critical third-party scripts

| Field | Value |
|---|---|
| Pillar | Performance |
| Surface | Sitewide — PDP and cart |
| URL | https://zenrojas.com/products/tea-bags |
| Evidence | artifacts/zenrojas_20260614_ab4535/screenshots/product_page_1_products_tea-bags.png |
| Hypothesis | Deferring the live-chat widget and other non-critical third-party scripts until browser idle will improve mobile interaction readiness, because the chat widget loads on the PDP and cart and such widgets commonly delay interactivity even when load timings look healthy (current mobile load 1733ms). |
| Primary change | Lazy-initialize the chat widget and analytics/non-critical tags on idle or first interaction |
| Primary KPI | Mobile Total Blocking Time / time-to-interactive |
| Decision rule | Ship if TBT improves ≥15% with no loss of chat engagement over a 2-week test |
| Expected lift | +5–10% (TBT improvement) |
| Confidence | 62% |

## Competitor Analysis

Selected on `store_category: tea / specialty organic beverages` and primary use cases (daily ritual, functional wellness, teaware attach).

| Competitor | Domain | Positioning | What they make easier | Zen Rojas edge | Pattern to adapt |
|---|---|---|---|---|---|
| Vahdam Teas | vahdam.com | Direct-from-India premium organic tea, sustainability-led | Dense star ratings and review counts on every PDP; subscribe-and-save built in | "Veteran owned" US brand story; cleaner, calmer UX | PDP review density (EXP-01) and subscription option (EXP-05) |
| Art of Tea | artoftea.com | Organic loose-leaf, wellness and gifting focus | Curated bundles/gift sets and clear free-shipping threshold messaging in cart | Stronger founder/mission narrative | In-cart AOV mechanics and free-ship progress (EXP-03, EXP-04) |
| Rishi Tea | rishi-tea.com | Botanical/organic sourcing authority, education-heavy | Content tightly linked to shoppable products; rich structured data | Active personal weekly blog with founder voice | Commercialized content + structured data (EXP-07, EXP-08) |
| Tea Drops | myteadrop.com | Modern, design-forward organic tea, ritual branding | Email capture with incentive on entry; strong sampler funnel | Broader teaware attach and 9 payment methods | Homepage email capture (EXP-06) |

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
