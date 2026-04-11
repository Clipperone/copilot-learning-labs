# Module 02: Configuration — Exercises

Complete these exercises in order. Each one applies a configuration concept from the module.

---

## Exercise 1: Extend Your Project-Level Instructions

**Goal:** Deepen the `.github/copilot-instructions.md` you wrote in Lab 02 by adding a security constraint and verifying Copilot applies it.

**Before this exercise, complete Tasks 1–2 in Lab 02** — the settings file and the initial instructions file must both exist.

**Instructions:**

1. Open `.github/copilot-instructions.md` from your Lab 02 `starter/` project.
2. Add a new `## Security` section after `## Do Not`:

```markdown
## Security
- Never concatenate user input into SQL strings. Use parameterized queries.
- Always validate function arguments at the boundary. Raise `ValueError` for out-of-range inputs.
- Do not generate code that suppresses exceptions with bare `except:` or `except Exception: pass`.
```

3. Save the file.
4. Open the Copilot chat panel in **Ask** mode and send:

```
What security constraints apply to this project?
```

5. Verify the response reflects the three new rules.
6. In **Edit** mode, send:

```
Add a function called parse_user_id that accepts a string and returns an integer user ID.
```

7. Inspect the generated code. Does it validate the input and raise `ValueError` for non-integer input?

**What to observe:** Security constraints in instructions propagate to code generation — not just to chat answers. A missing validation or a bare `except` in the output means the instruction needs to be more specific.

---

## Exercise 2: Test Instruction Effectiveness

**Goal:** Confirm that Copilot's code generation follows the instructions you wrote in Exercise 1.

**Instructions:**

1. In the same project, open the Copilot chat panel (Agent mode).
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

## Exercise 4: Extend Linting with Security Rules

**Goal:** Enable Ruff's security rule set (`S`) in the project you configured in Lab 02 Task 4 and observe the new violation class it surfaces.

**Before this exercise, complete Task 4 in Lab 02** — `pyproject.toml` and the Ruff extension must be active.

**Choose the exercise matching your primary language.**

### Python (Ruff)

1. Open `pyproject.toml` in the `starter/` project. Confirm the current `select` list.
2. Add `"S"` to the `select` list if it is not already there:

```toml
[tool.ruff.lint]
select = ["E", "F", "I", "N", "S"]
```

3. Open `src/calculator.py`. Add this function at the end of the file:

```python
def describe(value):
    print(f"Value is {value}")
```

4. Save. Confirm Ruff surfaces an `S002` violation (use of `print` is flagged as a security concern in production code under some rulesets) or `T201` depending on your Ruff version. If neither appears, the `print` call is not a security rule — instead add:

```python
import subprocess
subprocess.run("ls", shell=True)
```

5. Confirm Ruff surfaces `S602` (subprocess call with `shell=True`).
6. Remove the added code.

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

**What to observe:** Security rules surface patterns that convention rules miss. Enabling `S` in Ruff adds OWASP-aligned checks — `shell=True`, hardcoded passwords, unsafe `pickle` usage. These are exactly the issues Copilot might generate without a security-aware linter as a safety net.

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

## Exercise 6: Add a Project-Specific Extension to the Recommendations

**Goal:** Extend the `.vscode/extensions.json` you created in Lab 02 Task 6 by adding a project-specific extension and documenting the team justification for it.

**Before this exercise, complete Task 6 in Lab 02** — the base `extensions.json` must exist.

**Instructions:**

1. Open `.vscode/extensions.json` from the `starter/` project.
2. Add the [Todo Tree](https://marketplace.visualstudio.com/items?itemName=gruntfuss.todo-tree) extension or another extension relevant to your workflow:

```json
{
  "recommendations": [
    "github.copilot",
    "github.copilot-chat",
    "charliermarsh.ruff",
    "editorconfig.editorconfig",
    "gruntfuss.todo-tree"
  ]
}
```

3. Add a comment block at the top of the file explaining the rationale. Since JSON does not support comments, add it as the first key:

```json
{
  "_comment": "These extensions are required for this project. Install all before contributing.",
  "recommendations": [
    ...
  ]
}
```

4. Close and reopen `starter/`. Confirm VS Code includes the new extension in the workspace recommendations.
5. Open the Copilot chat panel in **Ask** mode. Attach `#file:.vscode/extensions.json` and ask:

```
Based on the extensions in this file, what kind of project is this and what toolchain does the team use?
```

6. Note how well the extension list communicates project intent to Copilot.

**What to observe:** The extension list itself is context. A well-curated `extensions.json` lets Copilot infer toolchain choices (Ruff → Python, ESLint + Prettier → JS) and tailor suggestions accordingly.

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
