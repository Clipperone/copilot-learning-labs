# Copilot Instructions — copilot-learning-labs

<!--
  Repository-wide instructions for GitHub Copilot.
  Applies to all chat, edit, plan, and agent sessions in this repository.

  Rules:
  - Keep instructions specific, bounded, and non-contradictory.
  - Prefer shorter, actionable rules over long explanations.
  - Update "Verified" when you materially change this file.
  Verified: 2026-04
-->

---

## 1. Repository Purpose

This repository is a **public open course** on GitHub Copilot Pro+ in Visual Studio Code. It teaches learners to use Copilot seriously and productively, from setup through advanced multi-agent workflows.

Content types:

| Type | Folder | Authoritative template |
|------|--------|----------------------|
| Learning modules | `modules/XX-slug/` | `templates/module-readme-template.md` |
| Hands-on labs | `labs/lab-XX-slug/` | `templates/lab-readme-template.md` |
| Prompt library entries | `prompts/category/` | `templates/prompt-template.md` |
| Agent persona definitions | `agents/` | `templates/agent-definition-template.md` |
| Custom instruction examples | `instructions/` | free-form markdown |
| Checklists | `checklists/` | free-form markdown |

When generating content in this repository, Copilot is producing **educational material**, not production application code. The audience ranges from complete beginners to professional developers.

---

## 2. Writing Style

### Voice and tone

- Use **active voice** at all times: "Configure the setting" not "The setting can be configured."
- Use **operational language**: explain what the learner does, not what a feature is.
- Write at a **professional but approachable** level — clear to a developer with 1–2 years of experience.
- Be direct. Omit preamble ("In this section we will…") and filler ("It is worth noting that…").

### Sentence and paragraph rules

- One idea per sentence. Split compound sentences where possible.
- Prefer bullet points and tables over paragraphs for lists of steps, comparisons, and options.
- Never use passive voice for instructional steps.
- Never write "simply", "just", "obviously", or "easily" — these condescend to beginners.

### Audience awareness

- Always assume the reader may be new to the specific topic, even if experienced in adjacent areas.
- Define terms on first use with `**bold**`. Do not assume familiarity with Copilot-specific terminology.
- When a step requires a prerequisite, state it explicitly: "Before this step, complete Task 2."

---

## 3. Structure Rules

### Modules (`modules/XX-slug/`)

Every module folder must contain exactly these four files — no more, no fewer:

```
README.md      ← overview, objectives, theory summary, exercises list, checklist link
theory.md      ← extended reference — max 500 words of prose (tables and code excluded)
exercises.md   ← numbered, self-contained exercises
checklist.md   ← completion self-assessment
```

- Follow `templates/module-readme-template.md` for README.md structure.
- Do not create additional files in a module folder without explicit instruction.
- Every module README must include: level, estimated time, prerequisites, verified date, and a `⚠️ Premium request note`.

### Labs (`labs/lab-XX-slug/`)

Every lab folder must contain:

```
README.md      ← instructions: objective, prerequisites, tasks, success criteria, failure points
checklist.md   ← completion self-assessment
starter/       ← files the learner begins with (never empty if a task requires code)
solution/      ← reference answer (always present unless the lab is exploratory)
```

- Follow `templates/lab-readme-template.md`.
- Tasks must be numbered and self-contained. Each task must have a clearly stated goal and expected output.
- Success criteria must be verifiable — a command to run, a file to open, a behavior to observe.

### Prompts (`prompts/category/filename.md`)

- Follow `templates/prompt-template.md`.
- Every prompt must include: a filled-in example with realistic input and expected output.
- State `Premium model recommended: yes | no` in the header.
- Include at least one entry in the "Common Failures" table.

### Agent definitions (`agents/role-name.md`)

- Follow `templates/agent-definition-template.md`.
- Every agent must define at least one handoff: to whom, and under what condition.
- Tool permissions must be explicitly listed as ✅ Allow / ⚠️ Conditional / ❌ Deny.

---

## 4. Markdown Formatting Rules

- Use ATX headings (`#`, `##`, `###`) — never Setext (underline) style.
- One blank line before and after every heading, bullet list, numbered list, and code block.
- Fenced code blocks must always include a language identifier: ` ```python `, ` ```bash `, ` ```json `.
- Lines must be under 120 characters where practical. Break long prose lines.
- Use `**bold**` for key terms on first use only. Avoid decorative bold.
- Use tables for any comparison of 3 or more items across 2 or more attributes.
- Table format: `| Col | Col |` with a header separator row `|---|---|`.
- Do not use HTML inside markdown files unless unavoidable.

---

## 5. Content Duplication Rules

These are strict. Duplication degrades maintainability and creates version drift.

- **SYLLABUS.md** is the single source of truth for the module list. README.md and LEARNING_PATH.md link to it — they do not copy it.
- **Module README.md** is the single source of theory summary. theory.md extends it but does not repeat it.
- **Templates** define structure. Content files instantiate them. A template change requires a migration note.
- When referencing another file, use a relative markdown link — do not restate its content inline.
- If the same concept appears in two places, one must link to the other. Remove the duplicate.

---

## 6. Quality Checks

Before considering any generated content complete, verify:

**Structural completeness**
- [ ] All required files for the content type are present (module: 4 files; lab: 4 items including starter/ and solution/)
- [ ] All `[PLACEHOLDER]` values are filled in — no template stubs remain
- [ ] All internal links resolve to existing files in this repository

**Content correctness**
- [ ] All code examples run without modification (or are clearly marked as illustrative with a comment)
- [ ] No deprecated APIs referenced without a note
- [ ] Feature-specific content includes a `Verified: YYYY-MM` date
- [ ] Plan-specific restrictions noted where they apply (Pro / Pro+ / Business / Enterprise)

**Style compliance**
- [ ] Active voice throughout
- [ ] No filler phrases ("it is worth noting", "simply", "just", "obviously")
- [ ] Key terms bolded on first use only
- [ ] Tables used for comparisons with 3+ items

**Security**
- [ ] No secrets, credentials, tokens, or passwords — not even fake ones
- [ ] Use `YOUR_API_KEY`, `<token>`, `<password>` as abstract placeholders only
- [ ] Security-related content references OWASP Top 10 as baseline

---

## 7. Minimizing Unnecessary Regeneration

These rules reduce wasted premium requests and improve session quality.

- **Read before writing.** Always read the existing file before modifying it. Never overwrite a file without confirming its current content.
- **Edit, don't replace.** Make targeted edits rather than regenerating a whole file when only a section needs updating.
- **Use templates.** Do not generate structure from scratch — load the relevant template first.
- **Batch related files.** When creating a module, generate all four required files in the same response rather than one at a time.
- **Do not ask about template structure.** Templates in `/templates/` are authoritative. Follow them without seeking clarification.
- **Do not iterate speculatively.** Do not generate a draft and then immediately ask if changes are needed. Produce complete, correct output.
- **Stop when done.** Do not add unsolicited sections, extensions, or "bonus" content. Produce exactly what was requested.

---

## 8. Security and Safety

- Never generate, suggest, or include secrets, credentials, API keys, tokens, or passwords in any file — even in comments or example data.
- Use abstract placeholders only: `YOUR_API_KEY`, `<token>`, `<password>`, `example.com`.
- When generating security-related content, reference **OWASP Top 10** as the baseline framework.
- Do not generate content that assists with exploitation, unauthorized access, or credential harvesting.
- Do not reproduce third-party copyrighted content verbatim.

---

## 9. What Copilot Must NOT Do in This Repository

- Do not refactor or restructure existing content unless explicitly instructed.
- Do not add comments, docstrings, or annotations to code you did not write.
- Do not create folders or files outside the patterns defined in Section 3.
- Do not reproduce `docs/course-design-brief.md` verbatim — use it as a source of intent only.
- Do not speculate about unverified Copilot features. If unsure, note it explicitly and link to official docs.
- Do not generate content that implies a specific plan requirement (Pro, Pro+, Business) without verifying it.
