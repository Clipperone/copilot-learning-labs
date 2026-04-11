# verify.py — Lab 01 solution

# This solution shows the expected result after applying Agent mode (Task 2b)
# and the inline chat validation improvement (Task 2c).
# Use this as a reference only — complete the lab using Copilot before consulting this file.


def add(a: int | float, b: int | float) -> int | float:
    """Return the sum of two numbers."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Expected numeric arguments, got {type(a).__name__} and {type(b).__name__}")
    return a + b


def subtract(a: int | float, b: int | float) -> int | float:
    """Return the result of subtracting b from a."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Expected numeric arguments, got {type(a).__name__} and {type(b).__name__}")
    return a - b


def multiply(a: int | float, b: int | float) -> int | float:
    """Return the product of two numbers."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Expected numeric arguments, got {type(a).__name__} and {type(b).__name__}")
    return a * b


def divide(a: int | float, b: int | float) -> float:
    """Return the result of dividing a by b. Raises ZeroDivisionError if b is zero."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Expected numeric arguments, got {type(a).__name__} and {type(b).__name__}")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
