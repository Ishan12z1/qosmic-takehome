# Evidence Summary — zenrojas_20260614_ab4535

## 1. Store identity

```
store_category: tea / specialty organic beverages
primary_use_cases:
  - daily tea ritual / mindfulness and relaxation
  - functional wellness (sleep, immune support, daily energy)
  - gifting and tea-accessory (teaware) attach
main_diagnosis: The funnel is technically frictionless (5.0/5 journey, 9 payment methods) but leaks revenue at the decision and basket stages — every PDP lacks social proof and the cart has no path to the stated $50 free-shipping threshold, so qualified traffic converts at lower rates and lower basket sizes than the product range supports.
```

## 2. Findings by pillar

### Conversion
- Shopping journey is frictionless: PDP → cart → checkout in 3 clicks, no errors, add-to-cart verified via `/cart.js` — `artifacts/zenrojas_20260614_ab4535/pages/shopping_journey.json`.
- PDPs have a complete buy box (Add to Cart + Buy with Shop, Shop Pay installments, 30-Day Warranty) — `artifacts/zenrojas_20260614_ab4535/screenshots/product_page_1_products_tea-bags.png`.
- Reviews widget exists but is empty ("No reviews yet") on the PDP — zero social proof at the decision point — `artifacts/zenrojas_20260614_ab4535/screenshots/product_page_1_products_tea-bags.png`.
- Cart has no trust badges / return reassurance on the cart page itself — `artifacts/zenrojas_20260614_ab4535/screenshots/cart_page_4_cart.png`.
- Collections lack sort/filter controls and per-card proof badges — `artifacts/zenrojas_20260614_ab4535/screenshots/collection_page_5_collections_teas.png`.
- "Veteran owned" + ethically-sourced trust cues live only on the About page, not on buying surfaces — `artifacts/zenrojas_20260614_ab4535/pages/about_page_9_pages_aboutus.md`.

### AOV
- PDP "Frequently bought together" bundle with pre-checked add-ons and "Add selected to cart" is a real, working AOV mechanic — `artifacts/zenrojas_20260614_ab4535/screenshots/product_page_1_products_tea-bags.png`.
- Every PDP carries a "Complete Your Ritual" cross-sell row — `artifacts/zenrojas_20260614_ab4535/pages/product_page_2_products_blacktea.json`.
- Cart has NO free-shipping progress bar despite a $50 threshold, and no in-cart upsell (`cart_upsell_present: false`) — `artifacts/zenrojas_20260614_ab4535/screenshots/cart_page_4_cart.png`, `artifacts/zenrojas_20260614_ab4535/pages/shopping_journey.json`.
- Teaware (infuser, mug) is positioned as an attach category but offered as standalone SKUs with no teaware+tea bundle — `artifacts/zenrojas_20260614_ab4535/pages/collection_page_6_collections_teaware.json`.

### Retention
- Checkout pre-checks "Email me with news and offers", capturing marketing consent on purchase — `artifacts/zenrojas_20260614_ab4535/screenshots/shopping_journey_checkout.png`.
- Newsletter "Subscribe" exists in footer/content pages but there is no homepage email incentive — `artifacts/zenrojas_20260614_ab4535/pages/about_page_9_pages_aboutus.json`, `artifacts/zenrojas_20260614_ab4535/pages/homepage_0_home.md`.
- No subscribe-and-save / replenishment on consumable teas — a major missed recurring-revenue hook for a repeat-purchase category — `artifacts/zenrojas_20260614_ab4535/pages/product_page_1_products_tea-bags.json`.

### Acquisition
- Active founder-led weekly blog supports organic content acquisition — `artifacts/zenrojas_20260614_ab4535/pages/blog_or_content_page_10_blogs_weekly-blog_building-a-family-lega.json`.
- Thin/templated metadata: homepage OG title is generic "Home Page"; blog title truncates mid-word ("Purpose-Driv") — `artifacts/zenrojas_20260614_ab4535/pages/homepage_0_home.json`.
- No JSON-LD structured data anywhere (no Product or FAQPage) — lost rich-result eligibility — `artifacts/zenrojas_20260614_ab4535/technical_checks.json`.

### Performance
- Mobile and desktop navigation timings are healthy (mobile load 1733ms, desktop 1978ms) — `artifacts/zenrojas_20260614_ab4535/technical_checks.json`.
- Mobile-friendly: viewport present, no horizontal overflow at 375px — `artifacts/zenrojas_20260614_ab4535/technical_checks.json`.
- 31/92 images (33%) missing alt text — both a Performance/accessibility and Acquisition (image SEO) drag — `artifacts/zenrojas_20260614_ab4535/technical_checks.json`.

## 3. Cross-page patterns

- **No social proof on any PDP.** Reviews widget empty on PDP1; no rating adjacent to buy box on PDP2/PDP3 — `artifacts/zenrojas_20260614_ab4535/screenshots/product_page_1_products_tea-bags.png`, `artifacts/zenrojas_20260614_ab4535/screenshots/product_page_2_products_blacktea.png`.
- **AOV mechanics strong on PDP, absent in cart.** Bundles/cross-sell on PDPs but the cart offers nothing toward the $50 threshold — `artifacts/zenrojas_20260614_ab4535/screenshots/product_page_1_products_tea-bags.png`, `artifacts/zenrojas_20260614_ab4535/screenshots/cart_page_4_cart.png`.
- **Trust signals siloed.** "Veteran owned" + organic/ethical sourcing appear on About/PDP copy but not on cart/checkout where doubt peaks — `artifacts/zenrojas_20260614_ab4535/pages/about_page_9_pages_aboutus.md`, `artifacts/zenrojas_20260614_ab4535/screenshots/cart_page_4_cart.png`.
- **Content is a funnel dead-end.** Blog and About build authority but contain no product CTAs or email capture — `artifacts/zenrojas_20260614_ab4535/pages/blog_or_content_page_10_blogs_weekly-blog_building-a-family-lega.md`, `artifacts/zenrojas_20260614_ab4535/pages/about_page_9_pages_aboutus.md`.
- **No structured data on any page** — `artifacts/zenrojas_20260614_ab4535/technical_checks.json`, `artifacts/zenrojas_20260614_ab4535/pages/faq_shipping_returns_8_pages_faqs.json`.

## 4. Purchase path constraints

Journey outcome `full_journey`, friction 5.0/5, no blockers, no errors, 3 clicks to checkout, trust badges at checkout true (`artifacts/zenrojas_20260614_ab4535/evidence_cards/shopping_journey.json`). Express checkout (Shop Pay/PayPal/wallets) and a discount field are present at checkout (`artifacts/zenrojas_20260614_ab4535/screenshots/shopping_journey_checkout.png`). The single constraint inside the journey is AOV: no cart upsell and no free-shipping progress, so basket size is never grown en route (`artifacts/zenrojas_20260614_ab4535/screenshots/shopping_journey_cart.png`).

## 5. Content commercialization opportunities

- The weekly blog (founder/wellness storytelling) has high dwell potential but zero in-content product links or email capture — convert to a funnel with contextual product cards + a newsletter incentive — `artifacts/zenrojas_20260614_ab4535/pages/blog_or_content_page_10_blogs_weekly-blog_building-a-family-lega.md`.
- The About page's "Veteran owned" story is a strong differentiator with no CTA back to the catalog — `artifacts/zenrojas_20260614_ab4535/pages/about_page_9_pages_aboutus.md`.
- FAQ leads with tea-history trivia instead of shipping/returns objections — reorder to resolve purchase friction — `artifacts/zenrojas_20260614_ab4535/pages/faq_shipping_returns_8_pages_faqs.md`.

## 6. Candidate experiments (pre-draft)

1. (Conversion) Add review collection + display reviews/stars on PDP buy box — empty widget today → High.
2. (Conversion) Surface "Veteran owned" + organic/ethical trust strip on cart & checkout → Medium.
3. (Conversion) Add sort/filter + best-seller badges to collection grids → Medium.
4. (AOV) Add free-shipping progress bar to cart tied to the $50 threshold → High.
5. (AOV) Add in-cart cross-sell (recommended teas/teaware) → High.
6. (AOV) Create explicit teaware+tea "starter ritual" bundle with bundle pricing → Medium.
7. (Retention) Add subscribe-and-save to consumable tea PDPs → High.
8. (Retention) Add homepage email-capture with first-order incentive → Medium.
9. (Acquisition) Add Product + FAQPage JSON-LD structured data sitewide → Medium.
10. (Acquisition) Fix templated/truncated metadata (OG title, blog titles) → Low.
11. (Acquisition) Commercialize blog posts with contextual product cards → Medium.
12. (Performance) Add alt text to the 33% of images missing it → Low/Medium.
13. (Conversion) Reorder FAQ to lead with shipping/returns/delivery questions → Low.

## 7. Technical findings summary

From `artifacts/zenrojas_20260614_ab4535/technical_checks.json` (17 checks):
- **Critical failures (Fail):** none.
- **Warnings (Warn) — 5:** Meta Tags & Social Previews (title+meta on 9/10 pages), Structured Data (no JSON-LD on 10 pages), Favicon (no favicon link tag), Broken Links (4 non-critical of 40 sampled), Image Optimization (31/92 images missing alt text).
- **Passing (Pass) — 12:** SSL, HTTPS Redirect, Sitemap, Robots.txt, Critical Pages Loading (10/10), Mobile-Friendly, Page Speed Mobile, Page Speed Desktop, Cookie/Privacy, Checkout Reachable, Payment Methods (9 detected), Shopping Journey (5.0/5).

## 8. Evidence gaps and uncertainty

- `/pages/where-to-buy` returned HTTP 404 and was excluded from crawl health; no where-to-buy evidence — `artifacts/zenrojas_20260614_ab4535/discovered_links.json`.
- PDP2/PDP3 structural observations (empty reviews, cross-sell) are inferred from the shared theme template confirmed on PDP1's screenshot plus PDP2/PDP3 metadata; full-page screenshots for PDP2/PDP3 were not individually inspected at the same depth.
- Page-speed checks are single-run navigation timings, not Lighthouse; treat as directional.
- Image optimization is alt-text coverage only; byte-level weight audit was not run.
- Post-purchase / account surfaces were not crawled — journey stops at checkout entry by policy.
