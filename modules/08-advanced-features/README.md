# Module 08: Advanced Features in Copilot + VS Code

> **Level:** Expert
> **Estimated time:** ~2.5 hours (module theory ~1.5 hrs · lab ~60 min)
> **Prerequisite:** [Module 07 — Multi-Agent Workflows](../07-multi-agent-workflows/) · One documented, repeatable workflow file must exist in `agents/` before this module.
> **Verified:** 2026-04

> ⚠️ **Premium request note:** Plan mode, terminal integration, and quality gate work run effectively on the default model. Escalate to Claude or o1 only for Security Reviewer sessions that require OWASP exploit-path reasoning. A common waste pattern at Expert level is opening a premium Agent session for a task that Plan mode or inline chat handles equally well.

---

## Learning Objectives

By the end of this module you will be able to:

1. Apply Plan mode to design a feature change with explicit scope and constraints before writing any code.
2. Run a structured AI-assisted code review session, producing numbered findings with severity and location.
3. Use Copilot in the VS Code terminal to explain errors, generate CLI commands, and validate them before execution.
4. Integrate Copilot with test runners, linters, and formatters as an active quality gate before every commit.
5. Scope Copilot context effectively in repositories with 500+ files to avoid premium waste and signal degradation.
6. Apply secure usage patterns: classify sensitive files by risk level, keep credentials out of context, and validate AI output against OWASP Top 10 before committing.

---

## Why This Module Exists

Module 07 taught manual multi-agent orchestration: write the workflow file first, initialize each session explicitly, hand off using the 3-part prompt, close each role session before opening the next. Every mechanism was manual and deliberate.

This module introduces the built-in VS Code features that reduce the manual overhead of what you did explicitly. Plan mode replaces a separate Planner session for many design tasks. Terminal integration brings Copilot assistance to CLI work without switching context. Quality tool integration closes the loop between generation and validation.

The module extends beyond VS Code features. Large repositories degrade AI context quality without deliberate management. Sensitive codebases require explicit security hygiene that no default configuration provides. Both are professional requirements at Expert level.

---

## Plan Mode

**Plan mode** is Copilot's built-in design step. Before changing any file, Plan mode reads the relevant context, reasons about the task, and produces a structured proposal for review.

**When to use Plan mode:**

| Scenario | Plan mode | Skip Plan mode |
|----------|:---------:|:--------------:|
| New feature with cross-file scope | ✅ | |
| Refactoring a module with unknown dependencies | ✅ | |
| Single-function fix with no cross-file impact | | ✅ |
| Implementation already scoped by a workflow breakdown | | ✅ |
| Design before implementation — any scope | ✅ | |

**Plan mode vs. Agent mode:**

| Dimension | Plan mode | Agent mode |
|-----------|-----------|-----------|
| Context cost | Lower — no tool-call overhead | Higher — tool calls accumulate |
| Output | Structured design proposal | Executed changes |
| Reversibility | High — nothing is written | Requires undo after execution |
| When to use | "Design before I commit" | "Execute a bounded task now" |

**What a complete Plan output contains:**

1. A one-paragraph restatement of the problem in the AI's own words — confirms correct understanding.
2. A list of files to be modified, with one sentence of reasoning per file.
3. A proposed change per file — function scope, not line-by-line code.
4. Explicit statement of what will NOT change.
5. One open question, if any scope ambiguity exists.

If the Plan output does not contain all five elements, it is incomplete. Add constraints and re-run Plan mode before moving to implementation.

> **Critical rule:** Plan mode output is a proposal, not code. Pass it to an Implementer session or Agent mode. Never copy Plan output directly to production without review and implementation.

---

## AI-Assisted Code Review

An AI-assisted review is a first-pass filter that catches mechanical issues — missing validations, insecure patterns, style violations — so the human reviewer can focus on architectural and logical concerns. It does not replace human review.

**Structured review loop:**

| Step | Action |
|------|--------|
| 1 | Stage or view the diff — identify the exact scope of the change |
| 2 | Open a Code Reviewer session with the diff as the only input |
| 3 | Require numbered findings: number, severity (Critical / High / Medium / Low), file and line, description, suggested fix |
| 4 | Evaluate each finding: accept, reject with reason, or escalate to human review |
| 5 | Commit only after all Critical and High findings are resolved |

**What constitutes a valid finding:**

A finding that does not include severity, a specific file and line reference, and a reproducible description is not actionable. Reject it and ask for a tighter response.

**What AI review catches well:**

- Missing input validation
- Hardcoded credentials or values that should be configurable
- Naming inconsistencies against the instruction file rules
- Missing error handling for known failure paths

**What AI review does not replace:**

- Architectural review by a human who understands the full system
- Security review requiring exploitation of the running application
- Team-level code ownership and design decisions

> ⚠️ **Premium request note:** Default model is sufficient for standards-checking and pattern-matching reviews. Escalate to Claude or o1 only when the review requires OWASP exploit-path reasoning across multiple files.

---

## Terminal and CLI Integration

Copilot is available in the VS Code terminal as the `@terminal` participant. It operates in Ask mode — no agent overhead, no tool calls, no writes.

**Use cases:**

| Scenario | How to invoke |
|----------|--------------|
| Explain a shell error | `@terminal explain this error: [paste]` |
| Generate a command | `@terminal how do I [task] on [OS]?` |
| Fix a failing command | `@terminal why does this fail: [command]` |
| Suggest a pipeline step | `@terminal write a CI step that runs pytest and exits on failure` |

**Validation before execution:**

Every AI-generated terminal command requires one review pass before execution — the same 4-question gate as any other AI output:

1. Does it do what I asked? (Intent match)
2. Does it do anything I did not ask? (Side effects)
3. Is it reversible? (Impact)
4. Am I confident enough to own the outcome? (Accountability)

Apply this gate especially for: `rm`, `git reset`, `git push --force`, database operations, and any command using elevated permissions.

---

## Quality Tool Integration

Connecting Copilot to quality tools closes the generation–validation loop: Copilot generates, the tool verifies, Copilot interprets failures and suggests fixes.

**Supported integration points:**

| Tool type | Integration method | What Copilot assists with |
|-----------|--------------------|-----------------------------|
| Test runner (pytest, Jest) | Run in terminal; paste failure into chat | Explain failure; suggest fix |
| Linter (ruff, ESLint) | Run in terminal or Problems panel | Explain violation; suggest compliant rewrite |
| Formatter (black, prettier) | Run via VS Code task | Confirm output matches intent |
| CI/CD pipeline | PR description; pipeline output | Explain failures; suggest pipeline improvements |

**Minimum quality gate before commit:**

1. All tests pass — zero failures, zero errors.
2. Linter reports zero errors (warnings reviewed, not blindly suppressed).
3. Formatter applied — diff contains no pure-whitespace noise.
4. AI output review gate applied to every AI-generated line in the commit.

CI/CD note: Copilot suggestions in pipelines get the same 4-question review gate as inline completions. An automated pipeline that accepts AI output without a human gate is an unmonitored code path.

---

## Large Repository Context Management

In repositories with hundreds of files, generic Copilot sessions degrade in quality because the context window fills with irrelevant signal. Deliberate scoping prevents this.

**Scoping techniques:**

| Technique | When to use | How |
|-----------|-------------|-----|
| `.copilotignore` | Files that should never appear in context | Add paths or patterns; mirrors `.gitignore` syntax |
| Directory scope in the prompt | Limiting a session to one module | `Scope: src/notifications/ only. Do not reference any other directory.` |
| Explicit file list in initialization | Agent session with known dependencies | List exactly 3–5 files the session is permitted to read |
| Chunked context injection | Files too large for one session | Pass one logical section per session turn |

**What to exclude from context:**

| Category | Why exclude |
|----------|------------|
| Generated files (`dist/`, `build/`, `.next/`) | No signal value; adds irrelevant noise |
| Vendored dependencies (`node_modules/`, `.venv/`) | Copies of external code; mislead generation |
| Secrets and configuration (`.env`, `secrets.json`) | Security boundary — never in AI context |
| Large binary assets | Not processable; wastes context budget |
| Test fixtures with long JSON/XML | Verbose data that drowns code signal |

**Sizing rule:** If a session reads more than 5 files not specified in the initialization prompt, the scope is undefined. Close the session and restate scope before continuing.

---

## Secure Usage Patterns

Copilot sends context to a cloud model. Every file open in a session, every prompt with pasted code, and every inline completion request includes the surrounding context.

> Treat AI context like a log: never put in it what you would not log.

**Sensitive file classification:**

| Level | Examples | AI context rule |
|-------|---------|-----------------|
| Public | README, public API docs, tests with no real data | No restriction |
| Internal | Business logic, internal architecture docs | Permitted in session; exclude from prompt examples |
| Confidential | Auth logic, encryption functions, PII-adjacent code | Session allowed; never paste verbatim into chat; review findings before sharing |
| Restricted | Private keys, `.env` files, secrets, credentials | Never in any AI context |

**Credential hygiene rules:**

1. `.env` files and `secrets.*` files must appear in `.copilotignore`.
2. Example code in prompts uses `<YOUR_KEY>`, `<password>`, or `example.com` — never real values.
3. When Copilot suggests code with a hardcoded string, treat it as a Critical finding in the review gate.
4. After each session, review the diff: if any committed file contains a string matching a credential pattern, do not push.

**OWASP Top 10 minimum checks for AI-generated code:**

| Category | Check |
|----------|-------|
| A01 — Broken Access Control | Does new code enforce authorization before returning data? |
| A02 — Cryptographic Failures | Does new code use a current, recommended algorithm? No MD5, SHA-1, or DES. |
| A03 — Injection | Are all inputs validated or parameterized before use in a query or command? |
| A07 — Identification and Authentication | Are there hardcoded credentials or authentication bypass conditions? |
| A09 — Security Logging | Does the code log security events without logging sensitive values? |

**Copilot for compliance codebases:** If your organization operates under SOC 2, PCI-DSS, HIPAA, or equivalent, confirm your Copilot plan terms and data residency settings before using Copilot on in-scope code. This is an organizational decision, not a VS Code setting.

---

## Exercises

See [exercises.md](./exercises.md) for full instructions.

**Quick list:**

1. **Plan mode design check** — Evaluate a Plan mode output against the 5-element completeness checklist. Identify missing elements and write the missing content.
2. **Review finding triage** — Classify 6 AI review findings as actionable or non-actionable. Rewrite each non-actionable one.
3. **Terminal command validation** — Apply the 4-question gate to 4 AI-generated terminal commands. State whether you would run each and why.
4. **Sensitivity classification** — Classify a 9-item file tree by sensitivity level. State which items to add to `.copilotignore`.
5. **OWASP gate** — Identify 3 OWASP issues in a code snippet, name the category, describe the exploit path, and state the minimum fix.

---

## Common Mistakes

| Mistake | Why it happens | How to fix it |
|---------|---------------|---------------|
| Treating Plan mode output as final code | Conflating design with implementation | Plan output is a proposal; pass it to an Implementer session or Agent mode |
| Accepting AI findings without severity and location | Treating AI review as infallible | Reject findings with no severity, file, or exploit path; require re-generation |
| Pasting credentials into terminal context | "Just a test key" reasoning | Any credential in context can leak; use `<placeholder>` values in all examples |
| Running AI suggestions in CI without a human gate | Assuming automation validates quality | Pipeline AI output gets the same 4-question review gate as inline completions |
| Opening large-repo sessions without explicit scope | "More context is better" | Broad context inflates cost without improving quality; scope to one directory |
| Skipping sensitive file classification | Security hygiene seen as optional | Classify before every session; Restricted files must appear in `.copilotignore` |

---

## Token and Premium Request Impact

| Action | Cost level | Notes |
|--------|-----------|-------|
| Plan mode session | Low–Medium | No agent tool-call overhead; default model handles design work |
| AI code review session | Medium | Default model sufficient for standards review; escalate only for OWASP exploit-path reasoning |
| Terminal integration (`@terminal`) | Low | Ask mode; no agent overhead; pattern matching |
| Quality tool interpretation | Low | Running tools is free; Copilot interprets output only |
| Large-repo scoping with `.copilotignore` | None | Configuration file; one-time setup cost |
| Secure-usage classification | Low (one-time) | One session prevents unlimited downstream risk exposure |

---

## Completion Criteria

You have completed this module when you can:

- [ ] State the 5 elements a complete Plan mode output must contain.
- [ ] Explain the difference between Plan mode and an Agent Planner session — and when each is preferable.
- [ ] Run a structured AI review loop and produce a numbered findings document with severity and location.
- [ ] Validate any AI-generated terminal command with the 4-question gate before executing it.
- [ ] List at least 5 categories of files that should never appear in AI context.
- [ ] Classify a file tree by sensitivity level and produce a `.copilotignore` entries list.
- [ ] Apply the OWASP minimum checks to AI-generated code before committing.

See [checklist.md](./checklist.md) for the full self-assessment.

---

## Files in This Module

| File | Purpose |
|------|---------|
| `README.md` | Module overview (this file) |
| `theory.md` | Extended reference — Plan mode internals, CI/CD integration patterns, enterprise context controls |
| `exercises.md` | All 5 exercises with full instructions and expected answers |
| `checklist.md` | Completion checklist and self-assessment |

---

## Paired Lab

[Lab 08 — Advanced Feature Tour](../../labs/lab-08-advanced-feature-tour/) — apply Plan mode, AI-assisted review, terminal integration, quality gate, and secure usage in five consecutive tasks on the same codebase.

---

## Next Module

[Module 09 — AI-Friendly Repository Engineering](../09-repository-quality/) · Complete Module 08 before advancing.

Module 08 applied the full Copilot feature set to a working codebase. Module 09 turns the lens inward: how to structure, name, and govern a repository so that AI context signals are strong, documentation serves both humans and AI, and every AI-assisted commit has a documented human review trail. Module 08's effectiveness degrades in a poorly structured repository; Module 09 is what sustains it.
