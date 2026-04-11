# Lab 06 — Agents and Personas

> **Difficulty:** Advanced
> **Estimated time:** ~60 minutes
> **Module:** [Module 06 — Agents and Role Specialization](../../modules/06-agents/)
> **Type:** Sequential — depends on Lab 05

---

## Learning Objective

After completing this lab you can write a complete agent persona definition using the 4-field anatomy, initialize a bounded Planner session, and write a 3-part handoff prompt that opens the next role without context leakage.

---

## Prerequisites

- [ ] Completed [Module 06 — Agents and Role Specialization](../../modules/06-agents/) and all 5 exercises
- [ ] GitHub Copilot Pro+ active in VS Code — Agent mode required
- [ ] Lab 05 complete (the starter project is the same codebase)
- [ ] [templates/agent-definition-template.md](../../templates/agent-definition-template.md) open in a reference tab

---

## Setup

1. Open `labs/lab-06-agents-and-personas/starter/` as your working directory in VS Code.
2. Open the Copilot Chat panel (`Ctrl+Alt+I` / `Cmd+Alt+I`).
3. Keep [Module 06 README.md](../../modules/06-agents/README.md) open as a reference tab — you will need the tool permissions matrix and the agent anatomy table.
4. Keep [templates/agent-definition-template.md](../../templates/agent-definition-template.md) open in a second tab.
5. Create an `agents/` folder at the repository root if it does not already exist. Your persona definition files go there, not in this lab folder.

> **Why this setup matters:** Agent definitions that live in `agents/` at the repository root are accessible by path in any Copilot session. Definitions buried in a lab folder cannot be referenced by file path in a new agent session.

---

## Tasks

### Task 1 — Write 3 Agent Definitions (20 min)

**Goal:** Produce complete persona definitions for the three roles you will use in Tasks 2 and 3: Planner, Implementer, and Code Reviewer.

**Instructions:**

1. For each of the three roles, copy `templates/agent-definition-template.md` into `agents/` with the appropriate filename:
   - `agents/planner.md`
   - `agents/implementer.md`
   - `agents/code-reviewer.md`
2. Fill in all 4 required anatomy fields for each role:
   - **Purpose** — one sentence naming what the role produces and for whom
   - **Constraints** — at least 3 explicit prohibitions (what this role must NOT do)
   - **Tool permissions** — fill the ✅ / ⚠️ / ❌ matrix; note conditions for each ⚠️
   - **Handoff criteria** — at least one named condition that signals the session is complete, and the name of the next persona to hand off to
3. Write the "Ideal Starting Prompt" for each role using the initialization prompt pattern from Module 06.
4. Pass the completeness test on each file before proceeding: can you answer all four questions — what does it produce, what is it not allowed to do, which tools can it use, how do I know it's done?

**Expected output:** 3 files in `agents/`, each passing the completeness test.

> **Constraint discipline:** The Code Reviewer definition must have ❌ for Edit files. If your definition says ✅, revise it — a reviewer that can edit is not a reviewer.

> **Check against solution only after completing all 3 independently.** Reference definitions are in `solution/` in this lab folder.

---

### Task 2 — Run a Planner Session (15 min)

**Goal:** Initialize a real Agent mode session using the Planner definition you wrote in Task 1, and practice clean session exit discipline.

**Instructions:**

1. Open `starter/feature-request.md` and read it.
2. Switch Copilot Chat to **Agent mode**.
3. Paste your Planner initialization prompt from `agents/planner.md` as the first message.
4. Adjust the scope to match the feature request exactly: `starter/feature-request.md`.
5. When the session produces a task breakdown, evaluate it against these criteria before accepting:
   - All sub-tasks are bounded to a specific file or function
   - Each sub-task has exactly one acceptance criterion
   - No sub-task contains the word "and" connecting two separate implementation steps
6. If any sub-task fails these criteria, ask for a tighter breakdown — do not accept a vague plan.
7. **Stop the session as soon as the task breakdown is complete.** Do not continue the session to discuss implementation.

**Expected output:** A task breakdown with 3–5 sub-tasks, each with a scope boundary and one acceptance criterion.

> **Session discipline:** The moment you have a usable task breakdown, end the session. Note the exact line where you decided to stop — this is the exit condition your Planner definition defines.

---

### Task 3 — Write the Planner → Implementer Handoff Prompt (10 min)

**Goal:** Using the task breakdown from Task 2, write the 3-part handoff prompt that opens an Implementer session scoped to the first sub-task only.

**Instructions:**

1. Identify the first sub-task from the Task 2 breakdown — the most self-contained one with the narrowest file scope.
2. Write the 3-part handoff prompt using the structure from Module 06:
   - **Part 1 — Summary:** What the Planner produced (filename, number of sub-tasks, which one this session covers)
   - **Part 2 — Objective:** The single bounded task the Implementer must accomplish (file name, function name, acceptance criterion)
   - **Part 3 — Carry-forward:** The active instruction file path, any architecture decisions, and explicit exclusions ("Do not open or modify [other files]")
3. Verify the prompt explicitly excludes all other sub-tasks from this session's scope.
4. Do not open a new Agent session yet — the handoff prompt is the deliverable for this task.

**Expected output:** A written handoff prompt that can be pasted directly into a new Implementer session.

> **Completeness test:** Read the carry-forward block. Does it reference `.github/copilot-instructions.md`? If not, the Implementer will run without the project's active instruction rules. Add it.

---

### Task 4 — Complete All 10 Agent Definitions (15 min)

**Goal:** Produce definition files for the remaining 7 roles so that `agents/` contains the full set of 10 personas the module defines.

**Instructions:**

1. For each of the remaining 7 roles, create a definition file in `agents/` using the template:
   - `agents/solution-architect.md`
   - `agents/refactoring-specialist.md`
   - `agents/security-reviewer.md`
   - `agents/test-engineer.md`
   - `agents/documentation-writer.md`
   - `agents/performance-optimizer.md`
   - `agents/devops-assistant.md`
2. For each file, fill in all 4 required fields. You may use the reference definitions in `solution/` to check your tool permissions matrix and handoff entries.
3. For the Security Reviewer definition, the "Main Risks" section must include at least one entry for hallucinated CVEs or inaccurate OWASP mappings, and the mitigation must cite verification steps.
4. Verify that no two definitions grant the same role contradictory permissions (e.g., both Solution Architect and Implementer claiming ownership of architectural decisions — only Architect produces architecture, Implementer follows it).

**Expected output:** 10 definition files in `agents/`, all passing the completeness test.

---

## Expected Outputs

By the end of this lab, you should have produced:

- [ ] `agents/planner.md` — complete 4-field definition, passes completeness test
- [ ] `agents/implementer.md` — complete 4-field definition with ✅ file write access and bounded scope
- [ ] `agents/code-reviewer.md` — complete 4-field definition with ❌ file edit access
- [ ] All 7 remaining definition files in `agents/` — complete, no `[PLACEHOLDER]` stubs remaining
- [ ] A written handoff prompt from Planner → Implementer for the first sub-task of the notification feature

---

## Success Criteria

| Criterion | How to verify |
|-----------|--------------|
| `agents/` contains all 10 definition files | Open Explorer panel — count 10 `.md` files |
| No file contains `[PLACEHOLDER]` stubs | Open each file — all template fields are filled in |
| Code Reviewer has ❌ Edit files | Open `agents/code-reviewer.md` — Edit row shows ❌ |
| Planner has ❌ Terminal and ❌ Edit | Open `agents/planner.md` — both rows show ❌ |
| Security Reviewer has ❌ Edit and ✅ Web | Open `agents/security-reviewer.md` — confirm both |
| Each definition has a named handoff target | Open any file — "Hand off to:" names a specific persona |
| Handoff prompt has all 3 parts | Read your Task 3 output — Summary, Objective, Carry-forward all present |

---

## Common Failure Points

| Symptom | Likely cause | Solution |
|---------|-------------|---------|
| Code Reviewer definition has ✅ Edit access | Confusion between "review" and "fix" | Reviewer roles evaluate — they never edit source files; remove the ✅ |
| Planner breakdown has sub-tasks like "add X and write tests" | "And" connecting two implementation steps | Split into two sub-tasks — each does exactly one thing |
| Handoff prompt does not reference `.github/copilot-instructions.md` | Forgetting instruction inheritance | Add it to the Carry-forward block explicitly |
| Agent session continues after the task breakdown is done | No exit discipline | Stop the session immediately when the deliverable exists; review first, then close |
| One definition file has passive constraints: "try to avoid…" | Carrying M04 anti-patterns into persona design | Rewrite as imperatives: "Do not…" or "Never…" |

---

## Review Checklist

See [checklist.md](./checklist.md) for the full self-assessment checklist.

---

## Extension Ideas

- Open an Implementer session using the handoff prompt from Task 3 — implement sub-task 1 of the notification feature and evaluate the output quality before accepting.
- Add a Handoff Triggers section to each definition file listing 2–3 observable signals that indicate the session has reached its exit condition without being explicitly asked.
- Create an `agents/README.md` index file linking all 10 definitions with a one-line description of each role's primary output.

---

## Files in This Lab

| File / Folder | Purpose |
|---------------|---------|
| `README.md` | Lab instructions (this file) |
| `checklist.md` | Completion checklist |
| `starter/feature-request.md` | Feature description — input for the Planner session |
| `starter/notifications.py` | Stub implementation file — scope reference for Implementer |
| `solution/` | Reference definitions for all 10 roles — check only after completing the task independently |
