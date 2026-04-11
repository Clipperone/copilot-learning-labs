# Capstone: End-to-End Copilot Workflow Integration

> **Level:** Expert
> **Estimated time:** ~2 hours
> **Prerequisite:** All 10 modules complete. `checklists/advanced-completion.md` fully checked.
> **Verified:** 2026-04

This capstone has no solution directory. Your deliverables reflect your project context. What they must contain is defined here; what they say is yours.

---

## Objective

Apply every substantive skill from this course to a single project context. You will configure the full Copilot integration layer, design an agent workflow, validate an AI-generated diff against governance standards, and produce a 90-day adoption plan — all committed as verifiable artifacts.

This is not a planning exercise. It is a build exercise that ends with a plan.

---

## Prerequisites

- [ ] Modules 01–10 complete
- [ ] `checklists/advanced-completion.md` fully checked
- [ ] `modules/10-adoption-roadmap/checklist.md` — Before Capstone section checked
- [ ] A designated project context (see Setup below)

---

## Setup

**Step 1 — Choose your project context.** Pick one:

- **Option A — Provided scenario:** Use the scenario in the Project Brief below. All deliverables go in this course repository under the paths in the Deliverables table.
- **Option B — Real project:** Apply the capstone to an active project from your work. Commit configuration deliverables (items 1–5) to that repository. Commit `capstone/validation-report.md` and `capstone/roadmap.md` to this course repository either way. Record the external repository URL in `capstone/roadmap.md` Section 1.

**Step 2 — Verify Copilot Pro+ is active** and all 5 modes are accessible in VS Code.

**Step 3 — Confirm** `checklists/advanced-completion.md` is fully checked before opening any session.

**Step 4 — Create** `capstone/validation-report.md` as an empty file in this repository. You will populate it in Deliverable 6.

---

## Project Brief

> Use this brief for Option A, or as a reference model for Option B.

You are configuring GitHub Copilot Pro+ for a 3-person Python team starting a new FastAPI project. The repository is a blank slate: no Copilot instructions, no conventions, no agents, no prompts. You will build the complete Copilot integration layer from scratch and apply it in a real session.

**Team profile:**
- 3 engineers, mixed seniority (1 senior, 2 mid-level)
- All have Copilot Pro+ — none have used it with any structure before
- Primary language: Python; secondary: SQL, shell scripts
- Deliverable: a REST API with authentication; data is user-sensitive

There are no starter files for this capstone. Begin from an empty directory or your own project.

---

## Required Deliverables

Seven deliverables. Each maps to one or more modules. All must be committed.

| # | Deliverable | Where it lives | Module |
|---|-------------|---------------|--------|
| 1 | `.github/copilot-instructions.md` — ≥5 rules in declarative format | Your project repo (Option A: this repo) | M05 |
| 2 | `CONVENTIONS.md` — governance policy, ≥5 rules, includes `AI-assisted:` and `Reviewed-by:` trailers | Your project repo (Option A: this repo) | M09 |
| 3 | `agents/` — ≥3 agent definitions, each with purpose, constraints, tool permissions, and handoff criteria | Your project repo (Option A: this repo `agents/`) | M06 |
| 4 | `prompts/` — ≥3 prompt entries in the course template format, each with a filled example | This course repo `prompts/` (extend Lab 04 work) | M04 |
| 5 | `agents/workflow-[name].md` — one multi-agent workflow with all 5 required sections | This course repo `agents/` | M07 |
| 6 | `capstone/validation-report.md` — gate-by-gate pre-merge validation of the diff below | This course repo `capstone/` | M08/M09 |
| 7 | `capstone/roadmap.md` — 90-day adoption plan with self-placement, milestones, KPIs, governance policy, and review cycle commitment | This course repo `capstone/` | M10 |

---

## The Validation Diff (for Deliverable 6)

Apply the 5-gate pre-merge validation protocol from Module 09 to this AI-generated diff. Record your findings in `capstone/validation-report.md`.

> ⚠️ **Note:** This diff contains deliberate OWASP vulnerabilities for educational identification. Never commit code resembling this to a production repository.

```diff
diff --git a/api/routes/users.py b/api/routes/users.py
--- a/api/routes/users.py
+++ b/api/routes/users.py
@@ -8,10 +8,28 @@ from sqlalchemy.orm import Session

-def get_user(db: Session, user_id: int) -> User | None:
-    """Return user by primary key."""
-    return db.query(User).filter(User.id == user_id).first()

+def get_user(db: Session, user_id: str) -> dict:
+    """Return user by id."""
+    query = f"SELECT * FROM users WHERE id = '{user_id}'"
+    result = db.execute(query)
+    return dict(result.fetchone())
+
+def delete_user(db: Session, user_id: str) -> bool:
+    """Delete user by id."""
+    db.execute(f"DELETE FROM users WHERE id = '{user_id}'")
+    db.commit()
+    return True
+
+import subprocess
+
+def export_user_data(user_id: str, output_path: str) -> None:
+    """Export user data to file."""
+    subprocess.run(f"pg_dump --table=users > {output_path}", shell=True)
```

**`capstone/validation-report.md` must contain:**

- One row per gate: Gate name | Pass / Fail / Partial | Finding (one sentence)
- An overall result: PASS or BLOCKED
- A clear statement of which gate(s) are blocking and why

---

## `capstone/roadmap.md` Structure (for Deliverable 7)

`capstone/roadmap.md` is the forward-looking plan. `checklists/adoption-milestones.md` is the rearward-looking tracker you update monthly. They are separate documents with separate purposes.

Your `capstone/roadmap.md` must contain all 5 sections:

**Section 1 — Current state self-placement**

For each level, write 1–3 sentences of evidence. Evidence must be specific — reference a committed file, a checklist, or an observable behavior. "I feel comfortable" does not count.

| Level | Skills covered | My evidence |
|-------|---------------|-------------|
| Beginner | Modes, configuration, cost awareness | [specific evidence] |
| Intermediate | Prompt engineering, custom instructions | [specific evidence] |
| Advanced | Agents, multi-agent workflows | [specific evidence] |
| Expert | Advanced features, repository quality, governance | [specific evidence] |

**Section 2 — 90-day roadmap**

Each row must have a gate deliverable that is a specific file or checklist — not an intention.

| Timeframe | Focus | Gate deliverable |
|-----------|-------|-----------------|
| 7 days | [aligned to your weakest Level 1–2 skill] | [specific file or checklist] |
| 30 days | [aligned to your Level 2–3 gaps] | [specific file or checklist] |
| 60 days | [aligned to your Level 3–4 gaps] | [specific file or checklist] |
| 90 days | Full integration and team rollout ready | Capstone all 7 deliverables committed; `checklists/expert-completion.md` reviewed |

**Section 3 — KPI selection**

Name your 3 KPIs from the module's minimum set. For each metric you are not tracking, write one sentence explaining why it misleads or cannot be verified. Reference Exercise 2 in `modules/10-adoption-roadmap/exercises.md` for the format.

**Section 4 — Governance policy**

Select a policy tier appropriate to your team size. Write a minimum 5-rule policy in declarative format. If working with a real project (Option B), also commit this policy to that project's `CONVENTIONS.md`.

**Section 5 — Premium request budget**

State your monthly premium request allocation for Copilot-assisted work. Identify one task category where you will default to the standard model and one where escalation to a premium model is justified. Reference the token impact table in the modules this course project uses most.

**Section 6 — Review cycle commitment**

State a specific monthly review date. Name who is responsible for each of the 4 monthly review steps. If solo, you are responsible for all 4.

---

## Success Criteria

The capstone is complete when:

1. All 7 deliverables are committed to the repository (or linked project for Option B)
2. `capstone/validation-report.md` exists with all 5 gates assessed, BLOCKED result, and Gate 4 (OWASP A03 — SQL injection) identified as the primary blocking gate
3. `capstone/roadmap.md` exists with all 6 sections filled — no `[specific evidence]` or `[specific file]` stubs remaining
4. `checklists/expert-completion.md` has been reviewed — every item is either checked or annotated with a remediation note
5. `checklists/adoption-milestones.md` reflects your actual current state at each milestone

---

## Evaluation Rubric

| Deliverable | Meets criteria when… |
|-------------|---------------------|
| `.github/copilot-instructions.md` | ≥5 rules; each rule is verifiable (yes/no answer); no vague guidance like "write clear code" |
| `CONVENTIONS.md` | ≥5 rules; includes `AI-assisted:` and `Reviewed-by:` trailer requirements; all rules in declarative format |
| `agents/` (≥3 definitions) | Each definition has: purpose statement, constraints, tool permissions table (✅/⚠️/❌), and ≥1 handoff criterion |
| `prompts/` (≥3 entries) | Each entry uses the course template; filled example with realistic input and visible expected output |
| `agents/workflow-[name].md` | All 5 required sections present; each sub-task has one named output file and one acceptance criterion; no compound steps |
| `capstone/validation-report.md` | All 5 gates assessed with Pass/Fail/Partial; Gate 4 (OWASP A03 — SQL injection) recorded as BLOCKING; overall result is BLOCKED |
| `capstone/roadmap.md` | All 6 sections present; no stubs; 3 KPIs from the minimum set; ≥5 governance rules in declarative format; review date specific |

---

## Common Failure Points

| Failure | Signal | Recovery |
|---------|--------|---------|
| Treating this as a planning exercise | Only roadmap.md completed; deliverables 1–6 skipped | Deliverables 1–6 are build artifacts, not reflections — produce and commit them |
| Reusing Lab deliverables without applying them to the capstone scenario | agents/ or prompts/ files reference Lab 06 scenario, not the FastAPI team profile | Write the deliverables for your capstone context; the lab work is the model, not the answer |
| Validation report missing the command injection | Only SQL injection identified in `get_user`; `export_user_data` not flagged | Apply OWASP A03 to all three new functions; `subprocess.run(shell=True)` is a command injection vector |
| Gate findings without overall result | Per-gate rows present but no PASS/BLOCKED conclusion | The final line must state the overall result and reference the blocking gate(s) by name |
| Writing roadmap.md last | Treated as a summary of what was done | Sections 1 and 2 are forward-looking from today — write them before completing deliverables 1–6 |
| Stubs remaining in roadmap.md | `[specific evidence]` or `[specific file]` text present at commit time | Every template placeholder must be replaced; the rubric is a binary check on this |

---

## Extension Ideas

1. Add a `.copilotignore` covering the FastAPI project's migration files, secrets, and generated fixtures — justify each entry with an inline comment
2. Write a Security Reviewer agent definition using the sensitivity classification table from Module 08; give it `❌ Edit files` permission and document the handoff to the Implementer
3. Run the multi-agent workflow you designed end-to-end on a real feature in your project and commit the outcome artifacts
4. Adapt the governance policy from Deliverable 2 for a second project at a different policy tier; document the delta
5. Run the first monthly review cycle using `checklists/adoption-milestones.md` and commit the updated tracker with evidence

---

## Premium Request Budget

This capstone exercises these Copilot modes:

| Deliverable | Recommended mode | Cost level |
|-------------|-----------------|-----------|
| `.github/copilot-instructions.md` | Ask (one session from project description) | Low |
| `CONVENTIONS.md` | Ask or Plan (multi-language projects) | Low–Medium |
| Agent definitions (≥3) | Ask (one definition per session) | Low |
| Prompt entries (≥3) | Edit (write directly in the template) | None |
| Workflow file | Ask (structure output; verify sub-tasks manually) | Low |
| Validation report | Ask (diff as input; binary per-gate output) | Low |
| `roadmap.md` | Plan mode (for structure); all decisions are yours | Low |

One Ask session and one Plan session for the roadmap is sufficient. No Agent session is warranted for any capstone deliverable — the decisions belong to you, not the model.

---

## When You Are Done

1. Verify all 7 deliverables are committed (use `capstone/checklist.md`)
2. Review `checklists/expert-completion.md` — check or annotate every item
3. Update `checklists/adoption-milestones.md` with your current actual state
4. Return to `modules/10-adoption-roadmap/checklist.md` and complete the After Capstone section

**You have completed the GitHub Copilot Pro+ Mastery course.**
