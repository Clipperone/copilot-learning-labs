# Module 11: Platform & GitHub.com Integration

> **Level:** Expert
> **Estimated time:** ~2 hours (theory ~1 hr · exercises ~60 min)
> **Prerequisite:** [Module 10 — Adoption Roadmap, Governance, and Capstone](../10-adoption-roadmap/) (theory + Exercises 6–7 — dashboard reading + content exclusions).
> **Verified:** 2026-04

> ⚠️ **Premium request note:** Three of the four exercises run *outside* VS Code — on github.com or in the terminal. Premium-request impact is concentrated in the Copilot coding agent (Exercise 1), which runs autonomous PR sessions. Treat coding-agent runs the same as long Agent-mode sessions: scope tightly and review the PR like any external contribution.

---

## Why This Module Exists

Modules 01–10 treat Copilot as a feature of VS Code. That framing is incomplete. Copilot is a platform with surfaces in **three places**:

1. **In the IDE** — Ask, Plan, Agent, inline chat, inline completion (Modules 01–10).
2. **In the terminal** — `gh copilot suggest` and `gh copilot explain`.
3. **In github.com** — PR summaries, "Copilot review", issue summarization, and the **Copilot coding agent** that turns issues into PRs autonomously.

A developer who only uses the IDE surface misses half the productivity gain available on a Pro+ plan. A team that ships work via PRs but does not use Copilot in the PR review flow leaves the largest single-point-of-leverage feature unused.

This module covers the non-IDE surfaces and teaches one thing above all: **the same Read → Run → Reason → Risk discipline applies on every surface**. The affordances change. The discipline does not.

---

## Learning Objectives

By the end of this module, you will be able to:

1. Delegate a bounded issue to the Copilot coding agent and review its PR end-to-end as you would review any external contribution.
2. Use Copilot in github.com for PR summaries, PR review comments, and issue triage.
3. Use the `gh copilot` CLI for command suggestion and explanation; integrate it into shell workflows responsibly.
4. Recognize what each surface (VS Code / github.com / CLI / Coding agent) is best at; choose the right one per task.
5. Apply the same critical-review discipline (Read → Run → Reason → Risk) on non-IDE surfaces.

---

## The Three Non-IDE Surfaces

### 1. Copilot coding agent (issue → PR)

The Copilot coding agent is an autonomous agent that picks up an issue you assign to it and produces a draft PR. It runs in a sandboxed environment, branches off main, makes commits, and opens the PR for human review. You do not watch it work — you delegate, then review.

**Best for:** small, well-scoped, low-risk changes where the acceptance criteria are mechanical (rename, dependency upgrade, test addition, lint fix, small bugfix with a failing test attached).

**Wrong for:** design decisions, security-sensitive changes, large refactors, anything where the acceptance criteria require human judgment.

**Treat the resulting PR like an external contributor's PR.** It is not "your" PR just because you opened the issue. Review the diff, run the tests locally, ask follow-up questions in the PR thread (the agent responds).

### 2. Copilot in github.com

Three surfaces inside the GitHub web UI, all with different review gates:

| Surface | What it produces | Review gate |
|---------|-----------------|-------------|
| PR summary (auto or on-demand) | Prose summary of the diff | Read before clicking merge; rewrite if it omits the *why* |
| Copilot review | Inline review comments on a PR diff | Same triage as a Code Reviewer session (M08): severity, location, fix |
| Issue summarization | Prose summary of long issue threads | Useful for triage; do not use as a substitute for reading an issue you are about to act on |

PR summaries are the highest-leverage feature for teams. A consistent summary format makes review faster for everyone.

### 3. `gh copilot` CLI

Two commands that wrap the Copilot model for terminal use:

```bash
gh copilot suggest "find files modified in the last 24 hours, larger than 1MB, excluding node_modules"
gh copilot explain "git log --since='2 weeks ago' --pretty=format:'%h %an %s' | grep -i fix | wc -l"
```

**`suggest`** generates a shell command from a description.
**`explain`** describes what an existing command does.

Both are subject to the same 4-question gate from Module 08 (`@terminal` discipline): does it do what was asked? what side effects? is it reversible? is the cost acceptable?

The CLI is best for one-off shell tasks during interactive work. **It is wrong for CI scripts** — generated commands need human review before they enter automation.

---

## Surface Decision Matrix

| Task | Best surface | Why |
|------|-------------|-----|
| Refactor across known files | VS Code (Agent mode, M08) | Per-file diff review, working-set discipline |
| Explore an unfamiliar codebase | VS Code (`@workspace`, M03) | Semantic index over the repo |
| Summarize a PR you are about to merge | github.com (PR summary) | Lives where the merge happens |
| Review a colleague's PR for mechanical issues | github.com (Copilot review) | Inline comments at line precision |
| Triage 30 unread issues | github.com (issue summarization) | Reduces reading time without losing the option to read deeply |
| Pick up a small mechanical issue from the backlog | Copilot coding agent | Autonomous; you review the PR not the process |
| Generate a one-off shell command | `gh copilot suggest` | Faster than opening the IDE chat panel |
| Explain a teammate's complex shell pipeline | `gh copilot explain` | Faster than reading `man` pages |
| Design a new feature | VS Code (Plan mode, M08) | Reversible, no tool calls, structured output |
| Implement a multi-step feature with tool calls | VS Code (Agent mode + workflow, M07) | Multi-agent workflow keeps scope bounded |

---

## Common Mistakes

| Mistake | Why it happens | How to fix it |
|---------|----------------|---------------|
| Asking the same question on three surfaces | Forgetting where you started; treating each surface in isolation | Pick the surface, finish the task there, move on |
| Using the coding agent for design tasks | Coding agent feels like "more autonomy" — confused with capability | Coding agent is for mechanical work; design belongs in Plan mode (Module 08) |
| Trusting coding-agent PRs without local verification | The PR looks polished; tests pass in the sandbox | Pull the branch locally, run tests, read the diff like an external contribution |
| Pasting `gh copilot suggest` output into a shell script without review | The suggestion looked right; "saved time" | Run it interactively first; commit only after you understand it |
| Auto-generating PR summaries and never reading them | Summary appears; merge button feels close | Summary is a draft for *your* review — rewrite it before clicking merge |
| Copilot review treated as a green light to merge | "If Copilot didn't flag it, it's fine" | Copilot review is a first-pass filter; human review is still required |

---

## Best Practices

- **Do:** Treat the coding agent's PR as an external contribution with all the trust implications that implies.
- **Do:** Use PR summaries as a first draft for *you* to revise; the *why* is yours to write.
- **Do:** Make the surface choice explicit at the start of a task; avoid mid-task surface-switching.
- **Don't:** Delegate issues to the coding agent if you cannot precisely state acceptance criteria.
- **Don't:** Use `gh copilot suggest` output in CI scripts without explicit review and version-pinning.
- **Don't:** Use Copilot review as a substitute for human review on security-sensitive PRs.

---

## Token / Premium Request Impact

| Action | Cost level | Notes |
|--------|-----------|-------|
| `gh copilot suggest` / `explain` | Low | Single-turn chat-equivalent; counts against your usage if premium model selected |
| github.com PR summary | Low–Medium | Produced once per PR; auto vs. on-demand depends on org settings |
| github.com Copilot review | Medium | Reviews entire diff; cost scales with diff size |
| Issue summarization | Low | Single chat-equivalent turn |
| Copilot coding agent run | High | Autonomous multi-step session; can equal a long Agent mode session in cost |

**Rule of thumb:** the coding agent is the only one of these that can surprise you on cost. Scope issues tightly before delegating.

---

## Completion Criteria

You have completed this module when you can:

- [ ] Delegate one issue to the coding agent and produce a reviewed PR (Exercise 1).
- [ ] Generate and rewrite one PR summary on github.com (Exercise 2).
- [ ] Run `gh copilot suggest` for at least 3 shell tasks and apply the 4-question gate to each (Exercise 3).
- [ ] Pick the right surface for 6 task descriptions and justify each choice (Exercise 4).

See [checklist.md](./checklist.md) for the full self-assessment.

---

## Files in This Module

| File | Purpose |
|------|---------|
| `README.md` | Module overview (this file) |
| `theory.md` | Extended reference — coding agent lifecycle, github.com surfaces, CLI patterns, surface decision rationale |
| `exercises.md` | All 4 exercises with full instructions and expected answers |
| `checklist.md` | Completion checklist and self-assessment |

---

## Related Capstone Deliverable

This module adds **Deliverable 8** to the capstone: one platform artifact — either a coding-agent PR with your review notes, or a configured content-exclusion + github.com PR review combo. See [capstone/README.md](../../capstone/README.md).

---

## Next

→ [Capstone](../../capstone/) — Deliverable 8 (platform artifact) is added in this module.
