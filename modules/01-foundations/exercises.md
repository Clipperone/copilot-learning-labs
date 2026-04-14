# Module 01: Foundations — Exercises

Complete these exercises in order. Each one targets a specific Copilot mode or skill.

Before each exercise: decide which mode you are using and why. Apply Read → Run → Reason → Risk before accepting any suggestion.

---

## Exercise 1: First Inline Completion

**Goal:** Experience the accept / reject / cycle workflow for ghost text.

**Instructions:**

1. Create a new file called `exercise1.py` in any folder.
2. Type the following line and pause after the colon:

```python
def calculate_area_of_circle(radius):
```

3. A grey completion should appear. Read it before doing anything.
4. Press `Tab` to accept it.
5. On the next line, start typing `def calculate_perimeter` and pause.
6. Press `Alt+]` to see an alternative suggestion.
7. Press `Esc` to dismiss without accepting.

**What to observe:** Ghost text appears based on context — the function name strongly influences the suggestion. Cycling alternatives shows the model has multiple plausible completions.

---

## Exercise 2: Ask Mode — Explain a Function

**Goal:** Use chat (ask mode) to get an explanation of code you paste in.

**Instructions:**

1. Open the Copilot chat panel (`Ctrl+Alt+I`).
2. Make sure the mode is set to **Ask** (not Edit or Agent).
3. Paste the following and send it with the question below:

```python
import hashlib

def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()
```

**Prompt:** `Explain what this function does and identify any security concerns.`

4. Read the response carefully. Did it identify the MD5 security weakness?
5. Follow up: `What should I use instead, and why?`

**What to observe:** Ask mode gives explanations without modifying files. It can identify security issues if asked explicitly — this is why you must ask.

---

## Exercise 3: Agent Mode — Rename a Variable

**Goal:** Use Agent mode to apply a targeted change across a file.

**Instructions:**

1. Create a file called `exercise3.js` with this content:

```javascript
function processData(d) {
  const result = d.map(d => d * 2);
  return result.filter(d => d > 10);
}
```

2. Open the Copilot chat panel and switch to **Agent** mode.
3. Send this prompt: `Rename the parameter 'd' to 'dataItems' and update all usages in exercise3.js.`
4. Review the proposed diff before accepting. Check: does every `d` that referred to the parameter get renamed? Did it accidentally rename anything else?

**What to observe:** Agent mode proposes a diff — you review and accept or reject it. Always review before accepting.

---

## Exercise 4: Plan Mode — Design Before You Code

**Goal:** Use Plan mode to think through a solution before writing any code.

**Instructions:**

1. Open the Copilot chat panel and switch to **Plan** mode.
2. Send this prompt:

```
I need a function that reads a CSV file, filters rows where the 'status' column equals 'active',
and writes the result to a new CSV file. The function should handle missing files gracefully.
Plan the implementation for Python — do not write code yet.
```

3. Read the plan. Does it mention:
   - How to open and read the file
   - How to handle the `FileNotFoundError`
   - The columns and filtering logic
   - Where to write the output

4. Follow up: `What edge cases should I consider?`
5. Only after reviewing the plan, switch to Agent mode and ask Copilot to implement it.

**What to observe:** Planning before coding catches design gaps before they become bugs. The plan is also context for the implementation step.

---

## Exercise 5: Inline Chat — Quick Fix

**Goal:** Use inline chat (`Ctrl+I`) to fix a problem without leaving the editor.

**Instructions:**

1. Create a file `exercise5.py` with this content:

```python
def divide(a, b)
    return a / b
```

2. Place your cursor on the `def` line.
3. Press `Ctrl+I` to open inline chat.
4. Type: `Fix the syntax error` and press Enter.
5. Review the proposed change — accept it.
6. Place your cursor on the `return` line.
7. Press `Ctrl+I` again and type: `Add a guard against division by zero.`
8. Review and accept.

**What to observe:** Inline chat is scoped to the immediate context. It's faster than opening the panel for small, localized changes.

---

---

## Exercise 6: Request Classification

**Goal:** Apply the included vs. premium distinction to real task descriptions without looking up documentation.

**Instructions:**

For each task below, decide: is this an **included request** (inline completion or Ask with the default model) or a **premium request** (premium model, agent session, or large-context operation)? Write one sentence explaining your reasoning.

| # | Task description | Your classification | Your reasoning |
|---|-----------------|--------------------|------------------|
| 1 | Accept a ghost text completion that suggests a loop body | | |
| 2 | Ask the default model to explain a 20-line Python function | | |
| 3 | Run an agent session to scaffold a new FastAPI project across 5 files | | |
| 4 | Use Ask with GPT-4o to review the architecture of a microservices design | | |
| 5 | Use Agent mode with the default model to rename a variable in one file | | |

Check your answers against [modules/01-foundations/theory.md](../../modules/01-foundations/theory.md) — see the Chat Mode Tool Access Reference table.

---

## Reflection Questions

After completing all six exercises, answer these in your own words (no submission required):

1. Which mode would you use to understand a 200-line function you've never seen before?
2. Which mode would you use to scaffold a new API endpoint across three files?
3. What's the cost difference between Exercise 2 (Ask, default model) and a full Agent session?
4. In Exercise 3 (Agent), why is reviewing the diff before accepting it important?
5. In Exercise 4 (Plan), what would have gone wrong if you had skipped to coding immediately?
6. In Exercise 6, which tasks were the hardest to classify, and why?
