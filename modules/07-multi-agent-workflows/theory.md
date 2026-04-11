# Module 07: Multi-Agent Workflows — Extended Reference

> This document extends [README.md](./README.md). Read the module overview first.
> **Prose word limit:** ≤ 500 words (tables and code blocks excluded).

---

## Artifact Design

An artifact is a committed file that survives a session boundary. Its quality determines whether the next role starts cleanly or spends the first 10 turns reconstructing what the previous session already decided.

**Properties of a well-designed artifact:**

| Property | Description |
|----------|-------------|
| **Named and committed** | Exists as a file at a known path before the session closes |
| **Self-contained** | The next role can act from the artifact without re-reading the prior session |
| **Scoped** | Contains only what the next role needs — no excess context from earlier steps |
| **Dated** | Includes a `<!-- Generated: YYYY-MM-DD -->` comment so the artifact can be audited |

**Artifact per pattern:**

| Pattern | Primary artifact | Downstream artifacts |
|---------|----------------|----------------------|
| Feature Delivery | `feature-breakdown.md` | Implemented code (committed), findings document |
| Bug Investigation | Root-cause hypothesis document | Fix (committed), regression test |
| Refactor and Validate | Refactored code (committed) | Test results document, review findings |

---

## Decomposition Decision Matrix

Use this matrix when evaluating whether a sub-task is correctly sized before assigning it to a session.

| Question | If yes | If no |
|----------|--------|-------|
| Does the sub-task name at least one specific file? | Proceed | Narrow the scope to a named file |
| Does the sub-task have exactly one acceptance criterion? | Proceed | Split or rewrite to isolate one criterion |
| Can one agent role complete it without switching roles? | Proceed | Assign the second concern to a separate session |
| Is the expected implementation time under 20 minutes? | Proceed | Split the sub-task |
| Does the description contain the word "and"? | Split immediately | Proceed |

---

## Workflow File Anatomy

A workflow file is a machine-readable plan. Every field has a specific function and a default that should never be omitted.

```markdown
## Pattern
[Feature Delivery | Bug Investigation | Refactor and Validate]

## Problem statement
[One paragraph: what the problem is, what success looks like, what is explicitly out of scope]

## Active context
- Instruction file: `.github/copilot-instructions.md`
- Architecture notes: [path to ADR or design doc, or "none"]
- Constraints: [copy the 3 most relevant constraints from the instruction file verbatim]

## Steps
1. **[Role]** → Input: [artifact or description] · Output: `[filename]` · Scope: [files] · Verify: [acceptance criterion]
2. **[Role]** → Input: `[filename from step 1]` · Output: `[filename]` · Scope: [files] · Verify: [acceptance criterion]

## Outcome
<!-- Fill in after workflow completion -->
- Artifacts produced:
- Deviations from plan:
- Issues found:
```

The `## Active context` section transfers project rules into every session without making learners retype them. State it once in the workflow file, copy it into every initialization prompt's `Carry-forward:` block.

---

## Extending the Three Patterns

The three patterns cover approximately 90% of common development scenarios. For the remaining cases, compose from the standard building blocks rather than inventing a new pattern.

| Scenario | Composition |
|----------|-------------|
| Feature that touches a security boundary | Feature Delivery + Security Reviewer after Code Reviewer (step 5) |
| Refactor a legacy file with no existing tests | Add Test Engineer as step 1 to baseline behavior; then run Refactor and Validate |
| Greenfield module | Solution Architect → Feature Delivery (one Planner + Implementer cycle per sub-module) |
| Dependency upgrade | Analyst (risk mapping) → Implementer → Test Engineer → Code Reviewer |

Do not invent new patterns for every novel scenario. Extend a known pattern by inserting one additional role at the correct position.

---

## Handoff Prompt Discipline at Workflow Scale

In a 2-session workflow, a slightly imprecise handoff is recoverable. In a 4-session workflow, imprecision compounds: each handoff narrows the next role's effective context.

**Anti-drift rules:**

- Copy the problem statement verbatim from the workflow file into every initialization prompt.
- State the step number explicitly: "This is Step 3 of 4 in the Feature Delivery workflow."
- Explicitly exclude prior-step artifacts that the current role does not need.
- Re-read the workflow file before writing any handoff prompt after step 3.
