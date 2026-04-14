# Module 11: Platform & GitHub.com Integration — Theory Reference

> Extended reference for [README.md](./README.md). Read the module overview first.
> Prose sections are capped at 500 words; tables and code blocks are excluded from that limit.

---

## The Copilot Coding Agent — Lifecycle in Detail

The coding agent runs in a sandboxed environment that GitHub provisions for you. The lifecycle has 5 distinct phases, each with its own failure modes.

| Phase | What happens | Most common failure |
|-------|--------------|---------------------|
| 1. Issue assignment | You assign the issue to Copilot (label, mention, or UI button) | Issue too vague or too large — agent cannot infer acceptance criteria |
| 2. Environment provisioning | Sandbox spins up; repo cloned; setup steps run | Missing setup steps in `.github/copilot-setup-steps.yml`; tests need infra the sandbox cannot provide |
| 3. Plan & implement | Agent reads issue, plans, edits, commits | Scope creep — agent edits files outside the implied scope of the issue |
| 4. PR open | Draft PR opened, reviewers requested | Description too thin; misses the *why* |
| 5. Iteration | You comment; agent responds with commits | Long iteration loops — better to close PR and re-issue with a sharper brief |

### Scoping an issue for delegation

A delegatable issue has these properties (a missing one is a reason to handle it yourself):

- **One acceptance criterion** stated as a verifiable observation (a test that passes, an output that matches, a file that exists).
- **Bounded file set** — either named explicitly in the issue or trivially derivable.
- **No design decision** — if the issue has the form "should we use X or Y?", that is human work.
- **No security exposure** — auth, crypto, data handling, anything OWASP-relevant goes through human review from the start.
- **Reversible** — if the change is wrong, reverting is cheap.

### Reviewing the resulting PR

Treat the PR like a contribution from a new external collaborator who you trust to follow conventions but not to make judgment calls.

**Mandatory steps before merge:**

1. Pull the branch locally. Do not trust "tests passed in CI" as the only signal.
2. Read the diff in full — not just the changed-line summary.
3. Run the test that the issue defined as the acceptance criterion.
4. Check files outside the implied scope — were any modified? If yes, ask the agent to justify or revert them.
5. Verify commit messages reference the issue and contain meaningful bodies (not just the agent's auto-generated text).

> Verify coding-agent UI, configuration, and limits against [GitHub Copilot coding agent docs](https://docs.github.com/en/copilot/concepts/agents/coding-agent) — feature scope and pricing have changed since launch.

---

## `copilot-setup-steps.yml` — Configuring the Sandbox

If the coding agent needs anything beyond `npm install` / `pip install -r requirements.txt`, you tell it via `.github/copilot-setup-steps.yml`. This file is the contract between your repo and the sandbox.

```yaml
name: Copilot setup steps
on: workflow_dispatch
jobs:
  copilot-setup-steps:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: pip install -e ".[dev]"
      - name: Provision local services
        run: docker compose -f compose.test.yml up -d
```

**Rules:**

- Keep setup steps idempotent. The sandbox may re-run them.
- Do not put secrets in this file. Use repo or org Actions secrets.
- If your tests require external services (DB, queue, browser), provision them in setup steps or the agent will fail in phase 2.
- Track this file the same as CI workflows — a broken `copilot-setup-steps.yml` blocks every coding-agent run.

---

## Copilot in github.com

### PR summaries — anatomy of a good one

A useful PR summary covers four things:

1. **What changed** — file-level summary, grouped by purpose.
2. **Why it changed** — the motivating issue, the user impact, the constraint.
3. **What did NOT change** — explicit out-of-scope statement (mirrors the Plan-mode 5-element rule from M08).
4. **Risk surface** — what to test or watch after merge.

The auto-generated summary covers (1) well, gestures at (2), and almost never includes (3) or (4). Treat the auto-summary as a draft for *your* revision.

### Copilot review — interpreting the comments

Copilot review produces inline comments at line precision. Triage each as you would Code Reviewer findings (M08): actionable findings have severity + location + description + fix.

**Comments to take seriously:**
- Naming inconsistencies vs. the rest of the file.
- Missing error handling on observable failure paths.
- Suggestions that match a convention you have explicitly documented.

**Comments to discount:**
- Style preferences not in `CONVENTIONS.md`.
- Suggestions for "more tests" without naming the gap.
- Generic "consider X" with no fix.

### Issue summarization — the triage workflow

For long issue threads (>20 comments), summarization saves real reading time. **Do not** use it for an issue you are about to close, comment on, or implement — for those, the threading and tone matters.

---

## `gh copilot` CLI — Patterns and Anti-Patterns

### Install and auth

```bash
gh extension install github/gh-copilot
gh copilot --version
```

Auth uses the same `gh auth` token as the rest of the CLI.

### `suggest` — generating commands

```bash
gh copilot suggest "rsync the build/ directory to the staging server, dry-run first"
```

Returns a candidate command. **Apply the M08 4-question gate before running:**

1. Does it do what was asked?
2. What side effects?
3. Is it reversible?
4. Is the cost (data sent, time, blast radius) acceptable?

### `explain` — describing existing commands

```bash
gh copilot explain "find . -name '*.py' -mtime +30 -not -path './venv/*' -delete"
```

Useful when reviewing a teammate's script before running it. Pair with the human reading — explanation is a starting point, not authority.

### When CLI beats IDE chat

| Scenario | Why CLI |
|----------|---------|
| One-off shell task during interactive work | No context-switch to IDE |
| Explaining a one-line command | Faster than opening chat panel |
| Working on a remote box where VS Code isn't available | The CLI is your only Copilot surface |
| Quick syntax check during scripting | Inline workflow |

### When CLI is wrong

- **CI scripts** — generated commands need explicit human review and version-pinning before automation.
- **Anything involving sensitive paths or credentials** — same content-exclusion considerations as the IDE, but with no `.copilotignore` analogue at the CLI layer.
- **Production operations** — a wrong CLI suggestion run on prod is unrecoverable. Use a runbook.

---

## Surface Decision Rationale

The matrix in [README.md](./README.md#surface-decision-matrix) summarizes choices. The reasoning behind those choices comes down to four questions:

1. **Where will the result be consumed?** A PR summary is consumed in github.com; produce it there.
2. **What context is needed?** A refactor needs file-level context; the IDE has it.
3. **What review gate fits?** Long-running autonomous work fits the PR review model; quick syntactic help fits inline.
4. **What is the failure mode?** Coding-agent failures are recoverable via PR rejection; CLI failures may run immediately.

Match the surface to the answers, not to your habit.

---

## Cross-Surface Anti-Patterns

- **Re-asking on three surfaces** — wastes premium requests, fragments thinking. Pick a surface, finish, move on.
- **Treating the coding agent as "more autonomous Agent mode"** — it is autonomous *over the PR loop*, not *over decision quality*. Scope it as you would a junior contributor.
- **Trusting coding-agent PRs without local verification** — sandbox-passed tests are necessary, not sufficient.
- **Using PR summaries as documentation** — they are summaries of a diff at a point in time. Documentation belongs in the repo, not in the merged PR.
- **Using `gh copilot suggest` in production scripts** — generated commands lack the review traceability that production work requires.
- **Ignoring `copilot-setup-steps.yml`** — every coding-agent failure that says "could not run tests" is fixable here.

---

## Official Resources

- [GitHub Copilot coding agent](https://docs.github.com/en/copilot/concepts/agents/coding-agent)
- [Customizing the development environment for Copilot coding agent](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent)
- [Copilot in pull requests (PR summaries, review)](https://docs.github.com/en/copilot/using-github-copilot/using-copilot-for-pull-requests)
- [GitHub Copilot in the CLI](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line)
- [GitHub Copilot documentation](https://docs.github.com/en/copilot)

---

← [Back to Module 11 README](./README.md)
