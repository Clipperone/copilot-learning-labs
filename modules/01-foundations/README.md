# Module 01: Foundations

> **Level:** Beginner
> **Estimated time:** 2 hours
> **Prerequisites:** A GitHub account with Copilot Pro+ activated. VS Code installed.
> **Verified:** 2026-04

> ⚠️ **Premium request note:** All tasks in this module use the included model and standard modes. No premium requests are consumed.

---

## Learning Objectives

By the end of this module, you will be able to:

- [ ] Describe what GitHub Copilot Pro+ is, how it differs from other plans, and what premium requests are
- [ ] Install, authenticate, and verify Copilot Pro+ in VS Code
- [ ] Identify the six Copilot interaction modes and choose the right one for each task type
- [ ] Apply the **Read → Run → Reason → Risk** critical review workflow to every AI suggestion
- [ ] Recognize the five most common AI output failure modes
- [ ] Apply the three first-session productivity habits
- [ ] Distinguish included requests from premium requests and make cost-aware mode choices

---

## Essential Theory

See [theory.md](./theory.md) for the full reference.

### What GitHub Copilot Pro+ Is

Copilot is a pair programmer that runs inside VS Code. It sends a **prompt** — your message plus surrounding file context — to a language model and returns a completion. The model does not have access to your file system beyond what VS Code passes it. It does not remember previous sessions.

Copilot Pro+ extends the base subscription with:

- Access to premium models (Claude, GPT-4o, o1, o3) in addition to the default model
- **Agent mode** — multi-step task execution with tool use (read files, run terminal commands, search)
- A monthly allotment of **premium requests**

Framing for new users: Copilot is a fast, knowledgeable, and confidently wrong pair programmer. Your job is to know when it's wrong.

### Install and Authenticate

1. Open VS Code → **Extensions** (`Ctrl+Shift+X`)
2. Search for and install **GitHub Copilot** (the Chat extension installs automatically)
3. Sign in with GitHub when prompted
4. Verify the Copilot icon appears in the status bar (bottom right)

If the icon shows a warning:

| Symptom | Likely cause | Fix |
|---------|--------------|----- |
| "No subscription" warning | Account lacks Copilot access | Check [github.com/settings/copilot](https://github.com/settings/copilot) |
| Completions never appear | Extension disabled | Enable in Extensions panel |
| Signed in as wrong account | Multiple GitHub accounts | **Accounts** icon → sign out → re-sign in |
| Completions appear then stop | Firewall / proxy blocking | Contact IT; see VS Code proxy docs |

### The Six Interaction Modes

| Mode | Trigger | Best for |
| **Inline completion** | Editor, as you type | Short completions, boilerplate, next lines |
| **Chat (ask)** | Chat panel / `Ctrl+Alt+I` | Questions, explanations, short generation |
| **Edit** | Chat panel → Edit mode | Apply changes to one or more open files |
| **Plan** | Chat panel → Plan mode | Design a solution before writing code |
| **Agent** | Chat panel → Agent mode | Multi-step tasks, tool use, file operations |
| **Inline chat** | Editor, `Ctrl+I` | Quick ask or edit in context |

**Mode decision — three questions:**

1. Does the task require changes to files? → **No** → Use Ask. **Yes** → go to 2
2. Is it one file or a targeted change? → **Yes** → Use Edit or Inline chat. **No** → go to 3
3. Does it require multi-step execution across files? → **No** → Plan then Edit. **Yes** → Agent

**Beginners:** Default to Ask and Edit. Defer Agent mode until Module 06 — agent sessions accumulate context and cost, and mid-session mistakes are harder to reverse. The one exception: Agent mode is appropriate from the start when scaffolding a new, empty project.

| Task type | Recommended mode | Why |
|-----------|-----------------|-----|
| Autocomplete a method signature | Inline completion | Lowest cost, fastest |
| Explain a confusing function | Ask | Conversational, no file edits |
| Refactor a single file | Edit | Targeted, creates a reviewable diff |
| Design a solution before coding | Plan | Prevents premature implementation |
| Scaffold a new feature across files | Agent | Multi-file, multi-step |
| Quick fix on the current line | Inline chat | No context switch |

### Critical Review: Read → Run → Reason → Risk

Never accept AI output without review. Apply this workflow to every suggestion:

| Step | Question | If no → |
|------|----------|--------|
| **Read** | Did you read the output line by line before accepting? | Read it now |
| **Run** | Does it compile and execute without errors? | Fix or reject |
| **Reason** | Does it do exactly what was asked, with no unintended side effects? | Revise the prompt |
| **Risk** | Does it introduce a security concern? | Ask Copilot to review for OWASP A01/A03 issues |

**The explain rule:** If you cannot explain a line of AI-generated code in your own words, ask Copilot to explain it before committing. Never commit code you do not understand.

**Five common AI failure modes:**

| Failure | Example | How to detect |
|---------|---------|--------------|
| Hallucinated API | Calls a method that does not exist in the installed version | Run the code; check the docs |
| Stale knowledge | Uses a deprecated function or removed argument | Search current official documentation |
| Missing error handling | Happy path only; exceptions will crash | Ask: "What can go wrong here?" |
| Security anti-pattern | Concatenates user input into a SQL query | Check against OWASP A03 (injection) |
| Correct pattern, wrong context | Adds `async/await` in a synchronous framework | Understand the framework before accepting |

See [checklists/ai-output-review.md](../../checklists/ai-output-review.md) and [checklists/pre-commit.md](../../checklists/pre-commit.md) for the full review gates.

### First Productivity Habits

Three habits to establish from session one:

1. **Choose the mode before writing the prompt.** Prevents mode-switching mid-session, which resets context and wastes requests. Decide: Ask, Edit, Plan, or Agent — then open the panel.

2. **Write your acceptance criteria first.** One sentence: *"I will accept this if it does X."* Prevents accepting plausible-looking wrong answers because you forgot what you actually needed.

3. **Close irrelevant files before a chat session.** Copilot includes open file content in context. Unrelated files dilute the signal, increase cost per turn, and can cause the model to reference the wrong file.

---

## Token and Premium Request Basics

Two request types govern Copilot usage:

| Type | Examples | Cost |
|------|---------|------|
| **Included** | Inline completion, Ask with default model | Unlimited on most plans |
| **Premium** | Ask/Edit/Agent with a premium model, agent sessions | Counts against monthly quota |

**The cost-aware decision rule:** Use the cheapest mode that can handle the task. Escalate only when the cheaper option gives an incorrect or incomplete result.

| Guideline | Rationale |
|-----------|-----------|
| Default model handles 80% of questions | Switch to premium only for hard reasoning or architecture design |
| Agent mode is expensive per turn | If a task fits in two Edit prompts, use Edit |
| Large open files increase cost per turn | Close files not needed for the current task |

After your first session, note one thing: did you use the right mode, or did you escalate unnecessarily? That's your first token audit.

---

## Exercises

See [exercises.md](./exercises.md) for full instructions.

1. First inline completion — accept, reject, and cycle alternatives
2. Ask mode — explain a function and identify a security issue
3. Edit mode — rename a variable and review the diff before accepting
4. Plan mode — design a utility before writing any code
5. Inline chat — fix a syntax error and a logic issue
6. Request classification — classify 5 tasks as included or premium

---

## Common Mistakes

| Mistake | Root cause | Fix |
|---------|------------|-----|
| Pressing `Tab` before reading ghost text | The gesture is reflexive; completions look plausible | Read first, then accept. One wrong Tab costs a revert and a re-prompt. |
| Using Agent mode for a one-file change | "More capable = better" | For single-file changes, Edit mode is faster and cheaper |
| Switching to premium model for every question | "Premium is better, why not always?" | Escalate only after the included model gives an insufficient answer |
| Accepting an explanation without running the code | Copilot explains confidently even when wrong | Always run or trace code before trusting the explanation |
| Ignoring the status bar icon | Easy to miss when focused on code | When completions stop, check the icon first |
| Pasting large irrelevant files into context | "More context = better answers" | Irrelevant context dilutes signal and increases cost |
| Continuing a new topic in an existing session | Feels efficient to keep going | Each unrelated topic should start a new chat session |

---



---



---

## Completion Criteria

You have completed this module when you can:

- [ ] Confirm Copilot Pro+ is active in VS Code
- [ ] Demonstrate all six modes and explain in one sentence when you would use each
- [ ] Apply Read → Run → Reason → Risk to a piece of AI-generated code and identify at least one issue
- [ ] Classify 5 task types correctly as included or premium requests
- [ ] Name the three first-session productivity habits from memory

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
| [Lab 01 — Getting Started](../../labs/lab-01-getting-started/) | All six modes on real tasks, critical review, three habits | 40–50 min |
| [Lab 01 — Setup and Verify](../../labs/lab-01-setup-and-verify/) | Installation verification, mode confirmation, request classification worksheets | 40–50 min |

See [labs/README.md](../../labs/README.md) for the full lab index.

---

## Next Module

→ [Module 02: Configuration](../02-configuration/)
