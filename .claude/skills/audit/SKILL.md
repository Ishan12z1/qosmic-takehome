---
name: audit
description: Run a full Qosmic Shopify CRO audit for a store URL — crawl, extract evidence, synthesize, write the report, and eval. Use when the user types /audit <url> or asks to audit/CRO-review a Shopify storefront.
---

# /audit <url>

Orchestrate a full Shopify CRO audit. Run each stage in order; every stage is
retry-safe (skip a stage whose output artifact already exists). The canonical,
detailed instructions live in `skills/audit.md` — follow it exactly.

## Pipeline

1. **Crawl** — `python -m crawler.crawl_store <url>` → `artifacts/<run_id>/`.
   Read `discovered_links.json` for `run_id` and `selected_pages`.
2. **Read the crawl health first** — open `artifacts/<run_id>/summary.md`.
   - If the verdict is **Blocked**, do NOT fabricate a full audit.
     Write `sample_output/<run_id>_audit.md` as a clearly-titled
     **"⚠ Partial Audit — Crawl Issues"** report that:
     - leads with the issues from `summary.md` (so a reader of the reports folder
       immediately sees the site had problems),
     - includes only the sections the available evidence supports,
     - never invents experiments or evidence for surfaces that were not crawled.
   - If the verdict is **Healthy** or **Degraded**, proceed to a full audit.
     For a Degraded crawl, explicitly cite `summary.md` and label every evidence
     gap or uncertainty; never generalize an observation to a missing surface.
3. **Per-page evidence** — `/page-evidence-extractor` for each `selected_pages`
   entry (skip soft-404 / blocked pages) + the shopping journey.
4. **Synthesize** — `/evidence-analyst` → `artifacts/<run_id>/evidence_summary.md`.
5. **Write** — `/audit-writer` → `sample_output/<run_id>_audit.md`.
6. **Eval** — `python evals/run_eval.py <run_id>`; fix only failed sections; for
   Layer 9 paste the printed prompt into `/eval-judge`.

## Invariants

- `run_id` is read from `discovered_links.json`, never constructed by hand.
- Every claim cites an artifact under `artifacts/<run_id>/` or a URL.
- Full audits contain exactly 10 experiments across all 5 pillars and reproduce
  all 17 technical checks verbatim from `technical_checks.json`.
- Expected lift is a numeric range (e.g. `+8–15%`); confidence is a percentage.
- Never assert the state of a surface the crawler did not visit (post-purchase /
  thank-you / account); label such evidence `inferred — journey stops at checkout entry`.
