# Lab 01: Setup and Verify

> **Difficulty:** Beginner
> **Estimated time:** 40–50 minutes
> **Module:** [Module 01 — Foundations](../../modules/01-foundations/)
> **Type:** Standalone

---

## Learning Objective

Complete this lab and you will have confirmed that GitHub Copilot Pro+ is installed, authenticated, and functional in VS Code; used all six interaction modes with a real prompt; applied the critical review workflow to an AI suggestion; and classified task types by request cost.

---

## Prerequisites

- [ ] A GitHub account with an active GitHub Copilot Pro+ subscription
- [ ] VS Code installed (version 1.90 or later)
- [ ] Internet connection (required for authentication)

---

## Setup

1. Clone or open this repository in VS Code.
2. When prompted, install the recommended extensions, or run **Extensions: Show Recommended Extensions** from the command palette.
3. Sign in to GitHub: **Accounts** icon (bottom-left) → **Sign in with GitHub**.

---

## Tasks

### Task 1: Verify Copilot is Active

**Goal:** Confirm the extension is installed, authenticated, and serving completions.

**Instructions:**

1. Check the VS Code status bar (bottom right). The Copilot icon must be visible with no warning or error state. If it shows a warning, click it and sign in.
2. Open `starter/verify.py`.
3. Place your cursor at the end of the last line and press `Enter`.
4. Type `def greet(` and pause. Grey ghost text should appear.
5. Press `Tab` to accept it. Then press `Ctrl+Z` to undo and restore the file.

**Success criterion:** Ghost text appeared, `Tab` accepted it, the file is back to its original state.

---

### Task 2: Complete the Mode Verification Worksheet

**Goal:** Confirm all six modes produce a valid response in your environment.

**Instructions:**

1. Open `starter/mode-verification.md`.
2. For each mode in the worksheet, run the test prompt and record the result (one sentence: what Copilot returned or did).
3. Mark each mode as ✅ (worked) or ❌ (error — note the error message).

**Test prompts by mode:**

| Mode | How to open | Test prompt |
|------|------------|------------|
| Inline completion | Type in any `.py` file | Type `def calculate_area(` and pause |
| Ask | `Ctrl+Alt+I`, set to Ask | `What does starter/verify.py do?` |
| Edit | `Ctrl+Alt+I`, set to Edit, add `verify.py` to working set | `Add a docstring to each function.` — review diff, then **Discard** |
| Plan | `Ctrl+Alt+I`, set to Plan | `Plan a function that reads a CSV and returns rows where status = active.` |
| Agent | `Ctrl+Alt+I`, set to Agent | `List all Python files in the starter/ folder and describe each one.` |
| Inline chat | Open `verify.py`, select the `add` function, press `Ctrl+I` | `Add input validation to reject non-numeric arguments.` — press `Esc` after reviewing |

> **Discard after each Edit or Inline chat test.** These tasks verify function only — do not save changes to `verify.py`.

**Success criterion:** `starter/mode-verification.md` has a result recorded for all six modes.

---

### Task 3: Apply the Critical Review Workflow

**Goal:** Use Read → Run → Reason → Risk on AI-generated code to identify a real flaw.

**Instructions:**

1. Open `starter/review-exercise.md`.
2. Read both code snippets in the file.
3. For each snippet, apply the four-step workflow and write your answers in the labeled fields.
4. Identify which snippet contains a flaw and describe it.

**Success criterion:** `starter/review-exercise.md` has written answers for all four steps on both snippets. The flaw in Snippet B is identified correctly.

Compare your answers with `solution/review-exercise.md`.

---

### Task 4: Request Classification

**Goal:** Classify five task descriptions as included or premium requests without looking up documentation.

**Instructions:**

1. Open `starter/request-classification.md`.
2. For each task description, write your classification (`included` or `premium`) and a one-sentence explanation.
3. Aim to answer from memory using the cost-aware decision rule: *use the cheapest mode that handles the task*.

**Success criterion:** At least 4 of 5 classifications match the solution. `starter/request-classification.md` has written reasoning for all five.

Compare your answers with `solution/request-classification.md`.

---

## Success Criteria

| Criterion | How to verify |
|-----------|--------------|
| Copilot active | Status bar icon shows no error |
| Inline completion works | Ghost text appeared in `verify.py` |
| All six modes work | `mode-verification.md` has ✅ for all six rows |
| Critical review applied | `review-exercise.md` has answers in all four fields per snippet |
| Flaw identified | Snippet B flaw is named correctly |
| Request classification | At least 4/5 correct in `request-classification.md` |

---

## Common Failure Points

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| No ghost text appears | Not authenticated, or extension disabled | Click the Copilot status bar icon and sign in |
| Chat panel won't open | Copilot Chat extension not installed | Install `github.copilot-chat` from the Extensions panel |
| Agent mode not available | Plan does not include Agent mode | Verify subscription at [github.com/settings/copilot](https://github.com/settings/copilot) |
| Edit mode diff is empty | File not added to the working set | Click **+** in the Edit mode header to add the file |
| Completions appear then stop | Firewall or proxy blocking requests | Check VS Code network proxy settings |

---

## Files in This Lab

| File / Folder | Purpose |
|---------------|---------|
| `README.md` | Lab instructions (this file) |
| `checklist.md` | Completion self-assessment |
| `starter/verify.py` | Python file used in Tasks 1 and 2 |
| `starter/mode-verification.md` | Blank worksheet for Task 2 |
| `starter/review-exercise.md` | Two code snippets + question fields for Task 3 |
| `starter/request-classification.md` | Five task descriptions for Task 4 |
| `solution/verify.py` | Reference: `verify.py` with docstrings and validation added |
| `solution/mode-verification.md` | Reference: filled mode verification example |
| `solution/review-exercise.md` | Reference: correct answers including flaw identification |
| `solution/request-classification.md` | Reference: classifications with rationale |

---

## Learning Objective

After completing this lab, you can confirm that GitHub Copilot Pro+ is correctly installed, authenticated, and configured in VS Code, and demonstrate each Copilot mode with working examples.

---

## Prerequisites

- [ ] A GitHub account with an active GitHub Copilot Pro+ subscription
- [ ] VS Code version 1.90 or later installed
- [ ] Internet connection (required for Copilot authentication)

---

## Setup

1. Clone or open this repository in VS Code.
2. When prompted, install the recommended extensions (a notification will appear, or run **Extensions: Show Recommended Extensions** from the command palette).
3. Sign in to GitHub in VS Code if not already signed in: **Accounts** icon (bottom-left) → **Sign in with GitHub**.

---

## Tasks

### Task 1: Verify Copilot is Active

**Goal:** Confirm the Copilot extension is installed, authenticated, and serving completions.

**Instructions:**

1. Check the status bar at the bottom of VS Code. You should see the Copilot icon (a small circle or the GitHub Copilot logo). If it shows a warning, click it and sign in.
2. Open `starter/verify.py` from this lab folder.
3. Place your cursor at the end of the last line and press `Enter`.
4. Start typing `def greet(` and pause. A grey ghost text completion should appear.
5. Press `Tab` to accept it. Then press `Ctrl+Z` to undo and restore the file.

**Expected output:**

The ghost text appeared and pressing `Tab` completed the function signature. The Copilot icon in the status bar shows no error.

---

### Task 2: Test Each Mode

**Goal:** Confirm all major modes work in your environment.

**Instructions:**

Open the Copilot chat panel (`Ctrl+Alt+I`) and run each of the following:

**2a — Ask mode:**

With the mode set to **Ask**, send:

```
What does the 'starter/verify.py' file in my workspace do?
```

Confirm Copilot references the file content in its response.

**2b — Edit mode:**

Switch to **Edit** mode. Add `starter/verify.py` to the working set. Send:

```
Add a docstring to each function describing what it does.
```

Review the diff. **Do not accept it** — press **Discard**. (This is a verification, not a permanent change.)

**2c — Inline chat:**

Open `starter/verify.py`. Select the `add(a, b)` function body. Press `Ctrl+I` and type:

```
Add input validation to reject non-numeric arguments.
```

Review the suggestion. Press `Esc` to discard.

**Expected output:**

Each mode responded without errors. The diff in Edit mode was syntactically correct. Inline chat showed a valid suggestion.

---

### Task 3: Confirm Premium Model Access

**Goal:** Verify that premium model selection is available with your plan.

**Instructions:**

1. Open the Copilot chat panel.
2. Click the model selector (usually a dropdown at the top of the chat panel showing the current model name).
3. Confirm you can see and select a premium model (e.g., **Claude Sonnet**, **GPT-4o**, or **o1**).
4. Select a premium model and send a simple message: `Hello — which model are you?`
5. Switch back to the default model after receiving the response.

> **Note:** If the model selector shows only one option, your plan may not include premium model access. Verify at [github.com/settings/copilot](https://github.com/settings/copilot).

**Expected output:**

The model selector shows multiple options. The premium model responded correctly. You successfully switched back to the default.

---

### Task 4: Review Your `.vscode/` Settings

**Goal:** Confirm the repository's VS Code settings are loaded and relevant.

**Instructions:**

1. Open `.vscode/settings.json` in this repository.
2. Verify these three settings are present:

```json
"github.copilot.chat.codeGeneration.useInstructionFiles": true,
"github.copilot.chat.generateTests.codeLens": true,
"github.copilot.chat.reviewSelection.enabled": true
```

3. Open `.vscode/extensions.json` and confirm the recommended extensions list is present.
4. Check which of the recommended extensions you still need to install.

**Expected output:**

Settings file is present with the Copilot configuration values. You know which recommended extensions are missing.

---

## Expected Outputs

By the end of this lab, you should have:

- [ ] Confirmed Copilot is active with no status bar errors
- [ ] Triggered and accepted an inline completion
- [ ] Used Ask, Edit, and Inline chat modes without errors
- [ ] Verified premium model access (or documented the limitation)
- [ ] Reviewed and understood the `.vscode/` configuration

---

## Success Criteria

| Criterion | How to verify |
|-----------|---------------|
| Inline completion works | Ghost text appeared in `starter/verify.py` |
| Ask mode works | Copilot answered a question about the file |
| Edit mode works | A diff was proposed and shown (discarded after review) |
| Inline chat works | A suggestion appeared on selected code |
| Premium model accessible | Model selector showed at least one premium option |
| Settings loaded | `.vscode/settings.json` contains the three Copilot keys |

---

## Common Failure Points

| Symptom | Likely cause | Solution |
|---------|-------------|---------|
| No ghost text appears | Not signed in or extension not active | Click the Copilot icon in the status bar and sign in |
| Chat panel won't open | Copilot Chat extension not installed | Install `github.copilot-chat` from Extensions |
| Model selector shows only one model | Plan does not include premium models | Verify subscription at github.com/settings/copilot |
| Edit mode diff is empty | File not added to the working set | Click the **+** icon in the Edit mode header to add files |

---

## Review Checklist

See [checklist.md](./checklist.md) for the full self-assessment.

---

## Extension Ideas

- Try agent mode: ask Copilot to explain the entire `starter/` folder's purpose
- Compare the default model and a premium model on the same question about `verify.py`
- Open the Copilot output log (`Output` panel → `GitHub Copilot`) to observe what's happening under the hood

---

## Files in This Lab

| File / Folder | Purpose |
|---------------|---------|
| `README.md` | Lab instructions (this file) |
| `checklist.md` | Completion checklist |
| `starter/verify.py` | Starter file for Tasks 1 and 2 |
| `solution/verify.py` | Reference solution showing completed docstrings and validation |
