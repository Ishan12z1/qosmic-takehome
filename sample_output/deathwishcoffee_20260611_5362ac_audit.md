# CRO Audit: Death Wish Coffee
Run ID: deathwishcoffee_20260611_5362ac
Date: 2026-06-11

---

## Executive Summary

Death Wish Coffee has a best-in-class DTC purchase path: a 5.0/5 friction score, 3 clicks from PDP to checkout, trust badges confirmed at the payment step, and 9 payment methods including Afterpay for BNPL buyers. The shopping journey mechanics are more polished than the vast majority of Shopify stores. Their subscription and bundle infrastructure is mature and well-merchandised — Subscribe & Save is prominently positioned in the navigation, "Build Your Own Bundle" with 15% off is linked from every page, and email capture with a 20% first-order discount appears across the cart, FAQ, blog, and about pages. For a brand founded in 2012, this represents years of CRO iteration that is clearly paying off.

The two most impactful remaining gaps are operational rather than foundational. First: the cart's "Featured collection" upsell section exists in the page template but failed to populate during the shopping journey — the cart recommends nothing, leaving potential order-value lift on the table at the final pre-checkout step. Second: a cookie consent banner is absent (Cookie/Privacy: Warn), creating a GDPR/CCPA compliance exposure that is not just a legal risk but reduces visitor trust for EU/California shoppers who expect the industry-standard consent flow. Both are fixable in days, not weeks.

The remaining opportunity is SEO precision: the "LIKE FREE SH*T?" giveaway promotion is inserted as the H1 heading across PDPs and collection pages, displacing the natural product keyword in the most important SEO signal on each page. The homepage has no H1 at all. Sitemap and robots.txt both return 429 rate limit errors, potentially blocking Googlebot from fully indexing the 132-product catalog. These technical SEO issues could be suppressing organic discoverability for a brand with strong educational content that deserves top-10 rankings.

---

## Store Overview

| Field | Value |
|---|---|
| Store URL | https://deathwishcoffee.com |
| Category | Bold/dark roast specialty coffee / subscription coffee brand |
| Primary use cases | Daily coffee subscription (ground, pods, cold brew, espresso), gift-giving (mugs, gift cards, bundles), coffee lifestyle/collector (limited-edition drinkware, apparel) |
| Pages crawled | 10/11 |
| Friction score | 5.0/5 |
| Shopping journey outcome | full_journey |

---

## Competitor Benchmarks

| Competitor | Category | Notable CRO strength | Relevant to |
|---|---|---|---|
| Black Rifle Coffee (blackriflecoffee.com) | Bold/roast specialty coffee subscription | Two-click subscription conversion; loyalty points system integrated into cart | EXP-01, EXP-06 |
| Bones Coffee (bonescoffee.com) | Flavored specialty coffee | Cart upsell with matching flavored coffee accessories; active cookie consent + GDPR compliance | EXP-03, EXP-05 |
| Atlas Coffee Club (atlascoffee.com) | Subscription single-origin coffee | Personalized subscription quiz on homepage; personalized email flows by roast preference | EXP-07, EXP-06 |
| Stone Street Coffee (stonestcoffee.com) | Dark roast specialty coffee | H1 keyword optimization on all PDPs; collection page meta descriptions for roast-type queries | EXP-02, EXP-09 |

---

## Experiments

### EXP-01: Implement Cookie Consent Banner

| Field | Value |
|---|---|
| Pillar | Conversion |
| Surface | Site-wide — entry point for all visitors |
| URL | https://www.deathwishcoffee.com/ |
| Evidence | artifacts/deathwishcoffee_20260611_5362ac/technical_checks.json |
| Hypothesis | Implementing a GDPR/CCPA-compliant cookie consent banner will close the current compliance gap and maintain marketing tracking consent across EU and California visitors because Cookie/Privacy is currently Warn with no consent popup detected. |
| Primary change | Install a Shopify-compatible cookie consent app (e.g. Pandectes GDPR, Consentmo, or CookieYes) and configure for GDPR + CCPA compliance |
| Secondary change | Configure consent categories (functional, analytics, marketing) with granular opt-in per region |
| Primary KPI | Cookie consent compliance rate (% of visitors accepting analytics cookies) |
| Decision rule | 0 compliance violations; analytics tracking reinstated for consenting visitors within 1 week |
| Expected lift | High |
| Confidence | High |

---

### EXP-02: Add H1 to Homepage and Restore Product H1s

| Field | Value |
|---|---|
| Pillar | Acquisition |
| Surface | Homepage + all PDP pages |
| URL | https://www.deathwishcoffee.com/ |
| Evidence | artifacts/deathwishcoffee_20260611_5362ac/evidence_cards/homepage_0_home.json |
| Hypothesis | Adding a keyword-rich H1 to the homepage ('The World's Strongest Coffee — USDA Organic, Fair Trade') and moving the 'LIKE FREE SH*T?' giveaway section to a position that doesn't override the product H1 on PDPs will improve organic keyword ranking because the homepage currently has no H1 and PDPs use a promotional tagline as the H1 instead of the product name. |
| Primary change | Add H1 heading to the homepage above or below the hero section. On PDPs, move the giveaway CTA block below the main product H1 |
| Secondary change | Audit all H1 tags across collection pages (currently 'LIKE FREE SH*T?' on /collections/all) and restore category-keyword H1s |
| Primary KPI | Organic impressions on homepage + primary coffee PDP search queries (Google Search Console) |
| Decision rule | Measurable improvement in organic impressions within 6 weeks of deployment |
| Expected lift | Medium |
| Confidence | High |

---

### EXP-03: Activate Cart Upsell with Coffee-in-Cart Recommendations

| Field | Value |
|---|---|
| Pillar | AOV |
| Surface | Cart page — 'Featured collection' section |
| URL | https://deathwishcoffee.com/cart |
| Evidence | artifacts/deathwishcoffee_20260611_5362ac/evidence_cards/cart_page_4_cart.json |
| Hypothesis | Activating the cart's 'Featured collection' section to display 1–2 product recommendations when a coffee item is in the cart (e.g. matching mug, bundle upgrade, or a second roast) will increase average order value because cart_upsell_present was confirmed false despite the section existing in the page template. |
| Primary change | Configure the Shopify cart's "Featured collection" section to show products dynamically based on cart contents (use Shopify's product recommendations API or a cart upsell app) |
| Secondary change | Test cross-selling from consumable to accessory (coffee → mug) and from single to bundle (1 bag → 3-bag bundle at discount) |
| Primary KPI | Average order value |
| Decision rule | +8% relative lift in AOV over 3-week test |
| Expected lift | High |
| Confidence | High |

---

### EXP-04: Coffee Cross-Sell on Mug and Drinkware PDPs

| Field | Value |
|---|---|
| Pillar | AOV |
| Surface | Product pages — mugs and drinkware |
| URL | https://www.deathwishcoffee.com/products/baba-yaga-mug |
| Evidence | artifacts/deathwishcoffee_20260611_5362ac/evidence_cards/product_page_2_products_baba-yaga-mug.json |
| Hypothesis | Adding a "Complete the ritual" coffee cross-sell widget on all mug/drinkware PDPs (showing the top-selling dark roast at a mug+coffee bundle price) will increase multi-product order rate because mug buyers are prime coffee conversion targets and no coffee cross-sell is currently surfaced on drinkware PDPs. |
| Primary change | Add a "Pair with our coffee" section to all mug and drinkware PDPs showing 1–2 coffee SKUs with an optional bundle discount |
| Secondary change | Frame as 'Your new mug deserves the best coffee. Try our signature dark roast.' |
| Primary KPI | Units per transaction from mug PDPs |
| Decision rule | +12% relative lift in units/transaction on mug PDPs over 3-week test |
| Expected lift | Medium |
| Confidence | Medium |

---

### EXP-05: Cart Free Shipping Threshold Bar

| Field | Value |
|---|---|
| Pillar | AOV |
| Surface | Cart page |
| URL | https://deathwishcoffee.com/cart |
| Evidence | artifacts/deathwishcoffee_20260611_5362ac/pages/shopping_journey.json |
| Hypothesis | Adding a free shipping progress bar to the cart ('You're $X away from free shipping') will increase average order value because the cart currently has no urgency signal or incentive to add products, and coffee is a lightweight, shippable repeat-purchase product where free shipping is a strong motivator. |
| Primary change | Add free shipping threshold bar at the top of the cart (set threshold ~15% above current AOV) |
| Secondary change | Pair with the activated 'Featured collection' product recommendations (EXP-03) to show what products would push the buyer over the threshold |
| Primary KPI | Average order value |
| Decision rule | +7% relative lift in AOV over 3-week test |
| Expected lift | Medium |
| Confidence | Medium |

---

### EXP-06: Personalize Cart Email Capture for Returning Customers

| Field | Value |
|---|---|
| Pillar | Retention |
| Surface | Cart page + all email capture banners |
| URL | https://deathwishcoffee.com/cart |
| Evidence | artifacts/deathwishcoffee_20260611_5362ac/evidence_cards/cart_page_4_cart.json |
| Hypothesis | Showing a different email capture offer to returning customers ('Upgrade to Subscribe & Save — never run out of coffee') vs. new visitors ('Save 20% on your first order') will improve retention conversion rate because the current offer is identical for all visitors, including repeat buyers who already have an account and are ineligible for the first-order discount. |
| Primary change | Use Shopify Customer API or a personalization app to detect logged-in vs. guest visitors and show segmented email/subscription CTAs |
| Secondary change | For logged-in subscribers, suppress the email capture entirely and show an account-specific loyalty offer |
| Primary KPI | Email capture rate (new visitors) + subscription upsell rate (returning visitors) |
| Decision rule | +5% improvement in email capture rate for new visitors OR +3% subscription upsell rate for returning visitors over 4-week test |
| Expected lift | Medium |
| Confidence | Medium |

---

### EXP-07: Subscribe & Save Post-Purchase Upsell for One-Time Buyers

| Field | Value |
|---|---|
| Pillar | Retention |
| Surface | Order confirmation page |
| URL | https://www.deathwishcoffee.com/products/death-wish-coffee |
| Evidence | artifacts/deathwishcoffee_20260611_5362ac/evidence_cards/about_page_9_pages_about.json |
| Hypothesis | Offering a Subscribe & Save upsell on the order confirmation page for one-time coffee buyers ('Never run out — subscribe and save 15%') will increase subscription conversion rate because customers who just completed a purchase have maximum confidence and are most receptive to a recurring purchase offer. |
| Primary change | Add post-purchase upsell via Shopify's thank-you page customization or a post-purchase app, showing Subscribe & Save for the coffee SKU just purchased |
| Secondary change | Test 15% off subscription vs. 'free shipping on every subscription order' as the incentive |
| Primary KPI | Subscription conversion rate from post-purchase upsell |
| Decision rule | >6% of one-time coffee buyers clicking Subscribe upsell over 4-week test |
| Expected lift | High |
| Confidence | Medium |

---

### EXP-08: Fix Sitemap and Robots.txt Rate Limiting

| Field | Value |
|---|---|
| Pillar | Acquisition |
| Surface | Technical — sitemap.xml and robots.txt |
| URL | https://deathwishcoffee.com/sitemap.xml |
| Evidence | artifacts/deathwishcoffee_20260611_5362ac/technical_checks.json |
| Hypothesis | Resolving the 429 rate limit responses on sitemap.xml and robots.txt will ensure Googlebot can fully crawl the 132-product catalog because both files currently return 429, which may cause Googlebot to reduce crawl frequency or miss newly added products. |
| Primary change | Investigate CDN/WAF rate limiting rules (Cloudflare or Fastly) and add an exception for Googlebot User-Agent on /sitemap.xml and /robots.txt |
| Secondary change | Submit the sitemap to Google Search Console after fixing to trigger a re-crawl |
| Primary KPI | Sitemap and robots.txt HTTP status (both should return 200) |
| Decision rule | Both return 200 for Googlebot requests within 1 week |
| Expected lift | Medium |
| Confidence | High |

---

### EXP-09: Add Meta Descriptions to Collection Pages

| Field | Value |
|---|---|
| Pillar | Acquisition |
| Surface | /collections/all and /collections/sale |
| URL | https://deathwishcoffee.com/collections/all |
| Evidence | artifacts/deathwishcoffee_20260611_5362ac/evidence_cards/collection_page_5_collections_all.json |
| Hypothesis | Adding unique meta descriptions to /collections/all ('Shop Death Wish Coffee — USDA Organic dark roast, cold brew, instant, and espresso. 132 products. Subscribe & Save 15%.') and /collections/sale will improve organic click-through rate from Google search results because both collection pages currently have empty meta descriptions. |
| Primary change | Add descriptive meta descriptions in Shopify for /collections/all and /collections/sale emphasizing key product categories and value propositions |
| Secondary change | Audit all other collection pages with empty meta descriptions (there may be several given the 40+ collections in the catalog) |
| Primary KPI | Organic CTR on collection-level pages (Google Search Console) |
| Decision rule | Measurable increase in CTR on targeted collection pages within 6 weeks |
| Expected lift | Medium |
| Confidence | High |

---

### EXP-10: Fix Alt Text on 12 Missing Product Images

| Field | Value |
|---|---|
| Pillar | Performance |
| Surface | Site-wide — product images |
| URL | https://deathwishcoffee.com/collections/all |
| Evidence | artifacts/deathwishcoffee_20260611_5362ac/technical_checks.json |
| Hypothesis | Adding descriptive alt text to the 12/170 product images currently missing it will improve image search indexing and accessibility compliance because 7% of product images are without alt text, and Google cannot interpret unlabelled coffee product images for image search. |
| Primary change | Add alt text to the 12 identified images in Shopify admin (Products → each image → alt text field) |
| Secondary change | Set a standard format: '[Product name] — [roast type/description] — Death Wish Coffee' |
| Primary KPI | Image search impressions (Google Search Console) |
| Decision rule | All 12 images have alt text within 1 week |
| Expected lift | Low |
| Confidence | High |

---

## Technical Checks

| Check | Status | Detail |
|---|---|---|
| SSL Certificate | Pass | HTTPS storefront loaded successfully. |
| HTTPS Redirect | Pass | HTTP redirected to HTTPS. |
| Sitemap | Warn | sitemap.xml returned status 429. |
| Robots.txt | Warn | robots.txt returned status 429. |
| Meta Tags & Social Previews | Pass | Title and meta description found. OG tags present. |
| Structured Data | Pass | JSON-LD found: Organization, WebSite. |
| Favicon | Pass | Favicon link tag found. |
| Cookie/Privacy | Warn | Privacy and Terms found but cookie consent policy not detected. |
| Broken Links | Warn | 1 non-critical broken links in 40 sampled. |
| Image Optimization | Warn | 12/170 images missing alt text (7%). Byte-level audit not run. |
| Mobile-Friendly | Warn | Desktop-only audit. Mobile viewport not tested. |
| Page Speed Mobile | Warn | No Lighthouse run performed. |
| Page Speed Desktop | Warn | No Lighthouse run performed. |
| Critical Pages Loading | Pass | 10/11 selected pages loaded successfully. |
| Checkout Reachable | Pass | Cart loaded and checkout entry reached. Journey stopped before payment entry. |
| Shopping Journey | Pass | Score 5.0/5 - no blockers detected. Payment: Visa, Mastercard, Amex, PayPal, Apple Pay, Shop Pay, Afterpay, Discover, JCB. |
| Payment Methods | Pass | Detected: Visa, Mastercard, Amex, PayPal, Apple Pay, Shop Pay, Afterpay, Discover, JCB. |

---

## Evidence Summary

**Conversion**
- Perfect 5.0/5 friction score — 3 clicks to checkout, trust badges, BNPL via Afterpay (`artifacts/deathwishcoffee_20260611_5362ac/pages/shopping_journey.json`)
- Cookie consent banner absent — GDPR/CCPA compliance gap (`artifacts/deathwishcoffee_20260611_5362ac/technical_checks.json`)
- Giveaway 'LIKE FREE SH*T?' as H1 on PDPs and collections displaces keyword-relevant headings (`artifacts/deathwishcoffee_20260611_5362ac/evidence_cards/collection_page_5_collections_all.json`)

**AOV**
- Bundle builder with 15% off prominently merchandised (`artifacts/deathwishcoffee_20260611_5362ac/pages/homepage_0_home.json`)
- Cart upsell not populating despite 'Featured collection' section existing (`artifacts/deathwishcoffee_20260611_5362ac/evidence_cards/cart_page_4_cart.json`)
- No coffee cross-sell on mug PDPs (`artifacts/deathwishcoffee_20260611_5362ac/evidence_cards/product_page_2_products_baba-yaga-mug.json`)

**Retention**
- Subscribe & Save and Society of Strong Coffee — mature subscription + loyalty ecosystem (`artifacts/deathwishcoffee_20260611_5362ac/pages/homepage_0_home.json`)
- Email capture with 20% off first order on cart, FAQ, blog, about — but not personalized for returning customers (`artifacts/deathwishcoffee_20260611_5362ac/evidence_cards/cart_page_4_cart.json`)

**Acquisition**
- Sitemap and robots.txt both 429 rate-limited — SEO crawl risk (`artifacts/deathwishcoffee_20260611_5362ac/technical_checks.json`)
- Collection pages missing meta descriptions (`artifacts/deathwishcoffee_20260611_5362ac/evidence_cards/collection_page_5_collections_all.json`)

**Performance**
- 12/170 images missing alt text (`artifacts/deathwishcoffee_20260611_5362ac/technical_checks.json`)
- Page speed unverified — Lighthouse not run (`artifacts/deathwishcoffee_20260611_5362ac/technical_checks.json`)
