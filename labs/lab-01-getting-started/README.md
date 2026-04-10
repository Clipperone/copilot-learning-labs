# Lab 01: Getting Started with GitHub Copilot Pro+

> **Difficulty:** Beginner
> **Estimated time:** 40–50 minutes
> **Module:** [Module 01 — Foundations](../../modules/01-foundations/)
> **Prerequisites:** GitHub Copilot Pro+ installed and authenticated in VS Code
> **Verified:** 2026-04

---

## Learning Objective

Complete this lab and you will have used GitHub Copilot Pro+ deliberately across five of the six interaction modes on real coding tasks (Agent mode is introduced in Module 06), applied the Read → Run → Reason → Risk critical review workflow to AI-generated code, and established the three first-session productivity habits.

---

## Prerequisites

- [ ] GitHub account with an active Copilot Pro+ subscription
- [ ] VS Code 1.90 or later installed
- [ ] GitHub Copilot and GitHub Copilot Chat extensions installed and authenticated
- [ ] The Copilot icon in the VS Code status bar shows no error

If any prerequisite is unmet, complete the setup steps in [Module 01 — Foundations](../../modules/01-foundations/README.md#install-and-authenticate) before continuing.

---

## Setup

1. Clone or open this repository in VS Code.
2. Install recommended extensions when prompted, or run **Extensions: Show Recommended Extensions** from the command palette.
3. Open a new VS Code terminal (`Ctrl+`` `) and confirm you are in the repository root.
4. Before starting Task 1: close any unrelated file tabs. Open only what each task requires.

---

## Tasks

### Task 1: Your First Deliberate Inline Completion

**Covers:** Module 01 §3 (The Six Interaction Modes) — inline completion

**Goal:** Experience the accept / reject / cycle workflow consciously, not reflexively.

**Before you type:** Decide your acceptance criterion. Write it here before starting:

> *I will accept this completion if it: _______________*

**Instructions:**

1. Create a new file `scratch/task1.py` in this repository.
2. Type the following line and pause after the colon. Do not press anything for two seconds.

   ```python
   def calculate_bmi(weight_kg: float, height_m: float):
   ```

3. When ghost text appears, **read it fully** before pressing anything.
4. Apply Read → Run → Reason → Risk mentally:
   - Does the suggested body make sense for this function name?
   - Would it execute without errors?
   - Does it handle edge cases (zero height, negative values)?
   - Is there a security or correctness risk?
5. Press `Alt+]` to see an alternative suggestion.
6. Accept the one that better matches your criterion with `Tab`, or press `Esc` if neither is acceptable.

**Expected output:** A completed `calculate_bmi` function in `scratch/task1.py`. You applied the review workflow before accepting.

---

### Task 2: Mode Selection Practice

**Covers:** Module 01 §3 — choosing the right mode for each task

**Goal:** Use Ask, Edit, Plan, and Inline chat on different task types to build mode-selection instinct.

Before each sub-task: state which mode you are using and why (one sentence in your own head or in a comment).

---

**2a — Ask mode: explain unfamiliar code**

1. Open `scratch/task1.py`.
2. Open the Copilot chat panel (`Ctrl+Alt+I`). Set mode to **Ask**.
3. Send this prompt:

   ```
   Explain this function line by line. Identify any edge cases it does not handle.
   ```

4. Read the response. Did it identify division by zero when `height_m = 0`?
5. Follow up: `What input validation would make this function production-safe?`

**Expected output:** A clear explanation and at least one follow-up identifying an unhandled edge case.

---

**2b — Edit mode: targeted code change**

1. Open `starter/verify.py`.
2. Switch the chat panel to **Edit** mode. Add `verify.py` to the working set.
3. Send this prompt:

   ```
   Add type annotations and input validation to all four functions.
   Raise TypeError for non-numeric arguments.
   Raise ZeroDivisionError if the divisor is zero in divide().
   Add a one-line docstring to each function.
   ```

4. **Review the diff carefully** before accepting. Check:
   - Do all four functions have type annotations?
   - Is the error message in each TypeError informative?
   - Does `divide()` guard against zero?
5. Accept the diff.
6. Compare your result with `solution/verify.py`.

**Expected output:** `starter/verify.py` has type annotations, docstrings, and input validation on all four functions. The diff was reviewed and accepted deliberately.

---

**2c — Plan mode: design before coding**

1. Switch the chat panel to **Plan** mode.
2. Send this prompt:

   ```
   I need a small Python module that:
   - Reads a list of people (name, weight_kg, height_m) from a JSON file
   - Calculates BMI for each person
   - Classifies each as Underweight, Normal, Overweight, or Obese
   - Writes the results to a CSV file

   Plan the implementation. Do not write any code yet.
   ```

3. Read the plan. Confirm it covers: file reading, calculation, classification, file writing, and error handling for missing input file.
4. Ask a follow-up: `What happens if the JSON file has a person with missing fields?`

**Expected output:** A complete implementation plan with edge cases. No code written yet.

---

**2d — Inline chat: quick scoped fix**

1. Open `scratch/task1.py`. Locate the `calculate_bmi` function body (not the validation).
2. Select the line with the BMI calculation (`return weight_kg / (height_m ** 2)` or similar).
3. Press `Ctrl+I`. Type:

   ```
   Round the result to 1 decimal place.
   ```

4. Review the inline suggestion. Accept it.

**Expected output:** The return statement rounds the result. Applied without switching to the chat panel.

---

### Task 3: Critical Review in Practice

**Covers:** Module 01 §4 — Read → Run → Reason → Risk

**Goal:** Apply the full four-step workflow to a piece of AI-generated code and identify a real flaw.

**Instructions:**

1. Open the Copilot chat panel. Set mode to **Ask**.
2. Send this prompt exactly:

   ```python
   Write a Python function that takes a username and password from the user,
   checks the password against the value stored in a dictionary, and returns
   True if matched. Use a simple dictionary like {"alice": "secret123"}.
   ```

3. Copy the generated function into `scratch/task3.py`.
4. Apply Read → Run → Reason → Risk:

   | Step | Question to answer in writing |
   |------|------------------------------|
   | **Read** | What does each line do? |
   | **Run** | Does it execute? What happens with an unknown username? |
   | **Reason** | Does it do what was asked, exactly? Are there unintended behaviors? |
   | **Risk** | Does it store or compare credentials in a way that introduces a security risk? Name the specific concern. |

5. Write your answers as comments at the bottom of `scratch/task3.py`.
6. Ask Copilot a follow-up: `What are the security risks in this function and how would you fix them?`
7. Read the response. Did it identify plaintext credential storage?

**Expected output:** `scratch/task3.py` contains the generated function and your four written answers as comments. The security flaw is named.

> **Reference:** OWASP A02 — Cryptographic Failures covers plaintext credential storage. OWASP A01 — Broken Access Control covers authentication logic that can be bypassed.

---

### Task 4: Establish Your Three Habits

**Covers:** Module 01 §5 — First Productivity Habits

**Goal:** Practise the three habits once each in a controlled context so they become automatic.

---

**Habit 1 — Choose the mode before writing the prompt**

1. Think of a task you would normally do with Copilot on a real project.
2. Before opening the chat panel, answer these three questions:
   - Does the task require file changes? (Yes/No)
   - Is it one file or multiple files? (One/Multiple)
   - Does it require multi-step execution? (Yes/No)
3. Based on your answers, select the mode using the decision flowchart from Module 01 §3.
4. Open the chat panel. Confirm you are already in the correct mode before typing the prompt.

**Expected output:** You opened the right mode on the first try, without switching after starting.

---

**Habit 2 — Write your acceptance criterion first**

1. Choose any short coding task (e.g., "add type hints to `task1.py`").
2. Before sending the prompt, write one sentence:

   *"I will accept this if: _______________"*

3. Send the prompt.
4. When Copilot responds, evaluate against your criterion — not against "does this look right."
5. Accept, revise, or reject based on the criterion.

**Expected output:** You evaluated Copilot's output against a pre-stated criterion, not by feel.

---

**Habit 3 — Close irrelevant files**

1. Open 3–4 unrelated files in VS Code tabs (any files from this repository you are not currently working on).
2. Open the chat panel.
3. Notice how many files Copilot might reference.
4. Close all files except `scratch/task1.py`.
5. Ask: `What open files does Copilot have access to right now?`
6. Observe the difference in what Copilot reports or references.

**Expected output:** You experienced the effect of open file count on Copilot's context scope.

---

### Task 5: Cost Classification Check

**Covers:** Module 01 §6 — Token and Premium Request Basics

**Goal:** Classify five task types by request cost from memory, then verify.

**Instructions:**

Without looking at your notes, classify each task below as **included** or **premium**:

| # | Task | Your classification |
|---|------|-------------------|
| 1 | Accept a ghost text completion for a function body | |
| 2 | Ask the default model to explain a 15-line function | |
| 3 | Run an agent session to scaffold a Django app across 8 files | |
| 4 | Use Edit mode with Claude Sonnet to refactor a class | |
| 5 | Use Plan mode with the default model to design a database schema | |

Check your answers against [modules/01-foundations/theory.md — Chat Mode Tool Access Reference](../../modules/01-foundations/theory.md).

**Expected output:** At least 4 of 5 correct. For any incorrect answer, write one sentence explaining the rule you missed.

---

## Expected Outputs

By the end of this lab you will have:

| Deliverable | Location |
|-------------|---------|
| BMI function with input validation | `scratch/task1.py` |
| `verify.py` with type annotations, docstrings, and input validation | `starter/verify.py` |
| Ask / Edit / Plan / Inline chat used on real tasks | VS Code chat history |
| Critical review answers for AI-generated code | `scratch/task3.py` (as comments) |
| Security flaw identified by name | `scratch/task3.py` |
| Task cost classification (4/5 correct) | Worksheet in Task 5 |

---

## Success Criteria

| Criterion | How to verify |
|-----------|--------------|
| Inline completion accepted deliberately | `task1.py` has a completed function; you can explain every line |
| All four chat modes used | Ask, Edit, Plan, and Inline chat each produced a result |
| Diff reviewed before accepting | Edit mode change was reviewed line by line before accepting |
| Critical review applied | `task3.py` has written answers for all four Read → Run → Reason → Risk steps |
| Security flaw named | OWASP A02 (plaintext credential storage) identified |
| Cost classification correct | 4/5 or 5/5 correct in Task 5 |

---

→ Self-assess with [checklist.md](./checklist.md) before moving on.

---

## Common Failure Points

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| Ghost text never appears | Extension disabled or not authenticated | Click the Copilot status bar icon and sign in |
| Edit mode diff is blank | File not added to the working set | Click **+** in the Edit mode header to add the file |
| Plan mode writes code immediately | Mode not set to Plan before sending | Discard; switch to Plan mode explicitly first |
| Task 3 security flaw not identified | Prompt accepted without running Risk step | Return to Task 3; ask Copilot: "What security risks does this function have?" |
| Agent mode unavailable | Plan does not include Pro+ | Verify at [github.com/settings/copilot](https://github.com/settings/copilot) |
| Task 5 cost classification mostly wrong | Conflating mode with model | Re-read: mode alone does not determine cost; premium model selection does |

---

## Extension Ideas

- Run Task 2c (Plan) and then immediately implement the plan using Edit mode — observe how planning first changes the quality of the generated code.
- Compare the default model and a premium model (e.g., Claude Sonnet) on the exact same Task 3 prompt. Are the security risks identified more clearly by one model?
- Take the `task1.py` BMI function through the full pre-commit checklist at [checklists/pre-commit.md](../../checklists/pre-commit.md).
- Redo Task 3 with a different AI failure mode category — try prompting for code that might produce a hallucinated API, then verify it in the documentation.

---

## Next Steps

→ Complete [modules/01-foundations/checklist.md](../../modules/01-foundations/checklist.md) before advancing.

→ Next: [Lab 02 — Project Configuration Baseline](../lab-02-configuration/)

→ Full lab index: [labs/README.md](../README.md)
