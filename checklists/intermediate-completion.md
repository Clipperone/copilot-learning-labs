# Intermediate Completion Checklist

Use this checklist after completing Modules 04–05 and Labs 04–05 to confirm you are ready for the advanced level.

---

## Module 04: Prompt Engineering

- [ ] Can decompose any coding task into the 4-component structure (task, role, constraints, output format)
- [ ] Can apply the correct prompt pattern for all 7 coding scenarios without looking them up
- [ ] Can name all 5 prompt anti-patterns on sight
- [ ] Can write a parameterized, reusable prompt template committable to the shared prompt library
- [ ] Knows when a prompt scenario warrants a premium model
- [ ] Can write a completeness test by reading the task line aloud and checking for one verb and one noun

## Lab 04: Prompt Engineering Workshop

- [ ] All 7 scenario prompts written and results reviewed in `starter/workbench.py`
- [ ] Two-prompt debug chain used for `merge_sorted` — diagnosis before fix
- [ ] Security review prompt anchored to OWASP A02 and produced correct finding + fix
- [ ] At least 3 anti-pattern prompts diagnosed and rewritten with different expected output noted
- [ ] All 5 prompt library files saved with no `[PLACEHOLDER]` stubs remaining
- [ ] All 6 success criteria verified from [labs/lab-04-prompt-engineering/checklist.md](../labs/lab-04-prompt-engineering/checklist.md)

---

## Module 05: Custom Instructions

- [ ] Can distinguish the 3 instruction scopes: user (personal), repository-wide, path-specific
- [ ] Knows the 4 design principles: specific, imperative, bounded, non-contradictory
- [ ] Can identify passive or vague language in an instruction file and rewrite it
- [ ] Can write a valid `applyTo` frontmatter glob and explain what it matches
- [ ] Can run the diagnostic prompt to verify instructions are active
- [ ] Can name 3 signs instructions are being ignored and the fix for each
- [ ] Has applied (or plans to apply) these patterns to a real project

## Lab 05: Write Your Project's Custom Instructions

- [ ] Scope analysis table complete — all 6 constraints classified across 3 columns
- [ ] `copilot-instructions.md` written for the starter project — at least four domains covered
- [ ] Path-specific `api-layer.instructions.md` created with valid `applyTo` frontmatter
- [ ] Diagnostic prompt run and output reviewed against each active instruction
- [ ] All lab success criteria verified from [labs/lab-05-custom-instructions/checklist.md](../labs/lab-05-custom-instructions/checklist.md)

---

## Mindset Check

Before moving to advanced level, confirm these behaviors:

- [ ] I write structured prompts automatically — no longer composing open-ended requests for coding tasks
- [ ] I do not repeat in a prompt what is already encoded in an active instruction file
- [ ] I review Copilot output against relevant OWASP categories before accepting security-related code
- [ ] I apply premium model discipline — security and migration prompts use o1 or Claude; completion tasks use default

---

## You're Ready for Advanced Level

→ [LEARNING_PATH.md — Path 3: Advanced](../LEARNING_PATH.md#path-3--advanced)
→ Start with [Module 06 — Agents and Role Specialization](../modules/06-agents/)
