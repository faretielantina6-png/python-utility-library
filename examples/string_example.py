"""Examples demonstrating the string utility functions."""

from pyutils.string_utils import (
    reverse_string,
    is_palindrome,
    count_vowels,
    word_count,
)


def main() -> None:
    """Run examples for the string utilities."""

    text = "Python"
    palindrome = "radar"
    sentence = "Python is a powerful programming language"

    print("String reversal:")
    print(f"reverse_string({text!r}) -> {reverse_string(text)!r}")

    print("\nPalindrome detection:")
    print(f"is_palindrome({palindrome!r}) -> {is_palindrome(palindrome)}")
    print(f"is_palindrome({text!r}) -> {is_palindrome(text)}")

    print("\nVowel counting:")
    print(f"count_vowels({sentence!r}) -> {count_vowels(sentence)}")

    print("\nWord counting:")
    print(f"word_count({sentence!r}) -> {word_count(sentence)}")


if __name__ == "__main__":
    main()