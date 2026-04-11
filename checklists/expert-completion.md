# Expert Completion Checklist

Use this checklist after completing Modules 08–10 and the Capstone to confirm you are ready to call yourself an Expert-level GitHub Copilot practitioner.

This is a synthesis checklist. It draws on skills from the full course — not just the Expert modules. If a section reveals a gap, return to the relevant module before signing off.

---

## Module 08: Advanced Features in Copilot + VS Code

- [ ] Can state the 5 elements a complete Plan mode output must contain
- [ ] Can apply the 5-step AI-assisted code review loop to any diff without referencing the module
- [ ] Can apply the 4-question gate to any AI-generated terminal command before executing it
- [ ] Can name the 4 components of the minimum quality gate before commit
- [ ] Can classify any file as Public, Internal, Confidential, or Restricted from memory
- [ ] Can apply the 5-category OWASP minimum check to any AI-generated function
- [ ] All 7 success criteria verified from [labs/lab-08-advanced-feature-tour/checklist.md](../labs/lab-08-advanced-feature-tour/checklist.md)

## Module 09: AI-Friendly Repository Engineering

- [ ] Can list all 6 properties of an AI-friendly repository and state the degradation caused by each missing property
- [ ] Knows the scoring rule: ≥5 = AI-ready; 3–4 = degraded; ≤2 = high-noise
- [ ] Can write an AI-useful README with all required labelled sections
- [ ] Can write a `CONVENTIONS.md` in declarative format with at least 5 rules
- [ ] Can apply the 5-gate pre-merge validation protocol to any diff — knows which gate fails for SQL injection
- [ ] Can write a `.copilotignore` for a given file inventory with inline justification comments
- [ ] All 7 success criteria verified from [labs/lab-09-repository-health-audit/checklist.md](../labs/lab-09-repository-health-audit/checklist.md)

## Module 10: Adoption Roadmap, Governance, and Capstone

- [ ] Can state all 4 time horizons of the adoption roadmap and their gate deliverables from memory
- [ ] Can name all 3 metrics in the minimum measurement set and reject the misleading metrics by name
- [ ] Can name all 5 documents in the minimum team rollout kit and recall which module introduced each
- [ ] Can state the 3 policy tiers and the team size that triggers each
- [ ] Can run the 4-step monthly review cycle on any repository without referencing the module

---

## Capstone

- [ ] `capstone/roadmap.md` is committed and all 5 sections are filled in — no stubs remaining
- [ ] `checklists/adoption-milestones.md` reflects actual current state at each milestone
- [ ] All gate deliverables in Section 2 of `capstone/roadmap.md` are specific committed files or checklists
- [ ] All 3 KPIs in Section 3 are from the module's minimum set
- [ ] Governance policy in Section 4 has at least 5 rules committed in correct location
- [ ] `capstone/checklist.md` is fully verified

---

## Cross-Level Synthesis

This section tests whether the Expert-level skills integrate with the foundations from earlier levels.

- [ ] My prompt library has ≥5 entries committed to `prompts/` using the course template (Module 04)
- [ ] My `instructions/` folder has ≥3 scoped examples: global, project, path-specific (Module 05)
- [ ] All 10 agent definitions exist in `agents/` and none contain `[PLACEHOLDER]` stubs (Module 06)
- [ ] At least one completed multi-agent workflow file is committed to `agents/` (Module 07)
- [ ] `CONVENTIONS.md` exists in at least one real project and is in declarative format (Module 09)
- [ ] My `checklists/adoption-milestones.md` is live and scheduled for monthly update (Module 10)

---

## Mindset Check

Before signing off:

- [ ] I apply the pre-merge 5-gate validation to every non-trivial AI-assisted commit — not selectively
- [ ] I would stop an agent session at its stated exit condition even if the agent "has more ideas"
- [ ] I treat `CONVENTIONS.md` as a living document — I update it when norms change
- [ ] I do not commit AI-generated code without a named reviewer in the commit trailer
- [ ] I know that the checklist completion rate is a better productivity signal than acceptance rate
- [ ] I understand that the capstone is a checkpoint, not a graduation — practice continues

---

## You Have Completed the Course

Completed by: *(your name)*
Date: *(YYYY-MM-DD)*

→ Keep `checklists/adoption-milestones.md` active on the schedule in your `capstone/roadmap.md`.
→ Revisit this checklist after 90 days — skills decay without use; gaps surface quickly on re-assessment.
→ Start with [LEARNING_PATH.md](../LEARNING_PATH.md) if onboarding a colleague to the course.
