# Token Audit Worksheet

Complete each section in order. This is your personal deliverable for Module 03.

---

## Section A: Interaction Audit

Classify your last 5 Copilot interactions. If you cannot recall 5, use the sample interactions below.

| # | What you asked Copilot to do | Mode used | Model | Request type | First response complete? |
|---|------------------------------|-----------|-------|-------------|------------------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

**Sample interactions (use if needed):**

1. "Write a function to parse a date string" — Ask mode, default model
2. "Refactor this class to use dataclasses" — Agent mode, GPT-4o
3. "Scaffold a new REST endpoint with tests" — Agent mode, Claude 3.5
4. "What does this function do?" — Ask mode, default model
5. "Fix all lint errors in the project" — Agent mode, default model

---

## Section B: Mode/Model Decision Cheat Sheet

Add your personal rows at the bottom. This becomes your reference for every coding session.

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
| _Add your task here_ | | | |
| _Add your task here_ | | | |
| _Add your task here_ | | | |

---

## Section C: Prompt Audit

Pick 3 prompts from your history that required 2+ follow-up messages. If you cannot recall any, use the samples below.

**Sample prompts that needed follow-ups:**

- Sample 1: "Help me with my Python code." → Model asked: which file? what problem? what language version?
- Sample 2: "Add error handling." → Model asked: which functions? which error types? raise or return?
- Sample 3: "Write tests." → Model asked: which function? which framework? which edge cases?

| # | Original prompt | What was missing | Compact rewrite |
|---|----------------|------------------|----------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |

---

## Section D: Context Hygiene self-assessment

Rate each habit from 1 (never) to 5 (always).

| Habit | Your rating (1–5) |
|-------|------------------|
| I close irrelevant files before starting an agent session | |
| I use `#file:` or `#selection` to scope my requests explicitly | |
| I start a new chat session for each distinct task | |
| I check which model is selected before starting a session | |
| I write my prompt before opening the chat panel | |

**Two habits I will change:**

1. _[Habit + one concrete action to change it]_

2. _[Habit + one concrete action to change it]_
