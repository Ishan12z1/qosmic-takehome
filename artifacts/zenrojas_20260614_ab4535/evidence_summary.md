# Evidence Summary - zenrojas_20260614_ab4535

## 1. Store identity

```
store_category: tea / organic wellness beverages and teaware
primary_use_cases:
  - daily tea ritual and relaxation
  - functional wellness support (sleep, immune support, daily energy)
  - tea-and-teaware attach for gifting and routine building
main_diagnosis: The biggest conversion constraint is inconsistent and poorly placed purchase reassurance: on 3/3 sampled PDPs no rating summary appears near the primary CTA, review depth is mixed below the fold, and the brand's strongest trust story lives on content pages rather than at the cart decision point.
```

## 2. Findings by pillar

### Conversion
- Shopping friction is low: the journey reached checkout in 3 clicks with no friction flags or errors, and checkout shows express checkout plus broad wallet coverage - `artifacts/zenrojas_20260614_ab4535/pages/shopping_journey.json`, `artifacts/zenrojas_20260614_ab4535/screenshots/shopping_journey_checkout.png`.
- On 3/3 sampled PDPs, no rating summary is visible near the primary CTA; PDP2 has a real reviews block below the fold, while PDP1 and PDP3 show an empty review state ("No reviews yet") below the fold - `artifacts/zenrojas_20260614_ab4535/screenshots/product_page_1_products_tea-bags.png`, `artifacts/zenrojas_20260614_ab4535/screenshots/product_page_2_products_blacktea.png`, `artifacts/zenrojas_20260614_ab4535/screenshots/product_page_3_products_tea-seeper.png`.
- On the sampled teas collection, sort is present and sold-out states are visible, but no filter control or proof badges are visible on the cards - `artifacts/zenrojas_20260614_ab4535/screenshots/collection_page_5_collections_teas.png`.
- On the populated journey cart, subtotal and checkout are clear, but no trust strip, cart upsell, or free-shipping progress module is visible near the checkout CTA - `artifacts/zenrojas_20260614_ab4535/screenshots/shopping_journey_cart.png`, `artifacts/zenrojas_20260614_ab4535/pages/shopping_journey.json`.
- The about page contains strong trust-story copy ("Veteran owned and family operated"), but that message is not echoed on the visible populated-cart surface - `artifacts/zenrojas_20260614_ab4535/screenshots/about_page_9_pages_aboutus.png`, `artifacts/zenrojas_20260614_ab4535/screenshots/shopping_journey_cart.png`.

### AOV
- PDP merchandising is stronger than cart merchandising: PDP1 and PDP2 show a visible "Frequently bought together" bundle, while PDP3 does not - `artifacts/zenrojas_20260614_ab4535/screenshots/product_page_1_products_tea-bags.png`, `artifacts/zenrojas_20260614_ab4535/screenshots/product_page_2_products_blacktea.png`, `artifacts/zenrojas_20260614_ab4535/screenshots/product_page_3_products_tea-seeper.png`.
- All 3 sampled PDPs show a "Complete Your Ritual" cross-sell row below the main product area - `artifacts/zenrojas_20260614_ab4535/screenshots/product_page_1_products_tea-bags.png`, `artifacts/zenrojas_20260614_ab4535/screenshots/product_page_2_products_blacktea.png`, `artifacts/zenrojas_20260614_ab4535/screenshots/product_page_3_products_tea-seeper.png`.
- The populated cart does not reinforce the "$50+ orders" threshold with a progress bar, and the journey JSON records `cart_upsell_present: false` - `artifacts/zenrojas_20260614_ab4535/screenshots/shopping_journey_cart.png`, `artifacts/zenrojas_20260614_ab4535/pages/shopping_journey.json`.
- The teaware collection provides a clear attach category, but the sampled collection view does not add bundle cues, proof badges, or filters by use case - `artifacts/zenrojas_20260614_ab4535/screenshots/collection_page_6_collections_teaware.png`.

### Retention
- Checkout pre-checks "Email me with news and offers," so purchase-time marketing capture is already in place - `artifacts/zenrojas_20260614_ab4535/screenshots/shopping_journey_checkout.png`.
- Homepage email capture is present in the footer as "Join the Zen Journey," but no first-order incentive or modal was observed on the sampled homepage artifact - `artifacts/zenrojas_20260614_ab4535/screenshots/homepage_0_home.png`.
- Footer subscribe capture also appears on sampled content/support surfaces (About, Blog, FAQ), but those captures are non-incentivized and low-prominence - `artifacts/zenrojas_20260614_ab4535/pages/about_page_9_pages_aboutus.md`, `artifacts/zenrojas_20260614_ab4535/pages/blog_or_content_page_10_blogs_weekly-blog_building-a-family-lega.md`, `artifacts/zenrojas_20260614_ab4535/pages/faq_shipping_returns_8_pages_faqs.md`.
- On the 2 sampled consumable tea PDPs, no subscription or subscribe-and-save option is visible; on the sampled teaware accessory PDP, subscription is not applicable - `artifacts/zenrojas_20260614_ab4535/screenshots/product_page_1_products_tea-bags.png`, `artifacts/zenrojas_20260614_ab4535/screenshots/product_page_2_products_blacktea.png`, `artifacts/zenrojas_20260614_ab4535/screenshots/product_page_3_products_tea-seeper.png`.

### Acquisition
- Metadata is weak on sampled discovery surfaces: the homepage OG title is the generic "Home Page," and the sampled blog title/OG title truncate at "Purpose-Driv" - `artifacts/zenrojas_20260614_ab4535/pages/homepage_0_home.json`, `artifacts/zenrojas_20260614_ab4535/pages/blog_or_content_page_10_blogs_weekly-blog_building-a-family-lega.json`.
- The structured-data technical check warns that no JSON-LD was detected across the 10 crawled pages - `artifacts/zenrojas_20260614_ab4535/technical_checks.json`.
- The sampled blog article is trust/story rich but commercially weak: no in-content product CTA is visible in the article body - `artifacts/zenrojas_20260614_ab4535/screenshots/blog_or_content_page_10_blogs_weekly-blog_building-a-family-lega.png`.
- The sampled about page is also a commercial dead end in-body: the trust story is strong, but the body does not route readers back to teas or teaware - `artifacts/zenrojas_20260614_ab4535/screenshots/about_page_9_pages_aboutus.png`.
- The sampled FAQ page does answer shipping later on the page, but it opens with tea-history and storage questions rather than leading with purchase-objection content - `artifacts/zenrojas_20260614_ab4535/screenshots/faq_shipping_returns_8_pages_faqs.png`.

### Performance
- Technical health is generally solid: mobile-friendly passed, mobile load measured 1733ms, and desktop load measured 1978ms in single-run navigation timing - `artifacts/zenrojas_20260614_ab4535/technical_checks.json`.
- The Image Optimization check warns that 31 of 92 sampled images (33%) are missing alt text; byte-level image auditing was not run - `artifacts/zenrojas_20260614_ab4535/technical_checks.json`.
- The Broken Links and Favicon checks both warn: 4 non-critical broken links were found in a 40-link sample, and no favicon link tag was detected across the crawl - `artifacts/zenrojas_20260614_ab4535/technical_checks.json`.
- There are no critical technical failures in the current run; the technical issues are quality and discoverability drags rather than blockers - `artifacts/zenrojas_20260614_ab4535/technical_checks.json`.

## 3. Cross-page patterns

- Pattern: Rating proof is not surfaced near the buy box on sampled PDPs
  Support:
  - PDP1 (`/products/tea-bags`): absent near CTA, empty review block below fold - `artifacts/zenrojas_20260614_ab4535/screenshots/product_page_1_products_tea-bags.png`
  - PDP2 (`/products/blacktea`): absent near CTA, 1 review below fold - `artifacts/zenrojas_20260614_ab4535/screenshots/product_page_2_products_blacktea.png`
  - PDP3 (`/products/tea-seeper`): absent near CTA, empty review block below fold - `artifacts/zenrojas_20260614_ab4535/screenshots/product_page_3_products_tea-seeper.png`
  Verdict: consistent

- Pattern: PDP AOV merchandising is stronger than cart AOV merchandising
  Support:
  - PDP1: bundle present and cross-sell present - `artifacts/zenrojas_20260614_ab4535/screenshots/product_page_1_products_tea-bags.png`
  - PDP2: bundle present and cross-sell present - `artifacts/zenrojas_20260614_ab4535/screenshots/product_page_2_products_blacktea.png`
  - PDP3: bundle absent, cross-sell present - `artifacts/zenrojas_20260614_ab4535/screenshots/product_page_3_products_tea-seeper.png`
  - Populated cart: upsell absent and no free-shipping progress visible - `artifacts/zenrojas_20260614_ab4535/screenshots/shopping_journey_cart.png`
  Verdict: mixed

- Pattern: Owned-surface email capture exists but is low-prominence and non-incentivized
  Support:
  - Homepage: footer capture present, no incentive observed - `artifacts/zenrojas_20260614_ab4535/screenshots/homepage_0_home.png`
  - About: footer subscribe present in rendered markdown, no incentive - `artifacts/zenrojas_20260614_ab4535/pages/about_page_9_pages_aboutus.md`
  - Blog: footer subscribe present in rendered markdown, no incentive - `artifacts/zenrojas_20260614_ab4535/pages/blog_or_content_page_10_blogs_weekly-blog_building-a-family-lega.md`
  Verdict: consistent

- Pattern: Content surfaces build trust but do not commercialize that attention well
  Support:
  - About page: trust story present, no body product CTA - `artifacts/zenrojas_20260614_ab4535/screenshots/about_page_9_pages_aboutus.png`
  - Blog page: trust/story content present, no in-content product CTA - `artifacts/zenrojas_20260614_ab4535/screenshots/blog_or_content_page_10_blogs_weekly-blog_building-a-family-lega.png`
  - FAQ page: objection-helpful content present, no product CTA - `artifacts/zenrojas_20260614_ab4535/screenshots/faq_shipping_returns_8_pages_faqs.png`
  Verdict: consistent

## 4. Purchase path constraints

The shopping journey outcome is `full_journey` with friction 5.0/5, no friction flags, and 9 detected payment methods - `artifacts/zenrojas_20260614_ab4535/pages/shopping_journey.json`. The populated-cart journey screenshot shows a clean subtotal and checkout path, and the checkout screenshot shows express checkout plus a pre-checked marketing opt-in - `artifacts/zenrojas_20260614_ab4535/screenshots/shopping_journey_cart.png`, `artifacts/zenrojas_20260614_ab4535/screenshots/shopping_journey_checkout.png`.

The main purchase-path weakness is not conversion friction but cart under-merchandising: the populated cart shows no upsell and no free-shipping progress cue before checkout - `artifacts/zenrojas_20260614_ab4535/screenshots/shopping_journey_cart.png`, `artifacts/zenrojas_20260614_ab4535/pages/shopping_journey.json`. The standalone cart-page artifact should be treated separately because it is an empty-cart state, not a populated-cart merchandising view - `artifacts/zenrojas_20260614_ab4535/screenshots/cart_page_4_cart.png`, `artifacts/zenrojas_20260614_ab4535/evidence_cards/cart_page_4_cart.json`.

## 5. Content commercialization opportunities

- Blog article (`/blogs/weekly-blog/...`): trust/story content present; footer email capture present in markdown; no in-content product CTA; current article body is a commercial dead end - `artifacts/zenrojas_20260614_ab4535/screenshots/blog_or_content_page_10_blogs_weekly-blog_building-a-family-lega.png`, `artifacts/zenrojas_20260614_ab4535/pages/blog_or_content_page_10_blogs_weekly-blog_building-a-family-lega.md`.
- About page (`/pages/aboutus`): strong trust-story content; footer email capture present in markdown; no body CTA back to the catalog - `artifacts/zenrojas_20260614_ab4535/screenshots/about_page_9_pages_aboutus.png`, `artifacts/zenrojas_20260614_ab4535/pages/about_page_9_pages_aboutus.md`.
- FAQ page (`/pages/faqs`): useful support content and footer email capture in markdown; no product CTA; question order starts with tea trivia rather than purchase objections - `artifacts/zenrojas_20260614_ab4535/screenshots/faq_shipping_returns_8_pages_faqs.png`, `artifacts/zenrojas_20260614_ab4535/pages/faq_shipping_returns_8_pages_faqs.md`.

## 6. Candidate experiments (pre-draft)

1. `pillar: Conversion` - Add a rating summary near tea PDP CTAs and seed more reviews so the strongest proof is above the fold rather than mixed below it. `expected impact: High` `support scope: cross-page consistent`
2. `pillar: Conversion` - Add a cart trust strip that carries veteran-owned / organic / secure-checkout reassurance onto the populated cart. `expected impact: Medium` `support scope: cross-page consistent`
3. `pillar: Conversion` - Add filters and stronger proof badges to collection cards, especially on the teas collection. `expected impact: Medium` `support scope: single page`
4. `pillar: AOV` - Add a dynamic free-shipping progress module to the populated cart tied to the visible $50+ threshold. `expected impact: High` `support scope: cross-page consistent`
5. `pillar: AOV` - Add in-cart recommendations so the cart continues the "Complete Your Ritual" behavior already present on sampled PDPs. `expected impact: High` `support scope: mixed but important`
6. `pillar: AOV` - Standardize bundle merchandising so accessory PDPs and teaware collection surfaces attach as strongly as tea PDPs. `expected impact: Medium` `support scope: mixed but important`
7. `pillar: Retention` - Add subscribe-and-save on consumable tea PDPs. `expected impact: High` `support scope: cross-page consistent`
8. `pillar: Retention` - Upgrade homepage/footer capture into an incentivized list-growth motion with clearer value exchange. `expected impact: Medium` `support scope: cross-page consistent`
9. `pillar: Acquisition` - Add Product and FAQPage JSON-LD to improve search-result richness. `expected impact: Medium` `support scope: technical check`
10. `pillar: Acquisition` - Fix homepage/blog metadata quality and use blog/about content to route readers into products. `expected impact: Medium` `support scope: cross-page consistent`
11. `pillar: Performance` - Remediate missing alt text across the image library and add image QA to publishing. `expected impact: Low` `support scope: technical check`
12. `pillar: Performance` - Fix broken links and favicon hygiene as part of a crawl-clean release checklist. `expected impact: Low` `support scope: technical check`

## 7. Technical findings summary

From `artifacts/zenrojas_20260614_ab4535/technical_checks.json`:

- Critical failures (Fail): none.
- Warnings (Warn) - 5: Meta Tags & Social Previews, Structured Data, Favicon, Broken Links, Image Optimization.
- Passing checks (Pass) - 12: SSL Certificate, HTTPS Redirect, Sitemap, Robots.txt, Critical Pages Loading, Mobile-Friendly, Page Speed Mobile, Page Speed Desktop, Cookie/Privacy, Checkout Reachable, Payment Methods, Shopping Journey.

## 8. Evidence gaps and uncertainty

- Only 3 PDPs were sampled. The findings describe sampled-PDP behavior, not the entire catalog - `artifacts/zenrojas_20260614_ab4535/discovered_links.json`.
- Review depth is mixed across sampled PDPs: PDP2 has one visible review, while PDP1 and PDP3 show empty review states - `artifacts/zenrojas_20260614_ab4535/screenshots/product_page_1_products_tea-bags.png`, `artifacts/zenrojas_20260614_ab4535/screenshots/product_page_2_products_blacktea.png`, `artifacts/zenrojas_20260614_ab4535/screenshots/product_page_3_products_tea-seeper.png`.
- Footer subscribe capture on About/Blog/FAQ is confirmed in rendered markdown, but not visible in the sampled screenshot crops - `artifacts/zenrojas_20260614_ab4535/pages/about_page_9_pages_aboutus.md`, `artifacts/zenrojas_20260614_ab4535/pages/blog_or_content_page_10_blogs_weekly-blog_building-a-family-lega.md`, `artifacts/zenrojas_20260614_ab4535/pages/faq_shipping_returns_8_pages_faqs.md`.
- Broken-link evidence is summarized in the technical check but the individual broken URLs are not enumerated in the committed artifact bundle - `artifacts/zenrojas_20260614_ab4535/technical_checks.json`.
- Page-speed results are single-run navigation timings, not a Lighthouse or byte-level performance audit - `artifacts/zenrojas_20260614_ab4535/technical_checks.json`.
- `https://zenrojas.com/pages/where-to-buy` was guessed but unavailable (HTTP 404), so no where-to-buy evidence exists in this run - `artifacts/zenrojas_20260614_ab4535/discovered_links.json`.
