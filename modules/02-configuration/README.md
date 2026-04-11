# Module 02: Configuration

> **Level:** Beginner
> **Estimated time:** 2 hours
> **Prerequisites:** [Module 01 — Foundations](../01-foundations/)
> **Verified:** 2026-04

> ⚠️ **Premium request note:** Configuration is a one-time setup effort. Writing `.github/copilot-instructions.md` uses one chat turn. The resulting instructions reduce ambiguity in every subsequent session, saving premium requests over time.

---

## Learning Objectives

By the end of this module, you will be able to:

- [ ] Configure a VS Code project with the settings that maximize Copilot effectiveness
- [ ] Write a project-level `.github/copilot-instructions.md` that guides Copilot consistently
- [ ] Organize files and folders in a way that gives Copilot clean, unambiguous context
- [ ] Set up linting and formatting so Copilot inherits correct code style automatically
- [ ] Define VS Code tasks for repeatable build, test, and run workflows
- [ ] Create a `.vscode/extensions.json` that recommends required tools to contributors
- [ ] Add type annotations and docstrings to functions and verify the effect on Copilot suggestion quality

---

## Essential Theory

See [theory.md](./theory.md) for the full reference.

### How Configuration Shapes Copilot's Context

Copilot generates completions and responses based on the context it receives. VS Code controls what ends up in that context. Configuration determines:

- Which files are included or excluded (via `.gitignore`, open tabs, `#file:` references)
- What code style is expected (linting/formatting tools signal conventions)
- What project-specific instructions are applied (copilot-instructions.md)
- How the editor surfaces completions (settings.json)

Clean, well-configured projects give Copilot stronger signals. Poorly organized projects with inconsistent style produce noisier, less reliable suggestions.

### The Three Configuration Layers

| Layer | File | Scope | Priority |
|-------|------|-------|----------|
| User settings | `~/.vscode/settings.json` | All projects on this machine | Lowest |
| Workspace settings | `.vscode/settings.json` | This project only | Medium |
| Copilot instructions | `.github/copilot-instructions.md` | Copilot behavior in this repo | Applied on top |

Always prefer workspace settings over user settings for project-specific configuration. Instructions in `.github/copilot-instructions.md` are applied automatically to every Copilot session in the repository.

### Project-Level Copilot Instructions

`.github/copilot-instructions.md` is a Markdown file Copilot reads at the start of every session. Use it to establish:

- The project's language, framework, and version
- Coding conventions (naming, file structure, error handling patterns)
- What Copilot should and should not do in this codebase
- Security constraints and review requirements

Keep instructions specific, bounded, and non-contradictory. Vague instructions ("write good code") have no effect. Precise instructions ("use `snake_case` for all Python functions, `PascalCase` for classes") are followed reliably.

Write rules in imperative form: "Use `snake_case` for all function names." Add a `Verified: YYYY-MM` header comment so you know when the file was last reviewed against actual Copilot behaviour.

### Useful Extensions

The `.vscode/extensions.json` file lists extensions the team recommends. VS Code prompts any new contributor to install them on first open.

```json
{
  "recommendations": [
    "github.copilot",
    "github.copilot-chat",
    "charliermarsh.ruff",
    "editorconfig.editorconfig"
  ]
}
```

| Extension | Publisher ID | Purpose |
|-----------|-------------|---------|
| Ruff | `charliermarsh.ruff` | Python lint + format (replaces Flake8 + Black) |
| ESLint | `dbaeumer.vscode-eslint` | JavaScript/TypeScript lint |
| Prettier | `esbenp.prettier-vscode` | Multi-language formatter |
| EditorConfig | `editorconfig.editorconfig` | Baseline whitespace consistency |
| GitLens | `eamodio.gitlens` | Inline Git history and authorship signals |
| Code Spell Checker | `streetsidesoftware.code-spell-checker` | Catches typos in identifiers and comments |

A curated extensions list ensures every contributor's VS Code setup produces consistent lint, format, and context signals — the same signals Copilot reads.

### File Organization for AI Context

Copilot's context is stronger when:

- **Files are small and focused.** One concern per file keeps context unambiguous.
- **Names are descriptive.** `order_validator.py` gives more signal than `utils.py`.
- **Related files are co-located.** Group by feature, not by file type.
- **Documentation is inline.** Docstrings and type annotations are read as context.

Avoid large monolithic files. A 1000-line `utils.py` dilutes context and makes Copilot suggestions less relevant. Keep each file under 400 lines and split at natural responsibility boundaries. Avoid leaving commented-out code blocks in files — they add noise to Copilot's context and can cause it to reference dead code.

### Documentation and Testing Baseline

Type annotations and docstrings are Copilot's primary signals for understanding function contracts. Compare:

```python
# Minimal signal — Copilot must guess intent
def process(x, items):
    ...

# Strong signal — Copilot inherits precise expectations
def process(multiplier: float, items: list[str]) -> list[str]:
    """Return items with each string prefixed by its index times multiplier."""
    ...
```

For testing, a passing test suite is a prerequisite for agent mode to self-validate changes:

- Use **pytest** (Python) or **Jest** (JavaScript/TypeScript) as the test runner.
- Keep tests in a top-level `tests/` folder, mirroring the `src/` structure.
- Define a `test` VS Code task so agent mode can run the suite without guessing the command.

Agent mode reads test output and self-corrects. Without tests, it cannot validate its own changes.

Apply these configuration steps in [Lab 02: Project Configuration Baseline](../../labs/lab-02-configuration/).

---

## Exercises

See [exercises.md](./exercises.md) for full instructions. Complete [Lab 02](../../labs/lab-02-configuration/) first — all exercises use the lab's `starter/` project.

1. Write your first project-level Copilot instructions — configure a minimal starter project
2. Test instruction effectiveness — verify Copilot applies your conventions
3. File organization audit — identify context dilution in a sample project
4. Configure a linter — install Ruff or ESLint and integrate with VS Code
5. Tasks and agent mode — define a task and invoke it through agent mode
6. Shared extensions file — create `.vscode/extensions.json` for the starter project
7. Documentation baseline signal test — add type annotations and docstrings to `calculator.py`, compare Copilot suggestion quality before and after

---

## Common Mistakes

| Mistake | Root cause | Fix |
|---------|------------|-----|
| Vague instructions ("use best practices") | Developer thinks any instruction is better than none | Replace with specific, verifiable rules: "use `snake_case` for all function names" |
| Forgetting `useInstructionFiles: true` | Default setting may be `false` | Add `github.copilot.chat.codeGeneration.useInstructionFiles: true` to `.vscode/settings.json` |
| Monolithic utility files | Legacy habit from non-AI codebases | Split into focused modules; each file should have one clear purpose |
| No type annotations or docstrings | "Copilot will add them later" | Add them upfront — they are primary context signals |
| Contradictory instructions | Instructions added incrementally without review | Review the full instructions file before adding. Remove obsolete rules. |

---

## Token and Premium Request Impact

| Action | Cost level | Notes |
|--------|-----------|-------|
| Writing copilot-instructions.md | Low | One chat turn; one-time effort |
| Applying instructions to every session | Zero additional | Instructions are injected automatically |
| Asking Copilot to audit instructions for contradictions | Low | Short context, single ask |
| Asking Copilot to reorganize a file structure | Medium | Multi-file read; use Agent mode |
| Agent mode: scaffold `.vscode/` config files | Low–Medium | Few small files; limited tool calls |

---

## Completion Criteria

You have completed this module when you can:

- [ ] Explain how VS Code settings, `copilot-instructions.md`, and a linter each affect Copilot suggestion quality
- [ ] Configure `.vscode/settings.json` with `useInstructionFiles: true` and formatting on save
- [ ] Write a `.github/copilot-instructions.md` with at least 3 specific, verifiable rules and verify Copilot reads them
- [ ] Set up a linter to surface violations on save
- [ ] Define a `test` task in `.vscode/tasks.json` and run it from VS Code
- [ ] Create a `.vscode/extensions.json` with team-required extension recommendations
- [ ] Add type annotations and docstrings to functions and observe the improvement in Copilot suggestions

See [checklist.md](./checklist.md) for the full self-assessment.

---

## Files in This Module

| File | Purpose |
|------|---------|
| `README.md` | Module overview (this file) |
| `theory.md` | Extended theory and reference material |
| `exercises.md` | All exercises with full instructions |
| `checklist.md` | Completion checklist and self-assessment |

---

## Related Labs

| Lab | Focus | Time |
|-----|-------|------|
| [Lab 02 — Project Configuration Baseline](../../labs/lab-02-configuration/) | VS Code workspace setup, Copilot instructions, Ruff linting, task runner, extensions recommendations | 45–60 min |

See [labs/README.md](../../labs/README.md) for the full lab index.

---

## Next Module

→ [Module 03: Token and Premium Request Optimization](../03-token-optimization/)
