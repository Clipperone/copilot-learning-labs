# Module 09: AI-Friendly Repository Engineering

> **Level:** Expert
> **Estimated time:** ~2.5 hours (module theory ~1.5 hrs · lab ~60 min)
> **Prerequisite:** [Module 08 — Advanced Features](../08-advanced-features/) · Complete the [Advanced Phase Checklist](../../checklists/advanced-completion.md) before this module.
> **Verified:** 2026-04

> ⚠️ **Premium request note:** Most repository audit and governance work runs effectively in Ask mode with the default model. Use Plan mode for `CONVENTIONS.md` authoring when the convention set spans multiple languages or frameworks. Escalate to the Security Reviewer persona only for compliance-critical repositories where `.copilotignore` scope decisions have regulatory implications. The most common waste pattern is opening an Agent session for a task that a single Ask query resolves in one turn.

---

## Learning Objectives

By the end of this module you will be able to:

1. Audit a repository against the 6-property AI-friendliness checklist and produce a ranked issue list.
2. Write READMEs and technical documentation structurally optimized for AI context — not just human readability.
3. Apply naming and structure conventions that maximize signal clarity for both human and AI readers.
4. Govern AI-generated code with a documented review protocol covering traceability, ownership, and merge criteria.
5. Apply the pre-merge validation protocol to any diff before committing.
6. Select appropriate convention sets for small, medium, and large repositories.

---

## Why This Module Exists

Module 08 taught how to apply Copilot's full feature set to a working codebase. Every technique — Plan mode, AI-assisted review, terminal integration, quality gates — depends on strong context signals reaching the model.

Context quality is not constant. It degrades as a repository grows: ambiguous names, vague documentation, mixed-concern files, and uncommitted conventions all reduce the signal-to-noise ratio of every session. A senior engineer running a well-structured repository with `.copilotignore`, clear naming, and a `CONVENTIONS.md` file gets systematically better AI responses than the same engineer working in an unstructured repository — even using identical prompts.

This module addresses that dimension. Repository structure is the enabler of everything learned in Modules 01–08. Without it, prompt discipline and agent workflows produce inconsistent results that require constant manual correction.

---

## The 6-Property AI-Friendliness Checklist

Every repository can be assessed against six properties. An AI-friendly repository has all six. A repository missing any property degrades AI context quality in a specific, diagnosable way.

| Property | Description | When missing |
|----------|-------------|--------------|
| **Clear naming** | Every file, function, and variable name uniquely identifies its purpose and scope | AI generates code that reuses ambiguous names; incorrectly infers relationships between unrelated concepts |
| **Structured documentation** | READMEs and inline docs have predictable, labelled sections the AI can extract context from | AI generates code that ignores documented constraints; cannot infer intent from prose-first docs |
| **Explicit conventions** | Naming, structure, and review rules are stated once in a machine-readable `CONVENTIONS.md` | AI invents conventions per session; inconsistencies accumulate across AI-assisted commits |
| **Scoped context** | `.copilotignore` and directory structure prevent noise from reaching the context window | Sessions acquire irrelevant signal; relevant files are diluted; generation quality drops |
| **Minimal redundancy** | No duplicate files, dead code, or large commented-out blocks that add noise without signal | AI treats stale code as active context; generates defensive workarounds for non-existent constraints |
| **Governed output** | Every AI-assisted commit has a named reviewer and a documented review trail | Ownership gaps accumulate; AI output drifts from team standards without visible checkpoints |

**Scoring rule:** Count satisfied properties (0–6). Score ≥ 5 = AI-ready. Score 3–4 = degraded — fix before any large AI-assisted effort. Score ≤ 2 = high-noise environment — expect inconsistent AI quality regardless of prompt quality.

---

## Documentation Quality for AI Context

Human-readable documentation and AI-readable documentation are not the same. A well-written prose README explains the project to a developer who reads it end-to-end. It is poor AI context: no section boundaries, no explicit constraints, no structure the model can locate and extract.

**The anatomy of an AI-useful README:**

| Section | Contents | AI signal value |
|---------|----------|-----------------|
| `## What this does` | One paragraph, functional description only | High — establishes project scope |
| `## Setup` | Numbered steps; every command on its own line | High — grounding for environment-dependent suggestions |
| `## Project structure` | File tree with one-line purpose per entry | High — prevents misidentification of file roles |
| `## Conventions` | Link to `CONVENTIONS.md`; key rules inline | High — prevents invention of inconsistent patterns |
| `## Known limitations` | Explicit constraints and out-of-scope items | High — prevents AI from generating solutions to non-problems |
| `## Architecture notes` (optional) | Data flow, key dependencies, non-obvious design decisions | High if present — explains *why* the code is structured as it is |
| `## Getting started` narrative | Human onboarding prose | Low for AI — useful for humans, ignored by model |

> **Rule:** Every section must have a heading. Prose without a heading is invisible to structured context extraction. If you would not label it in a table of contents, label it in the README.

**Inline documentation standards for AI context:**

| Item | Minimum content |
|------|----------------|
| Module/file docstring | What the file does; what it does NOT do |
| Function docstring | Input types, output type, failure modes, side effects |
| Class docstring | Responsibility, not implementation |
| Inline comment | Why the code does this — not what it does (the code shows what) |

Poor inline documentation is not just a human maintainability problem. A function with no docstring is a context gap: the AI infers intent from the implementation, which is often wrong for non-obvious functions.

**Issue writing standards:**

Issue descriptions are AI context when Copilot is used in the context of a linked task. An issue written as "fix the login bug" provides zero context. Write issues with:

1. **Observed behavior** — what happens now
2. **Expected behavior** — what should happen
3. **Scope** — files or functions affected (explicit)
4. **Acceptance criteria** — what "done" looks like, verifiable

---

## Naming and Structure Conventions

Consistent naming is a force multiplier for AI context quality. Within a session, Copilot infers patterns from the files it can see. Consistent names create consistent inferences. Inconsistent names create inconsistent inferences at scale.

**Naming principles:**

| Principle | Bad example | Good example |
|-----------|------------|--------------|
| Names describe scope, not action | `helpers.py`, `utils.py`, `misc.py` | `auth_validators.py`, `payment_formatters.py` |
| Names are stable after first use | Rename files only when the scope genuinely changes | — |
| Names carry type when ambiguous | `process(data)` | `process_payment(payment: Payment)` |
| No filler words | `handle_`, `do_`, `manage_` as standalone prefixes | Name the specific operation directly |

**Directory structure by repository size:**

| Size | Files | Structure principle |
|------|-------|---------------------|
| Small | ≤ 20 | Flat. One directory per concern. No nesting. |
| Medium | 20–200 | Layered. Top-level by concern; within by type. |
| Large | 200+ | Domain-driven. Top-level by domain; each domain has its own `src/`, `tests/`, `docs/`. |

Choosing a structure larger than the repository requires is as harmful as no structure: over-engineering confuses context by adding layers with no files. Choose the structure that matches current size, not anticipated size.

**What to put in `CONVENTIONS.md`:**

A `CONVENTIONS.md` file is machine-readable when it uses short, declarative sentences. Long prose blocks are not parsed as rules. Minimum content:

1. Naming rules (functions, classes, files, directories) — one rule per bullet
2. Import order
3. Test file location pattern
4. Commit message format
5. AI-assisted commit marker (how to label AI-assisted commits in the commit message)

---

## Governance of AI-Generated Code

The governance problem is not about trust — it is about traceability. When a bug appears in code that was AI-generated, a team without a governance protocol cannot determine: who reviewed it, what prompt produced it, and whether the output was validated before commit.

**The 3-tier audit trail:**

| Tier | What | Where |
|------|------|-------|
| Session log | The prompt(s) and chat history that produced the code | Committed Markdown file in `agents/` or a task-specific subfolder |
| Diff annotation | Which lines in the diff are AI-generated | `# AI-generated` inline comment (removed after review confirming correctness) |
| Merge annotation | Name of the human reviewer who cleared the AI output | Git commit message: `Reviewed-by: [name]` trailer, or PR approval record |

Not all three tiers are required for every commit. Apply the tier appropriate to risk:

| Risk level | Tiers required |
|------------|----------------|
| Low (cosmetic, docs) | Merge annotation only |
| Medium (logic, new functions) | Diff annotation + Merge annotation |
| High (auth, payments, external integrations) | All 3 tiers |

**AI-assisted commit marker:**

Use a consistent prefix in the commit message body to indicate AI-assisted commits. Example:

```
fix(auth): validate JWT expiry before returning user object

AI-assisted: generated check logic; reviewed against OWASP A07.
Reviewed-by: [name]
```

The marker is not an apology — it is a traceability signal. It does not reduce the authority of the commit. It makes future debugging and auditing faster.

---

## Pre-Merge Validation Protocol

Before any AI-assisted commit merges, apply the 5-gate checklist. Each gate is binary: pass or fail. A single failure blocks the merge.

| Gate | Check | Fails when |
|------|-------|-----------|
| 1. Scope | Does this diff contain exactly what was requested? | Diff includes unrequested changes |
| 2. Ownership | Is there a named human reviewer for every AI-generated function? | No reviewer identified for one or more functions |
| 3. Test coverage | Do existing tests cover the changed lines? | No test exercises a non-trivial AI-generated path |
| 4. OWASP check | Does the diff pass the 5-category OWASP minimum from Module 08? | Any OWASP category fails |
| 5. Convention compliance | Does the diff comply with `CONVENTIONS.md` rules? | Any naming, structure, or format rule is violated |

Record the result of this checklist in the commit message body or in a linked file. A "passed" record is documentation that the protocol ran. A "failed" record with the gate and reason attached is blocked from merge until the failure is resolved.

---

## Repository Size Considerations

The convention set appropriate to a repository depends on its size. Applying large-repository governance to a personal project creates bureaucratic overhead with no quality benefit. Applying small-repository simplicity to a large team codebase creates governance gaps.

| Dimension | Small (≤ 20 files) | Medium (20–200 files) | Large (200+ files) |
|-----------|---------------------|----------------------|-------------------|
| `.copilotignore` | Optional — usually not needed | Recommended — exclude generated and test fixture dirs | Required — define by domain |
| `CONVENTIONS.md` | Simple: 5–8 bullet rules | Structured: sections per language/concern | Formal: pull-request required to change it |
| Commit annotation | Optional marker | Marker + reviewer name | All 3 audit tiers |
| AI context scope | Entire repo is acceptable | Scope by directory | Scope by domain; never open full-repo sessions |
| Review protocol | Self-review acceptable | Peer review recommended | Formal PR + named reviewer required |

Changing convention set as the repository grows is expected — and should be documented in `CONVENTIONS.md` as a versioned entry. A repository that never updates its governing conventions is a repository that has outgrown them.

---

## Extension: Connecting to Secure Usage (Module 08)

Repository quality and secure usage reinforce each other. A well-structured `.copilotignore` covers secure-usage needs and context-scoping needs simultaneously. A `CONVENTIONS.md` that includes the sensitivity classification table from Module 08 makes secure usage a convention rather than a per-session decision.

Both are long-term maintenance artifacts, not one-time configurations. Audit `.copilotignore` whenever the file inventory changes. Update `CONVENTIONS.md` when the codebase adopts a new language, framework, or team standard. Neither file manages itself.

> See [Module 08 — Secure Usage Patterns](../08-advanced-features/) for the sensitivity classification framework and credential hygiene rules.

---

## Exercises

See [exercises.md](./exercises.md) for full instructions.

**Quick list:**

1. **AI-Friendliness Score** — rate a repository against the 6-property checklist; produce a ranked finding list with remediation priority.
2. **README Reconstruction** — rewrite a vague README section using the AI-useful structure from this module.
3. **Naming Convention Diagnosis** — identify 6 naming violations in a file tree; propose compliant replacements with reasoning.
4. **Governance Gap Analysis** — read a PR diff; identify missing governance elements (ownership, review trail, commit annotation).
5. **Pre-Merge Validation** — apply the 5-gate protocol to a code snippet; produce a pass/fail finding per gate.

---

## Common Mistakes

| Mistake | Why it happens | How to fix it |
|---------|---------------|---------------|
| Renaming files for AI clarity without updating imports | Treating file names as cosmetic | Run a dependency check before renaming; update all import paths atomically |
| Writing READMEs for human narrative only | "Good writing = good docs" assumption | Add labelled sections for AI structure; prose sections are invisible to context extraction |
| Treating AI-generated commits as owned without a named reviewer | Implicit trust in AI correctness | Apply the diff annotation + merge annotation tiers for every non-trivial AI-assisted commit |
| Using `.copilotignore` as a substitute for `.gitignore` | Confusing two distinct exclusion mechanisms | `.copilotignore` controls AI context; `.gitignore` controls version control — both are needed independently |
| Applying small-repo conventions to a large codebase | Starting conventions early and never updating them | Version `CONVENTIONS.md`; audit the convention set when the file count doubles |
| Writing convention rules in dense prose | Prose reads as documentation, not rules | Use one bullet = one rule format; Copilot parses declarative lists more reliably than embedded prose rules |

---

## Token and Premium Request Impact

| Action | Cost level | Notes |
|--------|-----------|-------|
| Repository audit (Ask mode) | Low | One Ask session per property in the 6-property checklist; no agent overhead |
| README reconstruction | Low | Edit mode on a specific file; bounded context |
| `CONVENTIONS.md` authoring | Low–Medium | Plan mode recommended for multi-language repos; Ask mode sufficient for single-language |
| `.copilotignore` authoring | Low | One Ask session from a file tree; deterministic output |
| Governance protocol setup | None | Documentation task; no Copilot session required beyond reference lookup |
| Pre-merge validation | Low | Ask mode; diff as input; binary output per gate |

---

## Completion Criteria

You have completed this module when you can:

- [ ] Score any repository against the 6-property AI-friendliness checklist and explain the impact of each missing property.
- [ ] Write an AI-useful README with all required labelled sections.
- [ ] Write a `CONVENTIONS.md` in declarative format with at least 5 rules.
- [ ] Describe the 3-tier AI-assisted commit audit trail and select the appropriate tier for a given risk level.
- [ ] Apply the 5-gate pre-merge validation protocol to any diff.
- [ ] Explain the difference between `.copilotignore` and `.gitignore` and when each is needed.
- [ ] Select the appropriate convention set for small, medium, and large repositories.

See [checklist.md](./checklist.md) for the full self-assessment.

---

## Files in This Module

| File | Purpose |
|------|---------|
| `README.md` | Module overview (this file) |
| `theory.md` | Extended theory — AI signal degradation mechanics, README anatomy deep-dive, commit message standards |
| `exercises.md` | All 5 exercises with full instructions and expected answers |
| `checklist.md` | Completion checklist and self-assessment |

---

## Paired Lab

[Lab 09 — Repository Health Audit](../../labs/lab-09-repository-health-audit/) — audit a deliberately degraded Python repository, rewrite its README, establish a governance protocol, and write a `CONVENTIONS.md`.

---

## Next Module

[Module 10 — Adoption Roadmap](../10-adoption-roadmap/) · Complete Module 09 before advancing.

Module 09 produces an audited, governed repository — with a score, a remediation plan, and a `CONVENTIONS.md` in place. Module 10 synthesizes everything learned across all nine modules into a personal and team adoption roadmap: 7, 30, 60, and 90-day milestones that make Copilot adoption measurable and transferable. The repository quality work done in Module 09 is the foundation for that roadmap.
