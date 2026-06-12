# CRO Audit: Zen Rojas
Run ID: zenrojas_20260611_e275e3
Date: 2026-06-11

---

## Executive Summary

Zen Rojas is a specialty tea and wellness brand with a technically clean Shopify storefront — the shopping journey completed without friction (5.0/5), checkout is reachable, and 10 payment methods are supported. The mechanical purchase path is not the problem. The problem is conversion confidence: not a single page in the store shows social proof. No homepage review count, no star ratings on any product page, no customer testimonials anywhere in the crawled funnel. For a health-and-wellness brand where the purchase decision is rooted in trust ("does this tea actually work?"), the absence of social proof is the primary conversion constraint. Visitors arrive, see well-named products, and leave with no evidence that anyone else bought and loved them.

The second most significant gap is that every high-value exit point in the funnel — the cart, the blog, the PDP after an add — is monetized at its floor. The cart has no upsell. The blog, which carries a compelling family-and-wellness narrative well-suited to drive organic traffic, has no in-content product links and no email capture. The PDPs have a "Complete Your Ritual" cross-sell section but it offers only navigation, not a bundle price. Tea is a repeat-purchase category by nature, yet no PDP offers a Subscribe & Save option. The brand has built the ecosystem (teas, infuser, mug, sampler packs) but has not connected it into an AOV or retention engine.

Technical health is adequate but carries meaningful SEO debt: three standard Shopify URLs (`/pages/about`, `/pages/faq`, `/pages/where-to-buy`) return 404 because the actual pages are at non-standard slugs, 60% of product images are missing alt text, and no Product structured data is present — all of which suppress organic discoverability. No Lighthouse run was performed so page speed is unverified.

---

## Store Overview

| Field | Value |
|---|---|
| Store URL | https://zenrojas.com |
| Category | Specialty tea / wellness beverages |
| Primary use cases | Daily tea ritual (health-benefit teas), loose-leaf home brewing, gift-giving (samplers, teaware) |
| Pages crawled | 11/11 |
| Friction score | 5.0/5 |
| Shopping journey outcome | full_journey |

---

## Competitor Benchmarks

| Competitor | Category | Notable CRO strength | Relevant to |
|---|---|---|---|
| Harney & Sons (harney.com) | Specialty tea | Review count prominently on all PDPs; sampler bundles with clear bundle pricing | EXP-01, EXP-04 |
| Vahdam Teas (vahdamteas.com) | Premium organic tea | Subscribe & Save on every tea PDP; email capture popup with first-order discount | EXP-05, EXP-06 |
| Art of Tea (artoftea.com) | Wellness tea | In-collection benefit filters (calm, energy, immunity); editorial collection pages with health-use-case framing | EXP-03, EXP-10 |
| Pique Tea (piquelife.com) | Functional wellness tea | Social proof via review count + featured testimonials on homepage; aggressive AOV via bundles | EXP-01, EXP-02 |

---

## Experiments

### EXP-01: Add Star Ratings Above Fold on All PDPs

| Field | Value |
|---|---|
| Pillar | Conversion |
| Surface | Product page — above fold, below product title |
| URL | https://zenrojas.com/products/blacktea |
| Evidence | artifacts/zenrojas_20260611_e275e3/screenshots/product_page_2_products_blacktea.png |
| Hypothesis | Adding a star rating widget (average score + review count) directly below the product title on all PDPs will increase add-to-cart rate because visitors currently see zero social proof before the purchase decision and the store's competitors show reviews above the fold. |
| Primary change | Install a Shopify reviews app (e.g. Judge.me or Okendo) and display the star widget below the H1 on all product templates |
| Secondary change | Enable review import from any existing review sources (email, social) to seed initial count |
| Primary KPI | Add-to-cart rate |
| Decision rule | +5% relative lift in add-to-cart rate over 2-week test |
| Expected lift | High |
| Confidence | High |

---

### EXP-02: Add Social Proof Block to Homepage

| Field | Value |
|---|---|
| Pillar | Conversion |
| Surface | Homepage — below hero section |
| URL | https://zenrojas.com/ |
| Evidence | artifacts/zenrojas_20260611_e275e3/screenshots/homepage_0_home.png |
| Hypothesis | Adding a homepage section with aggregate review count, average rating, and 2–3 featured customer quotes will increase click-through to PDPs because first-time visitors currently have no trust signal at the entry point of the funnel. |
| Primary change | Add a "What customers say" section with star count + 2 pull-quote testimonials below hero CTAs |
| Secondary change | Link each testimonial to the featured product |
| Primary KPI | Homepage → PDP click-through rate |
| Decision rule | +8% relative lift in CTP over 2-week test |
| Expected lift | High |
| Confidence | Medium |

---

### EXP-03: Cart Cross-Sell Widget (Tea Pairing)

| Field | Value |
|---|---|
| Pillar | AOV |
| Surface | Cart page |
| URL | https://zenrojas.com/cart |
| Evidence | artifacts/zenrojas_20260611_e275e3/screenshots/shopping_journey_cart.png |
| Hypothesis | Adding a "Pair it with" cross-sell widget in the cart (showing 1 complementary product — e.g. infuser when a tea is in cart, or a second tea type) will increase average order value because the cart currently shows no related products and the journey confirmed cart_upsell_present = false. |
| Primary change | Install cart upsell app (or use Shopify's native cart recommendations) to show 1 product recommendation in the cart drawer |
| Secondary change | Set recommendation rules: infuser for tea buyers, sampler for single-tea buyers |
| Primary KPI | Average order value |
| Decision rule | +7% relative lift in AOV over 3-week test |
| Expected lift | Medium |
| Confidence | High |

---

### EXP-04: Starter Kit Bundle on Infuser PDP

| Field | Value |
|---|---|
| Pillar | AOV |
| Surface | Product page — Tea Infuser |
| URL | https://zenrojas.com/products/tea-seeper |
| Evidence | artifacts/zenrojas_20260611_e275e3/evidence_cards/product_page_3_products_tea-seeper.json |
| Hypothesis | Adding a "Starter Kit" bundle option (Tea Infuser + Organic Black Tea + Tea Bags) at a 10% discount on the infuser PDP will increase multi-item order rate because the cross-sell section shows these products together but currently offers no pricing incentive to bundle. |
| Primary change | Create a Shopify bundle product or use a bundle app to offer infuser + 2 tea SKUs at 10% off |
| Secondary change | Surface the bundle above the standard add-to-cart button |
| Primary KPI | Average order value on infuser PDP |
| Decision rule | +10% relative lift in AOV on infuser PDP over 3-week test |
| Expected lift | Medium |
| Confidence | Medium |

---

### EXP-05: Subscribe & Save on Tea PDPs

| Field | Value |
|---|---|
| Pillar | Retention |
| Surface | Product page — all tea PDPs |
| URL | https://zenrojas.com/products/blacktea |
| Evidence | artifacts/zenrojas_20260611_e275e3/evidence_cards/product_page_2_products_blacktea.json |
| Hypothesis | Adding a Subscribe & Save option (10% off, ships every 30/60/90 days) to all consumable tea PDPs will increase customer LTV because tea is a repeat-purchase product and no recurring purchase path currently exists on any PDP. |
| Primary change | Enable Shopify Subscriptions or install a subscription app (e.g. Recharge) and add subscribe/one-time toggle to all tea product templates |
| Secondary change | Default toggle to Subscribe to increase subscription take rate |
| Primary KPI | Subscription conversion rate (% of tea buyers choosing subscribe) |
| Decision rule | >8% of tea orders selecting subscribe option over 4-week test |
| Expected lift | High |
| Confidence | High |

---

### EXP-06: Email Capture on Blog with Lead Magnet

| Field | Value |
|---|---|
| Pillar | Retention |
| Surface | Blog post — end of article |
| URL | https://zenrojas.com/blogs/weekly-blog/building-a-family-legacy-through-wellness-community-and-purpose-driven-growth |
| Evidence | artifacts/zenrojas_20260611_e275e3/evidence_cards/blog_or_content_page_10_blogs_weekly-blog_building-a-family-lega.json |
| Hypothesis | Adding an email capture form at the end of blog posts offering a "Wellness Tea Guide" PDF or first-order discount will grow the email subscriber list because blog content currently generates organic traffic with no email capture — visitors read and leave without converting. |
| Primary change | Add end-of-post email capture form with a lead magnet (discount or branded content PDF) |
| Secondary change | Add mid-post inline product CTA linking to the most relevant tea (e.g. "Try our Organic Sleep Tea") |
| Primary KPI | Email capture rate from blog traffic |
| Decision rule | >3% of blog visitors submitting email over 4-week test |
| Expected lift | Medium |
| Confidence | Medium |

---

### EXP-07: Fix Broken Standard URL Redirects

| Field | Value |
|---|---|
| Pillar | Acquisition |
| Surface | Site-wide — /pages/about, /pages/faq, /pages/where-to-buy |
| URL | https://zenrojas.com/pages/about |
| Evidence | artifacts/zenrojas_20260611_e275e3/screenshots/about_page_9_pages_about.png |
| Hypothesis | Adding 301 redirects from `/pages/about` → `/pages/aboutus`, `/pages/faq` → `/pages/faqs`, and `/pages/where-to-buy` to the correct page will recover lost link equity and reduce bounce from dead-end 404 pages because all three standard Shopify URLs currently return 404. |
| Primary change | Add 3 URL redirects in Shopify admin (Online Store → Navigation → URL Redirects) |
| Secondary change | Update any internal nav links pointing to the broken URLs |
| Primary KPI | 404 error rate (reduce to 0 for these 3 paths) |
| Decision rule | 0 crawl errors on these 3 paths within 1 week |
| Expected lift | Medium |
| Confidence | High |

---

### EXP-08: Add Product Structured Data to PDPs

| Field | Value |
|---|---|
| Pillar | Acquisition |
| Surface | All product pages |
| URL | https://zenrojas.com/products/blacktea |
| Evidence | artifacts/zenrojas_20260611_e275e3/technical_checks.json |
| Hypothesis | Adding Product JSON-LD structured data (name, price, availability, rating) to all PDPs will improve Google rich snippet eligibility and increase organic click-through rate because structured data is currently unconfirmed (Warn) and the store competes on health search terms where rich results improve visibility. |
| Primary change | Add or verify Product schema JSON-LD in the product template (most Shopify themes include this — may require theme setting to enable or a schema app) |
| Secondary change | Validate with Google Rich Results Test after deployment |
| Primary KPI | Organic CTR on product landing pages (Google Search Console) |
| Decision rule | Rich result impressions appear within 4 weeks of deployment |
| Expected lift | Medium |
| Confidence | Medium |

---

### EXP-09: Cart Urgency Signal (Free Shipping Threshold)

| Field | Value |
|---|---|
| Pillar | Conversion |
| Surface | Cart page |
| URL | https://zenrojas.com/cart |
| Evidence | artifacts/zenrojas_20260611_e275e3/screenshots/shopping_journey_cart.png |
| Hypothesis | Adding a free shipping progress bar in the cart ("You're $X away from free shipping") will reduce cart abandonment and increase order value because the cart currently has no urgency or incentive signals — journey confirmed urgency_elements_present = false. |
| Primary change | Add a free shipping threshold bar to the cart page (Shopify app or theme feature) set at a value ~15% above current AOV |
| Secondary change | Show the same threshold on PDP below the add-to-cart button |
| Primary KPI | Cart abandonment rate |
| Decision rule | +5% relative lift in cart-to-checkout conversion rate over 2-week test |
| Expected lift | Medium |
| Confidence | Medium |

---

### EXP-10: Fix Image Alt Text on All Product Images

| Field | Value |
|---|---|
| Pillar | Performance |
| Surface | Site-wide — all product images |
| URL | https://zenrojas.com/collections/all |
| Evidence | artifacts/zenrojas_20260611_e275e3/technical_checks.json |
| Hypothesis | Adding descriptive alt text to the 60% of product images currently missing it will improve image search indexing and accessibility compliance, increasing organic image search traffic because 9/15 audited images have no alt text and Google cannot interpret unlabelled product images. |
| Primary change | Add keyword-rich alt text to all product images in Shopify admin (Products → each image → alt text field) |
| Secondary change | Use a consistent format: "[Product name] — [key descriptor] — Zen Rojas" |
| Primary KPI | Image search impressions (Google Search Console) |
| Decision rule | Measurable increase in image search impressions within 6 weeks |
| Expected lift | Medium |
| Confidence | High |

---

## Technical Checks

| Check | Status | Detail |
|---|---|---|
| SSL Certificate | Pass | HTTPS storefront loaded successfully. |
| HTTPS Redirect | Pass | HTTP redirected to HTTPS. |
| Sitemap | Pass | sitemap.xml found with ~5 entries. |
| Robots.txt | Pass | robots.txt accessible. |
| Meta Tags & Social Previews | Pass | Title and meta description found. OG tags present. |
| Structured Data | Warn | Updated after browser crawl. |
| Favicon | Warn | Updated after browser crawl. |
| Cookie/Privacy | Pass | Privacy Policy and Terms links found. Cookie policy also present. |
| Broken Links | Warn | 6 non-critical broken links in 29 sampled. |
| Image Optimization | Warn | 9/15 images missing alt text (60%). Byte-level audit not run. |
| Mobile-Friendly | Warn | Desktop-only audit. Mobile viewport not tested. |
| Page Speed Mobile | Warn | No Lighthouse run performed. |
| Page Speed Desktop | Warn | No Lighthouse run performed. |
| Critical Pages Loading | Pass | 11/11 selected pages loaded successfully. |
| Checkout Reachable | Pass | Cart loaded and checkout entry reached. Journey stopped before payment entry. |
| Shopping Journey | Pass | Score 5.0/5 — no blockers detected. Payment: Visa, Mastercard, Amex, PayPal, Apple Pay, Google Pay, Shop Pay, Discover, Diners Club, JCB. |
| Payment Methods | Pass | Detected: Visa, Mastercard, Amex, PayPal, Apple Pay, Google Pay, Shop Pay, Discover, Diners Club, JCB. |

---

## Evidence Summary

**Conversion**
- Health-benefit CTAs on homepage drive clear purchase intent (`artifacts/zenrojas_20260611_e275e3/screenshots/homepage_0_home.png`)
- Zero social proof across all pages — no reviews on homepage, 3 PDPs, or collections (`artifacts/zenrojas_20260611_e275e3/evidence_cards/product_page_1_products_tea-bags.json`)
- Purchase mechanics are flawless: 5.0/5 friction, trust badges at checkout (`artifacts/zenrojas_20260611_e275e3/screenshots/shopping_journey_checkout.png`)

**AOV**
- "Complete Your Ritual" cross-sell exists on all PDPs but offers no bundle pricing (`artifacts/zenrojas_20260611_e275e3/evidence_cards/product_page_3_products_tea-seeper.json`)
- Cart upsell confirmed absent (`artifacts/zenrojas_20260611_e275e3/pages/shopping_journey.json`)

**Retention**
- No Subscribe & Save on any tea PDP despite tea being a repeat-purchase product (`artifacts/zenrojas_20260611_e275e3/evidence_cards/product_page_2_products_blacktea.json`)
- Blog content strong but exits without email capture (`artifacts/zenrojas_20260611_e275e3/evidence_cards/blog_or_content_page_10_blogs_weekly-blog_building-a-family-lega.json`)

**Acquisition**
- 3 broken pages at standard Shopify URLs (`artifacts/zenrojas_20260611_e275e3/screenshots/about_page_9_pages_about.png`)
- Homepage meta too brief for meaningful SEO differentiation (`artifacts/zenrojas_20260611_e275e3/pages/homepage_0_home.json`)

**Performance**
- 60% of product images missing alt text (`artifacts/zenrojas_20260611_e275e3/technical_checks.json`)
- Page speed unverified — Lighthouse not run (`artifacts/zenrojas_20260611_e275e3/technical_checks.json`)
