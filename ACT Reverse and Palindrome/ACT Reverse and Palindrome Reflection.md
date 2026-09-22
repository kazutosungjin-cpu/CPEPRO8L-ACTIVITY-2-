# Recursion Practice: `reverse` and `is_palindrome`

This document walks through two small recursive functions, their base cases,
and what happens if those base cases are removed.

## 1. `reverse(s, i=0)`

```python
def reverse(s, i=0):
    if i == len(s):
        return ""
    return reverse(s, i + 1) + s[i]
```

**How it works:** Each call moves `i` one step forward and asks "give me the
reverse of everything after me," then tacks the current character `s[i]`
onto the *end* of that result. Since the recursive call happens first and is
resolved from the deepest call outward, characters get appended in reverse
order.

**Base case:**
```python
if i == len(s):
    return ""
```
Once `i` reaches the length of the string, there are no more characters to
process, so recursion stops and returns an empty string to start building
the reversed string back up.

**If the base case were removed:**
The function would keep calling `reverse(s, i + 1)` past the end of the
string. Since there's no check to stop it, `i` would keep growing past
`len(s)`, either:
- raising an `IndexError` when trying to access `s[i]` for an out-of-range
  index, or
- if the index error were somehow avoided, recursing infinitely and
  eventually raising `RecursionError: maximum recursion depth exceeded`.

Either way, the program crashes because there's nothing telling it when to
stop.

## 2. `is_palindrome(s)`

```python
def is_palindrome(s):
    def check(left, right):
        if left >= right:
            return True
        if s[left] != s[right]:
            return False
        return check(left + 1, right - 1)

    return check(0, len(s) - 1)
```

**How it works:** Two pointers, `left` and `right`, start at opposite ends of
the string and move toward each other. At each step, it compares the
characters at those positions. If they don't match, the string isn't a
palindrome. If they do match, it moves both pointers inward and repeats.

**Base case:**
```python
if left >= right:
    return True
```
When `left` meets or passes `right`, every pair of characters has already
been checked and matched, so the string is confirmed to be a palindrome.

## 3. If the base case were removed:
The recursion would never resolve to `True`. `left` would keep increasing
and `right` would keep decreasing past each other, eventually comparing
`s[left]` and `s[right]` with invalid or mismatched (negative or
out-of-bounds) indices. This would likely produce incorrect comparisons,
unexpected `False` results, an `IndexError`, or infinite recursion leading to
a `RecursionError`, depending on exactly how the check is written.

## Key Takeaway

The base case is what gives a recursive function a defined stopping point.
Without it, the function has no way to know when to stop calling itself,
which either crashes the program (`RecursionError` or `IndexError`) or
produces wrong results if it manages to terminate incidentally.
