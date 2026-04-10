# Module 01: Foundations — Extended Theory

> Reference material to supplement the module README. Read this for deeper context or when the README summary is insufficient. Prose sections are capped at 500 words; tables and code are excluded from that limit.

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

The model has no access to anything outside what VS Code passes. It does not retain state between sessions. Restarting VS Code clears the conversation.

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

## Chat Mode Architecture

In chat modes (ask, edit, plan, agent), Copilot operates as a **conversation** with tool access:

| Mode | Tool access | File edits | Multi-step |
|------|-------------|-----------|-----------|
| Ask | Read-only reference | No | No |
| Edit | Current file(s) | Yes, direct | No |
| Plan | Read-only | No | No (plans only) |
| Agent | Read, write, terminal, search | Yes | Yes |

**Agent mode** is the most powerful but also the most expensive in terms of premium requests. It can loop through multiple steps, run commands, read and write files, and use web search if configured.

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

When you switch modes mid-session, VS Code discards the current context and starts a new one. Requests spent re-orienting a new session on the same problem are wasted. Deciding the mode first takes two seconds and saves one re-prompt.

**Habit 2 — Write your acceptance criteria first**

With no acceptance criteria, the brain defaults to pattern-matching: "This looks like what I asked for." A one-sentence criterion — *"I will accept this if the function handles a None input without raising an exception"* — forces you to check the specific behaviour you actually need.

**Habit 3 — Close irrelevant files before a chat session**

VS Code includes the content of open files in the context it sends to the model. A 500-line unrelated file in an open tab dilutes the prompt, consumes context window space, and increases the chance Copilot references the wrong file in its answer.

---

## Official Resources

- [GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/overview)
- [GitHub Copilot documentation](https://docs.github.com/en/copilot)
- [GitHub Copilot plan comparison](https://docs.github.com/en/copilot/about-github-copilot/subscription-plans-for-github-copilot)
- [VS Code Copilot keyboard shortcuts](https://code.visualstudio.com/docs/copilot/copilot-vscode-features)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
