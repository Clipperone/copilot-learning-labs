# Critical Review Exercise

Apply the **Read → Run → Reason → Risk** workflow to the two code snippets below. Write your answers in the fields provided. Then answer the final question at the bottom.

---

## Snippet A

```python
import csv

def read_active_users(filepath: str) -> list[dict]:
    results = []
    with open(filepath, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["status"] == "active":
                results.append(row)
    return results
```

**Read — Did you read every line before answering?**

```
(your answer here)
```

**Run — Does this code execute without errors given a valid CSV file with a 'status' column?**

```
(your answer here — describe what happens if the file is missing, or if the column is absent)
```

**Reason — Does it do exactly what was asked? Are there side effects or edge cases?**

```
(your answer here)
```

**Risk — Does it introduce any security or correctness concern? Reference OWASP A01 or A03 if relevant.**

```
(your answer here)
```

---

## Snippet B

```python
import hashlib

def store_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()
```

**Read — Did you read every line before answering?**

```
(your answer here)
```

**Run — Does this code execute without errors?**

```
(your answer here)
```

**Reason — Does it do what a password storage function is supposed to do?**

```
(your answer here)
```

**Risk — Does it introduce any security concern? Be specific.**

```
(your answer here)
```

---

## Final Question

Which snippet contains a flaw that would be dangerous in a real application? Describe the flaw in one sentence and name the correct alternative.

```
(your answer here)
```
