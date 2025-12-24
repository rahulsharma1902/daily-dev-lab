"""
Palindrome Checker - Multiple Approaches
"""

def is_palindrome_simple(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

def is_palindrome_two_pointer(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Test
if __name__ == "__main__":
    test_cases = ["A man a plan a canal Panama", "race a car", "Was it a car or a cat I saw"]
    for tc in test_cases:
        print(f"'{tc}': {is_palindrome_simple(tc)}")
