import pytest

from pyutils.string_utils import (reverse_string, is_palindrome, count_vowels, word_count)

# =====================
# reverse_string
# =====================

def test_reverse_string_normal_case():
    assert reverse_string("python") == "nohtyp"

def test_reverse_string_empty_string():
    assert reverse_string("") == ""

def test_reverse_string_single_character():
    assert reverse_string("a") == "a"

def test_reverse_string_invalid_input():
    with pytest.raises(TypeError):
        reverse_string(123)  # type: ignore[arg-type]


# =====================
# is_palindrome 
# =====================

def test_is_palindrome_palindrome():
    assert is_palindrome("radar") is True

def test_is_palindrome_not_palindrome():
    assert is_palindrome("python") is False

def test_is_palindrome_empty_string():
    assert is_palindrome("") is True

def test_is_palindrome_invalid_type():
    with pytest.raises(TypeError):
        is_palindrome(123)  # type: ignore[arg-type]


# =====================
# count_vowels
# =====================

def test_count_vowels_multiple():
    assert count_vowels("hello world") == 3

def test_count_vowels_none():
    assert count_vowels("rhythm") == 0

def test_count_vowels_uppercase():
    assert count_vowels("AEIOU") == 5

def test_count_vowels_empty():
    assert count_vowels("") == 0

def test_count_vowels_invalid_type():
    with pytest.raises(TypeError):
        count_vowels(123)  # type: ignore[arg-type]


# =====================
# word_count
# =====================

def test_word_count_multiple_words():
    assert word_count("Python is powerful") == 3

def test_word_count_empty():
    assert word_count("") == 0

def test_word_count_multiple_spaces():
    assert word_count("hello    world") == 2

def test_word_count_leading_trailing_spaces():
    assert word_count("   hello world   ") == 2

def test_word_count_invalid_type():
    with pytest.raises(TypeError):
        word_count(123)  # type: ignore[arg-type]