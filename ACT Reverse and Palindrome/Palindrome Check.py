def is_palindrome(s):
    def check(left, right):
        # Base case
        if left >= right:
            return True

        
        if s[left] != s[right]:
            return False
        
        return check(left + 1, right - 1)

    return check(0, len(s) - 1)

# Test cases — do not change these
print(is_palindrome("madam"))   # Expected: True
print(is_palindrome("racecar")) # Expected: True
print(is_palindrome("hello"))   # Expected: False