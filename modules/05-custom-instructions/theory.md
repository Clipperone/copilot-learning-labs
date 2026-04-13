# Module 05 — Theory Reference

> **Word limit discipline:** Prose sections are capped at 500 words total. Tables and code blocks are excluded from this count.

This page extends the README with three topics not covered there: instruction inheritance and override mechanics, designing instructions for monorepos with multiple `applyTo` scopes, and a step-by-step conflict resolution procedure.

---

## Instruction Inheritance and Override Mechanics

Copilot evaluates instruction files in a defined order. Understanding this order prevents accidental overrides and explains unexpected output.

**Evaluation order (narrowest scope last — last wins):**

```
1. Global instructions (VS Code user setting)
2. Repository-wide instructions (.github/copilot-instructions.md)
3. Path-specific instructions (.github/instructions/*.instructions.md)
   — multiple files may match; they are merged in filename alphabetical order
4. Inline prompt constraint (current turn only)
```

When the same concern is addressed in multiple scopes, the **narrowest scope wins**. A path-specific instruction for `src/api/**` overrides the repository-wide rule for the same concern — but only for files under `src/api/`.

**Important:** Path-specific files do not stack additively with unlimited depth. If three files all match the same path, their instructions are concatenated in alphabetical filename order. Contradictions within that merged set are not auto-resolved — earlier alphabetical entries lose when a later entry contradicts them.

---

## Designing Instructions for Monorepos

A monorepo typically contains multiple distinct areas: a frontend, a backend API, a CLI, a data pipeline, shared libraries. Each area may have legitimately different conventions.

**Pattern: one `applyTo` file per distinct contract.**

```
.github/instructions/
  backend-api.instructions.md     applyTo: "src/api/**"
  data-pipeline.instructions.md   applyTo: "src/pipeline/**"
  frontend.instructions.md        applyTo: "frontend/**"
  tests.instructions.md           applyTo: "tests/**"
```

Each file covers only the concerns that differ from the repository-wide baseline. Rules that apply everywhere go in `.github/copilot-instructions.md`. Rules that apply to one area go in that area's `instructions.md`.

**What not to do:** Do not replicate the repository-wide rules into each path-specific file. This creates a maintenance problem — when the base rule changes, you update it in every file instead of one.

**Scope ownership table (recommended practice):**

| Concern | Scope | File |
|---------|-------|------|
| Naming conventions | Repository | `.github/copilot-instructions.md` |
| Docstring format | Repository | `.github/copilot-instructions.md` |
| API input validation | Path | `backend-api.instructions.md` |
| Test assertion style | Path | `tests.instructions.md` |
| Frontend component naming | Path | `frontend.instructions.md` |

---

## Conflict Resolution Procedure

Use this procedure when instruction files produce contradictory output or when a new instruction needs to coexist with existing ones.

**Step 1 — Identify the conflict.**
Run the diagnostic prompt from the README against a file in the affected scope. Observe which rule is applied and which is ignored.

**Step 2 — Determine scope ownership.**
Ask: which scope is the authoritative source for this rule? If both scopes claim ownership, the narrower scope governs — but it is better practice to remove the rule from the wider scope rather than rely on override silently.

**Step 3 — Remove the redundant rule.**
Delete the rule from the wider-scope file. Add a comment if the removal might confuse a future reader:

```markdown
<!-- Naming rule for this layer is in .github/instructions/backend-api.instructions.md -->
```

**Step 4 — Verify.**
Re-run the diagnostic prompt. Confirm the correct rule is applied and the removed rule is no longer active.

**Step 5 — Update `Verified` dates** in both files.

---

## When Instruction Files Cannot Help

Instruction files are not a substitute for every type of guidance.

| Use case | Better tool |
|----------|------------|
| One-off task constraint | Prompt constraint (Constraints line) |
| Exploratory or experimental session | Prompt only — do not pollute instructions with temporary rules |
| Framework migration in progress | Prompt-per-turn with explicit version context, not an instruction — rules change during migration |
| Guidance that differs per task type | Prompt library template (parameterized) |

---

## Official Resources

- [Copilot customization in VS Code](https://code.visualstudio.com/docs/copilot/copilot-customization)
- [Custom instructions for GitHub Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot)
- [Prompt files and reusable prompts (VS Code)](https://code.visualstudio.com/docs/copilot/customization/prompt-files)
- [GitHub Copilot documentation](https://docs.github.com/en/copilot)
