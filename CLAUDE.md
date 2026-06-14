# CLAUDE.md

This file provides guidance to Claude Code when working with code in this
repository.

## Project

Qosmic Audit Harness: a generic Shopify CRO audit agent. Given any Shopify URL,
produce a full audit report with:

- an executive summary
- 10 experiments across 5 pillars
- competitor analysis
- 17 technical checks

The quality target is `docs/target_report.md`.

Reference files:

- `docs/plan.md` - architecture decisions
- `docs/README.md` - original assignment brief
- `docs/target_report.md` - calibration anchor for output quality

## Current state

Runtime and evaluator hardening are implemented, with regression coverage under
`tests/`.

Current committed validation runs:

| Store | Run ID | Crawl health | Eval |
|---|---|---|---|
| zenrojas.com | `zenrojas_20260614_ab4535` | Healthy, 10/10 sampled pages, full shopping journey | 9/9 deterministic, Layer 9 47/50 |
| beardbrand.com | `beardbrand_20260614_4df413` | Healthy, 10/10 sampled pages, full shopping journey | 9/9 deterministic, Layer 9 46/50 |

Known limitation worth stating honestly:

- `gingerpeople.com` is blocked by bot protection and should yield a truthful
  partial crawl-issues report, not a fabricated full audit.

Health policy:

- Healthy and Degraded crawls continue to a full audit.
- Degraded reports must label evidence gaps and cite `summary.md`.
- Blocked crawls produce only an honest partial crawl-issues report.

## Submission status

Submission-facing deliverables present in the repo:

- runtime harness
- eval system
- committed sample outputs
- committed cited verification artifacts for two full runs
- `AGENT_LOG.md`
- `WORKFLOWS.md`
- `EVAL_LOOP.md`

Still external to the repo:

- Loom walkthrough

## How to run

```bash
# Install dependencies
pip install -r requirements.txt
playwright install chromium

# Crawl a store
python -m crawler.crawl_store https://example-store.com

# Run the full pipeline in Claude Code
/audit https://example-store.com

# Run deterministic eval
python evals/run_eval.py <run_id>
```

Re-running is safe. Completed artifacts are reused unless `--force` is used.

## Pipeline

```text
/audit <url>
  ->
python -m crawler.crawl_store -> artifacts/<run_id>/
  ->
/page-evidence-extractor -> evidence_cards/<page>.json
  ->
/evidence-analyst -> evidence_summary.md
  ->
/audit-writer -> sample_output/<run_id>_audit.md
  ->
python evals/run_eval.py <run_id> -> eval_results/<run_id>_eval.md
  ->
/eval-judge -> Layer 9 scores appended
```

## Artifact structure

```text
artifacts/<run_id>/
  screenshots/           # one per crawled page + shopping journey screens
  pages/                 # <name>.html, <name>.md, <name>.json per page
  evidence_cards/        # <name>.json per page + shopping_journey.json
  technical_checks.json  # 17 checks
  discovered_links.json  # selected_pages, blocked pages, run_id
  summary.md             # crawl health and observed limitations
  evidence_summary.md    # store_category, use cases, findings by pillar
```

## Critical rules

- Every audit claim must cite a real `artifacts/<run_id>/...` path or a URL.
- Never invent screenshots or technical results.
- Never go past `/checkout` entry. Do not fill forms. Do not place orders.
- Full reports must have exactly four H2 sections:
  - Executive Summary
  - Proposed Experiments
  - Competitor Analysis
  - Technical Checks
- Full reports must contain exactly 10 experiments across all 5 pillars:
  Conversion, AOV, Retention, Acquisition, Performance.
- Technical statuses and details must match `technical_checks.json` verbatim.
- `run_id` must be read from `discovered_links.json`, never constructed manually.
- Competitors must be derived from `store_category`, never hardcoded.

## Eval layers

| Layer | Check |
|---|---|
| 1 | Exactly four required sections, in order |
| 2 | Exec summary is 2-3 paragraphs with diagnosis |
| 3 | Exactly 10 experiments |
| 4 | All required fields in every experiment |
| 5 | All 5 pillars present |
| 6 | Evidence paths exist on disk and under `artifacts/<run_id>/` |
| 7 | All 17 technical statuses and details match `technical_checks.json` |
| 8 | Competitor table has 3-4 rows relevant to `store_category` |
| 9 | Quality rubric - pre-filled prompt output, paste to `/eval-judge` |
| 10 | No claims about un-crawled post-purchase surfaces as observed |

## Repo notes

- `skills/` contains the canonical skill bodies.
- `.claude/skills/` contains Claude Code skill entry points.
- `evals/analyze_failures.py` and `evals/failure_log.jsonl` support the
  self-improving eval loop described in `EVAL_LOOP.md`.
- `tests/test_system.py` covers core regression behavior for the harness.
