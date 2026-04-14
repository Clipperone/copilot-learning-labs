# Module 11: Platform & GitHub.com Integration — Completion Checklist

Use this checklist after completing the module theory and all 4 exercises, and before claiming Capstone Deliverable 8.

---

## Coding Agent

- [ ] I can name the 5 lifecycle phases of a coding-agent run and the most common failure in each.
- [ ] I can state the 5 properties of a delegatable issue (one acceptance criterion, bounded files, no design ambiguity, no security exposure, reversible).
- [ ] I can run the 5-step PR review protocol on a coding-agent PR (pull, read, run, scope-check, verify commits).
- [ ] I know what `.github/copilot-setup-steps.yml` does and when to add one.
- [ ] I completed Exercise 1 — wrote a delegatable issue, assigned it, reviewed the PR, and made a merge/reject decision with reasoning.

## Copilot in github.com

- [ ] I can name the 4 properties of a useful PR summary (what changed, why, what did NOT change, risk surface).
- [ ] I can triage a Copilot review comment as actionable or not, using the same gate as M08 Code Reviewer findings.
- [ ] I know when issue summarization helps (long stale threads) and when it hurts (issues I'm about to act on).
- [ ] I completed Exercise 2 — generated a PR summary, scored it, and rewrote it to include all 4 properties.

## `gh copilot` CLI

- [ ] I have `gh copilot suggest` and `gh copilot explain` available locally.
- [ ] I apply the M08 4-question gate (does what asked / side effects / reversible / cost) before running any suggested command.
- [ ] I know why `gh copilot suggest` output should NOT enter CI scripts without explicit review.
- [ ] I completed Exercise 3 — ran 3 shell-task suggestions and classified each (run / verify / discard) with reasoning.

## Surface Decision

- [ ] I can name what each of the 4 surfaces (VS Code / github.com / CLI / coding agent) is best at, in one sentence each.
- [ ] I can pick the right surface for a task without falling back to "the IDE for everything".
- [ ] I know that design tasks belong in Plan mode, not in the coding agent.
- [ ] I completed Exercise 4 — assigned 6 task descriptions to surfaces with one-sentence justifications.

## Cross-Surface Discipline

- [ ] I do not re-ask the same question on multiple surfaces; I pick one and finish.
- [ ] I treat coding-agent PRs as external contributions — full review every time.
- [ ] I rewrite auto-generated PR summaries before merging, never accepting them as-is.
- [ ] I never use Copilot review as the sole gate on security-sensitive PRs.

---

## Ready for Capstone Deliverable 8?

All items above checked → proceed to [capstone/README.md](../../capstone/README.md) and complete **Deliverable 8 — platform artifact** (Option A: coding-agent PR with review notes, OR Option B: `copilot-setup-steps.yml` + rewritten PR summary).

Not all items checked → return to [exercises.md](./exercises.md) for the specific area you want to reinforce.

---

## Module Complete

→ Capstone deliverable: [capstone/README.md](../../capstone/README.md) — Deliverable 8
→ Expert self-assessment: [checklists/expert-completion.md](../../checklists/expert-completion.md)
