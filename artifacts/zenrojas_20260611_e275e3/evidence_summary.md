# Evidence Summary — zenrojas_20260611_e275e3

## 1. Store Identity

```
store_category: specialty tea / wellness beverages
primary_use_cases:
  - daily tea ritual (health-benefit teas: sleep, heartburn, immunity, energy)
  - gift-giving (sampler packs, gift cards, teaware bundles)
  - loose-leaf brewing at home (teaware accessories: infuser, mug, tea bags)
main_diagnosis: Zen Rojas has a clean purchase path and strong health-benefit product naming, but converts below its potential because no page shows social proof — no reviews, no star ratings, no customer count — leaving first-time visitors with nothing to trust before buying.
```

---

## 2. Findings by Pillar

### Conversion
- Product CTAs are health-benefit-led (Sleep Tea, Heartburn Tea, Bodyguard Tea) — high-intent framing on homepage (`artifacts/zenrojas_20260611_e275e3/screenshots/homepage_0_home.png`)
- Add-to-cart works on first try, cart loads cleanly, checkout entry reached — 0 friction flags (`artifacts/zenrojas_20260611_e275e3/pages/shopping_journey.json`)
- Trust badges present at checkout — security signals at highest-anxiety step (`artifacts/zenrojas_20260611_e275e3/screenshots/shopping_journey_checkout.png`)
- **No star ratings or review count on any page** — homepage, all 3 PDPs, both collection pages all lack social proof (`artifacts/zenrojas_20260611_e275e3/evidence_cards/product_page_1_products_tea-bags.json`, `product_page_2_products_blacktea.json`, `product_page_3_products_tea-seeper.json`)
- No urgency signals anywhere — no low-stock indicator, no countdown, no "X sold today" (`artifacts/zenrojas_20260611_e275e3/screenshots/shopping_journey_cart.png`)
- CTA text rendering bug: "Add to CartView cart" is concatenated on all PDPs — potential DOM issue (`artifacts/zenrojas_20260611_e275e3/pages/product_page_1_products_tea-bags.json`)

### AOV
- Cross-sell section "Complete Your Ritual" exists on all 3 PDPs — links infuser, black tea, samplers — brand ecosystem in place (`artifacts/zenrojas_20260611_e275e3/pages/product_page_1_products_tea-bags.json`)
- No bundle pricing offered — cross-sell is navigation only, no "buy together" offer (`artifacts/zenrojas_20260611_e275e3/evidence_cards/product_page_3_products_tea-seeper.json`)
- Cart upsell absent — confirmed by journey observation `cart_upsell_present: false` (`artifacts/zenrojas_20260611_e275e3/pages/shopping_journey.json`)
- Natural starter kit bundle (infuser + 2 teas) not surfaced anywhere in purchase flow (`artifacts/zenrojas_20260611_e275e3/evidence_cards/product_page_3_products_tea-seeper.json`)

### Retention
- Subscribe CTA visible in cart — some email/loyalty mechanism exists but nature unclear (`artifacts/zenrojas_20260611_e275e3/pages/cart_page_4_cart.json`)
- No subscription/recurring order option on consumable tea PDPs — tea is repeat-purchase by nature, no Subscribe & Save visible (`artifacts/zenrojas_20260611_e275e3/evidence_cards/product_page_2_products_blacktea.json`)
- No email capture on homepage or blog — organic traffic exits without retention hook (`artifacts/zenrojas_20260611_e275e3/evidence_cards/homepage_0_home.json`)
- Ambassador Program page exists (`/pages/ambassadorprogram`) — community layer present but not prominently featured (`artifacts/zenrojas_20260611_e275e3/pages/product_page_2_products_blacktea.json`)

### Acquisition
- OG tags properly configured — social sharing previews work (`artifacts/zenrojas_20260611_e275e3/technical_checks.json`)
- Teas collection has strong meta description: "100% organic, ethically sourced" + ritual framing (`artifacts/zenrojas_20260611_e275e3/pages/collection_page_6_collections_teas.json`)
- Homepage meta is only "100% Organic Loose Leaf tea" — no differentiation or benefit story for Google (`artifacts/zenrojas_20260611_e275e3/pages/homepage_0_home.json`)
- 3 broken pages at standard Shopify URLs: `/pages/about` (404), `/pages/faq` (404), `/pages/where-to-buy` (404) — actual pages are at `/pages/aboutus`, `/pages/faqs` — internal link mismatch (`artifacts/zenrojas_20260611_e275e3/screenshots/about_page_9_pages_about.png`, `faq_shipping_returns_8_pages_faq.png`, `where_to_buy_7_pages_where-to-buy.png`)
- Structured data: Warn — no Product schema detected, missing rich snippet eligibility (`artifacts/zenrojas_20260611_e275e3/technical_checks.json`)
- 6 broken links in 29 sampled (Broken Links: Warn) — SEO equity leaking (`artifacts/zenrojas_20260611_e275e3/technical_checks.json`)

### Performance
- Page Speed Mobile/Desktop: Warn — no Lighthouse run performed (`artifacts/zenrojas_20260611_e275e3/technical_checks.json`)
- Image alt text: 60% missing (9/15 images) — accessibility failure + SEO impact (`artifacts/zenrojas_20260611_e275e3/technical_checks.json`)
- Favicon: Warn — not confirmed detected (`artifacts/zenrojas_20260611_e275e3/technical_checks.json`)
- Mobile-Friendly: Warn — desktop-only audit performed (`artifacts/zenrojas_20260611_e275e3/technical_checks.json`)

---

## 3. Cross-Page Patterns (strongest signals)

**Pattern 1 — No social proof on any page (5/5 pages checked)**
Homepage, all 3 PDPs, both collection pages lack review stars, ratings count, or testimonials. For an organic wellness brand where trust is the purchase barrier, this is the single highest-leverage gap.
Evidence: `artifacts/zenrojas_20260611_e275e3/evidence_cards/homepage_0_home.json`, `product_page_1_products_tea-bags.json`, `product_page_2_products_blacktea.json`, `product_page_3_products_tea-seeper.json`, `collection_page_5_collections_all.json`

**Pattern 2 — Zero AOV mechanisms in purchase flow (cart + PDPs)**
Cart has no upsell widget. PDPs have a cross-sell section but no bundle pricing. The brand ecosystem (tea + infuser + mug) exists in the product catalog but is never packaged as a buy-together offer.
Evidence: `artifacts/zenrojas_20260611_e275e3/pages/shopping_journey.json`, `artifacts/zenrojas_20260611_e275e3/evidence_cards/cart_page_4_cart.json`, `product_page_3_products_tea-seeper.json`

**Pattern 3 — Three broken standard Shopify URLs (about, faq, where-to-buy)**
All three return 404. These are commonly linked from Google, other sites, and Shopify apps. Any external or internal link to these standard paths dead-ends the visitor.
Evidence: `artifacts/zenrojas_20260611_e275e3/screenshots/about_page_9_pages_about.png`, `faq_shipping_returns_8_pages_faq.png`, `where_to_buy_7_pages_where-to-buy.png`

**Pattern 4 — No retention mechanism at any stage**
No email capture on homepage, no Subscribe & Save on PDPs, no post-cart retention offer. Blog traffic (which has high organic potential) exits without any capture.
Evidence: `artifacts/zenrojas_20260611_e275e3/evidence_cards/homepage_0_home.json`, `blog_or_content_page_10_blogs_weekly-blog_building-a-family-lega.json`, `product_page_2_products_blacktea.json`

---

## 4. Purchase Path Constraints

Shopping journey outcome: **full_journey**, friction score **5.0/5** — the mechanical purchase path is flawless. Add-to-cart succeeded on first PDP, cart loaded, checkout entry reached. 4 clicks PDP to checkout. Trust badges at checkout. 10 payment methods.

The constraint is not mechanical friction — it is **conversion confidence**. First-time visitors have no evidence that others have bought and loved the product. The gap is social proof, not UX.

---

## 5. Content Commercialization Opportunities

The blog post ("Building a Family Legacy Through Wellness") has a strong meta and clear brand values narrative. It currently has only one CTA: "View cart." Inserting 1–2 in-content product links (e.g. "our Organic Sleep Tea" → PDP) and a post-read email capture would convert organic search traffic into customers and subscribers.

Evidence: `artifacts/zenrojas_20260611_e275e3/evidence_cards/blog_or_content_page_10_blogs_weekly-blog_building-a-family-lega.json`

---

## 6. Candidate Experiments

| # | Pillar | Hypothesis | Impact |
|---|---|---|---|
| 1 | Conversion | Adding star ratings above fold on all PDPs will increase add-to-cart rate because visitors currently see zero social proof before deciding | High |
| 2 | Conversion | Adding a review/testimonial section to the homepage will increase click-to-PDP rate because first-time visitors have no trust signal at entry | High |
| 3 | AOV | Adding a cart cross-sell widget (recommended tea to pair with current item) will increase order value because the cart currently shows no related products | Medium |
| 4 | AOV | Offering a "Starter Kit" bundle (infuser + 2 teas) with 10% discount on PDPs will increase average order value because the product ecosystem exists but is never packaged | Medium |
| 5 | Retention | Adding a Subscribe & Save option (10% off repeat orders) on tea PDPs will increase LTV because tea is a consumable product with no recurring purchase path | High |
| 6 | Retention | Adding an email capture popup (triggered at 40% scroll or exit intent) to homepage and blog will grow the email list because organic traffic currently exits with no capture | Medium |
| 7 | Acquisition | Expanding the homepage meta description to include brand story + top benefit will improve organic CTR because current meta is only "100% Organic Loose Leaf tea" | Medium |
| 8 | Acquisition | Redirecting `/pages/about`, `/pages/faq`, `/pages/where-to-buy` to their actual pages will recover link equity and reduce bounce from dead links | High |
| 9 | Acquisition | Adding Product structured data (JSON-LD) to PDPs will improve rich snippet eligibility in Google search results | Medium |
| 10 | Performance | Adding alt text to all product images (currently 60% missing) will improve accessibility compliance and image search indexing | Medium |
| 11 | Conversion | Adding urgency signal to cart page (low-stock badge or time-limited free shipping) will reduce cart abandonment | Medium |
| 12 | Conversion | Adding in-content product CTAs to blog posts will convert wellness-intent readers to purchasers | Medium |
| 13 | Retention | Surfacing the Ambassador Program in the homepage nav or footer will increase community signups from organic visitors | Low |
| 14 | AOV | Adding "frequently bought together" section to the infuser PDP (tea + infuser) will increase multi-item orders | Medium |

---

## 7. Technical Findings Summary

**Passing (7):** SSL, HTTPS Redirect, Sitemap, Robots.txt, Meta Tags & Social Previews, Cookie/Privacy, Critical Pages Loading, Checkout Reachable, Payment Methods, Shopping Journey

**Warnings (7):** Structured Data, Favicon, Mobile-Friendly, Page Speed Mobile, Page Speed Desktop, Broken Links (6/29 sampled), Image Optimization (60% missing alt text)

**Failures (0):** None

Key technical gaps: no Product schema (reduces rich snippet eligibility), 60% image alt text missing (SEO + accessibility), page speed unverified (no Lighthouse), 3 broken standard URL paths.

---

## 8. Evidence Gaps and Uncertainty

- Page speed actual scores unknown — Lighthouse not run, Mobile-Friendly unverified at mobile viewport
- Favicon status uncertain — Warn indicates not confirmed, may exist but not detected
- Structured data status uncertain — Warn, may be injected via Shopify theme after initial parse
- Subscription/loyalty mechanism in cart labeled "Subscribe" — unclear if this is email signup or a recurring purchase option; would require manual inspection to confirm
- Ambassador Program page not crawled — content and CTA unknown
- Actual reviews: it's possible the store has a reviews app (lb-reviews component detected in page HTML) but reviews were not rendered or populated — this affects Pattern 1 finding
