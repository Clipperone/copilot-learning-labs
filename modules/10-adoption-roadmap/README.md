# Module 10: Adoption Roadmap, Governance, and Capstone

> **Level:** Expert
> **Estimated time:** ~2 hours (module theory ~1 hr · capstone ~60 min)
> **Prerequisite:** [Module 09 — AI-Friendly Repository Engineering](../09-repository-quality/) · Complete the [Advanced Phase Checklist](../../checklists/advanced-completion.md) before this module.
> **Verified:** 2026-04

> ⚠️ **Premium request note:** This module is predominantly documentation and structured reflection. No Agent sessions are needed. Plan mode is useful for drafting the 90-day roadmap if you prefer AI-assisted structure. All other tasks — KPI selection, governance policy drafting, team onboarding kit — resolve in one Ask turn or require no Copilot session at all. This is intentional: the module teaches you to apply judgment, not to delegate it.

---

## Learning Objectives

By the end of this module, you will be able to:

1. Design a 7/30/60/90-day personal Copilot adoption roadmap with verifiable milestones.
2. Select KPIs that accurately reflect Copilot productivity — and reject the metrics that mislead.
3. Build a minimum team governance framework: policy, onboarding protocol, and review cycle.
4. Apply ongoing quality discipline as a recurring practice, not a pre-merge-only gate.
5. Execute a structured team introduction to Copilot using the course's conventions and checklists.
6. Complete the capstone: a self-assessed 90-day adoption plan applied to a real project context.

---

## Why This Module Exists

Every technique in Modules 01–09 produces full value only when applied consistently, in the right context, at the right level of intensity. The failure mode is not forgetting a feature — it is knowing the tools but not having a plan for how, when, and at what pace to apply them.

Teams that succeed with Copilot at scale share a common pattern: they set explicit expectations at week one, track behavior change (not output volume) at 30 and 60 days, and conduct a structured review at 90 days. Teams that stall share a different pattern: uncoordinated adoption, no shared conventions, and no moment where progress is evaluated.

This module converts the course's full skill set into a personal and team implementation plan. Mastery without a roadmap stays in the repository. With one, it enters your practice.

---

## The 7/30/60/90-Day Personal Roadmap

An adoption roadmap is a commitment to a sequence of behaviors, not a list of features to explore. Each time horizon has a specific focus and a binary gate deliverable — a file you commit or a checklist you sign off, not a vague intention.

| Timeframe | Focus | Gate deliverable |
|-----------|-------|-----------------|
| **7 days** | Setup, verification, first real usage | All 6 modes verified; `Module 01` checklist done; cheat sheet drafted |
| **30 days** | Prompt discipline, custom instructions live | Personal prompt library (≥5 entries) + `instructions/` folder on a real project |
| **60 days** | Agent workflows, advanced features in production | 10 agent definitions committed; first multi-agent workflow run; `Module 08` checklist done |
| **90 days** | Full mastery, governance, team rollout ready | Capstone complete; `checklists/expert-completion.md` self-assessed; adoption plan documented |

**The most important rule:** each gate is a binary artifact check, not a self-impression. Either the file exists and passes the checklist, or the gate is not met.

---

## KPIs and Measurement

Measuring the wrong things produces discouragement and bad decisions. Three metrics mislead most often:

- **Lines of code accepted** — conflates noisy suggestions with useful ones; rewards quantity over quality
- **Acceptance rate** — measures suggestions made, not value produced; a low acceptance rate on a well-scoped session is correct behavior
- **Time saved per task** — unverifiable without pre-AI baselines; susceptible to reporting bias

The **3-metric minimum set** that reliably reflects Copilot productivity:

| Metric | What it measures | How to track |
|--------|-----------------|-------------|
| **Checklist completion rate** | Whether skills are being applied consistently | Complete each module checklist; count checked items |
| **Session quality score** | Whether sessions achieve their stated objective in one attempt | After each non-trivial session, note: achieved objective? Yes / Partial / No |
| **Convention drift** | Whether AI-generated code is diverging from `CONVENTIONS.md` | Review each PR week one; track violations by type |

---

## Moving from Solo to Team Adoption

A team introduction to Copilot fails in a predictable way: each member discovers the tool independently, invents different norms, and complains about inconsistent results three weeks in. The root cause is the absence of shared starting conditions.

The **minimum rollout kit** — 5 documents that must exist before the first team session:

1. `CONVENTIONS.md` — naming, structure, and review rules (Module 09)
2. `.github/copilot-instructions.md` — project-level instructions (Module 02)
3. `checklists/ai-output-review.md` — the review gate every contributor uses (Module 01)
4. `agents/` directory — team-agreed role specializations (Module 06)
5. `checklists/adoption-milestones.md` — the shared 30/60/90-day progress tracker

Without these five documents, the team has tools but no shared language. Copilot becomes five different products used five different ways.

---

## Governance at Team Scale

Governance at team scale adds one layer beyond the solo governance protocol from Module 09: the **policy tier** and the **"Day 1" onboarding standard** for new team members.

### Policy tiers

| Team size | Policy approach |
|-----------|----------------|
| 2–5 members | Conventions live in `CONVENTIONS.md`; verbal agreement on review norms; AI-assisted commits marked with `AI-assisted:` trailer |
| 6–15 members | Formal `CONVENTIONS.md` with PR required to change it; named reviewer required on every AI-assisted commit; monthly policy review |
| 16+ members | Tiered conventions by domain; compliance review cycle; audit log at aggregate level |

### The "Day 1" onboarding checklist

Every new team member on Day 1 should:

- [ ] Fork or clone the repository and verify Copilot Pro+ status
- [ ] Read `CONVENTIONS.md` top-to-bottom before touching any file
- [ ] Read `.github/copilot-instructions.md` and verify they understand each rule
- [ ] Complete `checklists/ai-output-review.md` on their first AI-suggested code change
- [ ] Open a bounded Ask session — not an Agent session — for their first Copilot-assisted task

---

## Ongoing Quality Discipline

Quality is a rhythm, not a gate. The pre-merge validation protocol from Module 09 handles commit-time quality. This section handles the recurring audit cycle that prevents drift between reviews.

**Monthly review cycle — 4 steps:**

1. **Convention audit** — check the most recent 10 AI-assisted commits against `CONVENTIONS.md`; count violations; update the convention file if the pattern is systemic
2. **Checklist freshness audit** — verify that `checklists/ai-output-review.md` and `checklists/pre-commit.md` still match the codebase's risk profile
3. **Agent drift review** — open the 3 most frequently used agent definitions; confirm that stated tool permissions and handoff criteria match current practice
4. **Roadmap sync** — check the current 90-day milestone; update `checklists/adoption-milestones.md` to reflect actual progress

This cycle takes 20–30 minutes when run monthly. It takes 2–3 hours when skipped for a quarter.

---

## Course Continuation

The capstone marks the completion of the structured course. It does not mark the completion of practice. After the capstone:

- **Update your conventions** every time the codebase adopts a new language, framework, or tool
- **Evolve your agent definitions** when new patterns emerge from multi-agent usage — your 10 definitions are starting points, not final answers
- **Update your prompts** as Copilot feature releases change what's possible; commit dated versions to `prompts/`
- **Re-run the module checklists** annually — skills decay without use; the checklists identify specific gaps quickly

The repository you built this course around is now the example of everything you taught yourself. Maintain it as you would any production asset.

---

## Exercises

See [exercises.md](./exercises.md) for full instructions.

**Quick list:**

1. **Roadmap Gap Assessment** — given a developer's 30-day state, identify what's missing and produce a remediation sequence.
2. **KPI Selection** — select the correct 3 KPIs from a list of 10; explain why the other 7 mislead or cannot be verified.
3. **Team Onboarding Kit** — write the minimum 5-item new-member checklist for a given team profile.
4. **Governance Policy Draft** — given a team size and context, select a policy tier and write a 5-rule policy.
5. **Review Cycle Design** — design a monthly review cycle for a 3-person team with the 4 required steps scoped to their context.

---

## Common Mistakes

| Mistake | Why it happens | How to fix it |
|---------|----------------|---------------|
| Writing a roadmap for an idealized version of yourself | Optimism about available time and motivation | Write the roadmap for your current context — actual project, actual bandwidth, actual skill level |
| Measuring lines accepted or acceptance rate | These numbers are easy to extract from the IDE | Track behavior change instead: checklist completion rate, session quality, convention drift |
| Introducing Copilot to a team without a `CONVENTIONS.md` | "We'll establish norms as we go" | Norms do not emerge from AI-assisted code; they must be written before the first shared session |
| Treating governance as a one-time setup | The policy feels complete after `CONVENTIONS.md` is written | Schedule the monthly review cycle; without it, conventions become historical documents |
| Setting 90-day goals that require all 9 modules before value appears | Front-loading mastery before use | Front-load Day 7 wins — ghost text + basic Ask — and build complexity at 30, 60, 90 |
| Conflating the capstone with the course end | The capstone is the final deliverable | Mastery is a continuous practice; the capstone is a checkpoint, not a graduation |

---

## Token and Premium Request Impact

| Action | Cost level | Notes |
|--------|-----------|-------|
| Roadmap drafting (Ask or Plan mode) | Low | Ask mode for short roadmaps; Plan mode for team rollout planning with multiple constraints |
| KPI selection and reflection | None | Pure documentation; no Copilot session needed |
| Governance policy draft | Low | One Ask session from a team profile description; bounded and deterministic |
| Onboarding kit writing | None | Templates exist in this repository; copy and adapt manually |
| Monthly review cycle | None | A checklist task, not a generation task |
| Capstone | Low | Plan mode useful for structuring the 90-day plan document; no Agent session warranted |

---

## Completion Criteria

You have completed this module when you can:

- [ ] State all 4 time horizons of the adoption roadmap and their gate deliverables from memory.
- [ ] Identify all 3 misleading Copilot metrics and explain why each misleads.
- [ ] Name all 5 documents in the minimum team rollout kit and recall which module introduced each.
- [ ] Describe the governance policy tier that applies to your current team size.
- [ ] Run the 4-step monthly review cycle on your own repository without referencing this document.

**Next step:** → [Capstone — Adoption Roadmap Capstone](../../capstone/)

---

## Module Complete

This is the final module. You have completed the full GitHub Copilot Pro+ Mastery course.

→ Complete the [capstone](../../capstone/) to produce your self-assessed 90-day adoption plan.
→ Self-assess with [checklists/expert-completion.md](../../checklists/expert-completion.md) to verify Expert-level readiness.
