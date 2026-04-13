# Module 03: Token and Premium Request Optimization

> **Level:** Beginner
> **Estimated time:** 1.5 hours
> **Prerequisites:** [Module 01 — Foundations](../01-foundations/), [Module 02 — Configuration](../02-configuration/)
> **Verified:** 2026-04

> ⚠️ **Premium request note:** Mode and model choice is the most direct lever on your premium request budget. Escalating to agent mode or premium models for tasks the default model handles is the single largest source of unnecessary quota spend.

---

## Learning Objectives

By the end of this module, you will be able to:

- [ ] Distinguish between included requests and premium requests, and identify what triggers each
- [ ] Select the appropriate mode and model for any given coding task
- [ ] Write compact prompts that produce complete, focused results without multiple follow-ups
- [ ] Manage context window size to keep sessions efficient
- [ ] Estimate the approximate premium request cost of a workflow before starting

---

## Essential Theory

See [theory.md](./theory.md) for the full reference.

### What Consumes Requests

GitHub Copilot distinguishes between **included requests** (unlimited on most plans) and **premium requests** (monthly quota).

| Action | Request type | Notes |
|--------|-------------|-------|
| Inline completion (ghost text) | Included | Triggered continuously as you type |
| Chat with default model | Included | Ask, Plan modes |
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
| Apply a specific change to one file | Agent | Default | Targeted; default model is sufficient |
| Design a solution before coding | Plan | Default | Planning requires logic, not large-scale tool use |
| New file from scratch (single file) | Agent | Default | File creation does not require premium models |
| Refactor across multiple files | Agent | Default or GPT-4o | Needs tool use; premium justified |
| Complex debugging across codebase | Agent | Claude or GPT-4o | Deep reasoning; premium justified |
| Security review or code audit | Ask or Agent | o1 or Claude | Reasoning-heavy; premium investment worthwhile |
| Generate documentation | Ask | Default | Language task; default model is fully capable |

**Key rule:** Do not use premium models for tasks the default model handles correctly. Use inline chat (`Ctrl+I`) for quick, localized changes that do not need a full Agent session.

The decision table in [Lab 03, Section B](../../labs/lab-03-token-audit/) uses this framework as its starting template. You will add rows for your own task types during the lab.

> For the latest model tier assignments, see [Model Selection Reference](../../docs/model-selection-reference.md).

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

> **Preview:** Module 04 formalizes this as the **4-component prompt structure** — task, role, constraints, output format — with scenario-specific patterns. The compact prompt you practise here is the foundation that Module 04 extends.

**Verbose prompt (3 follow-ups required):**
> I have a Python function. Can you help me improve it?

**Compact prompt (single response):**
> Refactor the `calculate_discount` function in `order_utils.py` to accept a `Decimal` instead of `float`. Keep the existing function signature as a deprecated alias that calls the new one. Python 3.12.

Apply these skills in [Lab 03: Token Audit Exercise](../../labs/lab-03-token-audit/).

---

## Exercises

See [exercises.md](./exercises.md) for full instructions. Exercises use curated examples with reference answers. Complete [Lab 03](../../labs/lab-03-token-audit/) before Exercise 5 — the lab applies the same skills to your own Copilot history, and Exercise 5 builds on the lab worksheet.

1. Request type classification — categorize 10 actions as included or premium
2. Mode selection drill — match 8 task descriptions to the optimal mode/model
3. Prompt compaction — rewrite 3 verbose prompts as compact single-turn prompts
4. Context window experiment — compare responses with minimal vs. maximal context
5. Build your cheat sheet — produce a personal mode/model decision reference

---

## Common Mistakes

| Mistake | Root cause | Fix |
|---------|------------|-----|
| Using Agent mode for single-file edits | "Agent is seen as the default for every change" | For localized changes, use Inline chat. Use Agent only for multi-file or multi-step work. |
| Switching to premium models by default | Habit from having quota remaining | Default model handles most tasks. Reserve premium models for reasoning-heavy work. |
| Leaving all tabs open during agent sessions | Convenience | Open only files relevant to the task to reduce context noise and cost. |
| Expecting Copilot to extract requirements from a vague prompt | "It'll figure out what I mean" | State goal, constraints, and expected output format explicitly. |
| Never starting a new chat session | "The history helps" | Long history drops early context. Start a new focused session when topic changes. |

---

## Token and Premium Request Impact

This section helps you estimate how everyday Copilot usage affects your monthly quota.
The examples show relative cost levels, not exact billing values, so you can choose the right mode and model quickly.
Use the default model for routine tasks, reserve premium models for complex reasoning, and keep context focused on only the files you need.

Use these scenarios to calibrate your daily quota use. See [theory.md](./theory.md) for detailed cost heuristics and model-specific estimates.


| Scenario | Approximate cost | Notes |
|----------|-----------------|-------|
| 5 inline completions | Included | Counted but not against premium quota |
| 10 default-model chat turns | Included | Standard Ask/Plan |
| 1 agent session (5 tool calls, default model) | Low premium | Depends on context size |
| 1 agent session (5 tool calls, Claude Sonnet) | Higher premium | Premium model multiplier applies |
| Entire-codebase context, premium model | High | Avoid unless necessary; scope context first |

---

## Completion Criteria

You have completed this module when you can:

- [ ] Explain what triggers a premium request and what does not
- [ ] Apply the mode/model decision framework to any task in under 5 seconds
- [ ] Write a compact prompt that contains goal, constraints, and output format
- [ ] Manage context window size by closing irrelevant files and starting new sessions appropriately
- [ ] Estimate the approximate premium request cost of a given workflow
- [ ] Produce a personal mode/model cheat sheet you will use in practice

See [checklist.md](./checklist.md) for the full self-assessment.

---

## Files in This Module

| File | Purpose |
|------|---------|
| `README.md` | Module overview (this file) |
| `theory.md` | Extended theory and reference material |
| `exercises.md` | All exercises with full instructions |
| `checklist.md` | Completion checklist and self-assessment |

---

## Related Labs

| Lab | Focus | Time |
|-----|-------|------|
| [Lab 03 — Token Audit Exercise](../../labs/lab-03-token-audit/) | Interaction audit, mode/model cheat sheet, prompt compaction, context hygiene | 30–45 min |

See [labs/README.md](../../labs/README.md) for the full lab index.

---

## Next Module

→ [Module 04: Prompt Engineering for Coding](../04-prompt-engineering/)
