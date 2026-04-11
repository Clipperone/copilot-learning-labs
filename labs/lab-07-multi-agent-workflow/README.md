# Lab 07 — Run a Complete Multi-Agent Workflow

> **Difficulty:** Advanced
> **Estimated time:** ~70 minutes
> **Module:** [Module 07 — Multi-Agent Workflows](../../modules/07-multi-agent-workflows/)
> **Type:** Sequential — depends on Lab 06

---

## Learning Objective

After completing this lab you can write a workflow file before executing any session, run the Feature Delivery pattern end-to-end with clean handoffs, and produce all required artifacts as committed files.

---

## Prerequisites

- [ ] Completed [Module 07 — Multi-Agent Workflows](../../modules/07-multi-agent-workflows/) and all 5 exercises
- [ ] GitHub Copilot Pro+ active in VS Code — Agent mode required
- [ ] Lab 06 complete — all 10 agent definitions present in `agents/` at the repository root
- [ ] `agents/planner.md`, `agents/implementer.md`, and `agents/code-reviewer.md` specifically must be complete and passing the completeness test
- [ ] [Module 07 README.md](../../modules/07-multi-agent-workflows/README.md) open in a reference tab

---

## Setup

1. Open the repository root in VS Code — not the `starter/` subfolder. The workflow file and all agent session outputs go to the repository root, not inside this lab.
2. Open `labs/lab-07-multi-agent-workflow/starter/feature-request.md` and read it in full before starting.
3. Open the Copilot Chat panel (`Ctrl+Alt+I` / `Cmd+Alt+I`).
4. Open `agents/planner.md`, `agents/implementer.md`, and `agents/code-reviewer.md` as reference tabs.
5. Open [Module 07 README.md](../../modules/07-multi-agent-workflows/README.md) — you will need the workflow file anatomy and the Feature Delivery pattern step table.

> **Why set up the repository root, not `starter/`:** This lab produces artifacts in `agents/` and source files in `starter/`. Opening the root keeps all paths resolvable in the same VS Code window as agent sessions run.

---

## Tasks

---

### Task 1 — Write the Workflow File (15 min)

**Goal:** Produce `agents/workflow-feature-delivery.md` before running any Agent session. The workflow file is a plan, not a log — it must exist before the first session opens.

**Instructions:**

1. Create the file `agents/workflow-feature-delivery.md` at the repository root.
2. Using the workflow file anatomy from [Module 07 theory.md](../../modules/07-multi-agent-workflows/theory.md), fill in all required sections:
   - `## Pattern` — Feature Delivery
   - `## Problem statement` — one paragraph: what the feature does, what success looks like, what is out of scope
   - `## Active context` — path to `.github/copilot-instructions.md`; any constraints from that file relevant to Python code
   - `## Steps` — 5 steps: one Planner, one Implementer per sub-task (three total), and one Code Reviewer; for each step name the role, input, output artifact filename, file scope, and verification gate
   - `## Outcome` — leave as a template with placeholder comments
3. Commit the file before moving to Task 2.

> **Why commit now?** A workflow file that exists only in memory or an unsaved editor tab cannot be referenced in a session initialization prompt by path. Commit it first so the path is stable.

**Expected output:** `agents/workflow-feature-delivery.md` committed, all sections populated, `## Outcome` left as a template.

> **Check against solution only after completing this task independently.** See `solution/workflow-feature-delivery.md`.

---

### Task 2 — Run the Planner Session (15 min)

**Goal:** Initialize a real Agent mode session using `agents/planner.md`, decompose the feature request, and close the session as soon as the sub-task list is complete.

**Instructions:**

1. Switch Copilot Chat to **Agent mode**.
2. Paste your Planner initialization prompt from `agents/planner.md` as the first message.
3. Adjust the objective and scope to match the feature request: input is `labs/lab-07-multi-agent-workflow/starter/feature-request.md`. Do not open any other file.
4. When the session produces a sub-task breakdown, evaluate it against the 3-property rule before accepting:
   - Each sub-task names at least one specific file
   - Each sub-task has exactly one acceptance criterion
   - No sub-task contains "and" connecting two independent implementation steps
5. If any sub-task fails a property, request a tighter breakdown before accepting.
6. **Stop the session immediately when the sub-task list is acceptable.** Do not continue into architecture or implementation discussion.
7. Save the sub-task breakdown as `feature-breakdown.md` in `labs/lab-07-multi-agent-workflow/starter/` and commit it.

**Expected output:** `feature-breakdown.md` committed — 4–6 sub-tasks, each with a named file scope and one acceptance criterion.

> **Exit discipline:** The moment you have an acceptable sub-task list, stop. Note the exact output that told you the Planner was done — this is the exit condition your `agents/planner.md` definition describes.

---

### Task 3 — Run the Implementer Session (15 min)

**Goal:** Implement the first sub-task from the breakdown using a clean Implementer session. The session must be scoped to one sub-task and one file.

**Instructions:**

1. Identify sub-task 1 from your `feature-breakdown.md` — it should be the most self-contained, narrowest-scope sub-task.
2. Write the Planner → Implementer handoff prompt using the 3-part structure from Module 06/07:
   - **Part 1 — Summary:** What the Planner produced — filename, number of sub-tasks, which sub-task this session covers
   - **Part 2 — Objective:** The single bounded task — function name, file name, acceptance criterion verbatim from the breakdown
   - **Part 3 — Carry-forward:** `.github/copilot-instructions.md` path; any constraints relevant to this file; explicit list of files not to open or modify
3. Open a **new** Agent mode session. Paste the handoff prompt as the first message.
4. When the Implementer produces the implementation, evaluate it:
   - The function exists in the correct file
   - The acceptance criterion from the breakdown is met
   - No other files were modified
5. If the acceptance criterion is not met, ask for a targeted fix — do not open a new session.
6. Commit the implementation before closing the session.

**Expected output:** Sub-task 1 implemented and committed in `labs/lab-07-multi-agent-workflow/starter/notifications.py`.

> **Scope guard:** If the Implementer proposes changes to `user.py` or any other file not named in sub-task 1, decline immediately: "This session covers `notifications.py` only. Do not modify any other file."

---

### Task 4 — Run the Code Reviewer Session (15 min)

**Goal:** Run a Code Reviewer session against the implementation from Task 3. The Reviewer is read-only — it produces findings, not fixes.

**Instructions:**

1. Write the Implementer → Code Reviewer handoff prompt:
   - **Part 1 — Summary:** What the Implementer produced — function name, file committed, acceptance criterion confirmed
   - **Part 2 — Objective:** Review the implementation. Produce numbered findings. Mark each BLOCKING or NON-BLOCKING.
   - **Part 3 — Carry-forward:** `.github/copilot-instructions.md`; the acceptance criterion from the breakdown; explicit statement that the Reviewer must not modify any file
2. Open a **new** Agent mode session and paste the handoff prompt.
3. When the session produces findings, evaluate the review:
   - Findings are numbered
   - Each finding states severity (BLOCKING or NON-BLOCKING), file location, and a suggested fix
   - No source files were modified
4. Save the findings as `review-findings.md` in `labs/lab-07-multi-agent-workflow/starter/` and commit.
5. If there are BLOCKING findings, open a new Implementer session to resolve them (do not fix them in the Reviewer session).

> **Severity schema:** This lab uses BLOCKING / NON-BLOCKING. Module 08 introduces the 4-level scale (Critical / High / Medium / Low). Both are correct schemas for different use cases — you will use the richer scale in Lab 08.

**Expected output:** `review-findings.md` committed — numbered findings list, each marked BLOCKING or NON-BLOCKING.

> **Reviewer boundary:** If the Code Reviewer session produces a direct code edit in `notifications.py`, the Reviewer definition has a permissions error. Close the session and correct `agents/code-reviewer.md` before re-running.

---

### Task 5 — Update the Workflow File (10 min)

**Goal:** Fill in the `## Outcome` section of `agents/workflow-feature-delivery.md` with what actually happened during the workflow.

**Instructions:**

1. Open `agents/workflow-feature-delivery.md`.
2. Fill in the `## Outcome` section with:
   - **Artifacts produced:** list each committed file with its path
   - **Deviations from plan:** any steps that differed from the plan (scope adjustments, extra iterations, steps skipped)
   - **Issues found:** BLOCKING findings from the Code Reviewer, if any, and whether they were resolved
3. Commit the updated workflow file.
4. Do an integrity check: open the workflow file and verify it is a standalone document — a team member who was not present could understand what was done, what was produced, and what issues remain.

**Expected output:** `agents/workflow-feature-delivery.md` updated with a complete `## Outcome` section and committed.

---

## Expected Outputs

By the end of this lab you should have committed all of the following:

- [ ] `agents/workflow-feature-delivery.md` — complete workflow file including `## Outcome`
- [ ] `labs/lab-07-multi-agent-workflow/starter/feature-breakdown.md` — Planner output: 4–6 sub-tasks, each with file scope and acceptance criterion
- [ ] `labs/lab-07-multi-agent-workflow/starter/notifications.py` — updated with sub-task 1 implementation
- [ ] `labs/lab-07-multi-agent-workflow/starter/review-findings.md` — Code Reviewer output: numbered findings, each BLOCKING or NON-BLOCKING

---

## Success Criteria

| Criterion | How to verify |
|-----------|--------------|
| Workflow file exists and was written before Task 2 | Check commit history — `workflow-feature-delivery.md` commit predates the Planner session |
| All sub-tasks in `feature-breakdown.md` have a named file scope | Open the file — every sub-task names at least one specific file |
| No sub-task in `feature-breakdown.md` contains "and" | Read each sub-task description — no compound steps |
| Implementation is in the correct file | Open `notifications.py` — the function from sub-task 1 is present |
| No file outside sub-task 1 scope was modified | `git diff` — only `notifications.py` changed during the Implementer session |
| Reviewer session produced no source file edits | `git log` — the only commit from Task 4 is `review-findings.md` |
| `## Outcome` is filled in | Open `workflow-feature-delivery.md` — `## Outcome` has real content, not placeholder comments |

---

## Common Failure Points

| Symptom | Likely cause | Solution |
|---------|-------------|---------|
| Planner session continues past the sub-task list | No exit discipline — session drifted into design | End the session immediately when the breakdown is complete; do not ask follow-up questions |
| Implementer modifies `user.py` or another out-of-scope file | Scope not stated explicitly in the handoff prompt | Add "Do not open or modify [file list]" to Part 3 of the handoff prompt |
| Code Reviewer produces a direct code edit | Reviewer persona has ✅ Edit access | Fix `agents/code-reviewer.md` — Edit files must be ❌; re-run from Task 4 |
| `feature-breakdown.md` has sub-tasks with vague scope like "update the data layer" | Planner accepted a coarse breakdown | Ask the Planner to narrow each sub-task to a named file before stopping the session |
| `workflow-feature-delivery.md` was written after Task 2 | Treated as documentation rather than a guide | For future workflows: write the file completely before the first session |
| Handoff prompt omits `.github/copilot-instructions.md` | Forgot the carry-forward block | Re-read Part 3 of the 3-part handoff structure; instruction file path is always required |

---

## Review Checklist

See [checklist.md](./checklist.md) for the full completion self-assessment.

---

## Extension Ideas

- Run the Implementer session for sub-tasks 2 and 3 from your breakdown, writing a fresh Planner → Implementer handoff for each.
- Add a Test Engineer step after your final Implementer session: write the Implementer → Test Engineer handoff and evaluate the test quality before accepting.
- Attempt the Bug Investigation pattern on the `KeyError` scenario from Module 07 Exercise 5, using your `agents/planner.md` as the Analyst.
- Add a `## Handoff Triggers` section to each of the three agent definitions you used today — list 2–3 observable signals that indicate the session has reached its exit condition.

---

## Files in This Lab

| File / Folder | Purpose |
|---------------|---------|
| `README.md` | Lab instructions (this file) |
| `checklist.md` | Completion self-assessment |
| `starter/feature-request.md` | Feature description — input for the Planner session |
| `starter/notifications.py` | Stub implementation file — scope for the Implementer session |
| `starter/user.py` | Adjacent stub — must not be modified during sub-task 1 |
| `solution/workflow-feature-delivery.md` | Reference workflow file — check only after completing Task 1 independently |
| `solution/feature-breakdown.md` | Reference sub-task breakdown — check only after completing Task 2 independently |
