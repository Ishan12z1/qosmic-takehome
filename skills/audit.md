# /audit

Orchestrator skill for a full Shopify CRO audit. Runs each stage in order, checking for
existing artifacts before proceeding (retry-safe). If an output artifact already exists,
skip that step and move to the next.

## Usage

```
/audit <url>
```

Example: `/audit https://zenrojas.com`

---

## Pre-flight

1. Verify `requirements.txt` dependencies are installed and `playwright install chromium` has been run.
2. Confirm the URL starts with `https://`. If not, prepend it.

---

## Step 1 — Crawl

```bash
python -m crawler.crawl_store <url>
```

- Skip if `artifacts/<slug>_*/discovered_links.json` already exists for this URL's slug.
- Use `--force` only if explicitly asked.
- On completion, read `artifacts/<run_id>/discovered_links.json` to get:
  - `run_id` — used in every subsequent artifact path
  - `selected_pages` — list of pages that were crawled

---

## Step 2 — Extract per-page evidence cards

For **each entry in `selected_pages`** plus the shopping journey:

- Check if `artifacts/<run_id>/evidence_cards/<name>.json` already exists — skip if so.
- Run `/page-evidence-extractor` with the page's artifacts as input.
- Also create `artifacts/<run_id>/evidence_cards/shopping_journey.json` from
  `artifacts/<run_id>/pages/shopping_journey.json` and the shopping journey screenshots.

All evidence cards must be saved before proceeding.

---

## Step 3 — Synthesize evidence

- Check if `artifacts/<run_id>/evidence_summary.md` already exists — skip if so.
- Run `/evidence-analyst` with all evidence cards + `technical_checks.json` as input.
- Output: `artifacts/<run_id>/evidence_summary.md`

---

## Step 4 — Write audit report

- Check if `sample_output/<run_id>_audit.md` already exists — skip if so.
- Run `/audit-writer` with `evidence_summary.md` + `technical_checks.json` as input.
- Output: `sample_output/<run_id>_audit.md`

---

## Step 5 — Evaluate

```bash
python evals/run_eval.py <run_id>
```

- Output: `eval_results/<run_id>_eval.md`
- Review the failures list. For each failed layer, fix only the affected section of the audit report.
- After fixes, re-run eval to confirm all layers pass.
- For Layer 9: the script outputs a pre-filled prompt — paste it to `/eval-judge`.

---

## Critical rules

- **Never skip the crawl step** — all downstream stages depend on `technical_checks.json`
  and the page artifacts.
- **run_id is the canonical key** — read it from `discovered_links.json`, never construct it manually.
- **Do not re-use artifacts from a different run_id.** Every evidence citation must be
  under `artifacts/<run_id>/`.
- **All 17 technical checks** must appear in the final report. Read them from
  `technical_checks.json` — never infer or guess a status.
- **Exactly 10 experiments** across all 5 pillars (Conversion, AOV, Retention, Acquisition,
  Performance). No more, no fewer.
