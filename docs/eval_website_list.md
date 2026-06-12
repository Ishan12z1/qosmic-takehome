# Eval Website List

15 websites across 4 types for testing the Qosmic Audit Harness end-to-end.
Use this list to verify the harness generalizes, degrades gracefully, and fails clearly.

---

## Type A — Shopify stores: known-good baseline (already tested)

These 5 are fully validated — 8/8 eval layers pass, known friction scores, known issues.
Use them to verify any harness changes didn't regress the pipeline.

| # | URL | Niche | Friction | Key finding |
|---|---|---|---|---|
| 1 | zenrojas.com | Specialty tea | 5.0/5 | Zero social proof across all pages |
| 2 | beardbrand.com | Men's grooming | 4.5/5 | No guest checkout — only active friction flag |
| 3 | deathwishcoffee.com | Coffee subscription | 5.0/5 | Giveaway promo overriding H1 on every PDP |
| 4 | mudwtr.com | Wellness / mushroom coffee | 5.0/5 | 60k reviews in meta but invisible on PDPs |
| 5 | tentree.com | Sustainable apparel | 5.0/5 | OG tags empty sitewide (theme config failure) |

**Expected behavior:** Full 10/11 or 11/11 pages, complete shopping journey, 8/8 eval pass.

---

## Type B — Shopify stores: new targets (untested)

Diverse niches, all expected to be standard Shopify — use to verify generalization.

| # | URL | Niche | Why it's interesting |
|---|---|---|---|
| 6 | graza.co | Olive oil / food | Small-catalog DTC brand (~5 SKUs); tests how harness handles minimal product range |
| 7 | puravidabracelets.com | Jewelry / lifestyle | Large catalog, charity tie-in, subscription bracelets — tests AOV + retention signals |
| 8 | chubbiesshorts.com | Men's apparel | Heavy brand voice/humor in copy; tests whether evidence analyst captures tone-based CRO signals |

**Expected behavior:** Standard Shopify crawl, 8–11 pages, complete journey, full audit.

---

## Type C — Shopify stores: edge cases (expected partial or blocked)

These stores are Shopify but have known protection or structural quirks.
Use to verify the harness fails gracefully and reports what it can.

| # | URL | Niche | Expected issue | Why it's useful |
|---|---|---|---|---|
| 9 | gingerpeople.com | Ginger candy / health | Cloudflare blocks all pages except homepage; retailer-routed (no direct cart) | **Confirmed blocked** — 1/10 pages, friction 2.0/5, 9 bot_challenge_detected |
| 10 | allbirds.com | Sustainable footwear | Imperva enterprise bot protection — similar to gingerpeople, likely all non-homepage pages blocked | Tests harness behavior on SPA + enterprise WAF |
| 11 | gymshark.com | Fitness apparel | Shopify Plus, heavy JS, large catalog (1000+ products) | Tests URL selection and page-cap behavior on massive stores |

**Expected behavior:** Partial crawl (1–3 pages), degraded audit, crawler logs blocked pages clearly.

---

## Type D — Non-Shopify ecommerce

Standard ecommerce stores but on Magento, WooCommerce, or custom platforms.
The harness should still crawl (Playwright is platform-agnostic) but Shopify-specific signals
(like `/cart`, `/collections/`, `.myshopify.com`) will be absent.

| # | URL | Platform | Niche | Why it's useful |
|---|---|---|---|---|
| 12 | patagonia.com | Magento (custom) | Outdoor apparel | Large non-Shopify store; tests whether shopping journey works without Shopify cart structure |
| 13 | warbyparker.com | Custom platform | Eyewear | DTC brand with strong CRO fundamentals; tests audit quality on a non-Shopify store |
| 14 | rei.com | Custom (SAP Commerce) | Outdoor retail / co-op | Membership model, massive catalog, very different from DTC Shopify; tests edge of harness |

**Expected behavior:** Crawler succeeds on most pages, shopping journey may fail at cart/checkout
(non-standard URLs), audit produced but technical checks differ (no Shopify-specific paths).
Evidence analyst should still extract meaningful CRO findings from page content.

---

## Type E — Non-ecommerce websites (adversarial)

No products, no cart, no purchase path. These should stress-test graceful failure:
the harness should not crash, should report what it finds, and should flag in the audit
that this is not an ecommerce store.

| # | URL | Type | Why it's useful |
|---|---|---|---|
| 15 | stripe.com | SaaS / developer tools | No cart, no PDPs, pricing page but no checkout — tests harness behavior when there's zero purchase path |
| 16 | wikipedia.org | Informational / reference | No commerce signals at all — extreme adversarial case; harness should complete crawl and report honestly |
| 17 | vercel.com | SaaS / developer platform | Has a pricing page and "Start for free" CTA but no product cart — tests edge between SaaS and ecommerce |

**Expected behavior:** Crawler completes (pages load), shopping journey returns retailer_routed or
friction 1.0 (no cart found), audit is generated but exec summary should note "this is not
an ecommerce store" based on evidence. No hallucinated checkout flows.

---

## Summary table

| # | URL | Type | Expected outcome |
|---|---|---|---|
| 1 | zenrojas.com | Shopify baseline | Full audit, 8/8 eval ✅ |
| 2 | beardbrand.com | Shopify baseline | Full audit, 8/8 eval ✅ |
| 3 | deathwishcoffee.com | Shopify baseline | Full audit, 8/8 eval ✅ |
| 4 | mudwtr.com | Shopify baseline | Full audit, 8/8 eval ✅ |
| 5 | tentree.com | Shopify baseline | Full audit, 8/8 eval ✅ |
| 6 | graza.co | Shopify new | Full audit expected |
| 7 | puravidabracelets.com | Shopify new | Full audit expected |
| 8 | chubbiesshorts.com | Shopify new | Full audit expected |
| 9 | gingerpeople.com | Shopify blocked | Partial crawl (1 page), degraded audit ✅ confirmed |
| 10 | allbirds.com | Shopify blocked | Partial crawl expected |
| 11 | gymshark.com | Shopify large | Full or partial crawl, may be slow |
| 12 | patagonia.com | Non-Shopify ecommerce | Crawl succeeds, journey may degrade |
| 13 | warbyparker.com | Non-Shopify ecommerce | Crawl succeeds, journey may degrade |
| 14 | rei.com | Non-Shopify ecommerce | Crawl succeeds, journey may degrade |
| 15 | stripe.com | Non-ecommerce SaaS | Crawl succeeds, no purchase path |
| 16 | wikipedia.org | Non-ecommerce info | Crawl succeeds, zero commerce signals |
| 17 | vercel.com | Non-ecommerce SaaS | Crawl succeeds, no cart |

---

## How to use this list

```bash
# Run any site through the full pipeline
python -m crawler.crawl_store https://<url>
/audit https://<url>
python evals/run_eval.py <run_id>

# For blocked/partial sites — check the crawl output first before running /audit
# A 1-page crawl will produce a thin audit; note this in your eval log
```

## Grading scale for non-standard sites

| Site type | Pass condition |
|---|---|
| Shopify standard | 8/8 eval layers, full journey |
| Shopify blocked | Crawler reports blocked pages clearly, audit notes limited evidence |
| Non-Shopify ecommerce | Audit produced without crash; findings grounded in crawled evidence |
| Non-ecommerce | Crawler completes; exec summary flags non-ecommerce nature; no invented checkout |
