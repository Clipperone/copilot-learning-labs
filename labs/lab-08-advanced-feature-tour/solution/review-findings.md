# Code Review Findings — api/routes.py

<!-- Reference solution for Lab 08 Task 2. Produce your own findings before reading. -->
<!-- Produced by: Code Reviewer Agent session, input: starter/api/routes.py -->

---

## Finding 1 — `get_item()` ignores `requesting_user_id`

**Severity:** Medium
**File:** `starter/api/routes.py`
**Location:** `get_item()`, return statement

`get_item()` accepts `requesting_user_id` as a parameter but does not use it. The function returns any item to any caller regardless of ownership. This is an access control gap: a non-owner can retrieve an item that should only be accessible to its owner.

**Suggested fix:** Add an ownership check before returning: if the item exists and `item["owner_id"] != requesting_user_id`, either return `None` or raise `PermissionError`, depending on the intended authorization semantics.

---

## Finding 2 — `list_items()` returns all items regardless of caller

**Severity:** Medium
**File:** `starter/api/routes.py`
**Location:** `list_items()`, return statement

All items from `_items` are returned to every caller. If items are user-scoped, a caller can enumerate items they do not own. The `requesting_user_id` parameter is accepted but unused.

**Suggested fix:** Filter the return value: `return [item for item in _items.values() if item["owner_id"] == requesting_user_id]` — or document explicitly that `list_items()` is an admin-only operation that returns all items intentionally.

---

## Finding 3 — No input validation on `item_id` in `get_item()`

**Severity:** Low
**File:** `starter/api/routes.py`
**Location:** `get_item()`, first line of function body

`item_id` is passed directly to `_items.get()` without validation. A caller passing `None` or `""` will receive `None` rather than an error, making caller-side error handling ambiguous.

**Suggested fix:** Add `if not item_id or not isinstance(item_id, str): raise ValueError("item_id must be a non-empty string")` as the first line of the function.

---

## Summary

| # | Severity | Status |
|---|---------|--------|
| 1 | Medium | Action required — access control gap |
| 2 | Medium | Action required or document explicitly |
| 3 | Low | Fix before merge (ambiguous contract) |
