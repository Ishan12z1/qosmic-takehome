# Partial Audit - Crawl Issues: https://patagonia.com

Run ID: `patagonia_20260613_4b2883`  
Crawl health: **Blocked**

> This is **not** a full CRO audit. The storefront could not be crawled (bot protection, timeouts, or errors on the core pages), so there is not enough evidence to produce experiments, competitor analysis, or a reliable technical assessment.
> See `artifacts/patagonia_20260613_4b2883/summary.md` for the full machine record.

## Issues a reader should know

- Homepage could not be crawled — the site may be down or bot-protected.
- 3/3 pages were blocked by bot protection.
- Only 0/3 pages loaded cleanly.
- Shopping journey could not complete (outcome: no_product_found).
- No payment methods were detected.

## Technical checks captured

| Check | Status | Detail |
|---|---|---|
| SSL Certificate | Pass | HTTPS storefront loaded successfully. |
| HTTPS Redirect | Pass | HTTP redirected to HTTPS. |
| Sitemap | Warn | sitemap.xml returned status 200. |
| Robots.txt | Pass | robots.txt accessible. |
| Critical Pages Loading | Warn | 3/3 pages blocked by bot protection. |
| Meta Tags & Social Previews | Warn | Not measured; no valid browser evidence was collected. |
| Structured Data | Warn | Not measured; no valid browser evidence was collected. |
| Favicon | Warn | Not measured; no valid browser evidence was collected. |
| Mobile-Friendly | Warn | Mobile layout not measured (measurement pass did not run). |
| Page Speed Mobile | Warn | Page speed not measured (measurement pass did not run). |
| Page Speed Desktop | Warn | Page speed not measured (measurement pass did not run). |
| Broken Links | Pass | No broken links in 3 sampled links. |
| Image Optimization | Warn | Not measured; no valid browser evidence was collected. |
| Cookie/Privacy | Warn | Not measured; no valid browser evidence was collected. |
| Checkout Reachable | Warn | Not measured; no valid browser evidence was collected. |
| Payment Methods | Warn | Not measured; no valid browser evidence was collected. |
| Shopping Journey | Warn | No product page found to start journey. |

## What is NOT claimed

No experiments, competitor benchmarks, or pass/fail purchase-path verdicts are asserted — the evidence to support them was not captured. Re-run from a non-blocked network/IP to attempt a full audit.

Evidence: `artifacts/patagonia_20260613_4b2883/summary.md`, `artifacts/patagonia_20260613_4b2883/discovered_links.json`
