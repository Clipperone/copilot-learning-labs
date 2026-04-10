# Request Classification Worksheet — Reference Solution

---

| # | Task description | Classification | Explanation |
|---|-----------------|---------------|-------------|
| 1 | Accept a ghost text completion that suggests a loop body | **Included** | Inline completions always use the included request tier; they never consume premium quota regardless of model or plan. |
| 2 | Use Ask mode with the default model to explain a 20-line Python function | **Included** | Ask mode with the default (included) model is a standard chat request. No premium request is consumed. |
| 3 | Run an agent session to scaffold a FastAPI project across 5 new files | **Premium** | Agent sessions use premium models and tool calls (file reads/writes, terminal). Each agent turn consumes premium quota. |
| 4 | Use Ask mode with GPT-4o to review the architecture of a microservices design | **Premium** | Switching to a premium model (GPT-4o, Claude, o1, o3) in any mode upgrades the request to premium, regardless of the task complexity. |
| 5 | Use Edit mode with the default model to rename a variable in one file | **Included** | Edit mode with the default model is an included request. Single-file targeted edits do not require a premium model. |

---

## Notes

The hardest tasks to classify are typically those that combine mode and model choices (tasks 3 and 4 above). The rule is:

- **Mode alone does not determine cost** — Edit mode with the default model is included; Edit mode with Claude is premium.
- **Model choice is the primary driver** — switching to any named premium model (GPT-4o, Claude, o1, o3) makes the request premium.
- **Agent mode is always premium** — regardless of model selection, agent sessions involve tool use and multi-step execution that consume premium quota.
