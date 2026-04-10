# Module 01: Foundations — Exercises

Complete these exercises in order. Each one targets a specific Copilot mode.

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

## Exercise 3: Edit Mode — Rename a Variable

**Goal:** Use Edit mode to apply a targeted change across a file.

**Instructions:**

1. Create a file called `exercise3.js` with this content:

```javascript
function processData(d) {
  const result = d.map(d => d * 2);
  return result.filter(d => d > 10);
}
```

2. Open the Copilot chat panel and switch to **Edit** mode.
3. Add `exercise3.js` to the working set if it is not already there.
4. Send this prompt: `Rename the parameter 'd' to 'dataItems' and update all usages.`
5. Review the proposed diff before accepting. Check: does every `d` that referred to the parameter get renamed? Did it accidentally rename anything else?

**What to observe:** Edit mode proposes a diff — you review and accept or reject it. Always review before accepting.

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
5. Only after reviewing the plan, switch to Edit mode and ask Copilot to implement it.

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

## Reflection Questions

After completing all five exercises, answer these in your own words (no submission required — this is for your own consolidation):

1. Which mode would you use to understand a 200-line function you've never seen before?
2. Which mode would you use to scaffold a new API endpoint across three files?
3. What's the difference in cost between Exercise 2 (Ask) and a full Agent session?
4. When in Exercise 3 (Edit), why is reviewing the diff before accepting it important?
5. In Exercise 4 (Plan), what would have gone wrong if you had skipped to coding immediately?
