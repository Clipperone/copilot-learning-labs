# Lab 01: Getting Started — Completion Checklist

Use this checklist to self-assess before moving to Module 02.

---

## Setup

- [ ] GitHub Copilot Pro+ subscription is active
- [ ] VS Code 1.90 or later is installed
- [ ] GitHub Copilot and GitHub Copilot Chat extensions are installed
- [ ] The Copilot status bar icon is visible with no warning or error

---

## Task 1: First Deliberate Inline Completion

- [ ] Written acceptance criterion recorded before typing
- [ ] Ghost text appeared after typing the `calculate_bmi` function signature
- [ ] Read → Run → Reason → Risk applied before pressing `Tab`
- [ ] `Alt+]` used to see at least one alternative suggestion
- [ ] `scratch/task1.py` contains the accepted `calculate_bmi` function

---

## Task 2: Mode Selection Practice

- [ ] **2a — Ask:** Copilot explained `scratch/task1.py` line by line; at least one edge case identified
- [ ] **2b — Edit:** `starter/verify.py` has type annotations and input validation on all four functions; diff reviewed before accepting
- [ ] **2c — Plan:** A full implementation plan returned in Plan mode; no code was written
- [ ] **2d — Inline chat:** BMI return statement was modified using `Ctrl+I` without opening the chat panel

Compare `starter/verify.py` after Task 2b with `solution/verify.py` to check your result.

---

## Task 3: Critical Review in Practice

- [ ] Promptly generated a password-check function using Ask mode
- [ ] `scratch/task3.py` contains the generated function and all four Read → Run → Reason → Risk answers as comments
- [ ] The plaintext credential storage flaw is named in the comments
- [ ] Copilot follow-up confirmed OWASP A02 — Cryptographic Failures

---

## Task 4: Three Habits

- [ ] **Habit 1:** Mode selected before opening the chat panel — confirmed correct on the first try
- [ ] **Habit 2:** Acceptance criterion written before sending the prompt; result evaluated against it
- [ ] **Habit 3:** Observed the difference in context scope before and after closing unrelated files

---

## Task 5: Cost Classification

- [ ] All five tasks classified as included or premium before checking
- [ ] At least 4 of 5 correct after verifying against [theory.md](../../modules/01-foundations/theory.md)
- [ ] Any incorrect answer has a one-sentence explanation of the rule missed

---

## Knowledge Check

- [ ] Can name all six Copilot modes and give a one-sentence use case for each
- [ ] Can apply Read → Run → Reason → Risk without prompting
- [ ] Understand the difference between included and premium requests
- [ ] Closed irrelevant files before each chat session during this lab

---

## Ready for Module 02?

→ Complete [modules/01-foundations/checklist.md](../../modules/01-foundations/checklist.md) before advancing.

→ Next: [Lab 02 — Project Configuration Baseline](../../labs/lab-02-configuration/)
