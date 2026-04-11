# Module 02: Configuration — Exercises

Complete these exercises in order. Each one applies a configuration concept from the module.

---

## Exercise 1: Write Your First Project-Level Instructions

**Goal:** Create a `.github/copilot-instructions.md` for a minimal Python project and verify Copilot reads it.

**Before this exercise, complete Task 1 in Lab 02** to have a starter project to work with.

**Instructions:**

1. In the starter project from Lab 02, create `.github/copilot-instructions.md`.
2. Add the following content:

```markdown
# Copilot Instructions — my-python-project

## Project Context
- Language: Python 3.12
- No external frameworks. Standard library only.
- Style: PEP 8 with 120 character line limit

## Coding Conventions
- Use `snake_case` for all function and variable names.
- Use `PascalCase` for class names.
- Always include type annotations on function signatures.
- Raise `ValueError` for invalid inputs; never use `assert` for validation in production code.

## Do Not
- Suggest `print()` for logging. Use `logging.getLogger(__name__)`.
- Generate SQL by string concatenation. Use parameterized queries.
```

3. Ensure `.vscode/settings.json` contains `"github.copilot.chat.codeGeneration.useInstructionFiles": true`.
4. Open the Copilot chat panel and ask: `What are your coding conventions for this project?`
5. Verify the response references your instructions.

**What to observe:** Copilot should reflect back your naming conventions, type annotation rule, and the logging constraint. If it doesn't, check that `useInstructionFiles` is `true` and the file is in `.github/` (not `.vscode/`).

---

## Exercise 2: Test Instruction Effectiveness

**Goal:** Confirm that Copilot's code generation follows the instructions you wrote in Exercise 1.

**Instructions:**

1. In the same project, open the Copilot chat panel (Edit mode).
2. Send this prompt: `Add a function called validate_age that takes an integer and returns True if it is between 0 and 150. Raise an appropriate error if not.`
3. Observe the generated code. Check:
   - Is the function named in `snake_case`? ✓
   - Are there type annotations on the signature? ✓
   - Does it raise `ValueError` (not `AssertionError`)? ✓
   - Does it use `logging` rather than `print`? (N/A here, but note if it appears)
4. If the output violates a convention, add a follow-up: `Refactor to match the project's coding conventions.`

**What to observe:** Instructions improve—but do not guarantee—compliance. Verify manually. If Copilot consistently ignores a rule, make the instruction more specific or break it into a separate bullet.

---

## Exercise 3: File Organization Audit

**Goal:** Identify context dilution in a real or sample project.

**Instructions:**

1. Open the Copilot chat panel in **Ask** mode.
2. Reference a large utility file in your current project (or use the sample below) with `#file:`:

```
#file:src/utils.py
Review this file for context dilution: does it contain multiple unrelated concerns?
If yes, suggest how to split it into focused modules, giving each a descriptive name.
```

3. If you don't have a utility file, create a temporary `utils.py` with three unrelated concerns (e.g., date formatting, email validation, and database connection helpers) and run the prompt against it.
4. Write down the suggested split. You do not need to implement it — the goal is to recognize the pattern.

**What to observe:** Copilot identifies mixed concerns well when the file is large. Its split suggestions are usually sensible. Compare its suggestions to your own instinct.

---

## Exercise 4: Configure a Linter

**Goal:** Install Ruff (Python) or ESLint (JS/TS), configure it for 120-character lines, and wire it to run on save.

**Choose the exercise matching your primary language.**

### Python (Ruff)

1. Install the [Ruff VS Code extension](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff).
2. Add `pyproject.toml` to the project root:

```toml
[tool.ruff]
line-length = 120
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "I", "N", "S"]
```

3. Add these keys to `.vscode/settings.json`:

```json
"[python]": {
  "editor.defaultFormatter": "charliermarsh.ruff",
  "editor.formatOnSave": true
},
"ruff.enable": true
```

4. Open a Python file, write a function with a 130-character line, and save. Confirm Ruff underlines the violation.

### JavaScript (ESLint + Prettier)

1. Install the [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) and [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) extensions.
2. Initialize ESLint: run `npx eslint --init` in the terminal and follow the prompts.
3. Add `.prettierrc`:

```json
{
  "printWidth": 120,
  "singleQuote": true,
  "semi": true
}
```

4. Write a JS file with a long line and inconsistent quotes. Save. Confirm formatting applies.

**What to observe:** On-save formatting ensures Copilot's context is always correctly formatted. This improves suggestion quality for subsequent completions.

---

## Exercise 5: Define a Task and Invoke It from Agent Mode

**Goal:** Define a `test` task in `.vscode/tasks.json` and ask agent mode to run the tests.

**Instructions:**

1. Add `.vscode/tasks.json` to the project with a `test` task appropriate for your project:
   - Python: `python -m pytest`
   - Node.js: `npm test`
   - Other: use the relevant command

2. Open the Copilot chat panel in **Agent** mode.
3. Add a simple test file to your project (or use an existing one).
4. Send this prompt: `Run the project tests and tell me if they pass.`
5. Observe agent mode's terminal tool call. It should run the test command.

> Before running agent mode, read what it proposes to do. Agent mode can execute terminal commands and modify files.

**What to observe:** Agent mode can discover and run VS Code tasks. Defined tasks reduce ambiguity about which command to use. Compare this to what happens when there is no tasks.json — agent mode will guess.

---

## Exercise 6: Create a Shared Extensions File

**Goal:** Add `.vscode/extensions.json` to the starter project so VS Code prompts contributors to install required tools.

**Before this exercise, complete Task 6 in Lab 02.**

**Instructions:**

1. In the `starter/` project from Lab 02, create `.vscode/extensions.json`:

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

2. Close and reopen the `starter/` folder in VS Code.
3. Observe the notification: **"Do you want to install the recommended extensions for this repository?"**
4. Dismiss the notification — you have already installed these tools.
5. Open the Extensions panel (`Ctrl+Shift+X`), click the filter icon, and select **Show Recommended Extensions**. Confirm your extensions appear under **Workspace Recommendations**.

**What to observe:** VS Code displays workspace recommendations separately from global extensions. Any contributor who opens this project sees the same list — the same lint, format, and Copilot toolchain across the team.

---

## Exercise 7: Documentation Baseline Signal Test

**Goal:** Observe how type annotations and docstrings improve Copilot's inline suggestion quality.

**Before this exercise, complete Exercise 1.**

**Instructions:**

1. Open `starter/src/calculator.py` from Lab 02.
2. Add an unannotated function with no docstring at the end of the file:

```python
def clamp(value, min_value, max_value):
    pass
```

3. Position the cursor on `pass` and trigger inline completion (`Alt+\` or wait for the ghost text).
4. Note the suggestion(s) — quality will vary.
5. Now rewrite the function signature with full type annotations and a docstring:

```python
def clamp(value: float, min_value: float, max_value: float) -> float:
    """Return value clamped to the inclusive range [min_value, max_value]."""
    pass
```

6. Trigger inline completion again. Note the suggestion(s).
7. Compare the two results. The annotated version should produce a complete, correct implementation.

**What to observe:** Annotations and docstrings dramatically reduce Copilot's guesswork. The effect is most visible for numeric operations, validation logic, and any function with a non-obvious return type.
