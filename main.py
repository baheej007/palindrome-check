def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Optional: Remove spaces and convert to lowercase
    return s == s[::-1]

# Example usage
print(is_palindrome("A man a plan a canal Panama"))  # True
