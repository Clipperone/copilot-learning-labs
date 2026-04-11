# Module 04 — Theory Reference

> **Word limit discipline:** Prose sections are capped at 500 words total. Tables and code blocks are excluded from this count.

This page extends the README with three topics not covered there: the migration scenario, prompt chaining between scenarios, and advanced parameterization for shared prompt libraries.

---

## The 8th Scenario — API Migration

Migration prompts fail more often than any other type. The reason is scope: a migration spans multiple files, multiple call sites, and multiple failure modes. A single prompt cannot handle all of that reliably.

**Break migration into three sequential prompts:**

| Prompt | Task | Output |
|--------|------|--------|
| 1 | Identify all call sites that use `[OLD API]` in `[FILE]` | A numbered list of line references |
| 2 | For a single call site at `[FILE:LINE]`, rewrite it to use `[NEW API]` | The updated line(s) only |
| 3 | Confirm that the rewritten call preserves `[SPECIFIC BEHAVIOR]` | A yes/no with justification |

**Pattern for Prompt 1:**
```
Task: List every call site that uses [OLD API METHOD] in [FILE].
Constraints: Include only direct calls — exclude comments and import statements.
Output: A numbered list, one per line: line number · call expression.
```

**Key constraints for migration prompts:**
- State the source API version and the target API version explicitly.
- Specify what must be preserved: return type, error handling contract, side effects.
- Ask for breaking changes before asking for the rewrite.

---

## Prompt Chaining

Prompt chaining is the practice of using the output of one prompt as the context for the next. It is mandatory for multi-step tasks and optional for complex single-step tasks.

**When to chain:**
- The task has more than one distinct action.
- The second action depends on the result of the first.
- You need to verify an intermediate result before committing to the next step.

**Chaining rules:**

1. Each prompt in a chain must be completable on its own. If Prompt 2 is meaningless without Prompt 1's output, that output must be pasted into Prompt 2's context.
2. Never ask for diagnosis and fix in the same prompt. Diagnosis first, fix second.
3. End each prompt with a confirmation gate: "Reply only with the [DELIVERABLE]. Do not proceed to the next step."

**Example chain — debug and fix:**
```
# Prompt 1 — diagnose
Task: Diagnose why merge_sorted returns an incorrect result when one list is empty.
Constraints: Diagnose only. Do not propose a fix.
Output: Numbered list of candidate causes, ordered by likelihood.

# Prompt 2 — fix (after confirming diagnosis)
Context: The root cause is [PASTE CONFIRMED CAUSE FROM PROMPT 1].
Task: Fix `merge_sorted` to handle the empty-list case correctly.
Constraints: Change only the lines that address the root cause. Do not rename variables.
Output: The corrected function body only.
```

---

## Advanced Parameterization

A prompt template is ready for a shared library when every value that varies between uses is a named `[PLACEHOLDER]`. Generic placeholders like `[CODE]` or `[FUNCTION]` are not sufficient — they do not communicate what value is expected.

**Naming rules for placeholders:**
- Use a noun that names the category of value: `[FUNCTION_NAME]`, `[TARGET_FRAMEWORK]`, `[OWASP_CATEGORY]`.
- Use `_` between words. All uppercase.
- Include the unit where it matters: `[MAX_LINES]`, `[PYTHON_VERSION]`.

**Template validation checklist:**
- [ ] Every input that changes between uses has a `[PLACEHOLDER]`.
- [ ] The output format line names the exact structure (numbered list, code block, table).
- [ ] The constraints line states at least one thing the output must NOT contain.
- [ ] The template produces correct output when tested with at least two different sets of values.

**Example of under-parameterized vs well-parameterized:**

Under-parameterized:
```
Write a test for the validation function using pytest.
```

Well-parameterized:
```
Task: Write pytest tests for `[FUNCTION_NAME]` in `[FILE_PATH]`.
Constraints: Cover these cases: [EDGE_CASE_LIST]. One test function per case. Use bare `assert` — no TestCase.
Output: Test file content only — starting from the import line.
```

---

## Navigation

← [README.md](./README.md) — Module overview and scenario reference

→ [exercises.md](./exercises.md) — Apply each concept with a short exercise
