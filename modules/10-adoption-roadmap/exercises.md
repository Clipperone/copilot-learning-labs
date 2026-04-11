# Module 10: Adoption Roadmap, Governance, and Capstone — Exercises

Complete these exercises after reading the module README theory. Attempt each one without referencing the answer first.

For the lab equivalent of this module, see the [Capstone](../../capstone/).

---

## Exercise 1: Roadmap Gap Assessment

**Objective:** Identify missing milestones from a given 30-day state and produce a remediation sequence.

**Scenario:** A developer has been using Copilot for 30 days. Their current state:

- Inline completions are used daily and reviewed before every commit
- `checklists/ai-output-review.md` is used on complex code only, not consistently
- No prompt library committed to `prompts/`
- `instructions/` folder exists with one global instruction file; no project-specific file
- No agent definitions created yet
- No `CONVENTIONS.md` for any project

**Task:** Identify what is missing from the 30-day gate deliverables (see the roadmap table in README.md). Produce a remediation sequence — the order in which the gaps should be filled, with a one-sentence rationale for each.

**Expected output:**

Gaps at 30 days:
1. `checklists/ai-output-review.md` — not applied consistently (must be applied to every AI-assisted change, not selectively)
2. Prompt library — 0 entries instead of ≥5 (checklist gate not met)
3. Project-specific instruction file — global scope only is insufficient for a real project
4. No `CONVENTIONS.md` — this is a 30-day deliverable for team contexts and a strong recommendation for solo use

Remediation sequence (with rationale):
1. Correct the review checklist habit first — it is the highest-risk gap; AI-generated code has gone to commits without full review
2. Write a project-level instruction file — it can be written in one session; it immediately improves all subsequent sessions
3. Commit 5 prompts to `prompts/` — choose prompts already used repeatedly in the past 30 days; they already exist as muscle memory
4. Write `CONVENTIONS.md` — do this after the instruction file; the two documents share naming and structure decisions

---

## Exercise 2: KPI Selection

**Objective:** Identify the 3 KPIs that reliably reflect Copilot productivity. Explain why the others mislead.

**Scenario:** A team lead asks you to propose a Copilot measurement framework for their 8-person team. They have proposed these 10 metrics:

1. Lines of code accepted per day
2. Checklist completion rate
3. Time saved per feature (self-reported)
4. Acceptance rate (accepted / shown)
5. Session quality score (objective achieved? Yes / Partial / No)
6. Number of Copilot sessions opened per week
7. Convention drift count (violations per 10 AI-assisted commits)
8. "Feels like I'm more productive" (team survey)
9. Number of suggestions shown per hour
10. Pull request cycle time reduction

**Task:** Select the 3 KPIs from the list above that should be in the minimum measurement set. For each of the remaining 7, write one sentence explaining why it misleads or cannot be verified.

**Expected output:**

**Selected KPIs (from the module's 3-metric minimum set):**
- #2 — Checklist completion rate: verifiable artifact; measures application consistency
- #5 — Session quality score: per-session behavioral record; measures whether the method worked
- #7 — Convention drift count: code-level evidence; measures whether AI output meets team standards

**Rejected KPIs:**
1. Lines accepted per day — measures volume, not value; 100 boilerplate completions accepted is worse than 5 well-reviewed ones
3. Time saved (self-reported) — no pre-AI baseline exists; susceptible to confirmation bias
4. Acceptance rate — high rate can indicate under-scrutiny; low rate from a disciplined reviewer is correct behavior
6. Sessions opened per week — a throughput metric, not quality; more sessions can mean less focus
8. Team survey — too coarse; cannot separate AI improvement from task familiarity or flow state
9. Suggestions shown per hour — rewards context fragmentation over deep, scoped sessions
10. PR cycle time reduction — confounded by team size, task type, and pipeline changes; not attributable to Copilot alone

---

## Exercise 3: Team Onboarding Kit

**Objective:** Write the minimum 5-item new-member checklist for a given team profile.

**Scenario:** A 10-person engineering team is introducing Copilot Pro+. Their stack: Python + TypeScript. They have: a `CONVENTIONS.md`, a `.github/copilot-instructions.md`, and an `agents/` directory with 7 definitions. They do not have `checklists/adoption-milestones.md`.

**Task:** Write the minimum 5 items for the new-member Day 1 onboarding checklist. Each item must be a specific, verifiable action — not a suggestion.

**Expected output:**

Day 1 checklist for new Copilot team members:

- [ ] Verify Copilot Pro+ is active — open VS Code, confirm the Copilot icon in the status bar shows "active" (not "paused" or "error")
- [ ] Read `CONVENTIONS.md` from top to bottom — answer in writing: (a) the naming rule for AI-assisted commits, (b) the reviewer requirement, (c) one file category excluded from Copilot context
- [ ] Read `.github/copilot-instructions.md` — flag any rule you cannot yet implement and report it to the team lead before your first AI-assisted commit
- [ ] Apply `checklists/ai-output-review.md` to the first AI suggestion you accept — not after; at the moment of acceptance
- [ ] Open one agent definition from `agents/` and read it completely — do not open an Agent session until you can answer: what is this agent's scope? what is its exit condition?

**Note for this scenario:** `checklists/adoption-milestones.md` is missing. Add "Create `checklists/adoption-milestones.md` before the team member's first week ends" as item 6.

---

## Exercise 4: Governance Policy Draft

**Objective:** Select a policy tier and write a minimum 5-rule governance policy for a given team.

**Scenario:** A 12-person team, 3 different codebases (Python, TypeScript, Go), one shared `CONVENTIONS.md` per codebase. They have run Copilot for 6 weeks with no formal governance. A senior engineer has noticed inconsistent commit annotations and undocumented AI-generated functions.

**Task:** Select the correct policy tier. Write a minimum 5-rule governance policy in the format shown in theory.md.

**Expected output:**

**Policy tier:** 6–15 members — formal `CONVENTIONS.md` with PR required to change it; named reviewer required on every AI-assisted commit; monthly policy review.

```text
CONVENTIONS.md — Copilot Policy (v1.0 · YYYY-MM)

Rule 1: Every AI-assisted commit includes an `AI-assisted:` trailer specifying mode (Ask, Edit, Plan, or Agent).
Rule 2: Every AI-assisted commit includes a `Reviewed-by:` trailer with the reviewer's full name.
Rule 3: All AI-generated functions must include an inline comment with the originating prompt on the first commit.
Rule 4: `.copilotignore` entries may only be added or removed via pull request with a senior engineer approval.
Rule 5: CONVENTIONS.md may only be changed via pull request with at least two approvals.
```

---

## Exercise 5: Review Cycle Design

**Objective:** Design a monthly review cycle for a 3-person team with all 4 required steps, scoped to their context.

**Scenario:** A 3-person team, one shared Python project, no dedicated QA. They run 3–5 AI-assisted PRs per week. Their tooling: GitHub, VS Code, pytest. They have `CONVENTIONS.md`, `agents/`, and `checklists/ai-output-review.md`.

**Task:** Design their monthly review cycle using the 4-step structure from README.md. For each step, write the specific evidence they should produce given their context.

**Expected output:**

**Monthly review cycle — 3-person Python team:**

| Step | Action | Evidence of completion |
|------|--------|----------------------|
| Convention audit | Review the 10 most recent AI-assisted PR diffs against `CONVENTIONS.md`; count violations by type (trailer missing, prompt comment absent, reviewer not named) | A markdown note: violation count by type; updated `CONVENTIONS.md` if the same violation appears 3+ times |
| Checklist freshness audit | Open `checklists/ai-output-review.md`; verify the OWASP check section reflects the team's current use of AI-generated API endpoints and pytest coverage | One-sentence note per checklist section: whether current or flagged for update |
| Agent drift review | Open the 3 most-used agent definitions (by frequency of use in the past month); compare stated tool permissions to what was actually used; flag any handoff that did not match the documented criterion | Updated `## Revision Notes` section in each definition where mismatches were found |
| Roadmap sync | Open `checklists/adoption-milestones.md`; mark actual state for the current 30/60/90-day milestone; record gap if off-track | Updated `adoption-milestones.md` with current date and actual status |
