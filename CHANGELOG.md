# Changelog

All notable changes to this course repository are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
This project uses [semantic versioning](https://semver.org/): `MAJOR.MINOR.PATCH`.

| Segment | Meaning |
|---------|---------|
| MAJOR | Breaking restructure — paths, module numbering, or template changes |
| MINOR | New modules, labs, or major content additions |
| PATCH | Fixes, clarifications, link updates, date refreshes |

---

## [Unreleased]

### Added (Phase 1 — audit remediation, 2026-04-14)

- `modules/01-foundations/theory.md` — new section "When NOT to Use Copilot" (8-row situation table + rule of thumb)
- `modules/01-foundations/checklist.md` — 3 self-assessment items for the new section
- `modules/03-token-optimization/theory.md` — new section "Context Variables and Chat Participants" (`#file`, `#selection`, `#codebase`, `#sym`, `#changes`, `#terminalLastCommand`; `@workspace`, `@terminal`, `@vscode`; 4 discipline rules)
- `modules/03-token-optimization/checklist.md` — 4 self-assessment items
- `modules/06-agents/exercises.md` — Exercise 6: design an agent for a role outside the 10-role catalog
- `modules/06-agents/checklist.md` — 5 self-assessment items for Exercise 6
- `modules/08-advanced-features/exercises.md` — Exercise 6: Plan→Implementer handoff with drift diagnosis
- `modules/08-advanced-features/checklist.md` — 4 self-assessment items for Exercise 6

### Changed (Phase 2 sweep — deprecated mode terminology, 2026-04-14)

Edit mode was consolidated into Agent mode in VS Code 1.110. References across the course updated accordingly:

- `README.md`, `COURSE_OVERVIEW.md`, `docs/course-design-brief.md` — mode list updated to inline completion / inline chat / Ask / Plan / Agent
- `checklists/beginner-completion.md`, `checklists/advanced-completion.md` — Edit mode references removed
- `modules/01-foundations/exercises.md` — reflection question 4: Exercise 3 is Agent mode (not Edit)
- `modules/05-custom-instructions/README.md` — mode triple updated to (Ask, Plan, Agent)
- `modules/06-agents/checklist.md` — Agent vs. Ask/Plan (Edit removed)
- `modules/10-adoption-roadmap/exercises.md` — `AI-assisted:` trailer values updated to (Ask, Plan, or Agent)
- `labs/lab-01-getting-started/README.md` — Task 2 mode list updated to Ask, Agent, Plan, Inline chat

### Changed (Phase 1 count corrections)

- `modules/06-agents/checklist.md` — 5 → 6 exercises (Exercise 6 added)
- `modules/08-advanced-features/README.md` — 5 → 6 exercises
- `labs/lab-06-agents-and-personas/README.md` — prerequisite count 5 → 6

### Added (Phase 2 — prompt files, 2026-04-14)

- `modules/04-prompt-engineering/theory.md` — new section "Prompt Files (`.prompt.md`)": anatomy, frontmatter, body substitutions, decision table vs. instructions/agents, conventions, anti-patterns, migration steps
- `modules/04-prompt-engineering/exercises.md` — Exercise 6: promote one Markdown prompt from `prompts/` to `.prompt.md` with two-input verification
- `modules/04-prompt-engineering/checklist.md` — 5 self-assessment items for prompt files
- `modules/05-custom-instructions/theory.md` — new sub-section "Instruction file vs. prompt file vs. custom agent" with decision table and migration pattern
- `prompts/README.md` — added "Runnable via `/`" pathway, cross-referenced Module 04 prompt-files section

### Added (Phase 2 — Edits-style workflows in Agent mode, 2026-04-14)

Edit mode was consolidated into Agent mode in VS Code 1.110. New content teaches the equivalent capability:

- `modules/08-advanced-features/theory.md` — new section "Edits-Style Workflows in Agent Mode (and Custom Agents)": current panel-mode set, 5 discipline rules, custom agent anatomy with frontmatter example, decision table, working-set discipline, anti-patterns, migration note
- `modules/08-advanced-features/exercises.md` — Exercise 7: coordinated rename across 3 files in Agent mode with discipline rules + custom agent bonus
- `modules/08-advanced-features/checklist.md` — 4 self-assessment items
- `modules/08-advanced-features/README.md` — exercise count 6 → 7
- `modules/01-foundations/theory.md` — added "Note on Edit mode" pointing to Module 08

### Added (Phase 2 — MCP fundamentals, 2026-04-14)

- `modules/08-advanced-features/theory.md` — new section "MCP — Model Context Protocol": purpose, anatomy, `mcp.json` config, decision table vs. custom agent / instruction / prompt file, anti-patterns, end-to-end example with `@modelcontextprotocol/server-filesystem`
- `modules/08-advanced-features/exercises.md` — Exercise 8: configure one MCP server, verify scope boundary, inspect JSON-RPC trace
- `modules/08-advanced-features/checklist.md` — 5 self-assessment items
- `modules/08-advanced-features/README.md` — exercise count 7 → 8

### Added (Phase 2 — Metrics & Content Exclusions, 2026-04-14)

- `modules/10-adoption-roadmap/theory.md` — two new sections: "Reading the Copilot Usage Dashboard" (3 trustworthy signals, 3 misleading metrics, surface map) and "Content Exclusions — Admin Controls Beyond `.copilotignore`" (3 scopes, configuration, sensitivity-class mapping, limits, anti-patterns)
- `modules/10-adoption-roadmap/exercises.md` — Exercise 6 (read a dashboard snapshot) and Exercise 7 (draft a content-exclusion policy)
- `modules/10-adoption-roadmap/checklist.md` — 9 self-assessment items across the two new topic areas

### Added (Phase 2 — Module 11 + capstone integration, 2026-04-14)

New module covering non-IDE Copilot surfaces (coding agent, github.com, `gh copilot` CLI):

- `modules/11-platform-integration/README.md` — module overview: 5 learning objectives, surface decision matrix, common mistakes, best practices, token impact, completion criteria
- `modules/11-platform-integration/theory.md` — coding-agent lifecycle, `copilot-setup-steps.yml`, github.com surfaces, CLI patterns, surface-decision rationale, cross-surface anti-patterns
- `modules/11-platform-integration/exercises.md` — 4 exercises: delegate to coding agent, generate+rewrite PR summary, `gh copilot` 4-question gate, surface decision
- `modules/11-platform-integration/checklist.md` — 18 self-assessment items across 5 sections
- `capstone/README.md` — added Deliverable 8 (`platform-artifact.md`) with Option A / Option B; updated rubric, success criteria, premium budget; bumped 7→8 deliverables
- `capstone/checklist.md` — added Deliverable 8 row + dedicated gate section; bumped 7→8 deliverables

### Changed (Phase 2 — sweep for M11 + capstone Deliverable 8 + count fixes, 2026-04-14)

- `SYLLABUS.md` — added Module 11 section; updated Level 4 row (modules 08–11; 9 hrs); added M11 to dependency map; bumped capstone deliverable count 7→8
- `COURSE_OVERVIEW.md` — added M11 to skills list and structure table; bumped 10→11 modules
- `LEARNING_PATH.md` — added M11 step in Path 4; bumped 7→8 capstone deliverables; added M11 to dependency map
- `README.md` — added Module 11 row to module table
- `docs/index.md` — bumped 10→11 modules; bumped 7→8 capstone deliverables
- `docs/module-dependency-map.md` — added M11 to linear chain; added M11 row to lab-to-module map; added new asset rows (`mcp.json`, `.prompt.md`, custom agents, `copilot-setup-steps.yml`)
- `docs/module-lab-map.md` — added M11 entry noting in-module exercises (no separate lab) + capstone Deliverable 8 link
- `labs/README.md` — added M11 row (in-module exercises, no separate lab); updated capstone row 7→8 deliverables, M04–M10 → M04–M11
- `presentation/course-overview.md` — bumped 7→8 capstone deliverables
- `modules/10-adoption-roadmap/README.md` — Next Module section now points to M11 then capstone
- `modules/10-adoption-roadmap/checklist.md` — added "Platform deliverable (M11 applied)" section
- `checklists/expert-completion.md` — added "Platform deliverable (M11 skills applied)" section

### Notes

- Module 11 has no separate lab. Coding-agent / github.com / CLI work happens outside a local repo, so a `labs/lab-11-…/` folder would be artificial. Exercises live in `modules/11-platform-integration/exercises.md`. Capstone Deliverable 8 ties M11 work into the capstone.
- The CHANGELOG entry from v1.0.0 ("deliverables updated to reflect all 7 capstone artifacts") is preserved as historical record; current count is 8.

---

## [1.0.0] — 2026-04-11

### Added
- `modules/10-adoption-roadmap/` — complete: README, theory, exercises, checklist
- `capstone/` — complete: README (7-deliverable capstone with project brief, validation diff, evaluation rubric, extension ideas), checklist
- `checklists/expert-completion.md` — Level 4 gate: M08–M10 + capstone synthesis; cross-level synthesis section; mindset check; sign-off block
- `checklists/adoption-milestones.md` — 7/30/60/90-day milestone tracker with evidence columns; post-90-day monthly review log

### Changed
- `README.md` — Module 10 row linked; capstone contents row updated; roadmap row v1.0 marked Current
- `SYLLABUS.md` — Module 10 heading linked; deliverables updated to reflect all 7 capstone artifacts
- `LEARNING_PATH.md` — Path 4 Module 09 name corrected; capstone and expert-completion linked
- `labs/README.md` — capstone row added
- `docs/module-dependency-map.md` — capstone row added to Lab-to-Module table
- `modules/09-repository-quality/README.md` — Next Module: removed *(coming soon)*
- `modules/09-repository-quality/checklist.md` — Module Complete: removed *(coming soon)*

---

## [0.5.0] — 2026-04-10

### Added
- `modules/08-advanced-features/` — complete: README, theory, exercises, checklist
- `modules/09-repository-quality/` — complete: README, theory, exercises, checklist
- `labs/lab-08-advanced-feature-tour/` — complete: README, checklist, starter, solution
- `labs/lab-09-repository-health-audit/` — complete: README, checklist, starter (deliberately degraded Python project with OWASP A03 vulnerabilities), solution

---

## [0.4.0] — 2026-04-10

### Added
- `modules/06-agents/` — complete: README, theory, exercises, checklist
- `modules/07-multi-agent-workflows/` — complete: README, theory, exercises, checklist
- `labs/lab-06-agents-and-personas/` — complete: README, checklist, starter, solution
- `labs/lab-07-multi-agent-workflow/` — complete: README, checklist, starter, solution
- `agents/` — folder scaffold with README; populated during Lab 06
- `checklists/advanced-completion.md`

---

## [0.3.0] — 2026-04-10

### Added
- `modules/04-prompt-engineering/` — complete: README, theory, exercises, checklist
- `modules/05-custom-instructions/` — complete: README, theory, exercises, checklist
- `labs/lab-04-prompt-engineering/` — complete: README, checklist, starter, solution
- `labs/lab-05-custom-instructions/` — complete: README, checklist, starter, solution
- `instructions/` — global, project, and path-scoped custom instruction examples
- `checklists/intermediate-completion.md`

---

## [0.2.0] — 2026-04-10

### Added
- `modules/02-configuration/` — complete: README, theory, exercises, checklist
- `modules/03-token-optimization/` — complete: README, theory, exercises, checklist
- `labs/lab-02-configuration/` — complete: README, checklist, starter (Python project), solution (fully configured project with `.vscode/`, `.github/`, `.editorconfig`, `pyproject.toml`)
- `labs/lab-03-token-audit/` — complete: README, checklist, starter worksheet, solution worksheet
- `prompts/refactoring/refactor-for-clarity.md` — refactoring prompt library starter
- `prompts/refactoring/extract-function.md` — extract helper function prompt
- `checklists/pre-commit.md` — AI-assisted code pre-commit review checklist

---

## [0.1.0] — 2026-04-10

### Added
- Repository scaffold: folder structure, LICENSE, CODE_OF_CONDUCT
- `docs/course-design-brief.md` — source of truth for course design
- `COURSE_OVERVIEW.md` — scope, audience, outcomes
- `SYLLABUS.md` — full curriculum reference
- `LEARNING_PATH.md` — navigation by level and persona
- `CONTRIBUTING.md` — contribution guidelines
- `CHANGELOG.md` — this file
- `.github/copilot-instructions.md` — repo-wide Copilot behavior rules
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/` — bug report, content suggestion, lab feedback
- `.vscode/extensions.json` — recommended extensions
- `.vscode/settings.json` — repo-level editor config
- `templates/` — module, lab, prompt, and agent definition templates
- `modules/01-foundations/` — complete: README, theory, exercises, checklist
- `labs/lab-01-getting-started/` — complete: README, starter, solution, checklist
- `prompts/README.md` + starter prompts (generation, debugging)
- `checklists/beginner-completion.md`
- `docs/architecture.md`
- `docs/module-dependency-map.md`

