# Qosmic Audit Harness

A runtime harness that turns any coding agent (Claude Code / Codex) into a Qosmic
CRO audit agent, plus a self-improving eval system around it. Point it at any
Shopify storefront URL and it produces a structured CRO audit: executive summary,
10 experiments across 5 pillars, competitor analysis, and 17 technical checks,
at the quality bar of `docs/target_report.md`.

> Built for the Qosmic founding-engineer take-home (`docs/README.md`). The eval
> loop is the headline; the runtime harness is the substrate it improves.

---

## The thesis

A few humans steering agents, reliably. So the design is deliberately a thin,
deterministic spine (crawler + fail-closed evaluator in Python) wrapping a
reasoning layer expressed as skills (the parts that benefit from a model).
Quality improves by tightening the evaluator and the skills, not by hand-editing
reports.

```text
/audit <url>
  -> crawler (Python)        -> artifacts/<run_id>/      # deterministic capture
  -> page-evidence-extractor -> evidence_cards/*.json    # per-page cited evidence
  -> evidence-analyst        -> evidence_summary.md      # store-level synthesis
  -> audit-writer            -> sample_output/<run_id>_audit.md
  -> run_eval.py             -> eval_results/<run_id>_eval.md  (Layers 1-8, 10 + Layer 9 prompt)
  -> eval-judge              -> Layer 9 quality rubric appended
```

The crawl, evidence capture, and evaluation are deterministic and scriptable. The
three reasoning stages are skills an agent drives. Re-running is safe: completed
artifacts are reused, and `--force` starts fresh.

---

## Quick start

```bash
# 1. Install dependencies (once)
pip install -r requirements.txt
playwright install chromium

# 2. Crawl a store (creates artifacts/<run_id>/)
python -m crawler.crawl_store https://zenrojas.com

# 3. Run the deterministic eval on a run
python evals/run_eval.py <run_id>
```

Steps 2-3 are the deterministic spine you can run standalone. The full audit
(steps that need a reasoning agent) is driven inside Claude Code:

```text
/audit https://zenrojas.com
```

This orchestrates the whole pipeline: crawl, per-page evidence extraction,
synthesis, report writing, and eval, invoking the skills in `.claude/skills/`.
To run the reasoning stages individually: `/page-evidence-extractor`,
`/evidence-analyst`, `/audit-writer`, then `/eval-judge` for Layer 9.

---

## Crawl health policy

The crawler classifies every run and the harness reacts accordingly:

| Verdict | Behavior |
|---|---|
| **Healthy** | Full audit produced |
| **Degraded** | Full audit produced, but every evidence gap is labeled and `summary.md` is cited |
| **Blocked** | No fabricated audit - only an honest "Partial Audit - Crawl Issues" report |

This is why the harness generalizes safely: a bot-protected store yields an
honest partial report instead of invented findings.

---

## The eval system

`evals/run_eval.py` is fail-closed: any deterministic failure returns non-zero
and blocks the Layer 9 quality score. Layers:

| Layer | Check |
|---|---|
| 1 | Exactly four required sections, in order |
| 2 | Exec summary is 2-3 paragraphs with a diagnosis |
| 3 | Exactly 10 experiments |
| 4 | All required fields present; numeric expected-lift and confidence |
| 5 | All 5 pillars present |
| 6 | Every evidence path exists on disk and under the correct `run_id` |
| 7 | All 17 technical statuses + details match `technical_checks.json` verbatim |
| 8 | Competitor table has 3-4 rows relevant to the store category |
| 9 | 10-dimension quality rubric (`/eval-judge`, scored 1-5, /50) |
| 10 | No experiment asserts an un-crawled post-purchase surface as observed |

Each unique failure is appended once to `evals/failure_log.jsonl`, and
`evals/analyze_failures.py --min-runs 3` only proposes skill changes when a
failure repeats across distinct stores, so one bad run cannot inflate the signal.
The path from here to an autonomous, self-learning loop is in `EVAL_LOOP.md`.

---

## Repository map

| Path | What it is |
|---|---|
| `crawler/` | Modular Playwright crawler (URL discovery, page capture, technical checks, safe shopping journey) |
| `skills/` | Canonical skill bodies (progressive-disclosure instructions) |
| `.claude/skills/` | Claude Code skill entry points (`audit`, `page-evidence-extractor`, `evidence-analyst`, `audit-writer`, `eval-judge`) |
| `evals/` | `run_eval.py`, `rubric.md`, `analyze_failures.py`, `failure_log.jsonl` |
| `CLAUDE.md`, `AGENTS.md` | Entry-point context files for the agent |
| `sample_output/` | Generated audit reports |
| `eval_results/` | Eval outputs, including Layer 9 rubric scores |
| `artifacts/<run_id>/` | Crawl artifacts: screenshots, page HTML/MD/JSON, evidence cards, technical checks |
| `tests/` | Regression tests for crawler and evaluator behavior |
| `docs/` | Assignment brief, `target_report.md` calibration anchor, build plan, eval site list |
| `EVAL_LOOP.md` | How the eval system becomes autonomous and self-learning |
| `AGENT_LOG.md` | Time per part, prompts fed, where the agent drove vs. where I steered |
| `WORKFLOWS.md` | How I use coding agents day-to-day |

---

## Validation runs

Two full verification bundles are committed so a reviewer can follow citations
all the way back to the underlying artifacts.

| Store | Run ID | Crawl health | Deterministic eval | Layer 9 |
|---|---|---|---|---|
| zenrojas.com | `zenrojas_20260614_ab4535` | Healthy, 10/10 sampled pages, full journey | 9/9 layers passed | 47/50 |
| beardbrand.com | `beardbrand_20260614_4df413` | Healthy, 10/10 sampled pages, full journey | 9/9 layers passed | 46/50 |

Reviewer-friendly entry points:

- `sample_output/zenrojas_20260614_ab4535_audit.md`
- `eval_results/zenrojas_20260614_ab4535_eval.md`
- `sample_output/beardbrand_20260614_4df413_audit.md`
- `eval_results/beardbrand_20260614_4df413_eval.md`

---

## Design constraints

- Cite everything. Every audit claim resolves to an `artifacts/<run_id>/...`
  path or a URL.
- No hallucination. A check that was not performed is `Warn`, never `Pass`.
- No hardcoding. No store, competitor, or category logic in code or skills;
  `store_category` is inferred from crawled evidence.
- Safe journey. The shopping journey stops at the checkout entry; it never
  fills forms or places orders.
- Generalizes. The harness is run against stores it has never seen; the test
  matrix is in `docs/eval_website_list.md`.
