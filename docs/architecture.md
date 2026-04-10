# Repository Architecture

This document records the key design decisions for the `copilot-learning-labs` repository structure.

---

## Design Goals

1. **Anyone can clone and learn independently** — no registration, no external LMS, no paid tools beyond a Copilot subscription.
2. **Progressive learning** — content builds from beginner to expert; prerequisites are always explicit.
3. **Maintainable** — each content type has one authoritative template; modules are self-contained.
4. **Dogfooding** — the repository uses the conventions it teaches. Custom instructions, prompt templates, and agent definitions are real, not invented for illustration.
5. **Publication-ready** — meets GitHub open-source project quality standards: LICENSE, CODE_OF_CONDUCT, CONTRIBUTING, issue templates.

---

## Folder Responsibilities

| Folder | Purpose | Created by |
|--------|---------|-----------|
| `modules/` | Curriculum content — progressive learning units | Course author |
| `labs/` | Hands-on practice — paired to modules | Course author |
| `prompts/` | Reusable prompt library | Course author + contributors |
| `instructions/` | Custom instruction examples | Course author |
| `agents/` | Agent/persona definitions with handoffs | Course author |
| `templates/` | Structure templates for all content types | Course author (locked) |
| `checklists/` | Quality gates and self-assessment tools | Course author |
| `examples/` | Real-world scenario files (non-lab) | Course author + contributors |
| `capstone/` | Final project tying all skills together | Course author |
| `assets/` | Images, diagrams, non-text assets | Course author |
| `faq/` | Frequently asked questions | Course author + contributors |
| `docs/` | Design documents, not learner content | Course author |
| `.github/` | Community infrastructure | Course author |
| `.vscode/` | Editor config for this repository | Course author |

---

## Key Conventions

### Module files

Every module under `modules/XX-slug/` must contain exactly:

```
README.md      ← module overview, follows module-readme-template
theory.md      ← extended reference, under 500 words of prose
exercises.md   ← numbered exercises
checklist.md   ← self-assessment checklist
```

No other files should be created inside a module folder without a strong reason.

### Lab files

Every lab under `labs/lab-XX-slug/` must contain:

```
README.md      ← lab instructions, follows lab-readme-template
checklist.md   ← completion checklist
starter/       ← files the learner begins with
solution/      ← reference answer (hidden until after completion)
```

### Module numbering

Modules are numbered `01`–`10`. Numbers are fixed. If a new intermediate module is inserted in the future, a minor version bump is required and the dependency map must be updated.

### Lab numbering

Labs are numbered to match their primary module. If a module has multiple labs, they are sequenced with the module number as prefix: `lab-04a-`, `lab-04b-`, etc.

---

## Template Freeze Policy

Templates in `/templates/` are the single source of truth for structure. Changing a template:

- Requires an issue documenting the rationale
- Requires a PR with a migration note explaining what existing content must be updated
- Requires a CHANGELOG entry under `MAJOR` or `MINOR` depending on scope

---

## Versioning Strategy

| Tag pattern | Meaning |
|-------------|---------|
| `v0.1` | Foundation / MVC — one module, one lab, structural scaffold |
| `v0.2` | Beginner complete — Modules 01–03, Labs 01–05 |
| `v0.3` | Intermediate complete — Modules 04–05 |
| `v0.4` | Advanced complete — Modules 06–07, agents/ |
| `v1.0` | Full course — all 10 modules, capstone, examples |

Patch versions (`v0.1.1`) are used for typo fixes, broken links, and date refreshes.

---

## Single Source of Truth Hierarchy

```
docs/course-design-brief.md    ← intent and original vision
SYLLABUS.md                    ← authoritative module list
LEARNING_PATH.md               ← navigation (references SYLLABUS)
README.md                      ← entry point (references LEARNING_PATH and COURSE_OVERVIEW)
```

Never duplicate module lists or learning outcomes across files. Reference, don't copy.
