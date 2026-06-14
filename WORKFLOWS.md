# WORKFLOWS.md

## How I use coding agents day to day

My best coding-agent sessions usually start with planning. Before asking an agent to write code, I first break the project into smaller steps. Each step should connect to a real part of the system, such as a component, API route, workflow, evaluation script, or user-facing behavior.

For each step, I try to define the goal clearly. I write down what the input should be, what the output should be, what edge cases matter, and how I will know the step is done. This helps the agent stay focused and makes it easier for me to review the result later.

Before implementation, I usually run `/plan-review`. I use it to pressure-test the plan. I ask the agent to find vague requirements, missing cases, weak assumptions, and places where the design could fail. When the plan feels unclear, I improve the plan before moving into code.

My usual stack is Claude Code, Codex-style coding agents, repo-level context files like `CLAUDE.md` or `AGENTS.md`, and GitHub MCP. The context files are how I carry useful project state across sessions; GitHub MCP handles repo-related workflows like PRs, issues, and reviews. I also use small reusable commands instead of relying on one long prompt.

The two commands I use the most are `/plan-review` and `/code-critique`. `/plan-review` helps before coding starts. `/code-critique` helps after implementation, when I want the agent to review the code like a skeptical PR reviewer. I also have a custom skill for pushing code to GitHub in the style I prefer. It checks the changed files, summarizes what changed, and helps create clean commits that are easy to understand later.

During implementation, I usually keep the agent on one step or substep at a time. If a task starts getting too broad, I split it down further. Before larger edits, I ask the agent which files it expects to touch and why. This keeps the diff easier to review and makes it easier to catch when the agent is drifting away from the original goal.

After each step, I ask for a short handoff summary. I want to know what changed, why it changed, which files were updated, what was tested, and what still looks risky. These summaries are useful when I come back to a project later or start a new agent session.

I use agents heavily for first drafts, smaller implementation pieces, refactors, tests, documentation, repo exploration, and repetitive GitHub workflows. For architecture, safety-sensitive behavior, evaluation design, and large changes that affect many parts of the system, I stay closely involved and make the final call myself.

My general rule is simple. The agent can move quickly once the task is bounded, but the plan, acceptance criteria, review, and final judgment stay with me. That balance lets me delegate a lot of the execution while still keeping the project under control.
