# Plan Mode Output — delete_item() Design

<!-- Reference solution for Lab 08 Task 1. Produce your own Plan output before reading. -->
<!-- Produced by: Plan mode session, input: starter/api/routes.py TODO comment -->

---

## Problem Restatement

The `routes.py` module needs a `delete_item()` function that removes an item from the in-memory store. The function must enforce ownership authorization before deletion — only the item's owner may delete it. Two specific failure conditions must be handled: attempting to delete a non-existent item (raises `ValueError`) and attempting to delete an item the requesting user does not own (raises `PermissionError`). All deletions must produce an audit record before the item is removed, so the record exists even if subsequent operations fail.

---

## Files to Modify

| File | Reason |
|------|--------|
| `starter/api/routes.py` | This is the only file that owns item storage and business logic; `delete_item()` belongs here |

Files that must NOT change: `starter/auth.py` (authentication; out of scope), `starter/tests/test_routes.py` (tests are a separate concern; add tests in a follow-up step, not in this implementation pass).

---

## Proposed Change

**Function signature:**

```python
def delete_item(item_id: str, requesting_user_id: str) -> None
```

**Logic (function scope — not line-by-line code):**

1. Look up `item_id` in `_items`. If not found, raise `ValueError(f"Item {item_id!r} does not exist")`.
2. Confirm `_items[item_id]["owner_id"] == requesting_user_id`. If not, raise `PermissionError("Requesting user is not the item owner")`.
3. Record the deletion audit entry before removal. For this lab, use `print(f"AUDIT: {requesting_user_id} deleted {item_id}")` as a placeholder.
4. Remove the item: `del _items[item_id]`.

**What will NOT change:**

- `get_item()` and `list_items()` signatures and behavior remain unchanged.
- No changes to `auth.py`.
- The `_items` dict structure (`id`, `name`, `owner_id` keys) remains unchanged.
- No imports are added beyond what already exists.

---

## Open Question

The requirement says "must be audited before the item is removed." This lab uses a `print()` placeholder. A production implementation would import an audit log module — confirm whether that import is in scope for this session before proceeding, or accept the placeholder for lab purposes.
