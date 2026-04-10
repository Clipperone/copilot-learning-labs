# Token Audit Worksheet — Filled Example

This is a reference solution. Your answers will differ based on your own task history and work context.

---

## Section A: Interaction Audit

| # | What you asked Copilot to do | Mode used | Model | Request type | First response complete? |
|---|------------------------------|-----------|-------|-------------|------------------------|
| 1 | Write a function to parse a date string | Ask | Default | Included | No — follow-up needed for error handling |
| 2 | Refactor this class to use dataclasses | Edit | GPT-4o | Premium | Yes |
| 3 | Scaffold a new REST endpoint with tests | Agent | Claude 3.5 | Premium | Yes |
| 4 | What does this function do? | Ask | Default | Included | Yes |
| 5 | Fix all lint errors in the project | Agent | Default | Premium (agent) | Partial — missed 2 files |

**Observations from this example:**

- Interaction 1 could have been complete on the first turn with: `Write a function to parse ISO 8601 date strings in Python 3.12. Raise ValueError for unparseable input. Return a datetime object.`
- Interaction 2 used GPT-4o for a task the default model could handle — a habit to change.
- Interaction 5: agent mode missed files because no `#file:` scope was given.

---

## Section B: Mode/Model Decision Cheat Sheet

| Task type | Minimum mode | Preferred model | Justification |
|-----------|-------------|----------------|---------------|
| Accept a code completion suggestion | Inline | Default | Zero cost; automatic |
| Explain what a function does | Ask | Default | Read-only; default is sufficient |
| Rename a variable across one file | Edit | Default | Single-file, targeted |
| Design the architecture for a new feature | Plan | Default | Planning only; no code |
| Regenerate documentation for a module | Ask | Default | Language task; no tool use needed |
| Scaffold a feature across 3+ files | Agent | Default | Needs tool use; default is sufficient |
| Debug a complex multi-file issue | Agent | GPT-4o or Claude | Reasoning-heavy |
| Review code for security vulnerabilities | Ask or Agent | o1 | Deep reasoning required |
| Write a SQL query with 3+ joins | Ask | Default | Query writing is well within default capability |
| Migrate a module from Python 3.10 to 3.12 | Agent | Default | Multi-file changes; default handles syntax well |
| Analyze a 500-line log file for patterns | Ask | Claude 3.5 | Long context justified; not default territory |

---

## Section C: Prompt Audit

| # | Original prompt | What was missing | Compact rewrite |
|---|----------------|------------------|----------------|
| 1 | "Help me with my Python code." | Target file, specific problem, language version | `Review #file:payment.py for correctness. Focus on the calculate_total function. Identify any edge cases not handled. Python 3.12.` |
| 2 | "Add error handling." | Which functions, which error types, raise or return | `Add exception handling to every function in #file:api_client.py that makes HTTP requests. Raise specific exceptions (ConnectionError, TimeoutError, ValueError for bad responses). Never use bare except:.` |
| 3 | "Write tests." | Function name, framework, edge cases | `Write pytest tests for validate_email(email: str) -> bool in validators.py. Cover: valid email, empty string, missing @, missing domain, None input. Do not test third-party email formatting edge cases.` |

---

## Section D: Context Hygiene self-assessment

| Habit | Your rating (1–5) |
|-------|------------------|
| I close irrelevant files before starting an agent session | 2 |
| I use `#file:` or `#selection` to scope my requests explicitly | 3 |
| I start a new chat session for each distinct task | 2 |
| I check which model is selected before starting a session | 1 |
| I write my prompt before opening the chat panel | 2 |

**Two habits I will change:**

1. **Check the model before every session.** I will add a 3-second check of the model selector before typing any prompt. Default first; justify premium before switching.

2. **Start a new session for each task.** I will treat the chat panel like a terminal tab — open a new one per task rather than scrolling up to find where the previous task ended.
