# Module 03: Token and Premium Request Optimization

> **Level:** Beginner
> **Estimated time:** 1.5 hours
> **Prerequisites:** [Module 01 — Foundations](../01-foundations/), [Module 02 — Configuration](../02-configuration/)
> **Verified against:** GitHub Copilot feature set as of 2026-04

---

## Learning Objectives

By the end of this module, you will be able to:

- [ ] Distinguish between included requests and premium requests, and identify what triggers each
- [ ] Select the appropriate mode and model for any given coding task
- [ ] Write compact prompts that produce complete, focused results without multiple follow-ups
- [ ] Manage context window size to keep sessions efficient
- [ ] Apply a decision framework to make consistent mode/model choices

---

## Essential Theory

See [theory.md](./theory.md) for the full reference. The summary below covers what you need to proceed.

### What Consumes Requests

GitHub Copilot distinguishes between **included requests** (unlimited on most plans) and **premium requests** (monthly quota).

| Action | Request type | Notes |
|--------|-------------|-------|
| Inline completion (ghost text) | Included | Triggered continuously as you type |
| Chat with default model | Included | Ask, Edit, Plan modes |
| Chat with premium model (GPT-4o, Claude, o1) | Premium | Each message to the model consumes quota |
| Agent mode session | Premium | Each tool call + model call counts |
| Long-context operations | Higher premium cost | Files > ~10k tokens cost proportionally more |

> Plan quotas and model availability change. Verify current limits at [github.com/features/copilot](https://github.com/features/copilot).

### The Mode/Model Decision Framework

Match the tool to the task. Escalate only when necessary.

| Task complexity | Recommended mode | Model | Why |
|----------------|-----------------|-------|-----|
| Next line or small snippet | Inline completion | Default | Lowest cost; fastest |
| Quick question or explanation | Ask (chat) | Default | Conversational; no file edits |
| Apply a specific change to one file | Edit | Default | Targeted; default model is sufficient |
| Design a solution before coding | Plan | Default | Planning requires logic, not large-scale tool use |
| Simple single-file scaffold | Edit | Default | Agent overkill for a single file |
| Refactor across multiple files | Agent | Default or GPT-4o | Needs tool use; premium justified |
| Complex debugging across codebase | Agent | Claude or GPT-4o | Deep reasoning; premium justified |
| Security review or code audit | Ask or Agent | o1 or Claude | Reasoning-heavy; premium investment worthwhile |
| Generate documentation | Ask | Default | Language task; default model is fully capable |

**Key rule:** Do not use agent mode for tasks that Edit mode can complete. Do not use premium models for tasks the default model handles correctly.

### Context Window Discipline

The context window is finite. What you include matters:

- **Don't include more files than necessary.** Open only the files relevant to the task.
- **Start a new chat session for unrelated tasks.** Session history accumulates and eventually pushes useful context out.
- **Use `#file:` and `#selection` explicitly.** Don't assume Copilot knows which files are relevant.
- **Summarize long conversations before continuing.** If a session runs long, start a new one with a brief summary of what was established.

### Writing Compact Prompts

A compact prompt:

1. States the **goal** in one sentence
2. Names the **constraints** (language, framework, file to edit)
3. Specifies the **output format** if it matters (function signature, full file, explanation only)

**Verbose prompt (3 follow-ups required):**
> `I have a Python function. Can you help me improve it?`

**Compact prompt (single response):**
> `Refactor the `calculate_discount` function in order_utils.py to accept a `Decimal` instead of `float`. Keep the existing function signature as a deprecated alias that calls the new one. Python 3.12.`

> **⚠️ Premium request note:** Every incomplete prompt that requires a follow-up doubles the premium request cost of that task. Writing a complete prompt on the first try is the highest-value skill in this module.

---

## Practical Procedure

### Step 1: Audit your current mode habits

Review the last 5 tasks you used Copilot for. For each one, ask:

- Which mode did I use?
- Was that the minimum sufficient mode?
- Did I need multiple follow-ups? If so, why?

Record your answers in the Lab 03 worksheet.

### Step 2: Build your personal mode/model cheat sheet

Using the decision table above as a starting point, customize it for your work context. Add rows for the task types you encounter most often. Remove rows that don't apply.

See [Lab 03 — Token Audit Exercise](../../labs/lab-03-token-audit/) for the worksheet template.

### Step 3: Practice compact prompt construction

For your next 5 coding tasks with Copilot, write the prompt before sending it. Check:

1. Does it contain the goal, constraints, and output format?
2. Can you remove any words without losing meaning?
3. Is the target file or selection specified?

Send when you can answer "yes" to all three. Track whether the first response was complete.

### Step 4: Apply context hygiene

- Close all irrelevant tabs before starting a multi-file agent session.
- Start a new chat window for each distinct task.
- If a session exceeds 10 exchanges without resolution, summarize and restart.

---

## Exercises

See [exercises.md](./exercises.md) for full instructions.

**Quick list:**

1. Request type classification — categorize 10 actions as included or premium
2. Mode selection drill — match 8 task descriptions to the optimal mode/model
3. Prompt compaction — rewrite 3 verbose prompts as compact single-turn prompts
4. Context window experiment — compare responses with minimal vs. maximal context
5. Build your cheat sheet — produce a personal mode/model decision reference

---

## Common Mistakes

| Mistake | Why it happens | How to fix it |
|---------|----------------|---------------|
| Using agent mode for single-file edits | "Agent is most powerful, so best" | Agent mode costs 3–10× more than Edit for the same output. Use Edit unless multi-file or multi-step. |
| Switching to premium models by default | Habit from having quota remaining | Default model handles 80% of tasks. Reserve premium models for reasoning-heavy work. |
| Leaving all tabs open during agent sessions | Convenience | Each open file may be included in context. Open only what the task needs. |
| Expecting Copilot to extract requirements from a vague prompt | "It'll figure out what I mean" | Vague prompts produce vague results and required follow-ups. State the goal explicitly. |
| Never starting a new chat session | "The history helps" | Long history causes early context to drop silently. New sessions are cheaper and cleaner. |

---

## Best Practices

- **Do:** Classify your task before reaching for Copilot. Choose mode and model before opening the chat panel.
- **Do:** Write prompts in a text file first, review for completeness, then paste.
- **Do:** Start a new chat session for each distinct coding task.
- **Don't:** Ask "Can you help me with X?" — this wastes one turn on an acknowledgment.
- **Don't:** Include entire files when a selection or a function name would suffice.

---

## Token / Premium Request Impact

| Scenario | Approximate cost | Notes |
|----------|-----------------|-------|
| 5 inline completions | Included | Counted but not against premium quota |
| 10 default-model chat turns | Included | Standard Ask/Edit/Plan |
| 1 agent session (5 tool calls, default model) | Low premium | Depends on context size |
| 1 agent session (5 tool calls, Claude 3.5) | Higher premium | Premium model multiplier applies |
| Entire-codebase context, premium model | High | Avoid unless necessary; scope context first |

---

## Completion Criteria

Before proceeding to Module 04, confirm:

- [ ] I can explain what triggers a premium request vs. an included request
- [ ] I have drafted my personal mode/model cheat sheet (Lab 03)
- [ ] I rewrote at least 3 prompts to be compact and complete on the first turn
- [ ] All exercises in `exercises.md` are complete

Next: [Module 04 — Prompt Engineering for Coding](../04-prompt-engineering/)
