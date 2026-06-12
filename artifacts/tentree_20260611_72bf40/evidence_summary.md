# Evidence Summary — tentree_20260611_72bf40

## 1. Store Identity

```
store_category: sustainable outdoor apparel / eco-conscious fashion brand
primary_use_cases:
  - everyday sustainable clothing (men's + women's sweatpants, shirts, hoodies, jackets, accessories)
  - mission-driven gifting (e-gift codes for eco-conscious recipients)
  - eco-upgraded essentials via CLIMATE+ line (carbon-neutral apparel tier)
  - size-confident apparel buying (fit guide with fit profile system per product)
main_diagnosis: Tentree's mission — "Every Item Plants 10 Trees", 120+ million trees planted, organic/recycled materials — is a uniquely strong purchase motivator for eco-conscious buyers. But the brand is actively suppressing this differentiator: OG social meta tags are missing on every single page (homepage, all PDPs, collections, about), meaning every social share produces a blank preview card. The homepage headline is entirely discount-driven ("Up to 50% Off Almost Everything") with no H1 and no mission messaging — first-time visitors experience a clearance sale, not a sustainability brand. And 73% of product images lack alt text. The brand's story is strong; its technical distribution of that story is broken.
```

---

## 2. Findings by Pillar

### Conversion
- 5.0/5 friction score — 4 clicks to checkout, trust badges confirmed, 12 payment methods (widest of all 5 stores tested) including Klarna, Google Pay, Apple Pay (`artifacts/tentree_20260611_72bf40/pages/shopping_journey.json`)
- Dedicated Klarna FAQ page educates buyers on BNPL — active conversion strategy for $50–120 apparel purchases (`artifacts/tentree_20260611_72bf40/pages/faq_shipping_returns_8_pages_klarna-faq.json`)
- 'Every Item Plants 10 Trees' H2 present on all 3 crawled PDPs — consistent mission reinforcement at the purchase decision moment (`artifacts/tentree_20260611_72bf40/pages/product_page_2_products_m-atlas-sweatpant.json`)
- 'We Think You'll Like...' H2 on all PDPs — cross-sell recommendation section present on product pages (`artifacts/tentree_20260611_72bf40/pages/product_page_2_products_m-atlas-sweatpant.json`)
- **No H1 on homepage** — all 5 headings are H2 sale banners; brand has no primary identity statement at the first impression (`artifacts/tentree_20260611_72bf40/pages/homepage_0_home.json`)
- **OG title and OG description empty on every crawled page** — social preview cards for all content are blank; this is the highest-impact technical failure for a brand whose acquisition strategy relies on mission-story sharing (`artifacts/tentree_20260611_72bf40/pages/homepage_0_home.json`)
- Cart has no headings, no upsell, no urgency signals — bare-bones cart despite active free shipping deadline on homepage (`artifacts/tentree_20260611_72bf40/pages/cart_page_4_cart.json`)
- **Cookie/Privacy: Warn** — no cookie consent popup detected; same GDPR/CCPA compliance gap as all other tested stores (`artifacts/tentree_20260611_72bf40/technical_checks.json`)

### AOV
- Cart upsell not triggered (cart_upsell_present: FALSE) — no 'complete the look' recommendations after adding Atlas Sweatpant to cart; single-item checkout is the default path (`artifacts/tentree_20260611_72bf40/pages/shopping_journey.json`)
- Urgency absent from cart despite active free shipping deadline (urgency_elements_present: FALSE) — homepage H2 says 'Free Shipping on All Orders. Ends Friday at Midnight.' but this urgency signal doesn't appear in the cart (`artifacts/tentree_20260611_72bf40/pages/shopping_journey.json`)
- Klarna installment payments available — BNPL is active and supported at checkout, reducing price barrier for higher-ticket apparel orders (`artifacts/tentree_20260611_72bf40/pages/faq_shipping_returns_8_pages_klarna-faq.json`)
- PDP cross-sell ('We Think You'll Like...') present but not confirmed as outfit-building — recommendations exist on PDPs but cross-sell type (outfit pairing vs. similar product) was not confirmed from heading structure (`artifacts/tentree_20260611_72bf40/evidence_cards/product_page_2_products_m-atlas-sweatpant.json`)

### Retention
- No email capture detected on any page — no email signup heading found on homepage, about, fit guide, or cart; email acquisition touchpoints are absent across the entire crawled funnel (`artifacts/tentree_20260611_72bf40/pages/homepage_0_home.json`)
- Fit guide at /pages/fit-guide reduces sizing uncertainty — proactive fit education reduces returns and repeat-purchase friction by building size confidence (`artifacts/tentree_20260611_72bf40/evidence_cards/blog_or_content_page_10_pages_fit-guide.json`)
- CLIMATE+ collection in nav — premium eco-upgraded tier provides aspiration ladder for repeat purchasers who want to step up their sustainability commitment (`artifacts/tentree_20260611_72bf40/pages/homepage_0_home.json`)
- No loyalty program or "your impact" counter detected — the 10-trees-per-purchase promise is stated per item on PDPs but not aggregated into a personal impact dashboard or post-purchase reinforcement that would build emotional loyalty (`artifacts/tentree_20260611_72bf40/evidence_cards/shopping_journey.json`)

### Acquisition
- Meta title strong and differentiating: 'Tentree | Sustainable Clothing—Every Item Plants 10 Trees' — brand + mission + key benefit in one line (`artifacts/tentree_20260611_72bf40/pages/homepage_0_home.json`)
- Men's collection meta description is keyword-rich: organic cotton, hemp, recycled polyester, TENCEL, 10 Trees Planted — strong organic signal for 'sustainable men's clothing' queries (`artifacts/tentree_20260611_72bf40/evidence_cards/collection_page_6_collections_mens.json`)
- PDP meta descriptions are material-specific ('Organic Cotton & Recycled Polyester') — SEO foundation for product-level material queries is in place (`artifacts/tentree_20260611_72bf40/evidence_cards/product_page_2_products_m-atlas-sweatpant.json`)
- **OG tags empty sitewide** — organic social shares from Instagram, Facebook, Pinterest, and LinkedIn all produce blank preview cards; social sharing is a primary acquisition channel for mission-driven brands (`artifacts/tentree_20260611_72bf40/pages/homepage_0_home.json`)
- **/collections/all meta is 'all items'** — placeholder meta on the all-products page misses every 'sustainable clothing' search query (`artifacts/tentree_20260611_72bf40/evidence_cards/collection_page_5_collections_all.json`)
- **Structured Data: Warn** — no confirmed JSON-LD Product or Organization schema; limits rich snippet eligibility in Google Search (`artifacts/tentree_20260611_72bf40/technical_checks.json`)
- Where-to-buy page is 404 — retail store locator does not exist at standard URL (`artifacts/tentree_20260611_72bf40/evidence_cards/where_to_buy_7_pages_where-to-buy.json`)
- No H1 on homepage — zero primary keyword signal on the most-crawled page of the site (`artifacts/tentree_20260611_72bf40/pages/homepage_0_home.json`)

### Performance
- **Image Optimization: Warn** — 58/79 images missing alt text (73%); by far the worst of all 5 stores tested (mudwtr was 20%, deathwishcoffee 7%); severely impacts image search indexing and accessibility (`artifacts/tentree_20260611_72bf40/technical_checks.json`)
- **Page Speed Mobile/Desktop: Warn** — no Lighthouse run performed (`artifacts/tentree_20260611_72bf40/technical_checks.json`)
- **Mobile-Friendly: Warn** — desktop-only audit (`artifacts/tentree_20260611_72bf40/technical_checks.json`)
- **Broken Links: Warn** — 1/40 non-critical (`artifacts/tentree_20260611_72bf40/technical_checks.json`)

---

## 3. Cross-Page Patterns

**Pattern 1 — OG tags absent on every page (sitewide)**
Every crawled page (homepage, 3 PDPs, 2 collections, about, Klarna FAQ, fit guide, where-to-buy) has og_title: "" and og_description: "". This is a sitewide configuration failure, not a per-page omission. Social sharing from any page on tentree.com produces a blank preview card — no image, no title, no description. For a brand whose mission story ("plant 10 trees with every purchase") is inherently shareable, this is the highest-leverage single fix.
Evidence: `artifacts/tentree_20260611_72bf40/pages/homepage_0_home.json`, `product_page_2_products_m-atlas-sweatpant.json`, `about_page_9_pages_about.json`

**Pattern 2 — Mission narrative present on PDPs, absent from entry points**
"Every Item Plants 10 Trees" appears as an H2 on every PDP and is in the brand's meta title. But the homepage is dominated by sale messaging ("Up to 50% Off") with no mission H1. The about page has the mission story but no purchase CTA. The cart has no trees-per-item reinforcement. The mission is present at the product level but not closing the brand loop at entry (homepage) or exit (cart/thank-you page).
Evidence: `artifacts/tentree_20260611_72bf40/pages/homepage_0_home.json`, `product_page_2_products_m-atlas-sweatpant.json`, `cart_page_4_cart.json`

**Pattern 3 — Inconsistent SEO quality across collection pages**
Men's collection has a strong meta description, keyword H1, and benefit-copy H3 sections. The all-products collection has meta_description: "all items" and H1: "all items". This inconsistency suggests collection pages were individually optimized without a systematic audit — some pages are well-done, others have placeholder content.
Evidence: `artifacts/tentree_20260611_72bf40/pages/collection_page_5_collections_all.json`, `collection_page_6_collections_mens.json`

---

## 4. Purchase Path Constraints

Shopping journey outcome: **full_journey**, friction score **5.0/5**. First PDP (e-gift code) failed add-to-cart as expected (gift codes require value selection); crawler fell back to Atlas Sweatpant which succeeded. Cart: no upsell, no urgency. Checkout: trust badges confirmed. 12 payment methods. No structural purchase path blockers — the gaps are all in cart optimization, not mechanics.

---

## 5. Content Commercialization Opportunities

1. **Fit guide → collection CTAs**: Each fit profile section should link directly to the relevant filtered collection ('Shop Relaxed Fit → /collections/mens?fit=relaxed') to capture the conversion intent generated by fit-confident browsing
2. **About page → mission-to-cart CTA**: After the 'We Believe Big Change Starts Small' story, add 'Start with your first 10 trees → Shop Now' CTA above the fold
3. **OG tags on impact/mission pages**: Fix OG tags first on the about page and PDPs — these are the pages most likely to be shared on social media with environmental mission framing

---

## 6. Candidate Experiments

| # | Pillar | Hypothesis | Impact |
|---|---|---|---|
| 1 | Conversion | Fixing sitewide OG social meta tags will restore social sharing previews and increase click-through from social media shares | High |
| 2 | Conversion | Adding a mission H1 ('Sustainable Clothing That Plants Trees') to the homepage will align first-impression brand signals with the sustainability positioning that converts eco-conscious buyers | Medium |
| 3 | AOV | Adding cart upsell with 'complete the look' outfit recommendations will increase multi-item order rate | High |
| 4 | AOV | Surfacing the active free shipping deadline in the cart will increase checkout completion by converting the homepage urgency signal into a cart-step nudge | Medium |
| 5 | Retention | Adding email capture on the about page and fit guide with a sustainability-framed offer will build the email list from mission-engaged visitors | High |
| 6 | Retention | Adding a post-purchase 'you planted X trees' impact counter on the order confirmation page will create emotional loyalty reinforcement for first-time buyers | Medium |
| 7 | Acquisition | Replacing the /collections/all meta description placeholder 'all items' with keyword-rich copy will improve ranking for 'sustainable clothing' queries | High |
| 8 | Acquisition | Adding Product JSON-LD structured data to PDPs will enable Google rich snippets with ratings, price, and availability for organic search results | Medium |
| 9 | Performance | Fixing alt text on 58/79 images (73%) will improve image search indexing and accessibility compliance | High |
| 10 | Performance | Adding a cookie consent banner and running Lighthouse to establish a Core Web Vitals baseline will address compliance and performance monitoring gaps | Medium |

---

## 7. Technical Findings Summary

**Passing (7):** SSL, HTTPS Redirect, Sitemap, Robots.txt, Meta Tags & Social Previews (Pass with OG tag gap noted), Favicon, Critical Pages Loading (11/11), Checkout Reachable, Payment Methods, Shopping Journey

**Warnings (7):** Structured Data, Mobile-Friendly, Page Speed Mobile, Page Speed Desktop, Broken Links (1/40), Image Optimization (58/79 alt text — 73%), Cookie/Privacy

**Failures (0):** None

Notable: Image alt text at 73% missing is the most urgent technical issue — 6× worse than the next-worst store tested (mudwtr at 20%). Structured Data Warn is unique to tentree among the 5 stores tested. OG tags missing sitewide is captured in Meta Tags check detail.

---

## 8. Evidence Gaps

- OG tag status: checked via page JSON — confirmed empty on all 9 pages read; likely a theme-level configuration gap rather than per-page oversight
- Reviews on Ashwood Shirt PDP: not confirmed in heading structure — may be absent or below-fold JS-rendered; Atlas Sweatpant and gift code both have visible reviews
- Women's collection (/collections/womens) not crawled — whether SEO quality matches the strong men's collection or the degenerate all-items collection is unknown within the 12-page cap
- Shipping and returns FAQ not found — Klarna FAQ selected as the closest FAQ match; standard return/shipping policy FAQ URL not discovered in the sitemap
- Email capture: not detected in any heading structure; popup or exit-intent capture may exist but was not triggered by the crawler
