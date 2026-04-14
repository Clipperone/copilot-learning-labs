# Module 10: Adoption Roadmap, Governance, and Capstone — Completion Checklist

Use the first section before the Capstone as a readiness gate. Use the second section after the Capstone to confirm completion.

---

## Before Capstone — Module Theory

**The 7/30/60/90-day roadmap**

- [ ] I can state all 4 time horizons and their gate deliverables from memory.
- [ ] I know the rule: each gate is a binary artifact check, not a self-impression.
- [ ] I know what "Day 7 wins" means and can name two concrete examples.
- [ ] I can explain why front-loading mastery before use causes adoption stalls.

**KPIs and measurement**

- [ ] I can name all 3 metrics in the minimum measurement set.
- [ ] I can state why lines accepted, acceptance rate, and time saved mislead.
- [ ] I know what "convention drift count" measures and how to calculate it.
- [ ] I can apply the session quality score to a session I ran in the past week.

**Moving from solo to team adoption**

- [ ] I can name all 5 documents in the minimum team rollout kit without referencing this module.
- [ ] I know which module introduced each of the 5 documents.
- [ ] I can explain why conventions must be written before the second person enables Copilot.
- [ ] I know the correct sequence for presenting the 5 documents in a onboarding session.

**Governance at team scale**

- [ ] I can state the 3 policy tiers and the team size that triggers each.
- [ ] I can write a 5-rule governance policy from memory given a team profile.
- [ ] I know all 5 items in the "Day 1" onboarding checklist.
- [ ] I know what a new team member must do before opening their first Agent session.

**Ongoing quality discipline**

- [ ] I can name all 4 steps in the monthly review cycle.
- [ ] I know the evidence of completion for each step.
- [ ] I can explain why the cycle takes 20–30 min monthly vs. 2–3 hours quarterly.
- [ ] I understand that agent drift review requires checking actual usage against documented permissions.

**Course continuation**

- [ ] I know the 4 things to update after the capstone as practice evolves.
- [ ] I can state conditions that should trigger a `CONVENTIONS.md` update.
- [ ] I understand that the capstone is a checkpoint, not a graduation.

**Reading the Copilot usage dashboard (Exercise 6)**

- [ ] I can name where dashboard data lives at the individual, org-admin, and enterprise tiers.
- [ ] I can name the 3 trustworthy signals (engagement breadth, agent-vs-inline ratio, premium quota burn rate) and what each tells me.
- [ ] I can name the 3 misleading metrics (raw acceptance %, lines accepted, "time saved") and explain why each misleads.
- [ ] I completed Exercise 6 — read a dashboard snapshot, separated signals from noise, and chose one immediate action vs. one deferred conversation.

**Content exclusions — admin controls (Exercise 7)**

- [ ] I can distinguish `.copilotignore` (developer, workspace) from content exclusions (admin, org/enterprise).
- [ ] I know the 3 scopes (repo, org, enterprise) and the precedence rule.
- [ ] I can map a Module 08 sensitivity class (Restricted / Confidential / Internal / Public) to an exclusion treatment.
- [ ] I can name 3 things exclusions do NOT solve (retroactive removal, copy-paste bypass, replacement for `.gitignore`).
- [ ] I completed Exercise 7 — drafted 5 patterns tied to sensitivity classes and named 2 risks not solved by exclusions alone.

---

## After Capstone — Capstone Completion

**Build deliverables (M04–M09 applied)**

- [ ] `.github/copilot-instructions.md` committed — ≥5 declarative, verifiable rules.
- [ ] `CONVENTIONS.md` committed — ≥5 rules; `AI-assisted:` and `Reviewed-by:` trailers present.
- [ ] `agents/` — ≥3 definitions each with purpose, constraints, tool permissions, and handoff.
- [ ] `prompts/` — ≥3 course-template entries each with a filled example.
- [ ] `agents/workflow-[name].md` — all 5 required sections; bounded sub-tasks.
- [ ] `capstone/validation-report.md` — all 5 gates assessed; BLOCKED result; Gate 4 (SQL injection) named as blocking.

**Planning deliverables (M10 applied)**

- [ ] `capstone/roadmap.md` — all 6 sections filled; no stubs; 3 KPIs from minimum set; ≥5 governance rules; review date specific.
- [ ] `checklists/adoption-milestones.md` reflects actual current state at each milestone.
- [ ] `checklists/expert-completion.md` every item checked or annotated — none left blank.

**Platform deliverable (M11 applied)**

- [ ] `capstone/platform-artifact.md` — Option A (coding-agent PR + 5-step review notes + decision) OR Option B (`copilot-setup-steps.yml` + before/after PR summary with all 4 properties).

---

## Module Complete

→ Capstone delivered: [capstone/](../../capstone/)
→ Expert self-assessment: [checklists/expert-completion.md](../../checklists/expert-completion.md)
→ Adoption tracker: [checklists/adoption-milestones.md](../../checklists/adoption-milestones.md)
