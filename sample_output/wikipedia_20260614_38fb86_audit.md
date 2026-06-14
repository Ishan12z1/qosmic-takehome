# Partial Audit - Crawl Issues: https://wikipedia.org

Run ID: `wikipedia_20260614_38fb86`  
Crawl health: **Non-ecommerce**

> This is **not** a full CRO audit. The pages loaded, but no retail purchase surface was found — no product catalog with a working add-to-cart/checkout flow. This does not appear to be a retail ecommerce store (it may still be a SaaS or product site), so a storefront CRO audit (experiments, competitor benchmarks, checkout checks) does not apply.
> See `artifacts/wikipedia_20260614_38fb86/summary.md` for the full machine record.

## Issues a reader should know

- No retail purchase surface found — no product catalog with a working add-to-cart/checkout flow. This does not appear to be a retail ecommerce store (it may still be a SaaS or product site).
- 2/3 pages returned an HTTP error (4xx/5xx).
- Only 1/3 pages loaded cleanly.
- Shopping journey could not complete (outcome: no_product_found).
- No payment methods were detected.

## Technical checks captured

| Check | Status | Detail |
|---|---|---|
| SSL Certificate | Pass | HTTPS storefront loaded successfully. |
| HTTPS Redirect | Pass | HTTP redirected to HTTPS. |
| Sitemap | Warn | sitemap.xml returned status 404. |
| Robots.txt | Pass | robots.txt accessible. |
| Critical Pages Loading | Warn | 1/3 pages loaded. 0 blocked. |
| Meta Tags & Social Previews | Pass | Title, meta description, and OG tags present on all 1 crawled pages. |
| Structured Data | Warn | No JSON-LD detected across 1 crawled pages. |
| Favicon | Pass | Favicon link tag found. |
| Mobile-Friendly | Pass | Viewport meta present and no horizontal overflow at 375px. |
| Page Speed Mobile | Pass | Navigation timing (single run, not Lighthouse): load 767ms, DCL 749ms at 375px viewport. |
| Page Speed Desktop | Pass | Navigation timing (single run, not Lighthouse): load 1341ms, DCL 1311ms. |
| Broken Links | Pass | No broken links in 0 sampled links. |
| Image Optimization | Warn | 1/1 images missing alt text (100%) across 1 crawled pages. Byte-level audit not run. |
| Cookie/Privacy | Warn | Privacy and Terms found but cookie consent policy not detected. |
| Checkout Reachable | Warn | Not measured; no valid browser evidence was collected. |
| Payment Methods | Warn | No retail checkout surface detected; accepted payment methods were not assessed. Brand or  |
| Shopping Journey | Warn | No product page found to start journey. |

## What is NOT claimed

No experiments, competitor benchmarks, or pass/fail purchase-path verdicts are asserted — the evidence to support them was not captured. A storefront CRO audit is not applicable to this site type.

Evidence: `artifacts/wikipedia_20260614_38fb86/summary.md`, `artifacts/wikipedia_20260614_38fb86/discovered_links.json`
