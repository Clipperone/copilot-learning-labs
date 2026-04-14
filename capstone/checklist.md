# Capstone Completion Checklist

Use this checklist to confirm all 8 deliverables are complete and committed before marking the course done.

---

## Deliverable Verification

| # | Deliverable | Committed? | Passes rubric? |
|---|-------------|-----------|---------------|
| 1 | `.github/copilot-instructions.md` — ≥5 declarative, verifiable rules | ☐ | ☐ |
| 2 | `CONVENTIONS.md` — ≥5 rules; `AI-assisted:` and `Reviewed-by:` trailers included | ☐ | ☐ |
| 3 | `agents/` — ≥3 definitions each with purpose, constraints, permissions table, handoff | ☐ | ☐ |
| 4 | `prompts/` — ≥3 course-template entries each with a filled example | ☐ | ☐ |
| 5 | `agents/workflow-[name].md` — all 5 required sections; no compound sub-tasks | ☐ | ☐ |
| 6 | `capstone/validation-report.md` — all 5 gates; BLOCKED result; Gate 4 SQL injection named | ☐ | ☐ |
| 7 | `capstone/roadmap.md` — all 6 sections; no stubs; 3 KPIs; ≥5 governance rules; review date specific | ☐ | ☐ |
| 8 | `capstone/platform-artifact.md` — Option A (coding-agent PR + 5-step review notes + decision) OR Option B (`copilot-setup-steps.yml` + before/after PR summary with all 4 properties) | ☐ | ☐ |

---

## capstone/roadmap.md Gate

- [ ] All 6 sections are present and filled in — no `[specific evidence]` or `[specific file]` stubs remain
- [ ] Section 1 self-placement evidence cites committed files or observable behaviors, not self-impressions
- [ ] Section 2 Day 7 tasks are achievable at my actual current skill level
- [ ] Section 3 names exactly 3 KPIs from the minimum set; every rejected metric has a one-sentence explanation
- [ ] Section 4 governance policy has ≥5 rules in declarative format and is committed to the correct location
- [ ] Section 5 names a specific premium request budget category for escalation and one for default model
- [ ] Section 6 names a specific monthly review date and responsible person for each of the 4 review steps

---

## capstone/validation-report.md Gate

- [ ] All 5 pre-merge gates are assessed with Pass / Fail / Partial per gate
- [ ] Gate 4 (OWASP A03 — SQL injection) is recorded as BLOCKING for both `get_user` and `delete_user`
- [ ] The `subprocess.run(shell=True)` command injection in `export_user_data` is identified (OWASP A03)
- [ ] The overall result is stated as BLOCKED with the blocking gate(s) named

---

## capstone/platform-artifact.md Gate

- [ ] One option is fully completed (A or B — not a partial mix)
- [ ] **Option A:** PR URL + 5-step review notes (pull, read, run, scope-check, commits) + merge/reject decision with reasoning
- [ ] **Option B:** `.github/copilot-setup-steps.yml` committed + before-and-after PR summaries showing all 4 properties (what changed, why, what did NOT change, risk surface)

---

## Final Verification

- [ ] All 8 deliverable files are committed — not just saved locally
- [ ] `checklists/expert-completion.md` has been reviewed — every item checked or annotated
- [ ] `checklists/adoption-milestones.md` reflects actual current state at each milestone
- [ ] `modules/10-adoption-roadmap/checklist.md` After Capstone section is fully checked

---

**You have completed the GitHub Copilot Pro+ Mastery course.**

→ [checklists/expert-completion.md](../checklists/expert-completion.md)
→ [checklists/adoption-milestones.md](../checklists/adoption-milestones.md)
→ [modules/10-adoption-roadmap/checklist.md](../modules/10-adoption-roadmap/checklist.md)
