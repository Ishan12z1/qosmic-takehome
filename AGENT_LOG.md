# AGENT_LOG.md

How this harness was built with a coding agent (Claude Code), what the agent
drove, and where I took the wheel.

> Times below are **active hands-on steering** - the time I was engaged
> (reading, deciding, prompting, verifying), not wall-clock. Because the agent
> ran asynchronously while I reviewed, the work was spread across a few evenings;
> the brief allows turning it around over a few days, and the effort total stays
> within the stated hard ceiling.

## Time By Part

| Part | Time spent | Notes |
|---|---:|---|
| Part 1 - Runtime harness (crawler + skills + entry files) | ~2h | Modular crawler, 5 registered skills, CLAUDE.md / AGENTS.md |
| Part 2 - Eval system + autonomy plan | ~2h | 9 deterministic layers + LLM rubric, degraded mode, failure-log loop |
| Validation & packaging | ~1h | Multi-store runs, integrity fixes, sample outputs |
| Total | ~5h | At the stated hard ceiling |

## How I Worked

I drove the agent in tight, verifiable loops rather than one large prompt: set a
goal, have the agent implement, then make it prove each change before moving on.
The highest-leverage thing I did was hold the quality bar - I fed the agent a
detailed critique and made it verify every finding against the code before
fixing anything, so fixes were grounded in real defects, not guesses.

## Agent Prompts And Decisions

| Prompt / task I gave | What the agent drove | Where I took the wheel |
|---|---|---|
| "Read the repo and tell me the real current status: what is implemented, what is missing, and what looks broken." | Read the repo, mapped the pipeline, and summarized completed phases plus the highest-risk gaps. | Used that inventory to choose where to spend the remaining time. |
| "Build the crawler first. It needs to crawl a representative Shopify journey safely, stop at checkout entry, and save reusable artifacts." | Implemented and iterated on the crawler modules, URL discovery, technical checks, and shopping journey capture. | Set the safety boundary and held the line on not going past checkout. |
| "Write the skills next: page evidence extraction, evidence synthesis, audit writing, and eval judging." | Drafted the skill files and shaped the per-page -> summary -> audit pipeline. | Decided the skill boundaries and what each stage was and was not allowed to claim. |
| "Add a fail-closed eval. I want exact section checks, exact experiment counts, evidence-path validation, and technical-check fidelity." | Built the deterministic eval layers and the quality-rubric flow around them. | Chose the contract details that were important enough to gate the output. |
| "Check this critique against the code and tell me which points are real, which are wrong, and what else we are missing." | Verified each critique finding line-by-line against the actual implementation and surfaced additional issues. | Supplied the critique as the review bar and decided which findings mattered most. |
| "Fix all confirmed issues, but do it step by step. Also write a `summary.md` whenever a site is unreachable or blocked." | Produced a phased plan and implemented fixes across crawler, skills, and evals. | Added the requirement that blocked or unreachable runs must still leave an honest machine-readable record. |
| "After every meaningful change, run the relevant checks before moving on." | Re-ran tests, crawl flows, and evals after each batch of changes. | Enforced the verification cadence instead of letting the work drift into one big untested rewrite. |
| "I deleted the old artifacts. Re-run a few stores end-to-end and tell me what still breaks in practice." | Re-ran the system on multiple stores, surfaced a variant-selection gap and a CORS issue, then fixed and re-verified them. | Forced a clean-slate validation pass to expose issues hidden by stale artifacts. |
| "Do not hand-edit outputs. If a report is wrong, fix the pipeline or the skills, then regenerate it." | Regenerated reports through the pipeline after fixes instead of patching markdown outputs directly. | Set the rule that output quality had to come from the harness, not manual cleanup. |
| "Check the final system against the assignment README and tell me exactly where we match it and where we still fall short." | Mapped the implementation and outputs back to the assignment contract and produced a conformance review. | Judged the remaining gaps, especially around packaging, blocked-site handling, and submission framing. |
| Agent-initiated scoping questions during implementation | Implemented to the chosen scope after asking for decisions when tradeoffs were non-obvious. | **Decided:** real mobile/page-speed checks instead of hardcoded Warns; regenerate reports only through the pipeline; package blocked sites as honest partial audits instead of forcing full reports. |
| Tightened one contract edge manually | - | **Hand-edited `run_eval.py` and the writer skill** to enforce exactly four README sections, in order. |

## Decisions I Would Reverse

When the headless journey can't select a required product variant, I have it add
to cart via Shopify's `/cart.js` / `/cart/add.js` API as a fallback. This made
cart/checkout reachability reliable across stores, but it trades away some
pure-UX-simulation fidelity - a real shopper's variant-selection friction is no
longer fully exercised. I would revisit this to detect and report that friction
explicitly instead of routing around it.

## What I Did Not Measure

- **Real Core Web Vitals.** Page speed is a single-run navigation-timing proxy,
  clearly labeled as such - not a Lighthouse or field measurement.
- **Visual correctness of citations.** Citations are verified to resolve, sit
  under the correct run_id, and some contradiction cases are checked - but the
  system does not perform exhaustive human visual verification of every cited
  screenshot.
- **Live competitor benchmarks.** Competitors are selected by category and cited
  by URL, not crawled and measured the way the audited store is.
