# Module 09: AI-Friendly Repository Engineering — Theory

This document extends the README with technical reference material. Read the README first — this file assumes that content.

---

## AI Signal Degradation Mechanics

Context quality degrades in specific, predictable ways as a repository grows. Understanding the mechanics helps prioritize which properties to fix first.

**Signal-to-noise ratio:** The AI context window has a finite capacity. Every irrelevant token that enters the context displaces a relevant token. In a well-scoped session, the context window contains only the files relevant to the task. In an unscoped session against an unstructured repository, the context window fills with generated artifacts, vendored dependencies, and stale code — and the relevant files are diluted or absent.

**Ambiguity amplification:** A single ambiguous name (for example, `helpers.py`) creates a chain of inferences. The AI infers the file's purpose from its content, then uses that inference to generate code in other files. If the content is mixed-concern, the inferences are inconsistent. Five files with ambiguous names create compounding inference errors across sessions rather than localized, correctable gaps.

**Convention invention:** When no `CONVENTIONS.md` exists, the AI infers conventions from the files visible in the current session. Different sessions see different subsets of the codebase. Different conventions emerge. Over 20 AI-assisted sessions without explicit conventions, a medium-sized repository typically accumulates several distinct style variants in AI-generated code — none of which matches the human-authored style exactly.

**Stale context:** Commented-out code, dead functions, and obsolete documentation create false signals. The AI cannot distinguish "this is the old approach — do not use" from "this is an active approach." The result is defensive code that avoids patterns that are actually fine, or code that copies deprecated approaches.

---

## README Anatomy — Deep Dive

The 6-section AI-useful README structure from the module overview applies to any project documentation file, not just top-level READMEs. Apply the same principles to module-level READMEs, API documentation, and architecture decision records.

**Section ordering rationale:**

Place the highest AI-signal sections first. The context window processes the beginning of a file before later sections — if the context window fills before the end of the file, early sections are guaranteed to be included. Recommended order:

1. `## What this does` — scope (always present; defines what all other sections describe)
2. `## Setup` — environment context (affects all code-generation suggestions)
3. `## Project structure` — file roles (prevents misidentification)
4. `## Conventions` — rules (prevents rule invention)
5. `## Known limitations` — constraints (prevents generating solutions to non-problems)
6. `## Architecture notes` — design rationale (explains non-obvious decisions)
7. Human-facing sections (`## Getting started`, `## FAQ`, etc.) — last

**Anti-patterns to recognize and fix:**

| Anti-pattern | Signal | Fix |
|-------------|--------|-----|
| "About" narrative at the top | Long prose before any structure | Replace with `## What this does` — one functional paragraph |
| Undifferentiated setup + description | Mixed concerns in one section | Split into `## What this does` and `## Setup` |
| Inline conventions buried in prose | "We use snake_case for functions" in paragraph 5 | Extract to `## Conventions` section or `CONVENTIONS.md` |
| Version history table at the top | Changelog masquerading as documentation | Move to `CHANGELOG.md` or bottom of README |
| Badge walls at the top | 10+ status badges before any content | Move to bottom; one or two badges at the top are acceptable |

---

## Commit Message Standards for AI-Assisted Work

Commit messages are documentation. A commit message that reads "fix stuff" provides zero traceability for the AI-assisted code it describes. A well-formed commit message with AI metadata is a governance artifact.

**Conventional Commits format (recommended baseline):**

```
<type>(<scope>): <imperative description>

<body — explain why, not what>

<trailers>
```

Types: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `ci`, `perf`

**AI-assisted commit template:**

```
<type>(<scope>): <description>

AI-assisted: <brief note on what was AI-generated and what review was applied>
Reviewed-by: <name or GitHub handle>
```

Example:

```
fix(auth): validate JWT expiry before returning user object

AI-assisted: generated condition logic; reviewed against OWASP A07 (Identification
and Authentication Failures); no hardcoded credentials; expiry validation confirmed
against RFC 7519 §4.1.4.
Reviewed-by: Alex Chen
```

The `AI-assisted` trailer is:

- Not an admission of lower code quality
- A traceability signal for future debugging and auditing
- The equivalent of a `Co-authored-by` trailer — a factual record of who or what contributed

**When to omit the AI-assisted trailer:**

Omit when the AI contribution was purely mechanical and non-semantic: formatting, whitespace normalization, comment spelling corrections. Apply the trailer for anything that changes behavior, structure, or logic.

---

## `.copilotignore` Reference

`.copilotignore` uses `.gitignore` syntax and controls which files are excluded from GitHub Copilot's context. It does not affect version control.

**Common entries for a Python repository:**

```
# Generated output
__pycache__/
*.pyc
.pytest_cache/
dist/
build/
*.egg-info/

# Virtual environments
.venv/
venv/
env/

# Secrets and configuration with real values
.env
*.env.*
secrets.json
config/production.py

# Large static assets
*.pdf
*.zip
static/fonts/

# Test fixtures with verbose data
tests/fixtures/large-*.json
tests/fixtures/snapshots/
```

**`.copilotignore` vs `.gitignore` — the distinction:**

| Question | `.gitignore` | `.copilotignore` |
|----------|-------------|-----------------|
| Does it affect what Copilot sees? | No | Yes |
| Does it affect what is versioned? | Yes | No |
| Should it exclude `.env`? | Yes | Yes — independently |
| Should it exclude `dist/`? | Usually | Yes |
| Should it exclude test files? | No | Rarely — only large fixture files |

An entry removed from `.copilotignore` but not from `.gitignore` (or vice versa) does not restore the other behavior. Both files must be managed independently.

---

## CONVENTIONS.md — Authoring Guide

A `CONVENTIONS.md` file has high AI signal value only when written in declarative, parseable format. The following patterns increase parseability.

**High-signal format:**

```markdown
## Naming
- Files: `snake_case.py` — one concern per file; name describes the concern
- Functions: `verb_noun()` format — `validate_input()`, `format_response()`
- Classes: `PascalCase` — noun or noun phrase
- Constants: `UPPER_SNAKE_CASE`
- No filler words: avoid `helpers`, `utils`, `misc`, `handler`, `manager` as standalone file names

## Imports
- Standard library first
- Third-party second
- Local last
- One blank line between groups

## Tests
- Test files: `test_<module_name>.py` in `tests/` directory
- Test functions: `test_<function_name>_<scenario>()`
- No shared mutable state between tests

## Commits
- Format: Conventional Commits (`feat`, `fix`, `refactor`, `docs`, `test`, `chore`)
- AI-assisted commits: include `AI-assisted:` trailer with review note
- Body: explain why, not what

## AI Context
- `.copilotignore` controls context exclusion; see file for current entries
- Sessions scoped to one directory by default; state scope in first prompt
- Sensitive files: see sensitivity classification in `docs/security.md`
```

**Low-signal format to avoid:**

```markdown
We try to use snake_case for our Python files, and we generally follow PEP 8
conventions for naming because that's what the team decided when the project
started. For tests, we usually put them in a tests directory.
```

The low-signal format contains the same information but requires the AI to parse prose and infer rules — a pattern-matching task that introduces errors and inconsistencies at scale.

---

## Repository Quality Over Time

A repository that satisfies all 6 properties today may degrade over time without active maintenance. Three patterns accelerate degradation:

**Scope creep in existing files:** A file named `payment_validators.py` starts with input validation. Over six months, utility functions are added for convenience. The name no longer matches the content. New AI sessions infer the wrong scope. Fix: enforce the one-file-one-concern rule at code review; do not use existing files as holding areas for unrelated functions.

**CONVENTIONS.md drift:** The conventions file documents the rules in place when it was written. As the codebase evolves — new frameworks, new team members, new languages — the documented conventions become inaccurate. Fix: treat `CONVENTIONS.md` changes the same as configuration changes; require a brief comment explaining what changed and why.

**`.copilotignore` inventory gap:** The `.copilotignore` file excludes files present at the time it was written. New files with sensitive or noisy content added later are not automatically excluded. Fix: include a `.copilotignore` audit step in the repository onboarding checklist; run the audit whenever the file inventory grows significantly.

---

## Official Resources

- [Configuring ignored files for Copilot](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-ignored-files)
- [GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/overview)
- [GitHub Copilot documentation](https://docs.github.com/en/copilot)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
