def reverse(s, i=0):
    if i == len(s):
        return ""
    return reverse(s, i + 1) + s[i]

# Test cases — do not change these
print(reverse("hello"))   # Expected: olleh
print(reverse("python"))  # Expected: nohtyp
print(reverse("a"))       # Expected: a