# Module 01: Foundations — Theory Reference

> Extended reference for [README.md](./README.md). Read the module overview first.
> Prose sections are capped at 500 words; tables and code blocks are excluded from that limit.

---

## GitHub Copilot Pro+ vs. Other Plans

| Feature | Free | Pro | Pro+ | Business | Enterprise |
|---------|------|-----|------|----------|------------|
| Inline completion | ✅ | ✅ | ✅ | ✅ | ✅ |
| Chat (included model) | ✅ | ✅ | ✅ | ✅ | ✅ |
| Premium model access | ❌ | Limited | ✅ | ✅ | ✅ |
| Agent mode | ❌ | ❌ | ✅ | ✅ | ✅ |
| Premium request quota | — | — | Monthly allotment | Seat-based | Seat-based |
| Custom instructions | ❌ | ❌ | ✅ | ✅ | ✅ |
| Repository-scoped policies | ❌ | ❌ | ❌ | ✅ | ✅ |

> Plan features change frequently. Verify at [github.com/features/copilot](https://github.com/features/copilot).

---

## How Copilot Works: The Prompt Pipeline

Every Copilot interaction follows the same pipeline:

```
You type → VS Code builds a prompt → Model processes it → Completion returned → You review
```

The prompt VS Code sends contains:

| Component | Present in |
|-----------|----------|
| Your message or typed text | All modes |
| Content before/after cursor | Inline completion |
| Open file contents | Chat modes |
| Conversation history | Chat modes |
| Custom instruction files | All modes (if configured) |
| Referenced files (`#file:`) | Chat modes, when you add them |

The model has no access to anything outside what VS Code passes. It does not retain state between sessions. Starting a new chat session clears the conversation.

### What "context window" means in practice

The context window is the maximum amount of text the model can process in a single request. Anything outside the window is invisible. For large files or long conversations:

- Earlier parts of the conversation may be dropped
- Files you haven't opened may not be included
- Large files may be truncated

This is why context management matters — covered in Module 03.

---

## The Inline Completion Model (Ghost Text)

Inline completions are generated as you pause typing. VS Code sends:

- Content before the cursor (primary signal)
- Content after the cursor (used for "fill in the middle" completions)
- File type and language hint

**Key behaviors:**
- `Tab` — accept full suggestion
- `Ctrl+Right` (Windows/Linux) / `Option+Right` (Mac) — accept one word at a time
- `Esc` — dismiss
- `Alt+]` / `Alt+[` — cycle through alternative suggestions

---

## Chat Mode Architecture (Panel Modes)

In panel chat modes (Ask, Plan, Agent), Copilot operates as a **conversation** with different capabilities.
Inline completion and Inline chat are editor interactions and are not listed in this table.

| Mode | Tool access | File edits | Multi-step |
|------|-------------|-----------|-----------|
| Ask | Context-aware answers only | No | No |
| Plan | Read-only planning context | No | No (plans only) |
| Agent | Read, write, terminal, search | Yes | Yes |

**Agent mode** is the most powerful but also the most expensive in terms of premium requests. It can loop through multiple steps, run commands, read and write files, and use web search if configured.

> **Note on Edit mode.** Earlier VS Code versions had a separate **Edit mode** panel for coordinated multi-file edits. It was consolidated into Agent mode in **VS Code 1.110**. The capability still exists — see Module 08 for how to do "Edits-style" work inside Agent mode and via custom agents. Older docs, tutorials, or screenshots that show four panel modes (Ask / Edit / Plan / Agent) are out of date.

---

## AI Failure Mode Reference

Language models are optimised to produce **plausible text**, not verified code. The five failure modes a beginner will encounter most often:

| Failure | Concrete example | Detection method |
|---------|-----------------|------------------|
| **Hallucinated API** | Calls `pd.DataFrame.pivot_wider()` — this method does not exist in pandas | Run the code; read the traceback |
| **Stale knowledge** | Uses `app.run(debug=True)` in a Flask 3.x context where the API changed | Check the current official docs |
| **Missing error handling** | Opens a file with no `try/except`; any missing file crashes the program | Ask: "What can go wrong here?" |
| **Security anti-pattern** | Formats user input directly into a SQL string — SQL injection (OWASP A03) | Check against OWASP A03 Injection |
| **Correct pattern, wrong context** | Adds `async def` to a function in a synchronous Django view | Understand the framework conventions before accepting |

**OWASP anchors for beginners:**

- **A01 — Broken Access Control:** AI-generated code may expose resources without checking who the caller is. Ask: *"Does this code verify the caller has permission?"*
- **A03 — Injection:** AI-generated code may construct SQL, shell commands, or HTML from user inputs without sanitisation. Ask: *"Does any user-controlled value flow into a query, command, or rendered output?"*

For a full review protocol, see [checklists/ai-output-review.md](../../checklists/ai-output-review.md).

---

## The Three Productivity Habits: Rationale

**Habit 1 — Choose the mode before writing the prompt**

When you switch modes mid-flow, context continuity can degrade and you often need to re-orient the new turn. In many cases, mode changes keep part of the chat history, but you should not assume full carryover of intent, scope, and constraints. Decide the mode first to minimize re-prompting and avoid spending requests on repeated setup.

**Habit 2 — Write your acceptance criteria first**

With no acceptance criteria, the brain defaults to pattern-matching: "This looks like what I asked for." A one-sentence criterion — *"I will accept this if the function handles a None input without raising an exception"* — forces you to check the specific behaviour you actually need.

**Habit 3 — Close irrelevant files before a chat session**

VS Code includes the content of open files in the context it sends to the model. A 500-line unrelated file in an open tab dilutes the prompt, consumes context window space, and increases the chance Copilot references the wrong file in its answer.

---

## When NOT to Use Copilot

Copilot is a productivity amplifier, not a universal tool. Situations where reaching for it hurts more than helps:

| Situation | Why Copilot is the wrong tool | What to do instead |
|-----------|------------------------------|-------------------|
| **You do not understand the problem yet** | Copilot will generate plausible code for the wrong problem. You ship faster, but in the wrong direction. | Read, sketch, or ask a colleague first. Return when you can state the task in one sentence. |
| **The change is a one-character edit you already know** | Invoking chat or inline chat is slower than typing. | Type it. |
| **Sensitive data is in scope** (credentials, PII, regulated data, customer secrets) | The file may be included in the prompt and sent to the model. Check your org's content-exclusion policy first. | Close or exclude the file; redact before asking; use `.copilotignore` (Module 08). |
| **The code must be novel for legal or compliance reasons** (patents, licensing, clean-room) | Copilot's suggestions can echo training data. Code referencing and license filters reduce but do not eliminate the risk. | Disable suggestions for the file/repo; document the decision. |
| **You are learning a concept for the first time** | Accepting a suggestion skips the struggle that produces real learning. | Write the code yourself; use Ask mode afterwards to review your solution. |
| **The task is pure mechanical refactor your IDE can do safely** (rename symbol, extract method) | The IDE's static tools are exact; Copilot is probabilistic. | Use VS Code's built-in refactor (`F2` rename, extract method). |
| **You are debugging a race condition, memory leak, or concurrency issue** | These bugs require runtime evidence (logs, traces, profilers). Copilot cannot see runtime state. | Reproduce, profile, then bring findings to Copilot for analysis. |
| **The stakes of a wrong answer are severe and unverifiable locally** (production migrations, irreversible deletions, crypto parameters) | A plausible-looking answer that is subtly wrong is worse than no answer. | Use Copilot to draft a checklist of considerations; validate each against authoritative sources. |

**Rule of thumb:** If you cannot state how you will verify the output, you are not ready to use Copilot on this task.

---

## Official Resources

- [GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/overview)
- [GitHub Copilot documentation](https://docs.github.com/en/copilot)
- [GitHub Copilot plan comparison](https://docs.github.com/en/copilot/about-github-copilot/subscription-plans-for-github-copilot)
- [VS Code Copilot keyboard shortcuts](https://code.visualstudio.com/docs/copilot/copilot-vscode-features)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)

---

← [Back to Module 01 README](./README.md)
