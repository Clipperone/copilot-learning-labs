# Module 01: Foundations

> **Level:** Beginner
> **Estimated time:** 2 hours
> **Prerequisites:** A GitHub account with Copilot Pro+ activated. VS Code installed.
> **Verified against:** GitHub Copilot feature set as of 2026-04

---

## Learning Objectives

By the end of this module, you will be able to:

- [ ] Install and verify GitHub Copilot Pro+ in VS Code
- [ ] Identify the six Copilot interaction modes and choose the right one for a task
- [ ] Configure the essential Copilot settings in VS Code
- [ ] Evaluate AI output critically instead of accepting it blindly

---

## Essential Theory

See [theory.md](./theory.md) for the full reference. The summary below covers what you need to proceed.

### What GitHub Copilot Pro+ Gives You

GitHub Copilot Pro+ extends the base Copilot subscription with:

- Access to premium models (Claude, GPT-4o, o1/o3) in addition to the default model
- Agent mode with multi-step task execution and tool use
- Higher monthly limits for premium requests

> **⚠️ Premium request note:** Inline completions and standard chat use included requests (unlimited on most plans). Switching to a premium model, starting an agent session, or processing a large context window consumes premium requests. In this module, all tasks use standard mode — no premium requests are consumed.

### The Six Copilot Modes

| Mode | Where | Best for |
|------|-------|---------|
| **Inline completion** | Editor, as you type | Short completions, boilerplate, next lines |
| **Chat (ask)** | Chat panel / `Ctrl+Alt+I` | Questions, explanations, short generation |
| **Edit** | Chat panel → Edit mode | Apply changes to one or more open files |
| **Plan** | Chat panel → Plan mode | Design a solution before writing code |
| **Agent** | Chat panel → Agent mode | Multi-step tasks, tool use, file operations |
| **Inline chat** | Editor, `Ctrl+I` | Quick ask or edit in context |

### When to Use Each Mode

| Task type | Recommended mode | Why |
|-----------|-----------------|-----|
| Autocomplete a method signature | Inline completion | Lowest cost, fastest |
| Explain a confusing function | Ask (chat) | Conversational, no file edits |
| Refactor a single file | Edit mode | Targeted, reversible |
| Design a solution before coding | Plan mode | Prevents premature implementation |
| Scaffold a new feature across files | Agent mode | Multi-file, multi-step |
| Quick fix on the current line | Inline chat | No context switch |

### Evaluating AI Output Critically

**Never accept AI output without review.** Copilot can:

- Produce syntactically correct but logically wrong code
- Hallucinate APIs that do not exist
- Miss edge cases and security considerations
- Apply a pattern correctly in the wrong context

Use these four questions every time:

1. **Does it compile / run?** — Verify, don't assume.
2. **Does it do what I asked?** — Read the output, not just the intent.
3. **Does it break anything?** — Check dependencies, side effects, and edge cases.
4. **Do I understand it fully?** — If not, ask Copilot to explain it before committing.

---

## Practical Procedure

### Step 1: Install and authenticate

1. Open VS Code and go to **Extensions** (`Ctrl+Shift+X`).
2. Search for **GitHub Copilot** and install it (the Chat extension installs automatically).
3. Sign in with GitHub when prompted.
4. Verify the Copilot icon appears in the status bar (bottom right).

### Step 2: Verify activation

1. Open any code file and start typing — completions should appear as grey ghost text.
2. Press `Tab` to accept a completion. Press `Esc` to dismiss.
3. Open the chat panel (`Ctrl+Alt+I`) and type: `What is my Copilot plan?`
4. Confirm the response mentions Pro+ or your active plan.

### Step 3: Configure essential settings

Open VS Code settings (`Ctrl+,`) and verify or set the following:

```json
{
  "github.copilot.chat.codeGeneration.useInstructionFiles": true,
  "github.copilot.chat.generateTests.codeLens": true,
  "github.copilot.chat.reviewSelection.enabled": true
}
```

These are already set in this repository's `.vscode/settings.json`.

### Step 4: Try each mode

Complete the quick exercises in [exercises.md](./exercises.md) — one exercise per mode.

---

## Exercises

See [exercises.md](./exercises.md) for full instructions.

**Quick list:**

1. First inline completion — accept and reject a suggestion
2. Ask mode — explain a function you paste in
3. Edit mode — rename a variable throughout a file
4. Plan mode — design a small utility before writing it
5. Inline chat — fix a syntax error using `Ctrl+I`

---

## Common Mistakes

| Mistake | Why it happens | How to fix it |
|---------|----------------|---------------|
| Accepting completions without reading them | Tab is fast and completions look plausible | Always read the ghost text before pressing Tab |
| Using agent mode for a two-line fix | Agent sessions have higher startup cost | For small tasks, use inline chat or Edit mode |
| Ignoring the Copilot status bar icon | Status is easy to miss | Check it when completions stop appearing |
| Switching to a premium model for basic questions | Premium models are better, so "why not?" | Included model handles most questions; use premium for hard reasoning tasks |

---

## Best Practices

- **Do:** Start every significant task by choosing the right mode consciously.
- **Do:** Use inline completion for boilerplate; use chat for anything that benefits from a back-and-forth.
- **Don't:** Skip reading completions because they "look right."
- **Don't:** Use agent mode for tasks that can be done in Edit mode — agent sessions accumulate context and cost.

---

## Token / Premium Request Impact

| Action | Cost level | Notes |
|--------|-----------|-------|
| Inline completion | Low (included) | Never consumes premium requests |
| Standard chat (included model) | Low (included) | Default model on most queries |
| Chat with premium model | Medium | Justified for complex reasoning, architecture questions |
| Agent session | High | Multi-step, multi-tool; use deliberately |

---

## Completion Criteria

You have completed this module when you can:

- [ ] Open VS Code and confirm Copilot is active with a Pro+ plan
- [ ] Demonstrate inline completion, chat, edit, and inline chat modes
- [ ] Explain — in one sentence each — when you would choose each mode
- [ ] Apply the four critical review questions to a piece of AI-generated code

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

- [Lab 01 — Setup and Verify](../../labs/lab-01-setup-and-verify/)

---

## Next Module

→ [Module 02: Configuration](../02-configuration/)
