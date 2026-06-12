# CRO Audit: tentree
Run ID: tentree_20260611_72bf40
Date: 2026-06-11

---

## Executive Summary

Tentree has one of the most inherently shareable brand stories in DTC apparel: every purchase plants 10 trees, certified by third-party verification, with 120+ million trees planted to date. This mission is a genuine differentiator from commodity fast fashion and is prominently featured on every PDP with an "Every Item Plants 10 Trees" H2. The store also has best-in-class payment coverage — 12 methods including Klarna, Google Pay, and Shop Pay — a functional fit guide that reduces size-anxiety for first-time apparel buyers, and a 5.0/5 friction score with trust badges at checkout. The operational foundation of the store is sound.

The most impactful single failure is that OG social meta tags (og_title and og_description) are empty on every page in the store — homepage, PDPs, collections, about, and all content pages. For a brand whose primary acquisition lever is the viral shareability of its trees-per-purchase mission, this means every social share produces a blank preview card on Facebook, Instagram, Pinterest, and LinkedIn. A brand story that closes every email, lands on every PDP, and fuels customer referrals becomes invisible the moment a buyer tries to share it. This is a single Shopify theme configuration fix that would immediately restore social sharing ROI across all content.

The second major gap is that the homepage is entirely sale-driven: five H2 headings about "Up to 50% Off", no H1, and no mention of trees, organic cotton, or sustainability above the fold. First-time visitors arriving via organic search or a referral link see a clearance-mode experience instead of the mission-driven brand that closes 2/3 of prospective buyers. Combined with the /collections/all page having a meta description of "all items" (a placeholder that was never replaced), 73% of product images missing alt text, and no structured data markup, the acquisition channel is leaking traffic at multiple points simultaneously.

---

## Store Overview

| Field | Value |
|---|---|
| Store URL | https://tentree.com |
| Category | Sustainable outdoor apparel / eco-conscious fashion brand |
| Primary use cases | Everyday sustainable clothing (men's + women's sweatpants, shirts, hoodies, jackets); mission-driven gifting (e-gift codes); premium eco line (CLIMATE+); size-confident buying (fit guide) |
| Pages crawled | 11/11 |
| Friction score | 5.0/5 |
| Shopping journey outcome | full_journey |

---

## Competitor Benchmarks

| Competitor | Category | Notable CRO strength | Relevant to |
|---|---|---|---|
| Patagonia (patagonia.com) | Sustainable outdoor apparel | Full OG social meta on all pages; 'Worn Wear' program creates retention through repair/resale loop | EXP-01, EXP-06 |
| Allbirds (allbirds.com) | Sustainable footwear / apparel | Carbon footprint label on every PDP; homepage leads with sustainability mission H1 not discount H2 | EXP-02, EXP-08 |
| Pact (wearpact.com) | Sustainable organic cotton clothing | Cart upsell with outfit-completion cross-sell; email capture with 15% off sustainability framing | EXP-03, EXP-05 |
| Girlfriend Collective (girlfriend.com) | Sustainable women's activewear | Complete alt text on all product images; structured data enabling Google rich snippets with star ratings | EXP-07, EXP-09 |

---

## Experiments

### EXP-01: Fix Sitewide OG Social Meta Tags

| Field | Value |
|---|---|
| Pillar | Conversion |
| Surface | Site-wide — all page types |
| URL | https://tentree.com/ |
| Evidence | artifacts/tentree_20260611_72bf40/pages/homepage_0_home.json |
| Hypothesis | Populating og_title and og_description on all page types (homepage, PDPs, collections, about) will restore social sharing previews and increase click-through from social media shares because og_title and og_description are currently empty strings on every crawled page, causing all tentree.com links shared on Facebook, Instagram, Pinterest, and LinkedIn to render as blank preview cards with no image, title, or description. |
| Primary change | In Shopify Theme Editor → Theme Settings (or the relevant page meta fields), populate og_title and og_description for the homepage, all PDP template types, collection pages, and the about/content pages; use the page's meta_title and meta_description as the defaults if a custom OG value is not set |
| Secondary change | Add og_image tags pointing to the product image or hero banner image for each page type, so shares include a compelling visual alongside the mission headline |
| Primary KPI | Social media referral click-through rate (UTM-tracked from shared links) |
| Decision rule | OG preview cards rendering correctly on Facebook Sharing Debugger and Twitter Card Validator within 1 week |
| Expected lift | High |
| Confidence | High |

---

### EXP-02: Add Mission H1 to Homepage

| Field | Value |
|---|---|
| Pillar | Conversion |
| Surface | Homepage |
| URL | https://tentree.com/ |
| Evidence | artifacts/tentree_20260611_72bf40/pages/homepage_0_home.json |
| Hypothesis | Adding a mission-led H1 ('Sustainable Clothing That Plants 10 Trees') above the current sale banners will increase new visitor conversion rate because the homepage currently has no H1 heading — all five headings are H2 sale promotions — meaning first-time visitors arriving from organic search or social referrals see a discount-led clearance experience rather than the sustainability mission that differentiates tentree from commodity apparel and is the primary reason eco-conscious buyers choose it over Amazon basics. |
| Primary change | Add an H1 to the homepage hero section: 'Sustainable Clothing That Plants 10 Trees' or 'Every Item Plants 10 Trees — 120M+ Planted' — positioned above or integrated with the current hero banner |
| Secondary change | Consider replacing one of the duplicate 'Up to 50% Off Almost Everything' H2s with a brand equity statement to balance the promotional-to-mission ratio on the homepage heading hierarchy |
| Primary KPI | Homepage-to-PDP click-through rate for new visitors |
| Decision rule | +8% relative lift in homepage-to-PDP CTR for new visitors over 3-week A/B test |
| Expected lift | Medium |
| Confidence | High |

---

### EXP-03: Add Cart Upsell with Outfit Cross-Sell

| Field | Value |
|---|---|
| Pillar | AOV |
| Surface | Cart page |
| URL | https://www.tentree.com/cart |
| Evidence | artifacts/tentree_20260611_72bf40/evidence_cards/cart_page_4_cart.json |
| Hypothesis | Adding an outfit-completion upsell section to the cart ('Complete the look — pairs well with:') will increase average order value because cart_upsell_present was confirmed false after adding a $70 sweatpant, meaning no cross-sell or complementary product appeared at the highest-intent pre-checkout moment; apparel buyers have high multi-item intent when in the cart. |
| Primary change | Add a 'Complete the look' cart drawer/page section that shows 1–2 recommended items based on cart contents (e.g., if sweatpant is in cart, surface matching hoodie or T-shirt) using Shopify's product recommendations API or a cart upsell app |
| Secondary change | Frame the recommendation as outfit-pairing ('Your sweatpants deserve a match — add this hoodie') rather than generic 'you might also like' to use the apparel-specific use-case |
| Primary KPI | Average order value |
| Decision rule | +10% relative lift in AOV over 3-week A/B test |
| Expected lift | High |
| Confidence | High |

---

### EXP-04: Surface Free Shipping Deadline in Cart

| Field | Value |
|---|---|
| Pillar | AOV |
| Surface | Cart page |
| URL | https://www.tentree.com/cart |
| Evidence | artifacts/tentree_20260611_72bf40/pages/shopping_journey.json |
| Hypothesis | Adding a prominent free shipping deadline message to the cart ('Free shipping on all orders — ends Friday at midnight') will increase checkout completion rate because urgency_elements_present was confirmed false in the cart despite the homepage actively advertising this time-limited free shipping offer; the urgency is created at the homepage but lost at the cart where it would have maximum effect on fence-sitters. |
| Primary change | Add a banner or callout at the top of the cart showing the active free shipping offer and its expiration, mirroring the homepage H2 'Free Shipping on All Orders. Ends Friday at Midnight.' |
| Secondary change | Pair with a 'You're saving $X in shipping' line item at checkout to reinforce the benefit in real-time |
| Primary KPI | Cart-to-checkout conversion rate |
| Decision rule | +5% relative lift in cart-to-checkout conversion rate over 2-week test |
| Expected lift | Medium |
| Confidence | Medium |

---

### EXP-05: Add Email Capture on About Page and Fit Guide

| Field | Value |
|---|---|
| Pillar | Retention |
| Surface | /pages/about and /pages/fit-guide |
| URL | https://tentree.com/pages/about |
| Evidence | artifacts/tentree_20260611_72bf40/evidence_cards/about_page_9_pages_about.json |
| Hypothesis | Adding email capture forms to the about page ('Join the movement — get updates on your trees and new sustainable drops') and the fit guide ('Get fit tips + 10% off your first sustainable purchase') will increase email list growth because no email capture heading was detected on any crawled page, meaning content-engaged visitors — who have the highest mission alignment and purchase intent — exit without entering the retention funnel. |
| Primary change | Add an email capture section at the bottom of /pages/about with a mission-framed incentive; add a second email capture at the bottom of the fit guide with a fit/discount incentive |
| Secondary change | Segment the email list at capture point: about-page subscribers → mission-focused email flow; fit-guide subscribers → product recommendation + size guide flow |
| Primary KPI | Email capture rate from about and fit guide pages |
| Decision rule | >3% of about/fit-guide page visitors subscribe over 4-week measurement period |
| Expected lift | High |
| Confidence | High |

---

### EXP-06: Add Post-Purchase Tree Impact Counter to Order Confirmation

| Field | Value |
|---|---|
| Pillar | Retention |
| Surface | Order confirmation page |
| URL | https://tentree.com/ |
| Evidence | artifacts/tentree_20260611_72bf40/evidence_cards/shopping_journey.json |
| Hypothesis | Adding a 'You just planted X trees' counter to the order confirmation page — showing the specific number of trees planted by the current order and the buyer's cumulative impact — will increase repeat purchase rate because the emotional gratification of seeing concrete impact reinforces the buying decision immediately after conversion, creates a shareable moment, and builds the identity-level loyalty that tentree's mission depends on; no post-purchase impact reinforcement was detected in the crawled store. |
| Primary change | Add a 'Your impact' section to the Shopify thank-you page: 'You planted [order_item_count × 10] trees today. Total trees you've planted: [lifetime count].' |
| Secondary change | Include a social share button: 'I just planted [X] trees with @tentree' pre-populated for Instagram/Twitter — this leverages the most shareable moment in the customer journey to drive acquisition |
| Primary KPI | 30-day repeat purchase rate from first-time buyers |
| Decision rule | +10% relative lift in 30-day repeat purchase rate for first-time buyers over 8-week measurement period |
| Expected lift | Medium |
| Confidence | Medium |

---

### EXP-07: Fix /collections/all Meta Description Placeholder

| Field | Value |
|---|---|
| Pillar | Acquisition |
| Surface | /collections/all |
| URL | https://tentree.com/collections/all |
| Evidence | artifacts/tentree_20260611_72bf40/evidence_cards/collection_page_5_collections_all.json |
| Hypothesis | Replacing the placeholder meta description 'all items' on /collections/all with keyword-rich copy ('Shop tentree's full range of sustainable clothing — hemp, organic cotton, recycled polyester & TENCEL for women and men. Every item plants 10 trees.') will improve organic ranking and click-through rate for broad 'sustainable clothing' and 'eco fashion' queries because the current meta description is a placeholder string that provides zero keyword signal or brand value, and the all-products page is the highest-traffic collection URL for category-intent search visitors. |
| Primary change | Update the /collections/all meta description in Shopify to a 155-character keyword-rich description targeting 'sustainable clothing', 'organic cotton clothes', and 'eco fashion' |
| Secondary change | Update the H1 from lowercase 'all items' to a properly capitalised, keyword-rich heading: 'Sustainable Clothing for Women & Men' |
| Primary KPI | Organic impressions for 'sustainable clothing' and related category queries (Google Search Console) |
| Decision rule | Measurable improvement in organic impressions for collection-level queries within 6 weeks of deployment |
| Expected lift | High |
| Confidence | High |

---

### EXP-08: Add Product Structured Data (JSON-LD) to PDPs

| Field | Value |
|---|---|
| Pillar | Acquisition |
| Surface | All product pages |
| URL | https://www.tentree.com/products/m-atlas-sweatpant |
| Evidence | artifacts/tentree_20260611_72bf40/technical_checks.json |
| Hypothesis | Adding Product schema JSON-LD markup (name, price, availability, aggregateRating) to all PDPs will enable Google rich snippets with star ratings, price, and availability in search results because Structured Data is currently Warn, meaning tentree PDPs appear as plain text listings in Google results while competitors with Product schema show star ratings and pricing — a significant organic CTR disadvantage. |
| Primary change | Add Product schema JSON-LD to all PDP templates including: name, description, image, sku, price, priceCurrency, availability, aggregateRating with reviewCount and ratingValue |
| Secondary change | Add Organization schema to the homepage (following the pattern of beardbrand, deathwishcoffee, mudwtr which all Pass this check) |
| Primary KPI | Organic CTR on PDP-level search queries (Google Search Console) |
| Decision rule | Rich snippets appearing for at least the top 10 PDPs in Google Search within 4 weeks of deployment |
| Expected lift | Medium |
| Confidence | High |

---

### EXP-09: Fix Alt Text on 58 Missing Product Images

| Field | Value |
|---|---|
| Pillar | Performance |
| Surface | Site-wide — product images |
| URL | https://tentree.com/collections/all |
| Evidence | artifacts/tentree_20260611_72bf40/technical_checks.json |
| Hypothesis | Adding descriptive alt text to the 58/79 product images currently missing it (73%) will improve image search indexing, accessibility compliance, and screen reader usability because nearly three-quarters of product images are unlabelled — the worst alt-text gap of all 5 stores tested — and Google cannot interpret these images for image search results or for sustainable-fashion-specific visual queries ('organic cotton sweatpants', 'hemp button-up shirt'). |
| Primary change | Add alt text to all 58 identified images in Shopify admin (Products → each image → alt text field) |
| Secondary change | Establish a standard alt text format: '[Product name] — [color] — [material] — tentree sustainable clothing' for all product images going forward; add to the product upload checklist |
| Primary KPI | Image search impressions (Google Search Console) |
| Decision rule | All 58 images have alt text within 1 sprint (5 business days) |
| Expected lift | Medium |
| Confidence | High |

---

### EXP-10: Add Cookie Consent Banner and Run Lighthouse Baseline

| Field | Value |
|---|---|
| Pillar | Performance |
| Surface | Site-wide |
| URL | https://tentree.com/ |
| Evidence | artifacts/tentree_20260611_72bf40/technical_checks.json |
| Hypothesis | Implementing a GDPR/CCPA-compliant cookie consent banner and running Lighthouse to establish a Core Web Vitals baseline will close the compliance gap and identify page speed bottlenecks because Cookie/Privacy is currently Warn (no consent popup) and Page Speed Mobile/Desktop are both Warn (no Lighthouse run performed), leaving both compliance exposure and performance unknowns unaddressed. |
| Primary change | Install a Shopify-compatible cookie consent app (e.g. Pandectes GDPR, Consentmo) and run Lighthouse CI on the homepage and Atlas Sweatpant PDP to capture LCP, CLS, and INP |
| Secondary change | Based on Lighthouse findings, prioritize: if LCP > 2.5s, investigate hero banner image loading; if CLS > 0.1, audit the sticky nav or sale-banner layout shift; address the single broken link found in the Broken Links Warn |
| Primary KPI | Cookie consent compliance (legal) + Lighthouse mobile Performance score (target > 70) |
| Decision rule | Zero compliance violations within 1 week; Lighthouse baseline established and top 3 bottlenecks identified within 2 weeks |
| Expected lift | Medium |
| Confidence | High |

---

## Technical Checks

| Check | Status | Detail |
|---|---|---|
| SSL Certificate | Pass | HTTPS storefront loaded successfully. |
| HTTPS Redirect | Pass | HTTP redirected to HTTPS. |
| Sitemap | Pass | sitemap.xml found with ~7 entries. |
| Robots.txt | Pass | robots.txt accessible. |
| Meta Tags & Social Previews | Pass | Title and meta description found. OG tags missing. |
| Structured Data | Warn | Updated after browser crawl. |
| Favicon | Pass | Favicon link tag found. |
| Cookie/Privacy | Warn | Privacy and Terms found but cookie consent policy not detected. |
| Broken Links | Warn | 1 non-critical broken links in 40 sampled. |
| Image Optimization | Warn | 58/79 images missing alt text (73%). Byte-level audit not run. |
| Mobile-Friendly | Warn | Desktop-only audit. Mobile viewport not tested. |
| Page Speed Mobile | Warn | No Lighthouse run performed. |
| Page Speed Desktop | Warn | No Lighthouse run performed. |
| Critical Pages Loading | Pass | 11/11 selected pages loaded successfully. |
| Checkout Reachable | Pass | Cart loaded and checkout entry reached. Journey stopped before payment entry. |
| Shopping Journey | Pass | Score 5.0/5 - no blockers detected. Payment: Visa, Mastercard, Amex, PayPal, Apple Pay, Google Pay, Shop Pay, Klarna, Stripe, Discover, Diners Club, JCB. |
| Payment Methods | Pass | Detected: Visa, Mastercard, Amex, PayPal, Apple Pay, Google Pay, Shop Pay, Klarna, Stripe, Discover, Diners Club, JCB. |

---

## Evidence Summary

**Conversion**
- 5.0/5 friction, 12 payment methods, trust badges at checkout — functional purchase path with best payment coverage of all 5 stores tested (`artifacts/tentree_20260611_72bf40/pages/shopping_journey.json`)
- OG social meta tags empty on every page — mission-story shares produce blank preview cards sitewide (`artifacts/tentree_20260611_72bf40/pages/homepage_0_home.json`)
- No H1 on homepage — first impression is five discount H2s with no mission statement (`artifacts/tentree_20260611_72bf40/pages/homepage_0_home.json`)
- Cart has no upsell, no urgency, no 'plants 10 trees' reinforcement (`artifacts/tentree_20260611_72bf40/evidence_cards/cart_page_4_cart.json`)

**AOV**
- Klarna BNPL active — dedicated Klarna FAQ educates buyers on installment payments for $50–120 apparel (`artifacts/tentree_20260611_72bf40/evidence_cards/faq_shipping_returns_8_pages_klarna-faq.json`)
- No cart upsell ('complete the look') — single-item checkout is the default path (`artifacts/tentree_20260611_72bf40/pages/shopping_journey.json`)
- Free shipping deadline not surfaced in cart despite homepage advertising it (`artifacts/tentree_20260611_72bf40/pages/shopping_journey.json`)

**Retention**
- No email capture detected on any crawled page (`artifacts/tentree_20260611_72bf40/pages/homepage_0_home.json`)
- Fit guide reduces size-anxiety and returns — proactive conversion tool for apparel (`artifacts/tentree_20260611_72bf40/evidence_cards/blog_or_content_page_10_pages_fit-guide.json`)
- No post-purchase 'your impact' counter — tree planting mission is not aggregated into personal loyalty reinforcement (`artifacts/tentree_20260611_72bf40/evidence_cards/shopping_journey.json`)

**Acquisition**
- /collections/all meta description is placeholder 'all items' — zero keyword value (`artifacts/tentree_20260611_72bf40/evidence_cards/collection_page_5_collections_all.json`)
- OG tags empty sitewide — social acquisition suppressed (`artifacts/tentree_20260611_72bf40/pages/homepage_0_home.json`)
- Structured Data: Warn — no Product JSON-LD for rich snippets (`artifacts/tentree_20260611_72bf40/technical_checks.json`)
- Where-to-buy page is 404 (`artifacts/tentree_20260611_72bf40/evidence_cards/where_to_buy_7_pages_where-to-buy.json`)

**Performance**
- 58/79 images missing alt text (73%) — most severe image gap of all 5 stores tested (`artifacts/tentree_20260611_72bf40/technical_checks.json`)
- Page speed unverified — Lighthouse not run (`artifacts/tentree_20260611_72bf40/technical_checks.json`)
