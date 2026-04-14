# Module 04: Prompt Engineering for Coding — Theory Reference

> Extended reference for [README.md](./README.md). Read the module overview first.
> Prose sections are capped at 500 words; tables and code blocks are excluded from that limit.

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

## Prompt Files (`.prompt.md`)

A prompt file is the productized form of a parameterized template. Instead of pasting a Markdown prompt and filling placeholders by hand, you save the prompt as a `.prompt.md` file and invoke it directly in chat with `/`.

### Where prompt files live

| Scope | Location | When to use |
|-------|----------|-------------|
| Workspace | `.github/prompts/*.prompt.md` (or `.prompts/`) | Repo-wide team prompts, version-controlled |
| User | VS Code user prompts directory | Personal prompts that follow you across projects |

### Anatomy

```markdown
---
mode: agent
model: claude-sonnet
tools: ['codebase', 'editFiles']
description: Extract a long function into smaller helpers
---

Task: Refactor `${input:targetFunction}` in `${file}` by extracting helpers.
Constraints:
  - Each helper has one responsibility and ≤ 20 lines.
  - Public signature of `${input:targetFunction}` does not change.
  - Existing tests must still pass.
Output: The full updated file content only.
```

**Frontmatter fields:**

- `mode` — `ask`, `agent`, or omit to inherit current mode.
- `model` — pin a specific model; omit to use the chat's current model.
- `tools` — list of tool names (Agent mode only) the prompt may use.
- `description` — shown in the `/` picker.

**Body substitutions:**

- `${input:variableName}` — prompts the user when invoked.
- `${input:variableName:default}` — with a default value.
- `${selection}` — current editor selection.
- `${file}` — current file path.
- `${workspaceFolder}` — repo root.

### Decision table — instructions vs. prompt files vs. agents

| Mechanism | Activation | Best for |
|-----------|-----------|---------|
| Instruction file (Module 05) | Always-on for matching scope | Conventions, style, "always do X" |
| Prompt file (`.prompt.md`) | On-demand via `/` | Reusable actions: extract function, write tests, security audit |
| Custom agent (Module 06 + 08) | On-demand via `@` | Scoped role with bounded tool permissions |

**Quick rule:** If the rule should fire **every** turn → instruction file. If it is a **named action** I run sometimes → prompt file. If it is a **bounded role with restricted tools** → agent.

### Conventions

- **Naming:** `verb-object.prompt.md` — `extract-function.prompt.md`, `audit-security.prompt.md`.
- **One objective per file.** If you find yourself adding `OR` to the description, split it.
- **Version with the repo.** Treat prompts like code — review them in PRs, change `Verified` dates when they change.
- **Link upstream.** When a prompt relies on a path-specific instruction file, mention it in the description.

### Anti-patterns

- **Prompt files for one-off tasks.** If you will run it once, just type the prompt — no file needed.
- **Secrets in frontmatter.** Frontmatter is committed. No tokens, no internal hostnames.
- **Body bloat.** A prompt body over ~150 lines is doing too much — split into two prompts and chain them.
- **Inheriting a model with no rationale.** If a prompt pins `model: o3`, the description must say *why* — otherwise the next contributor will not know whether to keep or remove the pin.
- **Prompt files as documentation.** A `.prompt.md` file is something Copilot runs. If you want humans to read it for guidance, that belongs in `prompts/README.md` or in `instructions/`.

### Migrating an existing Markdown prompt to `.prompt.md`

The course already contains a Markdown prompt library at [prompts/](../../prompts/). Each file there can be promoted to a runnable `.prompt.md`:

1. Copy the prompt file to `.github/prompts/[name].prompt.md`.
2. Convert each `[PLACEHOLDER]` to `${input:placeholderName}`.
3. Add frontmatter with `mode`, `description`, and (if needed) `model` and `tools`.
4. Run it twice with different inputs to verify variables substitute correctly.
5. Add a one-line cross-reference back to the source Markdown so contributors know they are paired.

> Verify availability and frontmatter schema against the [VS Code prompt files docs](https://code.visualstudio.com/docs/copilot/customization/prompt-files) — both the format and the supported tools list evolve.

---

## Official Resources

- [GitHub Copilot documentation](https://docs.github.com/en/copilot)
- [GitHub Copilot Chat in your IDE](https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-ide)
- [Prompt engineering for Copilot Chat (VS Code)](https://code.visualstudio.com/docs/copilot/copilot-chat#_prompt-engineering-with-copilot-chat)
- [GitHub Copilot model selection (VS Code)](https://code.visualstudio.com/docs/copilot/copilot-chat#_use-a-specific-chat-model)

---

← [Back to Module 04 README](./README.md)
