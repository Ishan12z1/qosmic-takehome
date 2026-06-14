# /audit

Orchestrate a full CRO audit from crawl through evaluation. Keep the pipeline
retry-safe, but do not let an existing artifact bypass a stricter verification
step if that artifact is clearly stale, contradictory, or below the current
skill contract.

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

## Step 1 - Crawl

```bash
python -m crawler.crawl_store <url>
```

- Skip if `artifacts/<slug>_*/discovered_links.json` already exists for this URL's slug.
- Use `--force` only if explicitly asked.
- On completion, read `artifacts/<run_id>/discovered_links.json` to get:
  - `run_id` - used in every subsequent artifact path
  - `selected_pages` - list of pages that were crawled

---

## Step 2 - Apply crawl-health policy

Read `artifacts/<run_id>/summary.md`.

- **Blocked:** write an honest `Partial Audit - Crawl Issues` report using only
  `summary.md`, `discovered_links.json`, and `technical_checks.json`; do not create
  a full ten-experiment audit.
- **Healthy or Degraded:** continue through the full pipeline. For Degraded runs,
  cite `summary.md`, preserve uncertainty, and never make claims about missing
  surfaces that were not crawled.

---

## Step 3 - Extract per-page evidence cards

For each entry in `selected_pages` plus the shopping journey:

- Check if `artifacts/<run_id>/evidence_cards/<name>.json` already exists - skip if so.
- Run `/page-evidence-extractor` with the page artifacts as input.
- Also create `artifacts/<run_id>/evidence_cards/shopping_journey.json` from
  `artifacts/<run_id>/pages/shopping_journey.json` and the shopping journey screenshots.

All evidence cards must be saved before proceeding.

---

## Step 4 - Synthesize evidence

- Check if `artifacts/<run_id>/evidence_summary.md` already exists - skip if so.
- Run `/evidence-analyst` with all evidence cards + `technical_checks.json` as input.
- Output: `artifacts/<run_id>/evidence_summary.md`

### Evidence QA gate

Before moving to report writing, inspect `evidence_summary.md` for these failure modes:

- universal language without full support: `all`, `every`, `none`, `always`, `never`
- mixed evidence collapsed into a single-direction claim
- visible UI claims backed only by metadata when a screenshot exists
- cart claims backed by an empty-cart screenshot when populated journey evidence exists
- broad claims not reflected in the `Evidence gaps and uncertainty` section

If any of those appear, revise `evidence_summary.md` before writing the audit.

---

## Step 5 - Write audit report

- Check if `sample_output/<run_id>_audit.md` already exists - skip if so.
- Run `/audit-writer` with `evidence_summary.md` + `technical_checks.json` as input.
- Output: `sample_output/<run_id>_audit.md`

### Report QA gate

Before treating the report as finished, verify:

1. Each major diagnosis claim is backed by the strongest available artifact.
2. Any claim framed as missing, absent, or empty is not contradicted by another sampled page.
3. Any claim using universal language is supported across all sampled relevant pages.
4. Any page-specific URL is paired with evidence from that page, or the report explicitly labels the claim as a cross-page pattern.

If the report passes eval but fails this QA gate, fix the report anyway. A passing deterministic eval is necessary, not sufficient.

---

## Step 6 - Evaluate

```bash
python evals/run_eval.py <run_id>
```

- Output: `eval_results/<run_id>_eval.md`
- Review the failures list. For each failed layer, fix only the affected section of the audit report.
- After fixes, re-run eval to confirm all layers pass.
- For Layer 9: the script outputs a pre-filled prompt - paste it to `/eval-judge`.

---

## Critical rules

- Never skip the crawl step - all downstream stages depend on `technical_checks.json`
  and the page artifacts.
- `run_id` is the canonical key - read it from `discovered_links.json`, never construct it manually.
- Do not re-use artifacts from a different run ID. Every evidence citation must be
  under `artifacts/<run_id>/`.
- Full audits include all 17 technical checks. Read them from
  `technical_checks.json` - never infer or guess a status.
- Full audits include exactly 10 experiments across all 5 pillars: Conversion,
  AOV, Retention, Acquisition, Performance.
