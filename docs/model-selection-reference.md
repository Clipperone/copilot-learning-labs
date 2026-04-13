# Model Selection Reference

> Centralized model guidance for all modules. Individual modules reference this file
> rather than embedding model names that change with each Copilot update.
> **Verified:** 2026-04

## Current Model Tiers

| Tier | Examples (as of verified date) | Strengths | Relative cost |
|------|-------------------------------|-----------|---------------|
| **Included (default)** | Copilot default model | General coding, completions, 80% of daily tasks | Included |
| **Premium — balanced** | GPT-4o, Claude Sonnet, Gemini | Speed + reasoning, long context, multi-file refactors | Medium premium |
| **Premium — reasoning** | o1, o3-mini | Deep multi-step reasoning, algorithm design, security audit | High premium |

> Model names and tier assignments change as GitHub updates the Copilot model roster.
> Verify at [github.com/features/copilot](https://github.com/features/copilot).

## When to Escalate

Use the **included model** by default. Escalate to premium only when:

1. The task requires **multi-step causal reasoning** (security exploit paths, complex debugging, system design).
2. The default model **demonstrably fails** — you tried it and the output was incorrect or incomplete.
3. The task involves **large-context analysis** where a longer context window materially improves output.

## Role-Specific Guidance

| Role / Scenario | Recommended tier | Reasoning |
|----------------|-----------------|-----------|
| Inline completion | Included | Fastest; no reasoning needed |
| Ask — explanation, docs | Included | Language generation |
| Plan — design | Included | Logic, not depth |
| Agent — routine implementation | Included | Sufficient for most code generation |
| Agent — complex refactor | Premium balanced | Multi-file reasoning |
| Security review (OWASP) | Premium reasoning | Exploit-path analysis |
| Solution Architect | Premium balanced | System design depth |
| Performance Optimizer | Premium balanced | Profiling interpretation |
| Debugging — async/concurrency | Premium balanced | Causal chain reasoning |
