# Mode Verification Worksheet — Reference Solution

---

| Mode | Test prompt used | Result | Status |
|------|-----------------|--------|--------|
| Inline completion | Typed `def calculate_area(` and paused | Ghost text appeared suggesting `radius: float) -> float:` followed by `return math.pi * radius ** 2` or similar | ✅ |
| Ask | `What does starter/verify.py do?` | Copilot summarised the file: a small Python module with arithmetic utility functions (add, subtract, multiply, divide) | ✅ |
| Edit | `Add a docstring to each function.` (discarded after review) | Diff proposed adding a one-line docstring to each function describing its parameters and return value | ✅ |
| Plan | `Plan a function that reads a CSV and returns rows where status = active.` | Multi-step plan returned: open file with `csv.DictReader`, iterate rows, filter by `row["status"] == "active"`, collect results, return list. No code written. | ✅ |
| Agent | `List all Python files in the starter/ folder and describe each one.` | Agent listed `verify.py` and described its contents using file-reading tools | ✅ |
| Inline chat | Selected `add` function → `Ctrl+I` → `Add input validation to reject non-numeric arguments.` (dismissed after review) | Inline diff appeared adding `isinstance` checks or `raise TypeError` for non-numeric inputs | ✅ |

---

## Notes

No errors expected if Copilot Pro+ is correctly configured. If Agent mode is unavailable, the plan field is blank and the status is ❌ — verify subscription at [github.com/settings/copilot](https://github.com/settings/copilot).
