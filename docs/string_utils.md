````markdown
# String Utilities

The `string_utils` module provides small, reusable utilities for common
string manipulation and analysis operations.

Module:

```python
pyutils.string_utils
````

## Functions

The module provides four functions:

| Function           | Purpose                                      |
| ------------------ | -------------------------------------------- |
| `reverse_string()` | Reverses a string.                           |
| `is_palindrome()`  | Determines whether a string is a palindrome. |
| `count_vowels()`   | Counts the vowels contained in a string.     |
| `word_count()`     | Counts the words contained in a string.      |

---

## `reverse_string()`

```python
reverse_string(s: str) -> str
```

### Description

Returns a new string containing the characters of `s` in reverse order.

The original string is not modified.

### Parameters

| Parameter | Type  | Description        |
| --------- | ----- | ------------------ |
| `s`       | `str` | String to reverse. |

### Returns

`str`

The reversed string.

### Exceptions

Raises:

* `TypeError` if `s` is not a string.

### Algorithm

The implementation uses Python string slicing with a step of `-1`:

```python
s[::-1]
```

This creates a new string whose characters appear in reverse order.

### Complexity

For a string of length `n`:

* **Time:** `O(n)`
* **Space:** `O(n)`

The additional space is required because Python strings are immutable and
the reversed string is a new string.

### Examples

```python
from pyutils.string_utils import reverse_string

reverse_string("Python")
# "nohtyP"

reverse_string("hello")
# "olleh"
```

### Edge cases

```python
reverse_string("")
# ""

reverse_string("A")
# "A"
```

---

## `is_palindrome()`

```python
is_palindrome(s: str) -> bool
```

### Description

Determines whether a string is a palindrome.

A palindrome reads identically from left to right and from right to left.

The comparison performed by this function is:

* case-sensitive;
* character-sensitive;
* performed without removing spaces or punctuation.

For example:

```python
is_palindrome("level")
# True

is_palindrome("Level")
# False
```

### Parameters

| Parameter | Type  | Description     |
| --------- | ----- | --------------- |
| `s`       | `str` | String to test. |

### Returns

`bool`

* `True` if `s` is a palindrome.
* `False` otherwise.

### Exceptions

Raises:

* `TypeError` if `s` is not a string.

### Algorithm

The implementation compares characters symmetrically from both ends of
the string.

For each position in the first half of the string, it compares:

```python
s[i]
```

with:

```python
s[len(s) - 1 - i]
```

If any pair differs, the function immediately returns `False`.

If every pair matches, the function returns `True`.

Only half of the string needs to be examined because every comparison
covers two symmetric positions.

### Complexity

For a string of length `n`:

* **Time:** `O(n)`
* **Space:** `O(1)`

The function does not create a reversed copy of the string.

### Examples

```python
from pyutils.string_utils import is_palindrome

is_palindrome("level")
# True

is_palindrome("radar")
# True

is_palindrome("python")
# False
```

### Edge cases

```python
is_palindrome("")
# True

is_palindrome("A")
# True
```

An empty string is considered a palindrome because there are no character
pairs that contradict the palindrome condition.

---

## `count_vowels()`

```python
count_vowels(s: str) -> int
```

### Description

Counts the number of vowels contained in a string.

The implementation recognizes the following characters:

```text
a e i o u
A E I O U
```

The function does not count accented vowels or other Unicode vowel
characters because they are not included in the vowel set used by the
implementation.

### Parameters

| Parameter | Type  | Description        |
| --------- | ----- | ------------------ |
| `s`       | `str` | String to analyze. |

### Returns

`int`

The number of recognized vowels in `s`.

### Exceptions

Raises:

* `TypeError` if `s` is not a string.

### Algorithm

The implementation:

1. Validates that `s` is a string.
2. Defines the recognized vowels.
3. Iterates through every character in `s`.
4. Checks whether each character belongs to the vowel set.
5. Counts every matching character.
6. Returns the total.

The counting operation is implemented using:

```python
sum(1 for char in s if char in vowels)
```

### Complexity

For a string of length `n`:

* **Time:** `O(n)`
* **Space:** `O(1)` auxiliary space.

The vowel collection contains a fixed number of characters, so membership
checking remains bounded by a constant-size collection.

### Examples

```python
from pyutils.string_utils import count_vowels

count_vowels("hello")
# 2

count_vowels("Python")
# 1

count_vowels("AEIOU")
# 5
```

### Edge cases

```python
count_vowels("")
# 0

count_vowels("rhythms")
# 0

count_vowels("HELLO")
# 2
```

---

## `word_count()`

```python
word_count(s: str) -> int
```

### Description

Counts the number of words in a string.

Words are identified using Python's `str.split()` behavior without an
explicit separator.

As a result, consecutive whitespace characters are treated as
separators and leading or trailing whitespace is ignored.

### Parameters

| Parameter | Type  | Description                           |
| --------- | ----- | ------------------------------------- |
| `s`       | `str` | String whose words should be counted. |

### Returns

`int`

The number of words contained in `s`.

### Exceptions

Raises:

* `TypeError` if `s` is not a string.

### Algorithm

The implementation uses:

```python
len(s.split())
```

When `split()` is called without an explicit separator, Python separates
the string according to whitespace.

For example:

```python
"  Python   is   powerful  ".split()
```

produces:

```python
["Python", "is", "powerful"]
```

Therefore the result is:

```text
3
```

### Complexity

For a string of length `n`:

* **Time:** `O(n)`
* **Space:** `O(n)`

`split()` creates a list containing the extracted words.

### Examples

```python
from pyutils.string_utils import word_count

word_count("Python is powerful")
# 3

word_count("Hello world")
# 2
```

### Edge cases

```python
word_count("")
# 0

word_count("   ")
# 0

word_count("  Python   is   powerful  ")
# 3
```

---

# Input Validation

All functions in this module explicitly validate their input type.

A non-string argument raises `TypeError`.

Examples:

```python
reverse_string(123)
# TypeError

is_palindrome(123)
# TypeError

count_vowels(["a", "e", "i"])
# TypeError

word_count(42)
# TypeError
```

The module therefore follows a consistent input-validation policy across
all four functions.

---

# Complexity Summary

For a string of length `n`:

| Function           |   Time | Auxiliary Space |
| ------------------ | -----: | --------------: |
| `reverse_string()` | `O(n)` |          `O(n)` |
| `is_palindrome()`  | `O(n)` |          `O(1)` |
| `count_vowels()`   | `O(n)` |          `O(1)` |
| `word_count()`     | `O(n)` |          `O(n)` |

The space complexity distinguishes between algorithms that operate
directly on the input and those that create additional string or list
objects.

---

# Design Notes

The module follows a deliberately simple design:

* explicit input validation;
* small, focused functions;
* predictable return values;
* predictable exception behavior;
* standard Python operations where they improve clarity;
* no external dependencies;
* behavior covered by automated tests.

The functions are intentionally independent and can be reused
individually by other parts of a Python application.

The module does not attempt to perform advanced natural-language
processing or Unicode linguistic analysis. Its purpose is to provide
simple and predictable string utilities.

````