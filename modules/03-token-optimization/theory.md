# Module 03: Token and Premium Request Optimization — Extended Theory

> Reference material to supplement the module README. Read this for deeper context or when the README summary is insufficient.

---

## How Copilot Counts Requests

Copilot's billing model has two tiers:

**Included requests** — do not count against the premium quota:
- Inline completions (ghost text)
- Chat with the default Copilot model (Claude Sonnet, or the plan default)
- Short completions in standard modes

**Premium requests** — count against the monthly quota:
- Any message using a premium model (GPT-4o, Claude 3.5/3.7, o1, o3, Gemini)
- Agent mode sessions (each model call within a session counts)
- Requests that involve very large context windows (cost multiplier applies)

> The exact model-to-cost mapping changes as GitHub updates pricing. Check [docs.github.com/en/copilot](https://docs.github.com/en/copilot) for current quota rates and model tiers.

---

## Model Selection Reference

| Model | Strengths | Best for | Relative cost |
|-------|-----------|---------|---------------|
| Default (included) | General coding, completions | 80% of daily tasks | Included |
| GPT-4o | Speed + reasoning, strong code | Multi-file refactors, API integration | Medium premium |
| Claude 3.5/3.7 Sonnet | Long context, instruction following | Large codebase analysis, documentation | Medium premium |
| o1 / o3 | Deep multi-step reasoning | Algorithm design, security audit, complex debugging | High premium |
| Gemini | Multimodal, long context | Large-scale analysis, document-heavy tasks | Medium premium |

**Default first, premium when justified.** If the default model gives you 90% of the answer and one targeted follow-up closes the gap, you spent zero premium requests.

---

## Context Window Mechanics

The context window determines what the model "sees" in a given request. Its size varies by model:

| Model | Approximate context window |
|-------|--------------------------|
| Default Copilot model | ~10k–16k tokens |
| GPT-4o | ~128k tokens |
| Claude 3.5/3.7 | ~200k tokens |
| o1/o3 | ~128k tokens |

**One token ≈ 4 characters** of code or text.

### What fills the context window

1. System prompt (Copilot instructions, tool descriptions) — fixed overhead
2. `.github/copilot-instructions.md` content — added automatically if enabled
3. Open editor files referenced by VS Code
4. Chat history (all previous turns in the session)
5. `#file:` and `#selection` references you added explicitly
6. Tool outputs (in agent mode: terminal results, file reads, search results)

When the window fills:
- Older parts of the conversation drop silently
- Referenced files may be truncated
- The model loses access to context you thought it had

### Signals that you are approaching context limits

- Responses become vaguer or contradict earlier statements
- The model "forgets" constraints you defined earlier in the session
- Agent mode produces repeated or redundant tool calls

Remedy: start a new session with a compressed summary of what was established.

---

## Prompt Architecture

A complete prompt has three components. Missing any one forces a follow-up:

```
ROLE (optional)      You are a Python backend engineer.
TASK (required)      Refactor the `calculate_tax` function in billing.py
CONSTRAINTS          to return a `Decimal`, not a `float`. Preserve the
(required if any)    existing test suite in tests/test_billing.py.
OUTPUT FORMAT        Return only the modified function, not the full file.
(if non-default)
```

**Role** is optional when the context already establishes expertise (e.g., you are in a Python project with a configured instruction file).

**Task** must be one clear action: refactor, generate, explain, review, fix.

**Constraints** define what must not change, which framework/version, security requirements.

**Output format** matters when the default (full code) is not what you need (explanation only, diff format, abbreviated).

### The "one noun, one verb" test

Read your prompt and identify the primary verb and the primary noun. If there are two verbs or two primary nouns, split the task into two prompts.

**Two verbs — split it:**
> `Refactor this function to use `Decimal` AND add docstrings.`
→ Two prompts: one refactor, one for documentation.

**Single-task prompt:**
> `Refactor the `calculate_tax` function to use `Decimal` instead of `float`. Do not change the function signature.`

---

## Session Management Strategies

### When to start a new session

| Signal | Action |
|--------|--------|
| Moving to a completely new feature or file | New session |
| The model starts contradicting earlier answers | New session with summary |
| >10 exchanges without resolution | New session with focused rephrasing |
| Switching from debugging to documentation | New session |

### How to summarize before restarting

Ask the current session:
> `Summarize the decisions we've made so far in 5 bullet points. I'll start a new session with this summary.`

Paste the bullet points as the first message in the new session.

---

## Cost Estimation Heuristics

Use these to calibrate your daily quota usage:

| Scenario | Estimated premium requests |
|----------|--------------------------|
| 30 default-model chat turns | 0 |
| 5 GPT-4o turns (short context) | ~5 |
| 1 agent session: 10 tool calls + 5 model calls, default model | ~5–10 |
| 1 agent session: 10 tool calls + 5 model calls, GPT-4o | ~15–25 |
| Full codebase context (>50k tokens), premium model | High — scope first |

These are estimates. Check your actual usage at [github.com/settings/copilot](https://github.com/settings/copilot).

---

## Official Resources

- [GitHub Copilot subscription plans and quotas](https://docs.github.com/en/copilot/about-github-copilot/subscription-plans-for-github-copilot)
- [Premium requests documentation](https://docs.github.com/en/copilot/concepts/billing/copilot-requests)
- [GitHub Copilot model selection (VS Code)](https://code.visualstudio.com/docs/copilot/copilot-chat#_use-a-specific-chat-model)
- [Understanding context in Copilot](https://code.visualstudio.com/docs/copilot/copilot-chat#_use-chat-variables)
