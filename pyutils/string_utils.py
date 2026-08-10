def reverse_string(s: str) -> str:
    """Return the reverse of a string."""

    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return s[::-1]

def is_palindrome(s: str) -> bool:
    """Return True if s is a palindrome, False otherwise."""
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    for i in range(len(s) // 2):
        if s[i] != s[len(s) -1 - i]:
            return False
    return True

def count_vowels(s: str) -> int:
    """Return the number of vowels in a string."""
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def word_count(s: str) -> int:
    """Return the number of words in a string."""
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return len(s.split())