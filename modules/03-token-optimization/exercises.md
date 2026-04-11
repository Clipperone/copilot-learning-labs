# Module 03: Token and Premium Request Optimization — Exercises

Complete these exercises in order. Exercises 4 and 5 build the deliverable for Lab 03.

---

## Exercise 1: Request Type Classification

**Goal:** Correctly classify 10 actions as included or premium requests.

**Instructions:**

Classify each action below. Write "Included", "Premium", or "Depends" (and explain why).

| # | Action | Your classification |
|---|--------|-------------------|
| 1 | Accept a ghost text inline completion | |
| 2 | Ask the default model to explain a function | |
| 3 | Switch to GPT-4o and ask one question | |
| 4 | Run a 10-step agent session with default model | |
| 5 | Open Plan mode and design a database schema | |
| 6 | Use o1 to review a security-sensitive function | |
| 7 | Dismiss an inline completion with Esc | |
| 8 | Use Agent mode with the default model to rename a variable | |
| 9 | Use agent mode with Claude 3.5 to scaffold a new feature | |
| 10 | Ask the included model for a code review of a 500-line file | |

**Expected answers:** 1 Included, 2 Included, 3 Premium, 4 Premium (agent mode counts), 5 Included (Plan + default), 6 Premium, 7 Included (no request sent), 8 Included, 9 Premium, 10 Depends (large context may incur multiplier).

**What to observe:** Inline completions and default-model chat are cheap. Agent mode and premium models are where quota moves. The combination (agent + premium model + large context) is the highest-cost scenario.

---

## Exercise 2: Mode Selection Drill

**Goal:** Choose the minimum sufficient mode and model for 8 task descriptions.

**Instructions:**

For each task, decide: which mode? which model? Record your reasoning.

| # | Task | Your mode selection | Your model selection |
|---|------|--------------------|--------------------|
| 1 | Autocomplete a for loop over a list | | |
| 2 | Explain what a 20-line function does | | |
| 3 | Rename a parameter in one file, 5 occurrences | | |
| 4 | Design the architecture for a new microservice | | |
| 5 | Scaffold 6 files for a new REST endpoint | | |
| 6 | Debug a complex async race condition | | |
| 7 | Generate a docstring for a single function | | |
| 8 | Audit an authentication module for OWASP A07 | | |

**Reference answers:**

| # | Mode | Model | Why |
|---|------|-------|-----|
| 1 | Inline completion | Default | Lowest cost, ephemeral |
| 2 | Ask | Default | Read-only, short context |
| 3 | Edit | Default | Single-file, targeted |
| 4 | Plan | Default | Design only, no code |
| 5 | Agent | Default | Multi-file scaffold needs tool use |
| 6 | Agent | GPT-4o or Claude | Reasoning-heavy, multi-file |
| 7 | Inline chat or Ask | Default | Short, contained task |
| 8 | Ask or Agent | o1 | Security audit needs deep reasoning |

**What to observe:** There is rarely one correct answer. The goal is to develop a consistent rationale and default to the lower-cost option when the task is ambiguous.

---

## Exercise 3: Prompt Compaction

**Goal:** Rewrite 3 verbose prompts as concise, single-turn prompts.

**Instructions:**

Rewrite each prompt below so it can produce a complete, correct first response without follow-ups.

**Prompt A (verbose):**
> `I have a function that does some calculations. It might have some issues. Can you look at it and maybe improve it?`

Write your compact version here:

---

**Prompt B (verbose):**
> `I want to add error handling to my code. The code is in a Python file. There are some places where things could go wrong. Can you help me identify those and add appropriate handling?`

Assume the target file is `payment_processor.py`.

Write your compact version here:

---

**Prompt C (verbose):**
> `I need tests. The function processes orders. Use pytest. Make sure edge cases are covered.`

Assume the function is `def process_order(order_id: int, discount: Decimal) -> Order` in `orders.py`.

Write your compact version here:

---

**Reference compact versions:**

Prompt A: `Review the #selection for correctness and performance. State each issue you find, then suggest the fix. Python 3.12.`

Prompt B: `Add exception handling to every function in #file:payment_processor.py that performs I/O, external calls, or user input parsing. Raise specific exceptions (never bare except). Python 3.12.`

Prompt C: `Write pytest tests for `process_order(order_id: int, discount: Decimal) -> Order` in orders.py. Cover: valid order, invalid order_id (negative, non-integer), discount out of range (< 0, > 1), and zero-quantity order.`

**What to observe:** Compact prompts name the target, state the action, give constraints, and (for tests) list the expected cases explicitly. Every word removed from "verbose" reduces ambiguity.

---

## Exercise 4: Context Window Experiment

**Goal:** Compare response quality with minimal vs. maximal context.

**Instructions:**

Choose a moderately complex function from a project you have access to.

**Round 1 — Maximal context:**
1. Open 10+ files in VS Code.
2. Ask in chat with no `#file:` reference: `Review this function for edge cases and security issues.`
3. Note: which function did Copilot review? Was the response relevant?

**Round 2 — Minimal context:**
1. Open a new chat session. Close all files except the one with the function.
2. Select the function in the editor.
3. Ask: `Review #selection for edge cases and security issues. The function is part of a [Python/JS/etc.] project.`
4. Note: was the response more focused?

**Reflection questions:**

- Which response was more relevant to the actual function you wanted reviewed?
- Did the first response make assumptions about the wrong file?
- What does this tell you about when to use `#selection` vs. relying on open context?

**What to observe:** Explicit scope (`#selection`, `#file:`) consistently outperforms ambient open-tabs context. The model can only use what is clearly in front of it.

---

## Exercise 5: Build Your Decision Cheat Sheet

**Goal:** Produce a personal mode/model decision reference you will actually use.

**Instructions:**

1. Download or copy the worksheet from [Lab 03 — Token Audit Exercise](../../labs/lab-03-token-audit/).
2. Complete the cheat sheet section using the insights from Exercises 1–4.
3. Add at least 3 rows for task types specific to your work context (not already in the template).
4. Paste your completed cheat sheet as a comment or a file in your personal workspace.

**This is the primary deliverable of Module 03.** A cheat sheet you have personalized is more valuable than one you have only read.
