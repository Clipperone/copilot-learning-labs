# Module 05: Persistent Custom Instructions

> **Level:** Intermediate
> **Estimated time:** ~2 hours (module theory ~1 hr · lab ~50 min)
> **Prerequisite:** [Level 1 complete](../../SYLLABUS.md#level-1--beginner) (Modules 01–03) · Module 04 complete. Writing effective instructions requires the same structural thinking as prompt engineering.
> **Verified:** 2026-04

> ⚠️ **Premium request note:** No task in this module requires a premium model. Instruction authoring is the lowest-cost Copilot workflow. Well-written instruction files reduce total premium consumption across all future sessions by encoding constraints that would otherwise be typed into every prompt.

---

## Learning Objectives

By the end of this module you will be able to:

1. Explain the 3 instruction scopes — global, repository-wide, path-specific — and select the correct scope for a given constraint.
2. Write instruction statements that satisfy the 4 design principles: specific, imperative, bounded, non-contradictory.
3. Build an instruction file for each of 5 domains: coding style, architecture, testing, security, and documentation.
4. Configure path-specific instruction files with `applyTo` frontmatter for distinct codebase areas.
5. Verify that Copilot reads and applies instructions using a diagnostic test prompt, and diagnose why instructions are ignored.
6. Audit, update, and version instruction files as a codebase and team conventions evolve.

---

## Why This Module Exists

Module 04 built the constraint layer one prompt at a time. Every structured prompt you wrote included a Constraints line — because Copilot has no memory of the previous session and no knowledge of your project's conventions.

This module makes that constraint layer automatic. An instruction file is a constraint you write once. It applies to every Copilot session in its scope without typing it again.

The gain is not just convenience. Consistent instructions mean consistent output — across team members, across days, and across modes (Ask, Plan, Agent). A team that has invested 30 minutes writing a good instruction file gets systematically better output than a team that wings it each time.

---

## Instruction Scopes

**Three scopes.** Pick the narrowest scope that fits the constraint.

| Scope | Where the file lives | What it covers |
|-------|---------------------|----------------|
| **Global** | VS Code setting: `github.copilot.chat.codeGeneration.instructions` | Every project on this machine — personal habits |
| **Repository-wide** | `.github/copilot-instructions.md` | All Copilot sessions in this repo — project conventions |
| **Path-specific** | `.github/instructions/[name].instructions.md` with `applyTo` frontmatter | Files matching the glob — area-specific contracts |

**Decision rule:**
- Use **global** for preferences that are purely personal and apply everywhere: verbosity, preferred docstring format, naming conventions you always use.
- Use **repository-wide** for conventions that every contributor must follow: architecture patterns, import rules, testing framework, security baselines.
- Use **path-specific** for contracts that apply in one area only: API security rules, data layer constraints, a different testing style for integration tests.

**Conflict resolution:** Narrower scope wins. Path-specific overrides repository-wide. Repository-wide overrides global. If two files at the same scope contradict each other, the contradiction is silently evaluated — document scope ownership to avoid it.

---

## The 4 Design Principles

Every instruction statement must pass all four tests before it is useful.

| Principle | Violation example | Corrected instruction |
|-----------|------------------|----------------------|
| **Specific** — names exactly what to produce | "Write clean code." | "Use type annotations on all function parameters and return values." |
| **Imperative** — tells Copilot what to do | "It is preferred that functions be short." | "Keep functions under 30 lines. Extract helpers when a function exceeds that limit." |
| **Bounded** — states limits, not just intent | "Include tests for edge cases." | "Include test cases for: null input, empty collection, minimum value, maximum value." |
| **Non-contradictory** — does not conflict with another in-scope instruction | Global: "Use camelCase." / Repo: "Use snake_case." | Remove the global rule. Repo conventions always govern in a project context. |

### Completeness test

Read the instruction aloud. Ask: "Does this tell Copilot exactly what to produce?" If the answer depends on implied context, the instruction is incomplete.

### Before and after — bad to good

**Before:**
```
Be consistent with existing code style and follow best practices for Python.
```

**After:**
```
Use snake_case for all identifiers. Use type annotations on all function parameters and return values. Maximum line length: 100 characters. Use Google-style docstrings with Args, Returns, and Raises sections.
```

The "after" version produces deterministic output. The "before" version tells Copilot to guess.

---

## The 5 Instruction Domains

Each domain addresses a different category of Copilot output. Write separate instruction files or clearly separated sections for each one.

| Domain | What instructions encode that prompts cannot | Example instruction statement |
|--------|----------------------------------------------|-------------------------------|
| **Coding style** | Naming, formatting, import ordering, line length — applied to every generation | `Use snake_case for all identifiers. Maximum line length: 100 characters.` |
| **Architecture** | Patterns to use or avoid; which layers own which responsibilities | `Do not call the database layer directly from route handlers. All data access goes through the repository layer.` |
| **Testing** | Framework, coverage minimums, fixture conventions, assertion style | `Use pytest. Write one test function per case. Use bare assert statements — no unittest.TestCase. Cover null, empty, and boundary value cases explicitly.` |
| **Security** | OWASP categories to check by default; banned functions and patterns | `Do not use MD5 or SHA1 for password hashing. Flag OWASP A02 and A03 risks in any generated authentication or data-processing code.` |
| **Documentation** | Audience, docstring format, depth | `Write Google-style docstrings with Args, Returns, and Raises on every public function. Audience: the caller, not the maintainer.` |

### Domain template

For each domain, structure instructions as:
```
[DOMAIN]: [IMPERATIVE STATEMENT]. [EXPLICIT EXCEPTION IF ANY].
```

Examples:
```
Testing: Use pytest. One test function per case. Use bare assert statements.
Security: Do not use MD5 or SHA1 in any context. Prefer hashlib.pbkdf2_hmac with salt.
Documentation: Google-style docstrings. Include Args, Returns, Raises. No usage examples unless the function has non-obvious behaviour.
```

---

## Path-Specific Instructions

A path-specific instruction file applies only to files matching its `applyTo` glob. Use it when a specific area of the codebase has a tighter contract than the rest.

### Frontmatter format

```markdown
---
applyTo: "src/api/**"
---

# API Layer Instructions

Security: Validate all input at the route handler boundary before passing to service layer. Flag OWASP A03:2021 (Injection) risks explicitly.
Return types: Annotate every route handler return type. Use TypedDict or Pydantic models — never return a raw dict.
Error handling: All route handlers must catch and log exceptions. Return structured error responses — never expose stack traces.
```

### Common `applyTo` patterns

| Pattern | Applies to |
|---------|-----------|
| `"src/api/**"` | All files under the API layer |
| `"tests/**"` | All test files |
| `"src/models/**"` | Data model layer only |
| `"**/*.py"` | All Python files in the repo |
| `"docs/**/*.md"` | All documentation files |

**Glob rule:** Use `**` for recursive matching. `*` matches within one directory level only.

---

## How Instructions Interact with Prompts

| Layer | When it applies | Override? |
|-------|----------------|-----------|
| Instruction file (any scope) | Every session, automatically | Yes — a prompt can override for one turn |
| Prompt constraint | Current turn only | Overrides the instruction file for this turn |

Instructions set the **default**. Prompts set the **exception**.

If you find yourself adding the same constraint to every prompt, that constraint belongs in an instruction file.

If you find yourself removing the same instruction from every prompt ("ignore the docstring rule for this one"), move that instruction to a narrower scope — or remove it entirely.

---

## Testing and Maintenance

### Verify instructions are active

After creating or updating any instruction file, run this diagnostic prompt in Ask mode:

```
Task: Write a single Python function `greet(name)` that returns a greeting string.
Output: The function only.
```

Check the output against each active instruction. If a rule applies (type annotation, docstring format), it should appear without you requesting it. If it does not appear, the instruction is not being read — see the failure diagnosis below.

### 3 signs instructions are being ignored

1. **Wrong file path.** Repository-wide instructions must be at `.github/copilot-instructions.md` exactly. Path-specific files must follow the `.github/instructions/` path pattern.
2. **File too long.** Copilot context is finite. Files with more than ~400 words of prose exceed what reliably fits. Split by domain.
3. **Passive or vague language.** "It is preferred that..." and "Try to use..." are not instructions. Copilot interprets them as optional.

### Versioning

Add a comment at the top of every instruction file:

```markdown
<!--
  Verified: 2026-04
  Update this date whenever you make a material change.
-->
```

### Audit triggers

Review instruction files when:
- A major dependency is updated (testing framework, linter, framework version).
- A team naming or architecture convention changes.
- A security vulnerability is fixed that was related to a previously uninstanced pattern.
- The codebase is restructured and `applyTo` paths no longer match.

---

## Common Mistakes

| Mistake | Root cause | Fix |
|---------|------------|-----|
| Using an instruction file for a one-off task | Confusing persistent guidance with per-task prompts | Move to prompt library; instruction files are for constraints that apply every time |
| Vague instruction: "write good tests" | Habitual informal language | Rewrite with an explicit metric: "Include cases for null, empty, and boundary values in every test suite" |
| Contradictory global + repo instructions | Written at different times, not cross-checked | Document which scope owns each rule. Audit both files before committing either. |
| Instruction file too long (>~400 words prose) | "More is more thorough" reasoning | Split by domain; Copilot silently ignores what cannot fit in context |
| Not verifying after writing | Assuming Copilot reads what is committed | Always run the diagnostic prompt immediately after creating or updating any instruction file |
| Credentials or internal URLs committed in instruction files | "It's just config" — committed with no concern | Use abstract placeholders only; instruction files are version-controlled and may be public |

---

## Exercises

Hands-on exercises are in [exercises.md](./exercises.md).

> See also: [instructions/](../../instructions/) — Working example files: global, project-wide, path-specific · `.github/copilot-instructions.md` — This repository's own instruction file (a live teaching artifact).

---

## Completion Criteria

You have completed this module when you can:

- [ ] Explain the 3 instruction scopes and select the correct scope for a given constraint.
- [ ] Write instruction statements that satisfy all 4 design principles.
- [ ] Build an instruction file for each of the 5 domains.
- [ ] Configure a path-specific instruction file with correct `applyTo` frontmatter.
- [ ] Verify instructions are active using the diagnostic test prompt.
- [ ] Audit and update instruction files when conventions change.

See [checklist.md](./checklist.md) for the full self-assessment.

---

## Files in This Module

| File | Purpose |
|------|---------|
| `README.md` | Module overview (this file) |
| `theory.md` | Extended theory and reference material |
| `exercises.md` | All exercises with full instructions |
| `checklist.md` | Completion checklist and self-assessment |

> See also: [theory.md](./theory.md) — Instruction inheritance mechanics, monorepo `applyTo` design, conflict resolution procedure.

> **Agent mode connection:** The 4 design principles practised here — specific, imperative, bounded, non-contradictory — are the same ones used to write an agent persona in Module 06, applied to a role rather than a file. Active instruction files also reduce agent drift: in-scope instructions are inherited automatically on every agent turn.

---

## Paired Lab

| Lab | Focus | Time |
|-----|-------|------|
| [Lab 05 — Write Your Project's Custom Instructions](../../labs/lab-05-custom-instructions/) | Global, project-wide, and path-specific instruction authoring and verification | 50 min |

---

## Next Module

→ [Module 06: Agents and Role Specialization](../06-agents/)
