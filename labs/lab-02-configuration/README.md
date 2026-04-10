# Lab 02: Project Configuration Baseline

> **Difficulty:** Beginner
> **Estimated time:** 45–60 minutes
> **Module:** [Module 02 — Configuration](../../modules/02-configuration/)
> **Type:** Hands-on project setup

---

## Learning Objective

After completing this lab, you will have configured a minimal Python project with a working VS Code workspace, project-level Copilot instructions, a linter, and a task runner — and you will have verified that Copilot uses your instructions.

---

## Prerequisites

- [ ] Module 01 completed
- [ ] Module 02 theory read
- [ ] Python 3.10+ installed (`python --version` in terminal)
- [ ] Ruff VS Code extension installed (`charliermarsh.ruff`)

---

## Setup

1. Open the `starter/` folder in VS Code as a workspace (or open the parent folder and navigate to `starter/`).
2. Inspect the project structure — notice what is missing.
3. Do not copy files from `solution/` until you have attempted each task.

---

## Tasks

### Task 1: Create a Workspace Settings File

**Goal:** Add a `.vscode/settings.json` that activates Copilot instruction files and configures formatting.

**Instructions:**

1. Create the `.vscode/` folder inside `starter/` if it does not exist.
2. Create `.vscode/settings.json` with the following minimum content:

```json
{
  "editor.formatOnSave": true,
  "editor.rulers": [120],
  "github.copilot.chat.codeGeneration.useInstructionFiles": true,
  "files.exclude": {
    "**/__pycache__": true,
    "**/.pytest_cache": true
  }
}
```

3. Reload the VS Code window (`Ctrl+Shift+P` → **Developer: Reload Window**) to apply the settings.

**Success criterion:** Open VS Code Settings (`Ctrl+,`), search for `useInstructionFiles`, and confirm the workspace value is `true`.

---

### Task 2: Write Project-Level Copilot Instructions

**Goal:** Create a `.github/copilot-instructions.md` with specific, verifiable rules.

**Instructions:**

1. Create the `.github/` folder inside `starter/` if it does not exist.
2. Create `.github/copilot-instructions.md` with at minimum:

```markdown
# Copilot Instructions — lab-02-project

## Project Context
- Language: Python 3.12
- No external dependencies. Standard library only.

## Coding Conventions
- Use `snake_case` for all function and variable names.
- Use `PascalCase` for class names.
- Always include type annotations on function signatures.
- Raise `ValueError` for invalid input. Never use bare `except:`.

## Do Not
- Suggest `print()` for logging. Use `logging.getLogger(__name__)`.
- Generate any code outside the `src/` folder unless explicitly asked.
```

3. Open the Copilot chat panel in **Ask** mode and send:

```
What are your coding conventions for this project?
```

4. Verify the response reflects the rules you wrote.

**Success criterion:** Copilot's response mentions `snake_case`, type annotations, and `ValueError` — the three most specific rules.

---

### Task 3: Add an EditorConfig File

**Goal:** Establish consistent whitespace settings for all contributors.

**Instructions:**

1. Create `.editorconfig` in the `starter/` root:

```ini
root = true

[*]
indent_style = space
indent_size = 4
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true
```

2. Open `src/calculator.py` from the starter files. Add a trailing space to one line and save.
3. Verify the trailing space is removed on save (requires the [EditorConfig extension](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)).

**Success criterion:** Trailing whitespace is removed on save. Final newline is present.

---

### Task 4: Configure Ruff Linting

**Goal:** Add `pyproject.toml` to configure Ruff and confirm lint errors are surfaced.

**Instructions:**

1. Create `pyproject.toml` in `starter/`:

```toml
[tool.ruff]
line-length = 120
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "I", "N"]
```

2. Add these keys to `.vscode/settings.json`:

```json
"[python]": {
  "editor.defaultFormatter": "charliermarsh.ruff",
  "editor.formatOnSave": true
},
"ruff.enable": true
```

3. Open `src/calculator.py`. Add an unused import at the top: `import os`.
4. Confirm Ruff underlines it as an `F401` error (unused import).
5. Remove the unused import. Save. Confirm the underline disappears.

**Success criterion:** Ruff detects `F401` on the unused import and clears when the import is removed.

---

### Task 5: Define a Test Task

**Goal:** Create `tasks.json` so the test suite can be run from VS Code and from agent mode.

**Instructions:**

1. Create `.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "test",
      "type": "shell",
      "command": "python -m pytest tests/ -v",
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
      "command": "ruff check src/",
      "group": "build"
    }
  ]
}
```

2. Run the test task: `Ctrl+Shift+P` → **Tasks: Run Test Task**.
3. Confirm the tests in `tests/test_calculator.py` pass.

**Success criterion:** All 4 tests in `test_calculator.py` pass. Output is visible in the terminal panel.

---

## Success Criteria

| Item | Verified |
|------|---------|
| `.vscode/settings.json` exists with `useInstructionFiles: true` | ☐ |
| `.github/copilot-instructions.md` has at least 3 specific rules | ☐ |
| Copilot reflects your conventions when asked | ☐ |
| `.editorconfig` removes trailing whitespace on save | ☐ |
| Ruff detects unused imports in `src/calculator.py` | ☐ |
| `test` task runs and all 4 tests pass | ☐ |

---

## Common Failure Points

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| Copilot does not mention conventions when asked | `useInstructionFiles` is `false` or the file is not in `.github/` | Check setting value; confirm file path is `.github/copilot-instructions.md` |
| Ruff does not show errors | Ruff extension not installed or `ruff.enable` missing | Install `charliermarsh.ruff` extension; add `"ruff.enable": true` |
| Tests fail to run | `pytest` not installed | Run `pip install pytest` in the terminal |
| Trailing whitespace not removed | EditorConfig extension not installed | Install the EditorConfig extension from the marketplace |

---

## Reference Solution

The `solution/` folder contains the fully configured project. Compare your configuration files to the reference after completing all tasks — not before.
