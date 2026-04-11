# Module 06 — Exercises

Complete these exercises before starting Lab 06. Each builds one skill from the module learning objectives.

---

## Exercise 1 — Anatomy Check

**Objective:** Identify which of the 4 required fields is absent or incomplete in a persona definition.

The following persona definition is incomplete. Read it and answer the questions below.

```
Role: Expert Python refactoring assistant with a focus on clean architecture
      and SOLID principles.

Instructions: Refactor the provided Python module to improve readability and
              maintainability. Use best practices throughout.
```

**Questions:**

1. Which of the 4 required anatomy fields (purpose, constraints, tool permissions, handoff criteria) is missing entirely? Name all missing fields.
2. Which present field violates the **bounded** design principle from Module 05?
3. Rewrite the constraints field so it passes the bounded test: name exact rules, not intent.

> **Tip:** "Use best practices" is not a constraint — it is an intent. A constraint names what must or must not happen.

---

## Exercise 2 — Initialization Prompt

**Objective:** Write a complete initialization prompt for the Planner role that passes the completeness test.

**Scenario:** A team needs to add per-user rate limiting to a REST API. The feature request reads: "Limit API calls to 100 per user per hour. Return HTTP 429 with a `Retry-After` header when the limit is exceeded."

Write a Planner initialization prompt that:

- Contains all 4 anatomy fields
- Names the exact deliverable (a file, not just "a plan")
- Sets tool permissions correctly for a role that reads documents only and never writes source code
- Passes the completeness test: all four questions — what does it produce, what is it not allowed to do, which tools can it use, how do I know it's done — have specific answers

> **Note:** The Planner's permissions matrix must show ❌ for Edit and Terminal. The role that evaluates never modifies.

---

## Exercise 3 — Handoff Prompt

**Objective:** Write a 3-part handoff prompt from a Planner to an Implementer for a single sub-task.

The Planner session produced this output:

```
Task 1: Add RateLimitExceeded exception class to exceptions.py
        Acceptance: Class inherits from Exception. Message includes user_id and window.

Task 2: Implement check_rate_limit(user_id, window_seconds, max_requests) in rate_limiter.py
        Acceptance: Returns True if within limit. Raises RateLimitExceeded if exceeded.

Task 3: Add rate limit middleware to Flask app in app.py
        Acceptance: Middleware calls check_rate_limit before each route handler.
                    Returns 429 with Retry-After header when RateLimitExceeded is raised.

Task 4: Write pytest suite for check_rate_limit
        Acceptance: Covers: within limit, at limit, over limit, expired window.
```

Write the handoff prompt that opens an Implementer session scoped to **Task 1 only**.

The prompt must contain:
1. Summary of what the Planner produced
2. Implementer's bounded objective (Task 1 only — name the file and function)
3. Carry-forward constraints (active instruction files, tasks not in scope for this session)

> **Constraint discipline:** The handoff must explicitly exclude Tasks 2, 3, and 4 from this session. Each sub-task belongs in its own Implementer session.

---

## Exercise 4 — Permissions Justification

**Objective:** Fill in the full tool permissions matrix for the Code Reviewer role and justify every ❌ entry.

Complete this table:

| Tool / Capability | Permission | Justification for ❌ (if applicable) |
|-------------------|:----------:|--------------------------------------|
| Read files | ✅ | — |
| Edit files | ? | |
| Run terminal | ? | |
| Create files | ⚠️ | — |
| Web search | ? | |

After completing the table, answer this question: what specific failure mode from the module's Risks and Safeguards section does granting the Code Reviewer Edit access enable? Name the failure mode and explain how the permission triggers it.

---

## Exercise 5 — Failure Mode Diagnosis

**Objective:** Identify which of the 3 failure modes is operating in each session description and cite evidence.

Failure modes: **context pollution** · **over-delegation** · **unbounded scope**

| Session description | Failure mode | Evidence from the description |
|--------------------|-------------|-------------------------------|
| "Act as a senior engineer. Review this PR, then fix all the issues you find, and write tests for the fixed code." | ? | |
| An agent session started to implement one function. It has been running for 80 minutes and has modified 12 files across 3 modules. The last 10 agent responses each begin with a restatement of decisions made in the first 10 messages. | ? | |
| "Implement the notification feature." No files specified. No exit condition stated. The agent has opened `app.py`, `models.py`, `notifications.py`, `test_notifications.py`, `config.py`, and `README.md`. | ? | |

For each row: name the failure mode, then quote the phrase from the description that is the strongest evidence.

---

## Answer Guidance

Confirm your answers against the [README.md](./README.md) sections Risks and Safeguards, Agent Anatomy, and Tool Permissions Model before proceeding to Lab 06.

If you are uncertain about Exercise 1 or 5, revisit the Risks and Safeguards section. If Exercise 3 is unclear, re-read the Handoff Criteria and the Handoff Prompt section and the Planner example in Agent Anatomy.

Reference solutions are in [`labs/lab-06-agents-and-personas/solution/`](../../labs/lab-06-agents-and-personas/solution/) — check only after completing the exercises independently.
