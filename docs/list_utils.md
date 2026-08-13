````markdown
# List Utilities

The `list_utils` module provides reusable utilities for common list
processing operations.

Module:

```python
pyutils.list_utils
````

## Functions

The module currently provides four functions:

* `remove_duplicates()`
* `flatten_list()`
* `find_max()`
* `chunk_list()`

---

## `remove_duplicates()`

```python
remove_duplicates(items: list) -> list
```

### Description

Removes duplicate elements from a list while preserving the order of
their first occurrence.

The function returns a new list and does not modify the original list.

### Parameters

| Parameter | Type   | Description                             |
| --------- | ------ | --------------------------------------- |
| `items`   | `list` | List from which duplicates are removed. |

### Returns

`list`

A new list containing only the first occurrence of each element.

### Exceptions

Raises `TypeError` if `items` is not a list.

### Algorithm

The implementation uses two collections:

* `seen` — a set containing elements already encountered.
* `result` — the output list preserving the original order.

For each element:

1. Check whether the element is already in `seen`.
2. If it is not present, add it to `seen`.
3. Append it to `result`.
4. Ignore subsequent occurrences.

The use of a set provides efficient membership testing.

### Complexity

For hashable elements:

* **Time:** `O(n)` average case
* **Space:** `O(n)`

where `n` is the number of elements in the input list.

### Important Constraint

Elements must be hashable because the implementation uses a `set`.

For example, integers and strings are hashable:

```python
remove_duplicates([1, 2, 2, 3])
# [1, 2, 3]

remove_duplicates(["a", "b", "a"])
# ["a", "b"]
```

Lists and dictionaries are not hashable:

```python
remove_duplicates([[1], [1]])
# TypeError
```

---

## `flatten_list()`

```python
flatten_list(items: list) -> list
```

### Description

Flattens a list containing lists into a single list.

The function performs **one level of flattening**.

It does not recursively flatten nested lists.

The original input list is not modified.

### Parameters

| Parameter | Type   | Description               |
| --------- | ------ | ------------------------- |
| `items`   | `list` | List containing sublists. |

Each element of `items` must itself be a `list`.

### Returns

`list`

A new list containing the elements of all sublists in their original
order.

### Exceptions

Raises `TypeError` when:

* `items` is not a list;
* an element of `items` is not a list.

### Algorithm

The function:

1. Validates that the input is a list.
2. Creates an empty result list.
3. Iterates over each sublist.
4. Verifies that the element is a list.
5. Extends the result with the elements of the sublist.
6. Returns the resulting list.

### Complexity

Let `n` be the total number of elements contained in all sublists.

* **Time:** `O(n)`
* **Space:** `O(n)`

### Examples

```python
flatten_list([[1, 2], [3, 4], [5]])
# [1, 2, 3, 4, 5]

flatten_list([[1], [], [2, 3]])
# [1, 2, 3]

flatten_list([])
# []
```

The function performs only one level of flattening:

```python
flatten_list([[1, 2], [[3, 4]]])
# [1, 2, [3, 4]]
```

---

## `find_max()`

```python
find_max(items: list) -> int
```

### Description

Finds the maximum value contained in a non-empty list.

The function uses an iterative comparison algorithm rather than Python's
built-in `max()` function.

### Parameters

| Parameter | Type   | Description                          |
| --------- | ------ | ------------------------------------ |
| `items`   | `list` | Non-empty list of comparable values. |

### Returns

`int`

The greatest value found in the list.

### Exceptions

Raises:

* `TypeError` if `items` is not a list.
* `ValueError` if `items` is empty.

The elements must also support comparison with `>`.

### Algorithm

The function uses a linear scan:

1. Validate that the input is a list.
2. Reject an empty list.
3. Assume the first element is the current maximum.
4. Compare each remaining element with the current maximum.
5. Replace the maximum whenever a larger value is found.
6. Return the final maximum.

### Complexity

For `n` elements:

* **Time:** `O(n)`
* **Space:** `O(1)`

### Examples

```python
find_max([1, 2, 3, 4, 5])
# 5

find_max([-10, -4, -20])
# -4

find_max([7])
# 7
```

An empty list is invalid:

```python
find_max([])
# ValueError
```

---

## `chunk_list()`

```python
chunk_list(items: list, size: int) -> list
```

### Description

Splits a list into consecutive sublists of a specified maximum size.

The final chunk may contain fewer elements than `size`.

The original list is not modified.

### Parameters

| Parameter | Type   | Description                           |
| --------- | ------ | ------------------------------------- |
| `items`   | `list` | List to split into chunks.            |
| `size`    | `int`  | Maximum number of elements per chunk. |

`size` must be strictly positive.

### Returns

`list`

A list containing the generated chunks.

### Exceptions

Raises:

* `TypeError` if `items` is not a list.
* `TypeError` if `size` is not an integer.
* `ValueError` if `size <= 0`.

### Algorithm

The implementation iterates over the input list using a step equal to
`size`.

For each position `i`, it creates:

```python
items[i:i + size]
```

and appends the resulting slice to the output list.

### Complexity

For `n` input elements:

* **Time:** `O(n)`
* **Space:** `O(n)`

The output contains all elements of the original list distributed among
the generated chunks.

### Examples

```python
chunk_list([1, 2, 3, 4, 5], 2)
# [[1, 2], [3, 4], [5]]

chunk_list([1, 2, 3, 4], 2)
# [[1, 2], [3, 4]]

chunk_list([1, 2, 3], 10)
# [[1, 2, 3]]

chunk_list([], 3)
# []
```

Invalid chunk sizes are rejected:

```python
chunk_list([1, 2, 3], 0)
# ValueError

chunk_list([1, 2, 3], -1)
# ValueError
```

---

# Input Validation

The functions in this module explicitly validate their primary input
parameters.

Examples:

```python
remove_duplicates("abc")
# TypeError

flatten_list("abc")
# TypeError

find_max("123")
# TypeError

chunk_list("123", 2)
# TypeError
```

Functions also validate values that violate their contracts:

```python
find_max([])
# ValueError

chunk_list([1, 2, 3], 0)
# ValueError

chunk_list([1, 2, 3], -1)
# ValueError
```

---

# Design Notes

The module follows several design principles:

* explicit input validation;
* preservation of input data;
* simple and readable algorithms;
* appropriate use of Python data structures;
* explicit handling of invalid input;
* predictable return values;
* complexity appropriate to each operation;
* behavior verified through automated tests.

The implementation deliberately avoids unnecessary abstractions.

Each function represents a small, focused operation that can be reused
independently.

---

# Complexity Summary

| Function              | Time           | Auxiliary Space | Main Technique         |
| --------------------- | -------------- | --------------- | ---------------------- |
| `remove_duplicates()` | `O(n)` average | `O(n)`          | Set + linear scan      |
| `flatten_list()`      | `O(n)`         | `O(n)`          | Iteration + `extend()` |
| `find_max()`          | `O(n)`         | `O(1)`          | Linear scan            |
| `chunk_list()`        | `O(n)`         | `O(n)`          | List slicing           |

For `remove_duplicates()`, the `O(n)` time complexity assumes that the
elements are hashable and that set membership operates in average
constant time.

---

# Testing

The behavior of `list_utils` is verified using `pytest`.

The test suite covers:

* normal inputs;
* empty lists;
* duplicate elements;
* order preservation;
* invalid input types;
* invalid chunk sizes;
* negative values;
* single-element lists;
* lists containing empty sublists;
* expected exceptions.

Run the complete test suite with:

```bash
python -m pytest
```

The `list_utils` module is considered valid when all associated tests
pass.

````