# AGENT_LOG.md

How this harness was built with a coding agent (Claude Code), what the agent
drove, and where I took the wheel.

> Time numbers below are mine to fill in from my actual sessions — replace each
> `TODO` with the real figure before submission.

## Time By Part

| Part | Time spent | Notes |
|---|---:|---|
| Part 1 — Runtime harness (crawler + skills + entry files) | TODO | Modular crawler, 5 registered skills, CLAUDE.md / AGENTS.md |
| Part 2 — Eval system + autonomy plan | TODO | 9 deterministic layers + LLM rubric, degraded mode, failure-log loop |
| Validation & packaging | TODO | Multi-store runs, integrity fixes, sample outputs |
| Total | TODO | Within the stated hard ceiling |

## How I Worked

I drove the agent in tight, verifiable loops rather than one large prompt: set a
goal, have the agent implement, then make it prove each change before moving on.
The highest-leverage thing I did was hold the **quality bar** — I fed the agent a
detailed code-review critique and made it verify every finding against the code
before fixing anything, so fixes were grounded in real defects, not guesses.

## Agent Prompts And Decisions

| Prompt / task I gave | What the agent drove | Where I took the wheel |
|---|---|---|
| "What's the current status of the project?" | Read the repo and summarized state, completed phases, and open gaps | Used the summary to decide where to focus next |
| "Run the eval website list… just do Type B" | Crawled and audited a Type B store end-to-end through the pipeline | Scoped the work down to Type B instead of all 17 sites |
| Pasted a detailed code-review critique: "check if this is correct, and are we missing more — thoroughly" | Verified all critique findings line-by-line against the actual code; confirmed which were real and found additional gaps | Supplied the critique as the explicit quality bar to audit against |
| "Fix all of these issues — make a step-by-step plan; also write a summary.md for unreachable sites" | Produced a phased plan and implemented every fix across crawler, skills, and evals | Defined the requirements, including the always-on `summary.md` for broken/blocked sites |
| Three scoping decisions (asked by the agent) | Implemented to spec | **Decided:** real mobile/page-speed checks (not hardcoded Warns); regenerate reports only by running the pipeline (never hand-edited); leave artifact handling as-is |
| "Check each update after you make it, before moving forward" | Compile/unit-tested and re-ran the pipeline after every change | Imposed the incremental-verification cadence |
| "I deleted all artifacts — run 2–3 sites to confirm it does what we want" | Ran several stores end-to-end; surfaced a real journey gap (variant selection) and a CORS bug, then fixed and re-verified both | Forced a clean-slate validation that exposed the gaps |
| Tightened the report contract myself | — | **Hand-edited `run_eval.py` and the writer skill** to enforce exactly four README sections, in order |
| "Check it against the README — does what we built match?" | Mapped each requirement to evidence and produced a conformance assessment | Judged the result and the remaining gaps |

## Decisions I Would Reverse

When the headless journey can't select a required product variant, I have it add
to cart via Shopify's `/cart.js` / `/cart/add.js` API as a fallback. This made
cart/checkout reachability reliable across stores, but it trades away some
pure-UX-simulation fidelity — a real shopper's variant-selection friction is no
longer fully exercised. I would revisit this to detect and report that friction
explicitly instead of routing around it.

## What I Did Not Measure

- **Real Core Web Vitals.** Page speed is a single-run navigation-timing proxy,
  clearly labeled as such — not a Lighthouse/field measurement.
- **Visual correctness of citations.** Citations are verified to resolve, sit
  under the correct run_id, and match the claim's artifact type — but I did not
  confirm that each screenshot visually proves its specific claim.
- **Live competitor benchmarks.** Competitors are selected by category and cited
  by URL, not crawled and measured the way the audited store is.
