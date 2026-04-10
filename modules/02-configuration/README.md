# Module 02: Configuration

> **Level:** Beginner
> **Estimated time:** 2 hours
> **Prerequisites:** [Module 01 — Foundations](../01-foundations/)
> **Verified against:** GitHub Copilot feature set as of 2026-04

---

## Learning Objectives

By the end of this module, you will be able to:

- [ ] Configure a VS Code project with the settings that maximize Copilot effectiveness
- [ ] Write a project-level `.github/copilot-instructions.md` that guides Copilot consistently
- [ ] Organize files and folders in a way that gives Copilot clean, unambiguous context
- [ ] Set up linting and formatting so Copilot inherits correct code style automatically
- [ ] Define VS Code tasks for repeatable build, test, and run workflows

---

## Essential Theory

See [theory.md](./theory.md) for the full reference. The summary below covers what you need to proceed.

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

### File Organization for AI Context

Copilot's context is stronger when:

- **Files are small and focused.** One concern per file keeps context unambiguous.
- **Names are descriptive.** `order_validator.py` gives more signal than `utils.py`.
- **Related files are co-located.** Group by feature, not by file type.
- **Documentation is inline.** Docstrings and type annotations are read as context.

Avoid large monolithic files. A 1000-line `utils.py` dilutes context and makes Copilot suggestions less relevant.

> **⚠️ Premium request note:** Configuration is a one-time effort with no runtime cost. Writing `.github/copilot-instructions.md` uses a chat turn (low cost). The resulting instructions reduce ambiguity in every subsequent session, making subsequent responses shorter and more accurate — a net premium request saving over time.

---

## Practical Procedure

### Step 1: Create or update `.vscode/settings.json`

Add these settings to your workspace settings file. They enable and tune Copilot for professional use:

```json
{
  "editor.formatOnSave": true,
  "editor.rulers": [120],
  "editor.wordWrap": "off",
  "github.copilot.enable": {
    "*": true
  },
  "github.copilot.editor.enableAutoCompletions": true,
  "github.copilot.chat.codeGeneration.useInstructionFiles": true,
  "github.copilot.chat.codeGeneration.instructions": [],
  "files.exclude": {
    "**/__pycache__": true,
    "**/.pytest_cache": true,
    "**/node_modules": true
  }
}
```

`useInstructionFiles: true` activates `.github/copilot-instructions.md` automatically.

### Step 2: Create `.github/copilot-instructions.md`

Create the folder if it does not exist, then create the file. Start with this minimal structure and expand it for your project:

```markdown
# Copilot Instructions — [project name]

## Project Context
- Language: [Python 3.12 / TypeScript 5.x / etc.]
- Framework: [FastAPI / React 18 / etc.]
- Style guide: [PEP 8 / Airbnb / etc.]

## Coding Conventions
- [Convention 1 — be specific]
- [Convention 2]

## Do Not
- [Prohibition 1 — explain why]
- [Prohibition 2]
```

### Step 3: Configure a linter and formatter

Formatting tools signal code style to Copilot. Install and configure at minimum:

- **Python projects:** [Ruff](https://docs.astral.sh/ruff/) for lint + format, or Black + Flake8
- **JavaScript/TypeScript:** ESLint + Prettier
- **All projects:** [EditorConfig](https://editorconfig.org/) for baseline whitespace consistency

Add a `.editorconfig` to the project root:

```ini
root = true

[*]
indent_style = space
indent_size = 4
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.{js,ts,json,yaml,yml}]
indent_size = 2
```

### Step 4: Define VS Code tasks

Tasks standardize how you build, test, and run the project — and make these commands available to Copilot's agent mode. Create `.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "test",
      "type": "shell",
      "command": "python -m pytest",
      "group": {
        "kind": "test",
        "isDefault": true
      },
      "presentation": {
        "reveal": "always",
        "panel": "shared"
      }
    },
    {
      "label": "lint",
      "type": "shell",
      "command": "ruff check .",
      "group": "build"
    }
  ]
}
```

---

## Exercises

See [exercises.md](./exercises.md) for full instructions.

**Quick list:**

1. Write your first project-level Copilot instructions — configure a minimal starter project
2. Test instruction effectiveness — verify Copilot applies your conventions
3. File organization audit — identify context dilution in a sample project
4. Configure a linter — install Ruff or ESLint and integrate with VS Code
5. Tasks and agent mode — define a task and invoke it through agent mode

---

## Common Mistakes

| Mistake | Why it happens | How to fix it |
|---------|----------------|---------------|
| Vague instructions ("use best practices") | Developer thinks any instruction is better than none | Replace with specific, verifiable rules: "use `snake_case` for all function names" |
| Forgetting `useInstructionFiles: true` | Default setting may be `false` | Add `github.copilot.chat.codeGeneration.useInstructionFiles: true` to `.vscode/settings.json` |
| Monolithic utility files | Legacy habit from non-AI codebases | Split into focused modules; each file should have one clear purpose |
| No type annotations or docstrings | "Copilot will add them later" | Add them upfront — they are primary context signals |
| Contradictory instructions | Instructions added incrementally without review | Review the full instructions file before adding. Remove obsolete rules. |

---

## Best Practices

- **Do:** Write instructions in imperative form: "Use `dataclasses` for all data models."
- **Do:** Version your instructions — add `Verified: YYYY-MM` to the header.
- **Do:** Keep each file under 400 lines. Split at natural boundaries.
- **Don't:** Put all helper functions in a single `utils.py` — context becomes ambiguous for Copilot.
- **Don't:** Leave commented-out code blocks in files — they add noise to Copilot's context.

---

## Token / Premium Request Impact

| Action | Cost level | Notes |
|--------|-----------|-------|
| Writing copilot-instructions.md | Low | One chat turn; one-time effort |
| Applying instructions to every session | Zero additional | Instructions are injected automatically |
| Asking Copilot to audit instructions for contradictions | Low | Short context, single ask |
| Asking Copilot to reorganize a file structure | Medium | Multi-file read; use Edit mode |
| Agent mode: scaffold `.vscode/` config files | Low–Medium | Few small files; limited tool calls |

---

## Completion Criteria

Before moving to Module 03, confirm:

- [ ] Your project has a `.vscode/settings.json` with `useInstructionFiles: true`
- [ ] Your project has a `.github/copilot-instructions.md` with at least 3 specific rules
- [ ] A linter or formatter is configured and runs on save
- [ ] `.vscode/tasks.json` defines at least one `test` task
- [ ] All exercises in `exercises.md` are complete

Next: [Module 03 — Token and Premium Request Optimization](../03-token-optimization/)
