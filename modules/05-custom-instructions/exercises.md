# Module 05 — Exercises

These exercises build instruction authoring into a reliable skill. Each exercise is self-contained. Complete them before Lab 05 — the lab applies these skills under time pressure to a live project.

---

## Exercise 1 — Apply the 4 Design Principles

**Objective:** Identify which principle each instruction violates and rewrite it.

For each instruction below, state which principle is violated (Specific / Imperative / Bounded / Non-contradictory) and write a corrected version.

**Instruction A:**
```
Write Python code that follows best practices.
```

**Instruction B:**
```
It would be better if functions were kept at a reasonable length.
```

**Instruction C:**
```
Include tests.
```

**Instruction D (two instructions in the same project, different files):**
```
Global: Use camelCase for all identifiers.
Repo:   Use snake_case for all Python identifiers.
```

**Expected answers:**
- A: Not specific — no measurable standard named. Rewrite: "Use type annotations on all function parameters and return values. Maximum line length: 100 characters."
- B: Not imperative — passive preference. Rewrite: "Keep functions under 30 lines. Extract a helper when a function exceeds that limit."
- C: Not bounded — no criteria. Rewrite: "Write pytest tests for null input, empty collection, boundary minimum, and boundary maximum values."
- D: Contradictory — same concern owned by two scopes. Rewrite: Remove the global rule. Repo rule governs in project context.

---

## Exercise 2 — Scope Assignment

**Objective:** Assign each constraint to the correct scope and give a one-sentence reason.

For each constraint, choose: **Global**, **Repository-wide**, or **Path-specific (src/api/**)**.

| Constraint | Your answer | Reason |
|------------|-------------|--------|
| "Use Google-style docstrings on all public functions" | | |
| "All route handlers must validate input against a schema before calling service layer" | | |
| "Never use print() for logging — use the project's logger instance" | | |
| "My preferred verbosity: return the complete function, not a diff" | | |
| "All data access goes through the repository layer — no direct DB calls from routes" | | |

**Reference answers:**

| Constraint | Scope | Reason |
|------------|-------|--------|
| Docstring format | Repository | Applies to all contributors on this project; personal elsewhere |
| Route handler input validation | Path (`src/api/**`) | Specific to the API layer only; irrelevant in models or tests |
| Logging convention | Repository | Project-wide convention — all contributors must follow |
| Verbosity preference | Global | Personal habit that applies across all projects |
| Repository layer rule | Repository | Architecture convention for all contributors |

---

## Exercise 3 — Write a Domain Instruction Block

**Objective:** Produce a production-ready instruction block for one domain from scratch.

Choose one of the five domains (coding style, architecture, testing, security, documentation) for a Python FastAPI project. Write a complete instruction block that:
- Contains between 3 and 6 imperative statements.
- Includes at least one bounded statement (with an explicit metric or list).
- Passes all 4 design principles when read aloud.

**Try this example domain:** Testing

**Your instruction block should cover:** framework, assertion style, edge case requirement, fixture conventions.

**Reference answer (Testing):**
```
Testing: Use pytest. One test function per case — not one function with multiple assertions.
Use bare assert statements. Do not use unittest.TestCase.
Cover these cases in every test suite: null input, empty collection, minimum value, maximum value, invalid type.
Use pytest fixtures for shared setup. Do not use setUp/tearDown methods.
```

---

## Exercise 4 — Write a Path-Specific Instruction File

**Objective:** Create a complete `.instructions.md` file with correct frontmatter for a specific codebase area.

You are working on a project with the following structure:
```
src/
  api/
    users.py     ← Flask user routes
    auth.py      ← JWT authentication handler
  models/
    user.py      ← SQLAlchemy model
  services/
    user_service.py
```

Write a path-specific instruction file for `src/api/**` that:
- Has correct YAML frontmatter with the `applyTo` glob.
- Includes instructions for: input validation scope (OWASP A03), return type annotation requirement, error handling (no stack trace exposure).
- Does not repeat any rule that would already be in the repository-wide file.

**Checklist for your file:**
- [ ] Frontmatter block opens and closes with `---`.
- [ ] `applyTo` key is present with a double-quoted glob.
- [ ] Each instruction uses an imperative verb.
- [ ] No passive voice.
- [ ] File is under 400 words of prose.

---

## Exercise 5 — Verify and Fix

**Objective:** Diagnose why instructions might be ignored and apply the fix.

A developer has written the following repository-wide instruction file. It is 600 words long and Copilot appears to be ignoring most of it after the first few rules.

```
We really value clean code in this project. It is important to us that developers write
code that is easy to read and maintain. Code reviews often catch issues with naming...

[continues for 580 more words of prose explanation and rationale]

Final rule: Use pytest.
```

**Questions:**
1. Identify two reasons this file is likely being ignored.
2. Rewrite the `pytest` rule as a single bounded instruction statement.
3. Describe the structure of a replacement file that would work reliably — without writing the full file.

**Reference answers:**
1. (a) File exceeds ~400 words — Copilot cannot fit the full context. (b) Most statements are passive explanations, not imperative instructions.
2. `Testing: Use pytest. Write one test function per case. Use bare assert statements.`
3. Replace prose with an imperative statement per rule. Group by domain with a one-line domain header. Target total prose under 300 words. Move rationale to comments, not instruction text.

---

## Navigation

← [README.md](./README.md) — Module overview and all design principles

→ [checklist.md](./checklist.md) — Self-assessment before moving to the lab

→ [Lab 05](../../labs/lab-05-custom-instructions/) — Apply all three scopes to a sample project
