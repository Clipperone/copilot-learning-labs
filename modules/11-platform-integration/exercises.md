# Module 11 — Exercises

These exercises run mostly **outside VS Code**. You will need: a sandbox repo on github.com you control, the `gh` CLI installed and authenticated, and access to the Copilot coding agent (Pro+/Business/Enterprise; check your plan).

Complete all 4 exercises before claiming Module 11 complete. Capstone Deliverable 8 references this module.

---

## Exercise 1 — Delegate One Issue to the Copilot Coding Agent

**Objective:** Scope, delegate, and review one bounded issue end-to-end.

**Setup:**

1. Use a sandbox repo you control (or fork a small open-source project — your choice).
2. Confirm your account/plan has access to the coding agent.
3. Optional: add `.github/copilot-setup-steps.yml` if your tests need anything beyond the default sandbox.

**Pick a delegatable issue.** A good first issue:

- Has a single acceptance criterion that can be checked by running a command (e.g., a failing test that should pass).
- Touches a bounded set of files (≤3).
- Has no design ambiguity.
- Is reversible — if the agent gets it wrong, rejecting the PR loses nothing.

**Bad first-issue examples (do not pick):** "redesign the auth module"; "improve performance"; "add tests" (too vague — name *which* tests); anything OWASP-relevant; anything where the right answer requires a meeting.

**Task:**

1. Write the issue. It must contain:
   - One sentence stating the change.
   - One sentence stating the acceptance criterion (e.g., *"`pytest tests/test_parse.py::test_handles_empty_input` passes"*).
   - The file(s) likely to change.
   - An explicit out-of-scope statement (mirrors M08 Plan-mode discipline).
2. Assign the issue to Copilot.
3. Wait for the draft PR. Note the time the agent took.
4. Review the PR using the 5-step protocol from `theory.md` (pull locally, read diff, run acceptance criterion, check out-of-scope edits, verify commits).
5. Either approve and merge, or close with feedback. **Do not** approve an agent PR you have not pulled locally.

**Deliverable:** A short note (`exercise-1-coding-agent.md` in your scratch dir or repo) with:

- The issue text you wrote.
- The PR URL.
- The 5-step review notes.
- Your decision (merged / rejected) and reasoning.

**Self-check:**

- [ ] Acceptance criterion was a verifiable observation, not a feeling.
- [ ] You pulled the branch locally before approving.
- [ ] You checked for out-of-scope file modifications.
- [ ] If you rejected, the rejection comment explained what was missing — not just "no thanks".

> **Anti-pattern check:** If you found yourself thinking "well, the tests pass, ship it" without reading the diff — close this PR and re-run the exercise. The whole point of the review gate is the diff read.

---

## Exercise 2 — Generate and Rewrite One PR Summary

**Objective:** Treat auto-generated PR summaries as drafts that you finish, not artifacts to accept blindly.

**Setup:** A PR you can summarize — your own from Exercise 1, a teammate's, or one in a sandbox repo. Avoid PRs containing sensitive data.

**Task:**

1. Generate the PR summary using github.com's Copilot summary feature.
2. Read the auto-generated text. Score it against the 4-property checklist:
   - **What changed** — files and high-level grouping. Usually present.
   - **Why it changed** — motivating issue, user impact. Usually thin.
   - **What did NOT change** — explicit out-of-scope. Usually missing.
   - **Risk surface** — what to test or watch after merge. Usually missing.
3. Rewrite the summary to include all 4 properties. Replace the auto-summary with your version.
4. Save both versions (auto and rewritten) to `exercise-2-pr-summary.md`.

**Self-check:**

- [ ] Your rewritten summary names at least one thing the PR did NOT change.
- [ ] Your rewritten summary names at least one risk surface (test to run, area to watch).
- [ ] Length is shorter than auto-version, not longer (rewriting prunes; it should not bloat).
- [ ] A teammate reading only your summary could confidently approve or push back.

> **Anti-pattern check:** If your rewritten summary just adds emoji and bold to the auto-version, you have not rewritten — you have decorated. Try again.

---

## Exercise 3 — `gh copilot` for Three Shell Tasks

**Objective:** Apply the M08 4-question gate to CLI-generated commands.

**Setup:** Install `gh-copilot` if needed: `gh extension install github/gh-copilot`.

**Task:** Run `gh copilot suggest` for each of these shell tasks. For each: capture the suggested command, decide (run / verify-first / discard), and write one-sentence reasoning grounded in the 4-question gate.

| # | Task |
|---|------|
| 1 | Find files modified in the last 7 days, larger than 1MB, excluding `node_modules` and `.git`. |
| 2 | Delete all `__pycache__` directories recursively from the current directory. |
| 3 | Force-push the current branch to overwrite `origin/main`. |

**Self-check / expected reasoning:**

| # | Likely decision | Reason (one sentence) |
|---|----------------|----------------------|
| 1 | Run | Read-only `find`; no side effects; matches the request. |
| 2 | Verify first | Side effect (deletion) but reversible (regenerates on next Python run); confirm the working directory before running. |
| 3 | Discard | Irreversible to collaborators; failing the M08 4-question gate on accountability and reversibility. Never run an AI-suggested force-push on a shared branch. |

**Deliverable:** Save the three suggested commands and your reasoning to `exercise-3-cli.md`.

> **Anti-pattern check:** Running suggestion #3 because it "did what was asked" is the structural failure. The 4-question gate asks more than that.

---

## Exercise 4 — Surface Decision

**Objective:** Choose the best surface for 6 task descriptions; justify each.

**Task:** For each task below, name the best surface (VS Code mode / github.com / `gh copilot` CLI / Coding agent) and write one-sentence justification grounded in the surface decision matrix from [README.md](./README.md#surface-decision-matrix).

| # | Task |
|---|------|
| 1 | Refactor a 200-line function across `service.py`, `model.py`, and the corresponding tests. |
| 2 | Bump the `requests` library from 2.28 to 2.32 across `requirements.txt` + lockfile + remove deprecated kwarg uses. |
| 3 | Triage 40 stale issues that have not been touched in 6 months. |
| 4 | Explain a teammate's bash one-liner that uses `awk` and `xargs`. |
| 5 | Design the schema for a new `audit_log` table; decide partitioning, indexing, retention. |
| 6 | Generate the PR description for a feature you just finished implementing locally. |

**Expected answers:**

| # | Surface | Reason |
|---|---------|--------|
| 1 | VS Code Agent mode (M08 Edits-style discipline) | Coordinated multi-file edit on a known scope; per-file diff review needed. |
| 2 | Copilot coding agent | Mechanical, bounded, well-defined acceptance (lockfile valid + tests pass + no deprecated kwargs); ideal delegation candidate. |
| 3 | github.com issue summarization | Lives where the issues are; cuts triage time without losing the option to read deeply. |
| 4 | `gh copilot explain` | One-off CLI explanation; faster than opening IDE chat for a single command. |
| 5 | VS Code Plan mode (M08) | Design decision; reversible structured output; not a delegation candidate. |
| 6 | github.com PR summary (then rewrite per Exercise 2) | Lives where the PR will be reviewed; auto-draft + your revision is the right pattern. |

**Self-check:**

- [ ] You named one surface per task — no "either VS Code or github.com".
- [ ] Your justification refers to a property of the surface, not just a habit.
- [ ] You did not assign a design or security task to the coding agent.
- [ ] Your answer for task 5 was Plan mode — not Agent mode and not the coding agent.

---

## Capstone Note

These four exercises produce material for **Capstone Deliverable 8 (platform artifact)**. Deliverable 8 accepts either:

- **Option A:** A reviewed coding-agent PR (Exercise 1 output) plus your review notes.
- **Option B:** A configured `.github/copilot-setup-steps.yml` plus your rewritten PR summary from Exercise 2 (combined evidence of both surfaces).

See [capstone/README.md](../../capstone/README.md) for full deliverable spec.
