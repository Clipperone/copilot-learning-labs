# Solution — Lab 06: Agents and Personas

> **Important:** Your working agent definition files belong in `agents/` at the **repository root**, not in this folder.
> Use these reference definitions to check your own work after completing each task independently.
> Do not copy these files directly into `agents/` — the learning objective is to write your own definitions from scratch.

---

## What Is in This Folder

| File | Purpose |
|------|---------|
| `planner.md` | Reference definition for the Planner / Analyst role |
| `implementer.md` | Reference definition for the Implementer / Developer role |
| `code-reviewer.md` | Reference definition for the Code Reviewer role |
| `security-reviewer.md` | Reference definition for the Security Reviewer role |
| `solution-architect.md` | Reference definition for the Solution Architect role |
| `refactoring-specialist.md` | Reference definition for the Refactoring Specialist role |
| `test-engineer.md` | Reference definition for the Test Engineer role |
| `documentation-writer.md` | Reference definition for the Documentation Writer role |
| `performance-optimizer.md` | Reference definition for the Performance Optimizer role |
| `devops-assistant.md` | Reference definition for the DevOps / Release Assistant role |
| `handoff-prompts.md` | Three reference handoff prompts: Planner → Implementer, Implementer → Code Reviewer, Code Reviewer → Security Reviewer |

---

## How to Use These Files

**Tasks 1 and 4:** After writing each definition file in `agents/`, compare it to the corresponding reference file here. Check:

1. Does your Purpose match the role's primary output?
2. Do your constraints use imperatives ("Do not…", "Never…") not hedges?
3. Does your tool permissions matrix have explicit ✅ / ⚠️ / ❌ for every row?
4. Does your Handoff section name a specific next role and a concrete trigger condition?

**Task 3:** After writing your Planner → Implementer handoff prompt, compare it to `handoff-prompts.md`. The structure must match regardless of the specific task content.

---

## Completeness Self-Check

Before comparing against these solutions, confirm each of your files passes the four-question completeness test:

- [ ] What does this role produce? (readable in the Purpose section)
- [ ] What is it not allowed to do? (readable in the Constraints section)
- [ ] Which tools can it use? (every row of the permissions matrix is filled)
- [ ] How do I know the session is done? (exit condition is stated explicitly)
