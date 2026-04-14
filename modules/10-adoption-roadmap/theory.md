# Module 10: Adoption Roadmap, Governance, and Capstone — Theory Reference

> Extended reference for [README.md](./README.md). Read the module overview first.
> Prose sections are capped at 500 words; tables and code blocks are excluded from that limit.

---

## Why Adoption Plans Fail

Four patterns explain virtually every failed Copilot adoption:

**1. Feature orientation without skill depth.** Teams explore all five modes in week one, use none reliably by week four. The fix is depth before breadth: achieve consistent results with inline completion and Ask before touching Agent mode.

**2. Solo adoption without shared conventions.** One engineer adopts fully. Three others adopt inconsistently. The result is a codebase with four different norms for AI-assisted commits. The fix is `CONVENTIONS.md` before the second person enables Copilot.

**3. Measurement without baseline.** "We're saving X hours" with no pre-Copilot baseline is not measurement — it is impression management. The fix is tracking behavior change (checklist completion, convention adherence) rather than output estimates.

**4. No review cycle.** Governance is written at setup and forgotten. Conventions drift from practice. Agent definitions describe roles no one plays. The fix is a scheduled monthly review, not a commitment to stay disciplined.

This course is a direct inoculation against all four patterns. Module 01 builds skill depth before breadth. Module 09 establishes conventions. This module installs measurement and the review cycle.

---

## KPI Anti-Pattern Analysis

The following metrics appear useful but produce misleading signals in practice:

| Metric | Why it misleads |
|--------|----------------|
| Lines of code accepted | Measures suggestion volume, not quality; a single well-placed suggestion produces more value than 100 boilerplate completions |
| Acceptance rate | A rigorous reviewer with a well-scoped session rejects more suggestions than a passive user; high acceptance rate can indicate under-scrutiny |
| Time saved per task | Requires a pre-AI baseline that usually does not exist; task time is confounded by task complexity, not just AI assistance |
| Suggestions shown per hour | A throughput metric that rewards context fragmentation — many small suggestions instead of few good ones |
| "I feel more productive" | Too coarse; cannot distinguish AI improvement from general flow state or task familiarity effects |

Apply the 3-metric minimum set instead: checklist completion rate, session quality score, convention drift count. These are verifiable, actionable, and resistant to gaming.

---

## Governance Policy Template Walkthrough

A minimum team governance policy has 5 rules. Each rule is one declarative statement:

```text
CONVENTIONS.md — Copilot Policy (v1.0 · YYYY-MM)

Rule 1: Every AI-assisted commit includes an `AI-assisted:` trailer with the mode used.
Rule 2: Every AI-assisted commit includes a `Reviewed-by:` trailer with the reviewer's name.
Rule 3: No AI-generated code is merged without a named human reviewer.
Rule 4: `.copilotignore` is reviewed and approved by a senior engineer before any change is committed.
Rule 5: CONVENTIONS.md may only be changed via pull request with at least one approval.
```

Tier this policy by team size using the table in [README.md](./README.md#governance-at-team-scale). Increase rule count as team size grows. Never reduce it without explicit team agreement.

---

## Team Onboarding Sequencing

The 5-document minimum rollout kit is sequenced deliberately. Do not present all five at once. Structure the first team session as follows:

| Session order | Document | Action |
|--------------|----------|--------|
| 1 | `CONVENTIONS.md` | Read top-to-bottom; answer 3 questions: what is the naming rule? what is the review rule? what may not be committed? |
| 2 | `.github/copilot-instructions.md` | Read and confirm understanding; identify any rule the team member cannot yet follow (flag for training) |
| 3 | `checklists/ai-output-review.md` | Apply to the first real Copilot suggestion the team member accepts |
| 4 | `agents/` directory | Choose one agent definition and read it completely; do not open an Agent session yet |
| 5 | `checklists/adoption-milestones.md` | Set the 7-day target; schedule the 30-day check-in |

This sequence installs constraints before capabilities. A team member who understands the review gate and conventions before running a session makes fewer governance errors per session.

---

## The Monthly Review Cycle in Detail

Each of the 4 steps in the monthly review cycle has a specific evidence requirement. "I checked" without evidence is not a completed step.

| Step | Evidence of completion |
|------|----------------------|
| Convention audit | Commit count reviewed; violation count recorded; `CONVENTIONS.md` updated if violations are systemic |
| Checklist freshness audit | Both checklists opened; any outdated items noted and either corrected or flagged for deprecation |
| Agent drift review | 3 most-used definitions compared to actual usage; mismatches documented in the definition file under `## Revision Notes` |
| Roadmap sync | `checklists/adoption-milestones.md` updated with current actual state; gap analysis recorded if off-track |

A completed monthly review takes 20–30 minutes and produces at least one updated file. If no files change, the review was either skipped or the team is perfectly on track — one of these is more likely.

---

## Reading the Copilot Usage Dashboard

Copilot exposes usage data on three surfaces: the individual usage page (any plan), the Business/Enterprise admin dashboard, and per-repo activity views. A governance plan that ignores these is flying blind.

### What lives where

| Surface | Audience | Granularity | What it shows |
|---------|---------|-------------|---------------|
| Individual usage (`github.com/settings/copilot/usage`) | The user themself | Daily / monthly | Premium-request count, model breakdown, quota burn |
| Org admin dashboard (Business/Enterprise) | Org admin | Per-user, per-repo, per-day | Active users, suggestions, acceptance rate, chat usage, agent sessions, content-exclusion hits |
| Enterprise insights / API | Enterprise admin | Org-wide aggregates | Trend data, cross-org comparison, exportable for BI tools |

### Three signals worth tracking

1. **Engagement breadth.** *What fraction of seats had at least one Copilot interaction this week?* Distinguishes "deployed" from "adopted." Below 60% breadth at week 4 is an adoption-failure signal — return to the M10 onboarding sequence rather than buying more seats.
2. **Agent-vs-inline ratio.** *What fraction of premium requests come from Agent sessions vs. inline/chat?* A team with a sudden Agent-mode spike is either solving harder problems (good) or has lost discipline on mode selection (M03/M06 problem). Investigate the spike before re-budgeting.
3. **Premium quota burn rate.** *At current rate, when does the team exhaust its monthly premium allotment?* Linear projection from week 1 against the monthly cap. Burning faster than 1/4 the cap per week means a model-selection conversation is overdue.

### Three metrics that mislead

These appear on the dashboard but should not drive decisions:

- **Raw acceptance %.** A rigorous reviewer rejects more than a passive user; high acceptance can indicate under-scrutiny.
- **Lines accepted.** Volume metric; a single well-placed completion can outperform 100 boilerplate lines.
- **"Time saved."** Almost always derived from a missing baseline. Treat as marketing, not measurement.

### Org-level vs. individual-level

- **Individual surface:** sees only their own data.
- **Admin surface:** sees per-user data — this is the data-handling boundary that drives the privacy conversation in onboarding. State explicitly in `CONVENTIONS.md` what the admin can see and why.

> Verify dashboard URLs and feature availability against the [GitHub Copilot dashboard docs](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/reviewing-activity-related-to-github-copilot-in-your-organization) — fields and access controls evolve.

---

## Content Exclusions — Admin Controls Beyond `.copilotignore`

`.copilotignore` (Module 08) is workspace-scope and developer-controlled. **Content exclusions** are admin-controlled rules that prevent matching files from being sent to Copilot at all — for suggestions and for chat — across every developer's machine.

### Three scopes

| Scope | Set by | Applies to |
|-------|--------|-----------|
| Repository | Repo admin | One repository |
| Organization | Org admin | All repos in the org |
| Enterprise | Enterprise admin | All orgs in the enterprise |

**Precedence:** Wider scope wins on inclusion; narrower scope wins on additional exclusion. An enterprise-level exclusion cannot be overridden at org or repo level.

### Configuration

Set at: org settings → Copilot → Content exclusions. Format: glob patterns, one per line, with optional comment.

```text
# Restricted by data classification
**/secrets/**
**/.env
**/.env.*

# Regulated client data
clients/regulated/**

# Generated code we don't want surfaced as suggestions
**/generated/**
```

After saving, the status bar Copilot icon shows an "exclusion active" state in any matching file, and `Copilot: Diagnostics` lists why context is reduced.

### Mapping to sensitivity classes from Module 08

| Sensitivity (M08) | Exclusion treatment |
|-------------------|---------------------|
| Restricted | **Always exclude** at org or enterprise scope |
| Confidential | Consider exclusion; if not excluded, document the rationale |
| Internal | Allow with `.copilotignore` developer overrides for specific files |
| Public | Allow |

### Limits — what exclusions do not solve

- **Best-effort, not airtight.** Exclusions reduce risk; they are not a DLP system. Combine with secret scanning and regular audits.
- **Not a replacement for `.gitignore`.** Both exist for different reasons; an excluded file can still be committed if not also gitignored.
- **No retroactive removal.** Excluding a file today does not remove its content from any model that has already trained on it.
- **Exclusions can break workflows.** Excluding `**/migrations/**` may make Copilot unable to help with database changes — review with users before rolling out.

### Anti-patterns

- **Relying on `.copilotignore` for compliance-mandated exclusions.** It is a developer tool, not an admin control. Compliance requires admin-level enforcement.
- **Granular per-developer exceptions that nobody maintains.** Two-month-old exception lists become security gaps. Sunset every exception with a date.
- **Exclusions without documented rationale.** When the next admin reviews the list, "why is this excluded?" must be answerable from the comment, not from oral history.
- **Treating exclusions as one-time setup.** They drift like any other policy. Add to the M10 monthly review cycle: confirm the active exclusion list still matches the sensitive-file inventory.

> Verify configuration UI and behavior against the [GitHub content exclusions docs](https://docs.github.com/en/copilot/how-tos/configure-content-exclusion) — both location and matching semantics have changed in past releases.

---

## The Mastery Loop

The course ends at the capstone. Mastery does not. The practices installed across 10 modules interact:

- Better prompts (M04) make agent sessions (M06) more efficient
- Better agent definitions (M06) make multi-agent workflows (M07) more reliable
- Better repository structure (M09) makes all sessions more accurate
- Better governance (M10) makes all improvements persistent

Each module you revisit with experience from the others produces a qualitatively different result. The adoption roadmap's 90-day gate is a checkpoint, not a terminus. At 90 days, evaluate each layer and upgrade the weakest one first.

---

## Official Resources

- [GitHub Copilot plans for organizations and enterprises](https://docs.github.com/en/copilot/concepts/billing/organizations-and-enterprises)
- [Managing your company's spending on GitHub Copilot](https://docs.github.com/en/copilot/how-tos/manage-and-track-spending/manage-company-spending)
- [GitHub Copilot documentation](https://docs.github.com/en/copilot)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)

---

← [Back to Module 10 README](./README.md)
