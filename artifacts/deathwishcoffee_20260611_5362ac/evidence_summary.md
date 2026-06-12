# Evidence Summary — deathwishcoffee_20260611_5362ac

## 1. Store Identity

```
store_category: bold/dark roast specialty coffee / subscription coffee brand
primary_use_cases:
  - daily coffee ritual via subscription (ground, whole bean, pods, cold brew, espresso capsules, instant)
  - gift-giving (gift cards, limited-edition mugs, coffee bundles)
  - coffee lifestyle / collector (limited-edition drinkware, branded apparel, Society of Strong Coffee membership)
main_diagnosis: Death Wish Coffee has a best-in-class DTC purchase path (5.0/5 friction, 3 clicks to checkout, trust badges, BNPL via Afterpay) and a mature subscription + bundle infrastructure. The primary conversion gaps are operational: cart upsell fails to populate, a cookie consent policy is absent creating GDPR/CCPA compliance risk, and the 3 PDPs sampled were all non-coffee products — meaning Subscribe & Save behavior on the core coffee SKUs was not verified.
```

---

## 2. Findings by Pillar

### Conversion
- Perfect shopping journey: 5.0/5 friction, 3 clicks PDP → checkout, trust badges confirmed, 9 payment methods including Afterpay (`artifacts/deathwishcoffee_20260611_5362ac/pages/shopping_journey.json`)
- 'WIN FREE COFFEE FOR A YEAR' giveaway CTA sitewide — purchase-entry mechanic drives urgency (`artifacts/deathwishcoffee_20260611_5362ac/pages/homepage_0_home.json`)
- '20% OFF FIRST ORDER' email capture on cart, FAQ, blog, and about pages — email acquisition touchpoints across entire funnel (`artifacts/deathwishcoffee_20260611_5362ac/pages/cart_page_4_cart.json`)
- Reviews on all 3 sampled PDPs (gift card + 2 mugs) — review infrastructure confirmed store-wide (`artifacts/deathwishcoffee_20260611_5362ac/pages/product_page_2_products_baba-yaga-mug.json`)
- **Cookie/Privacy: Warn** — privacy and terms found but no cookie consent popup detected — GDPR/CCPA compliance gap (`artifacts/deathwishcoffee_20260611_5362ac/technical_checks.json`)
- No H1 on homepage; 'LIKE FREE SH*T?' promotional section overrides H1 on PDPs and collection pages — weakens SEO keyword signals (`artifacts/deathwishcoffee_20260611_5362ac/pages/homepage_0_home.json`)

### AOV
- 'Build Your Own Bundle' with 'Save Up to 15% Off' linked from homepage and all pages — bundle builder actively merchandised (`artifacts/deathwishcoffee_20260611_5362ac/pages/homepage_0_home.json`)
- Subscribe & Save prominently in nav with 'Subscription Perks' page — subscription infrastructure is mature and visible (`artifacts/deathwishcoffee_20260611_5362ac/pages/homepage_0_home.json`)
- Cart has 'Featured collection' section suggesting product recommendations — but journey confirms cart_upsell_present: false (`artifacts/deathwishcoffee_20260611_5362ac/pages/cart_page_4_cart.json`)
- No coffee cross-sell on mug PDPs — natural pairing (mug + coffee) not surfaced (`artifacts/deathwishcoffee_20260611_5362ac/evidence_cards/product_page_2_products_baba-yaga-mug.json`)
- No urgency in cart (no free shipping threshold bar) — zero AOV lift incentive at cart stage (`artifacts/deathwishcoffee_20260611_5362ac/pages/shopping_journey.json`)

### Retention
- Subscribe & Save collection exists (/collections/subscribe-save) and Society of Strong Coffee exclusives — tiered loyalty ecosystem in place (`artifacts/deathwishcoffee_20260611_5362ac/pages/homepage_0_home.json`)
- '20% OFF FIRST ORDER' email capture on 4+ pages — email list building integrated throughout funnel (`artifacts/deathwishcoffee_20260611_5362ac/pages/faq_shipping_returns_8_pages_help.json`)
- Email capture offer ('20% OFF YOUR FIRST ORDER') in cart is shown to all visitors including returning customers — personalization gap (`artifacts/deathwishcoffee_20260611_5362ac/evidence_cards/cart_page_4_cart.json`)

### Acquisition
- Structured Data: Pass (Organization, WebSite JSON-LD found) — technical SEO above baseline (`artifacts/deathwishcoffee_20260611_5362ac/technical_checks.json`)
- Blog has strong educational content ('How to Make Adaptogenic Coffee', 'What Is Instant Coffee') targeting coffee-intent queries (`artifacts/deathwishcoffee_20260611_5362ac/pages/blog_or_content_page_10_blogs_news.json`)
- About page at standard /pages/about works correctly — no broken standard URL (`artifacts/deathwishcoffee_20260611_5362ac/pages/about_page_9_pages_about.json`)
- **Sitemap: Warn** — sitemap.xml returned 429 rate limit; Googlebot may be rate-limited when crawling (`artifacts/deathwishcoffee_20260611_5362ac/technical_checks.json`)
- **Robots.txt: Warn** — robots.txt returned 429 rate limit (`artifacts/deathwishcoffee_20260611_5362ac/technical_checks.json`)
- Collection and sale page meta descriptions are empty — missing SEO opportunity for collection-level queries (`artifacts/deathwishcoffee_20260611_5362ac/pages/collection_page_5_collections_all.json`)
- Where-to-buy page failed to load during crawl — status unknown (`artifacts/deathwishcoffee_20260611_5362ac/technical_checks.json`)

### Performance
- Image Optimization: Warn — 12/170 images missing alt text (7%) (`artifacts/deathwishcoffee_20260611_5362ac/technical_checks.json`)
- Page Speed Mobile/Desktop: Warn — no Lighthouse run performed (`artifacts/deathwishcoffee_20260611_5362ac/technical_checks.json`)
- Mobile-Friendly: Warn — desktop-only audit (`artifacts/deathwishcoffee_20260611_5362ac/technical_checks.json`)
- Cookie/Privacy: Warn — GDPR/CCPA compliance exposure (`artifacts/deathwishcoffee_20260611_5362ac/technical_checks.json`)

---

## 3. Cross-Page Patterns

**Pattern 1 — Subscription and bundle infrastructure fully built but upsell didn't activate in cart**
Subscribe & Save, Build Your Own Bundle, Featured collection in cart — all three AOV/retention mechanisms exist. But the journey confirms cart_upsell_present: false. The "Featured collection" section in cart did not populate. This is likely a cart-empty state issue — the most important test is whether upsell fires with coffee in the cart.
Evidence: `artifacts/deathwishcoffee_20260611_5362ac/pages/shopping_journey.json`, `cart_page_4_cart.json`

**Pattern 2 — Email capture sitewide but not personalized for returning customers**
'STAY BOLD, STAY CAFFEINATED. SIGN UP AND SAVE 20% OFF YOUR FIRST ORDER' appears on cart, FAQ, blog, and about pages. This offer is shown to all visitors including existing subscribers and repeat buyers. Personalization to show a different offer (loyalty discount, subscription upgrade) to logged-in returning customers is a retention improvement.
Evidence: `artifacts/deathwishcoffee_20260611_5362ac/pages/cart_page_4_cart.json`, `faq_shipping_returns_8_pages_help.json`, `blog_or_content_page_10_blogs_news.json`

**Pattern 3 — Promotional H1 overrides product/collection headings on key SEO pages**
'LIKE FREE SH*T?' appears as H1 on collection/all, collection/sale, and PDPs (mugs). This overrides natural keyword-relevant H1s. While the giveaway drives engagement, the SEO cost is weakened H1 keyword signal on pages that should rank for coffee product queries.
Evidence: `artifacts/deathwishcoffee_20260611_5362ac/pages/collection_page_5_collections_all.json`, `product_page_2_products_baba-yaga-mug.json`

---

## 4. Purchase Path Constraints

Shopping journey outcome: **full_journey**, friction score **5.0/5** — the best possible score. No friction flags. 3 clicks PDP to checkout. Trust badges present. Afterpay for BNPL buyers. This is best-in-class for any DTC Shopify store.

The constraints are operational (cart upsell not firing, cookie consent absent) not mechanical. Core coffee PDPs weren't sampled — Subscribe & Save toggle behavior on the primary revenue SKUs is the key unverified assumption.

---

## 5. Content Commercialization Opportunities

Blog has strong educational content that targets high-intent searches ('how to make adaptogenic coffee', 'what is instant coffee'). Adding:
1. In-post product CTAs: "Try our Instant Coffee → [link]" in the instant coffee article
2. In-post subscription CTA: "Subscribe & Save 15% on this roast" in each brew guide
3. Personalized email capture (non-subscribers: 20% off; subscribers: exclusive society offer)

---

## 6. Candidate Experiments

| # | Pillar | Hypothesis | Impact |
|---|---|---|---|
| 1 | Conversion | Implementing a cookie consent banner will close the GDPR/CCPA compliance gap and restore visitor trust signals | High |
| 2 | Conversion | Adding an H1 heading to the homepage ('The World's Strongest Coffee') will strengthen organic keyword ranking for core coffee queries | Medium |
| 3 | AOV | Activating cart 'Featured collection' recommendations with coffee in cart will surface subscription upsell at the highest-intent moment | High |
| 4 | AOV | Adding coffee cross-sell to mug PDPs ('Complete the ritual: add your coffee') will increase multi-product order rate | Medium |
| 5 | AOV | Adding a free shipping threshold bar to the cart will increase order value by incentivizing add-on products | Medium |
| 6 | Retention | Personalizing the cart email capture ('20% off first order' for new visitors, loyalty offer for returning) will improve both email capture rate and retention | Medium |
| 7 | Retention | Adding Subscribe & Save CTA to about page after the ethical sourcing story will convert brand-story-driven visitors to subscribers | Medium |
| 8 | Acquisition | Resolving sitemap.xml and robots.txt 429 rate limiting will ensure Googlebot can fully crawl the 132-product catalog | High |
| 9 | Acquisition | Adding meta descriptions to /collections/all and /collections/sale pages will improve collection-level organic CTR | Medium |
| 10 | Performance | Adding alt text to 12/170 missing images and running Lighthouse to establish a speed baseline will clear remaining technical debt | Low |

---

## 7. Technical Findings Summary

**Passing (8):** SSL, HTTPS Redirect, Critical Pages Loading, Meta Tags & Social Previews, Structured Data (Organization + WebSite), Favicon, Checkout Reachable, Payment Methods, Shopping Journey

**Warnings (7):** Sitemap (429), Robots.txt (429), Mobile-Friendly, Page Speed Mobile, Page Speed Desktop, Broken Links (1/40 non-critical), Image Optimization (12/170 alt text), Cookie/Privacy (no consent popup)

**Failures (0):** None

Notable: No Fail status across all 17 checks. Sitemap/robots.txt 429 rate limit is the highest-risk technical issue (may block SEO crawling).

---

## 8. Evidence Gaps

- All 3 sampled PDPs are non-coffee products (gift card, 2 mugs) — Subscribe & Save toggle on core coffee PDPs (death-wish-coffee, power-surge, valhalla-java) was not observed
- Cart upsell behavior when cart contains coffee products is unknown
- Where-to-buy page failed to load — retail distribution presence unknown
- Individual blog post in-content CTAs not verified (blog index crawled, not post)
- /pages/faq (standard URL) is in rejected pages — whether it 404s or redirects to /pages/help is unverified
