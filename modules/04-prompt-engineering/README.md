# Module 04: Prompt Engineering for Coding

> **Level:** Intermediate
> **Estimated time:** ~2.5 hours (module theory ~1.5 hrs · lab ~50 min)
> **Prerequisite:** [Level 1 complete](../../SYLLABUS.md#level-1--beginner) (Modules 01–03) — Module 03 in particular. This module extends compact prompting with full structured scenario coverage.
> **Verified:** 2026-04

> ⚠️ **Premium request note:** Most exercises in this module use the default model. Security review exercises recommend o1 or Claude — those are marked at the point of use.

---

## Learning Objectives

By the end of this module you will be able to:

1. Decompose any coding task into the 4-component prompt structure: task, role, constraints, output format.
2. Apply the correct prompt pattern for each of 7 coding scenarios without looking them up.
3. Identify 5 prompt anti-patterns on sight; diagnose and rewrite at least 3 in the lab.
4. Write a parameterized, reusable prompt template committable to a shared prompt library.
5. Scope prompts for security review and migration without generating vague or hallucinated output.
6. Estimate whether a given prompt scenario warrants a premium model.

---

## Why This Module Exists

Module 03 taught you to keep prompts small and choose the right mode. This module teaches you what to put inside those prompts.

A structural prompt is not a better-worded request — it is a different type of input. When you give Copilot a **specific task** with **explicit constraints** and a **stated output format**, you get deterministic, reviewable output. When you give it an open-ended request, you get generic output that requires iterative correction. Iteration is the enemy of efficient context usage.

---

## Prompt Architecture

Every effective Copilot prompt contains between two and four components:

| Component | Required? | Purpose |
|-----------|-----------|---------|
| **Task** | Always | A single verb + a single noun: what to produce |
| **Role** | Optional | The expert perspective Copilot should take |
| **Constraints** | Always when any apply | What must be true of the output |
| **Output format** | Always when non-default | How the result should be structured |

**Completeness test:** Read your task line aloud. Does it contain exactly one verb and one noun? If two actions are in the sentence, split the prompt.

### Example: before and after

**Before (incomplete):**
```
Help me with this function — it seems broken and also the tests aren't great.
```

**After (structured):**
```
Role: Act as a Python debugging specialist.
Task: Diagnose why `merge_sorted(a, b)` returns an incorrect result when one list is empty.
Constraints: Do not propose a fix yet — provide the diagnosis first.
Output: A numbered list of candidate causes, each with one supporting observation from the code.
```

---

## The 7 Coding Scenarios

### Scenario 1 — Code Generation

**Key discipline:** Name the function, name its parameter types and return type, state the constraints, and ask for only the function body.

**Pattern:**
```
Task: Write a Python function `[NAME]([PARAMS])` that [ONE-SENTENCE DESCRIPTION].
Constraints: [TYPE CONSTRAINTS] · [EDGE CASE HANDLING] · [WHAT TO OMIT]
Output: Function body only — no surrounding module, no usage example.
```

**What goes wrong without it:** Copilot generates a plausible stub with wrong assumptions about parameter types or missing edge case handling.

---

### Scenario 2 — Refactoring

**Key discipline:** State what changes. State what must not change. Specify the file and selection.

**Pattern:**
```
Task: Refactor `[FUNCTION NAME]` in [FILE] to extract [SPECIFIC CONCERN] into a separate function.
Constraints: Do not change the public interface. Do not change behavior. Keep existing tests passing.
Output: The refactored function and the extracted helper — no other changes.
```

**What goes wrong without it:** Copilot renames variables, adds imports, or modifies the calling code — all outside the stated scope.

---

### Scenario 3 — Debugging

**Key discipline:** Describe symptoms, expected behavior, and actual behavior. Ask for diagnosis before asking for a fix.

**Pattern:**
```
Task: Diagnose why [FUNCTION NAME] produces [ACTUAL OUTPUT] when the expected output is [EXPECTED OUTPUT].
Context: [PASTE FUNCTION] [PASTE FAILING CALL]
Constraints: Diagnose only — do not suggest a fix in this message.
Output: A numbered list of candidate causes ordered by likelihood, each with one supporting observation.
```

**What goes wrong without it:** Copilot proposes a fix before identifying the root cause, fixing a symptom rather than the problem.

---

### Scenario 4 — Testing

**Key discipline:** Name the function under test. List the edge cases explicitly. Specify the framework and assertion style.

**Pattern:**
```
Task: Write pytest tests for `[FUNCTION NAME]`.
Constraints: Cover these cases: [LIST EACH CASE]. Use `assert` statements — no `unittest.TestCase`. Each test in its own function.
Output: Test file content only — no CLI instructions.
```

**What goes wrong without it:** Copilot writes the happy path only. Boundary cases, null input, and error conditions are skipped.

---

### Scenario 5 — Documentation

**Key discipline:** State the audience, format, and depth.

**Pattern:**
```
Task: Write a docstring for `[FUNCTION NAME]`.
Constraints: Audience is a Python developer who will call this function, not maintain it. Use Google-style format. Include Args, Returns, Raises — no usage example.
Output: The docstring only, inside triple quotes.
```

**What goes wrong without it:** Copilot writes a one-line description that restates the function name. Or adds a verbose usage example the caller doesn't need.

---

### Scenario 6 — Code Review

**Key discipline:** Scope the review to a specific concern. State what is out of scope.

**Pattern:**
```
Task: Review `[FUNCTION NAME]` for [SCOPE: logic errors | OWASP A01 | style | test coverage].
Constraints: Focus only on [SCOPE]. Do not comment on naming, formatting, or anything outside [SCOPE].
Output: A numbered list — each item: finding · severity · suggested fix.
```

**What goes wrong without it:** Copilot produces a wall of vague suggestions across every concern at once. Nothing is actionable.

---

### Scenario 7 — Security Review

**Key discipline:** Anchor to an OWASP category. Give the language, framework, and version. Ask for the exploit path before the fix.

**Pattern:**
```
Role: Act as a security engineer specializing in [LANGUAGE/FRAMEWORK].
Task: Review `[FUNCTION NAME]` for vulnerabilities matching [OWASP CATEGORY, e.g., A02:2021 Cryptographic Failures].
Context: [LANGUAGE] [VERSION] · [FRAMEWORK] [VERSION]
Constraints: Describe the exploit path before proposing any fix. Limit scope to [OWASP CATEGORY].
Output: Finding · exploit path · recommended fix · one-line code example of the fix.
```

**What goes wrong without it:** Copilot generates a broad list of generic security advice not tied to the actual code or framework version.

---

## Prompt Anti-patterns

| Anti-pattern | Why it fails | Rewrite rule |
|---|---|---|
| **Vague target** — "Improve this function" | Copilot must guess the intent | Name the specific change: "Extract the rate lookup into a separate function" |
| **Double task** — "Fix the bug and add tests" | Two tasks compete for the same output | Split: diagnose → fix → then prompt for tests separately |
| **Context dump** — Paste 300 lines with no question | Copilot summarises instead of acts | Scope to the specific function; state the exact question |
| **Missing output format** — "Explain how to add error handling" | Copilot writes prose when you want code | Add "Output: code only" or "Output: numbered list" |
| **Premature fix** — "Fix the off-by-one error in merge_sorted" | Assumes the diagnosis is correct | Ask for diagnosis first; confirm it; then ask for the fix |

---

## Reusable Template Design

A prompt is reusable when it contains `[UPPERCASE]` placeholders for every value that changes between uses, and the surrounding text is stable.

**Signs a prompt is ready to commit to the library:**
- You have used it successfully at least twice.
- All variable parts are marked with `[PLACEHOLDER]` names.
- The output format is explicit.
- You have noted one common failure and how to fix it.

Use [templates/prompt-template.md](../../templates/prompt-template.md) as the standard format. See [prompts/](../../prompts/) for working examples.

---

## Premium Model Decision — Scenario by Scenario

| Scenario | Recommended model | Reasoning |
|---|---|---|
| Code generation | Default | Syntax tasks — no multi-step reasoning needed |
| Refactoring | Default | Structural, not semantic |
| Documentation | Default | Language generation, well within default capability |
| Code review — style + logic | Default | Pattern matching |
| Testing | Default | Mechanical coverage expansion |
| Debugging — simple logic | Default | Sufficient for most bugs |
| Debugging — async / concurrency | GPT-4o or Claude | Multi-step causal reasoning needed |
| Security review (OWASP scope) | o1 or Claude | Exploit-path reasoning requires depth |
| Migration, large codebase | Default or GPT-4o | Depends on complexity |

**Rule of thumb:** Only escalate to a premium model when the task requires multi-step causal reasoning that the default model demonstrably gets wrong. Always try default first.

---

## Common Mistakes

| Mistake | Root cause | Fix |
|---|---|---|
| "Reusing one long chat for unrelated tasks" | Assumes more history always helps | Start a new session per task and paste a 3-5 bullet summary if needed |
| Reviewing too much code at once | Equates larger scope with better quality | Review one function or one concern per prompt |
| Skipping the expected vs actual behavior in debugging prompts | Assumes the error message is enough | Always provide expected output, actual output, and one failing input |
| Escalating to premium models before trying default | Habit or fear of weak output | Try default first, then escalate only if reasoning quality is insufficient |
| Accepting first output without validation | Treats model output as final | Run tests or check acceptance criteria before adopting changes |

---

## Exercises

Hands-on exercises are in [exercises.md](./exercises.md).

> See also: [templates/prompt-template.md](../../templates/prompt-template.md) — Prompt authoring standard · [prompts/](../../prompts/) — Working prompt library by category.

---

## Completion Criteria

You have completed this module when you can:

- [ ] Decompose a coding task into the 4-component prompt structure without referencing the module.
- [ ] Apply the correct prompt pattern for at least 5 of the 7 coding scenarios.
- [ ] Identify and rewrite 3 prompt anti-patterns.
- [ ] Write a parameterized prompt template that passes the template validation checklist.
- [ ] Scope a security review prompt anchored to a specific OWASP category with exploit-path-first output.
- [ ] Justify whether a given scenario warrants a premium model.

See [checklist.md](./checklist.md) for the full self-assessment.

---

## Files in This Module

| File | Purpose |
|------|---------|
| `README.md` | Module overview (this file) |
| `theory.md` | Extended theory and reference material |
| `exercises.md` | All exercises with full instructions |
| `checklist.md` | Completion checklist and self-assessment |

> See also: [theory.md](./theory.md) — Migration scenario, prompt chaining, and advanced parameterization reference.

---

## Paired Lab

| Lab | Focus | Time |
|-----|-------|------|
| [Lab 04 — Prompt Engineering Workshop](../../labs/lab-04-prompt-engineering/) | Structured prompts across all 7 scenarios, anti-pattern diagnosis, prompt library | 50 min |

---

## Next Module

→ [Module 05: Persistent Custom Instructions](../05-custom-instructions/)
