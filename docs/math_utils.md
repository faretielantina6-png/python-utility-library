````markdown
# Math Utilities

The `math_utils` module provides small, reusable utilities for common
integer-based mathematical operations.

Module:

```python
pyutils.math_utils
````

## Functions

The module provides four functions:

| Function      | Purpose                                                 |
| ------------- | ------------------------------------------------------- |
| `is_prime()`  | Determines whether an integer is prime.                 |
| `factorial()` | Calculates the factorial of a non-negative integer.     |
| `gcd()`       | Calculates the greatest common divisor of two integers. |
| `lcm()`       | Calculates the least common multiple of two integers.   |

---

## `is_prime()`

```python
is_prime(n: int) -> bool
```

### Description

Determines whether `n` is a prime number.

A prime number is an integer greater than or equal to `2` that has no
positive divisors other than `1` and itself.

### Parameters

| Parameter | Type  | Description      |
| --------- | ----- | ---------------- |
| `n`       | `int` | Integer to test. |

### Returns

`bool`

* `True` if `n` is prime.
* `False` otherwise.

### Exceptions

Raises:

* `TypeError` if `n` is not an integer.

### Algorithm

The implementation uses trial division with several early exits:

1. Validate that `n` is an integer.
2. Return `False` when `n < 2`.
3. Return `True` when `n == 2`.
4. Return `False` for even numbers greater than `2`.
5. Test only odd divisors starting from `3`.
6. Stop when `divisor * divisor > n`.

Testing divisors only up to `√n` is sufficient. If `n` has a divisor
greater than `√n`, it must have a corresponding divisor smaller than
`√n`.

### Complexity

* **Time:** `O(√n)`
* **Space:** `O(1)`

### Examples

```python
from pyutils.math_utils import is_prime

is_prime(17)
# True

is_prime(20)
# False

is_prime(2)
# True

is_prime(1)
# False
```

### Edge cases

```python
is_prime(0)
# False

is_prime(1)
# False

is_prime(2)
# True
```

---

## `factorial()`

```python
factorial(n: int) -> int
```

### Description

Calculates the factorial of a non-negative integer.

The factorial of `n` is defined as:

```text
n! = 1 × 2 × 3 × ... × n
```

with:

```text
0! = 1
```

### Parameters

| Parameter | Type  | Description           |
| --------- | ----- | --------------------- |
| `n`       | `int` | Non-negative integer. |

### Returns

`int`

The factorial of `n`.

### Exceptions

Raises:

* `TypeError` if `n` is not an integer.
* `ValueError` if `n` is negative.

### Algorithm

The implementation uses iteration:

1. Validate that `n` is an integer.
2. Reject negative values.
3. Initialize `result` to `1`.
4. Multiply `result` successively by each integer from `1` through `n`.
5. Return the accumulated result.

The implementation is iterative rather than recursive, avoiding recursive
function calls and therefore avoiding recursion-depth limitations.

### Complexity

* **Time:** `O(n)`
* **Auxiliary space:** `O(1)`

The returned integer itself can require more memory as `n` increases, but
the algorithm uses constant auxiliary space.

### Examples

```python
from pyutils.math_utils import factorial

factorial(5)
# 120

factorial(0)
# 1

factorial(7)
# 5040
```

### Edge cases

```python
factorial(0)
# 1

factorial(-1)
# ValueError
```

---

## `gcd()`

```python
gcd(a: int, b: int) -> int
```

### Description

Calculates the greatest common divisor (GCD) of two integers.

The GCD is the greatest positive integer that divides both numbers.

Negative inputs are supported. The implementation converts both values
to their absolute values before applying the algorithm.

### Parameters

| Parameter | Type  | Description     |
| --------- | ----- | --------------- |
| `a`       | `int` | First integer.  |
| `b`       | `int` | Second integer. |

### Returns

`int`

The greatest common divisor of `a` and `b`.

### Exceptions

Raises:

* `TypeError` if either `a` or `b` is not an integer.

### Algorithm

The implementation uses the **Euclidean algorithm**.

At each iteration, the pair:

```text
(a, b)
```

is replaced by:

```text
(b, a mod b)
```

The process continues until `b` becomes `0`.

At that point, `a` is the GCD.

### Complexity

* **Time:** `O(log(min(|a|, |b|)))`
* **Auxiliary space:** `O(1)`

### Examples

```python
from pyutils.math_utils import gcd

gcd(48, 18)
# 6

gcd(84, 36)
# 12

gcd(-48, 18)
# 6
```

### Edge cases

```python
gcd(0, 5)
# 5

gcd(5, 0)
# 5

gcd(0, 0)
# 0
```

---

## `lcm()`

```python
lcm(a: int, b: int) -> int
```

### Description

Calculates the least common multiple (LCM) of two integers.

The LCM is the smallest non-negative integer that is divisible by both
inputs.

For non-zero integers, the mathematical relationship is:

```text
LCM(a, b) = |a × b| / GCD(a, b)
```

The Python implementation uses integer division:

```python
abs(a * b) // gcd(a, b)
```

### Parameters

| Parameter | Type  | Description     |
| --------- | ----- | --------------- |
| `a`       | `int` | First integer.  |
| `b`       | `int` | Second integer. |

### Returns

`int`

The least common multiple of `a` and `b`.

Special cases:

* If exactly one argument is `0`, returns `0`.
* If both arguments are `0`, raises `ValueError`.

### Exceptions

Raises:

* `TypeError` if either `a` or `b` is not an integer.
* `ValueError` if both arguments are `0`.

### Algorithm

The implementation follows these steps:

1. Validate that both arguments are integers.
2. Handle the `(0, 0)` case.
3. Return `0` if exactly one argument is `0`.
4. Calculate the GCD using `gcd()`.
5. Calculate the LCM using:

```python
abs(a * b) // gcd(a, b)
```

### Complexity

* **Time:** `O(log(min(|a|, |b|)))`
* **Auxiliary space:** `O(1)`

The complexity is dominated by the call to `gcd()`.

### Examples

```python
from pyutils.math_utils import lcm

lcm(12, 18)
# 36

lcm(8, 12)
# 24

lcm(0, 5)
# 0
```

### Edge cases

```python
lcm(0, 5)
# 0

lcm(5, 0)
# 0

lcm(0, 0)
# ValueError
```

---

# Input Validation

The functions in this module explicitly validate their input types.

Examples:

```python
is_prime("17")
# TypeError

factorial(3.5)
# TypeError

gcd(10, "5")
# TypeError

lcm(10, None)
# TypeError
```

Invalid values are also rejected when required by the function's
contract.

Examples:

```python
factorial(-1)
# ValueError

lcm(0, 0)
# ValueError
```

---

# Complexity Summary

| Function      |        Time | Auxiliary Space |   |   |      |        |
| ------------- | ----------: | --------------: | - | - | ---- | ------ |
| `is_prime()`  |     `O(√n)` |          `O(1)` |   |   |      |        |
| `factorial()` |      `O(n)` |          `O(1)` |   |   |      |        |
| `gcd()`       | `O(log(min( |               a | , | b | )))` | `O(1)` |
| `lcm()`       | `O(log(min( |               a | , | b | )))` | `O(1)` |

The complexity values describe the algorithms implemented in the module,
not the cost of Python's arbitrary-precision integer arithmetic itself.

---

# Design Notes

The module follows a deliberately simple design:

* explicit input validation;
* small, focused functions;
* iterative algorithms where appropriate;
* constant auxiliary space where practical;
* predictable exception behavior;
* reusable functions without unnecessary abstractions.

The implementations are intentionally independent of external
dependencies and rely only on Python's standard functionality.

The behavior described in this document is covered by the project's
automated test suite.

````