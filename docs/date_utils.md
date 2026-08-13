````markdown
# Date Utilities

The `date_utils` module provides small, reusable utilities for common
operations involving Python `datetime.date` objects.

Module:

```python
pyutils.date_utils
````

## Functions

The module currently provides four functions:

* `days_between_dates()`
* `add_days()`
* `is_weekend()`
* `format_date()`

---

## `days_between_dates()`

```python
days_between_dates(start: date, end: date) -> int
```

### Description

Returns the number of days between two dates.

The result is the signed difference:

```text
end - start
```

Therefore:

* if `end` is after `start`, the result is positive;
* if `end` is before `start`, the result is negative;
* if both dates are equal, the result is `0`.

### Parameters

| Parameter | Type   | Description    |
| --------- | ------ | -------------- |
| `start`   | `date` | Starting date. |
| `end`     | `date` | Ending date.   |

### Returns

`int`

The signed number of days between `start` and `end`.

### Exceptions

Raises `TypeError` if either argument is not a
`datetime.date` object.

### Algorithm

The function relies on Python's native date subtraction:

```python
(end - start).days
```

Python calculates the difference between the two dates and exposes the
result through the `days` attribute of the resulting `timedelta`.

### Complexity

* **Time:** `O(1)`
* **Space:** `O(1)`

### Examples

```python
from datetime import date
from pyutils.date_utils import days_between_dates

days_between_dates(
    date(2026, 8, 10),
    date(2026, 8, 15)
)
# 5
```

The order matters:

```python
days_between_dates(
    date(2026, 8, 15),
    date(2026, 8, 10)
)
# -5
```

Identical dates return zero:

```python
days_between_dates(
    date(2026, 8, 10),
    date(2026, 8, 10)
)
# 0
```

---

## `add_days()`

```python
add_days(dates: date, days: int) -> date
```

### Description

Returns a new date obtained by adding a specified number of days to
the given date.

The original `date` object is not modified.

Positive and negative values are supported:

* positive `days` moves forward;
* negative `days` moves backward;
* `0` returns an equivalent date.

### Parameters

| Parameter | Type   | Description            |
| --------- | ------ | ---------------------- |
| `dates`   | `date` | Starting date.         |
| `days`    | `int`  | Number of days to add. |

### Returns

`date`

A new `datetime.date` object representing the resulting date.

### Exceptions

Raises:

* `TypeError` if `dates` is not a `datetime.date`;
* `TypeError` if `days` is not an integer.

### Algorithm

The function uses `datetime.timedelta`:

```python
dates + timedelta(days=days)
```

The `timedelta` represents the requested duration, which is then added
to the input date.

### Complexity

* **Time:** `O(1)`
* **Space:** `O(1)`

### Examples

```python
from datetime import date
from pyutils.date_utils import add_days

add_days(date(2026, 8, 10), 5)
# date(2026, 8, 15)
```

Negative values move backward:

```python
add_days(date(2026, 8, 10), -3)
# date(2026, 8, 7)
```

Zero leaves the date unchanged:

```python
add_days(date(2026, 8, 10), 0)
# date(2026, 8, 10)
```

---

## `is_weekend()`

```python
is_weekend(dates: date) -> bool
```

### Description

Determines whether a date falls on a weekend.

The function considers:

* Saturday as a weekend;
* Sunday as a weekend;
* Monday through Friday as weekdays.

### Parameters

| Parameter | Type   | Description       |
| --------- | ------ | ----------------- |
| `dates`   | `date` | Date to evaluate. |

### Returns

`bool`

* `True` if the date is Saturday or Sunday;
* `False` otherwise.

### Exceptions

Raises `TypeError` if `dates` is not a
`datetime.date` object.

### Algorithm

The function obtains the weekday index using
`date.weekday()`.

Python uses the following numbering:

```text
Monday    = 0
Tuesday   = 1
Wednesday = 2
Thursday  = 3
Friday    = 4
Saturday  = 5
Sunday    = 6
```

The function therefore checks whether the weekday value belongs to:

```text
{5, 6}
```

### Complexity

* **Time:** `O(1)`
* **Space:** `O(1)`

### Examples

```python
from datetime import date
from pyutils.date_utils import is_weekend

is_weekend(date(2026, 8, 8))
# True
```

```python
is_weekend(date(2026, 8, 10))
# False
```

---

## `format_date()`

```python
format_date(dates: date) -> str
```

### Description

Converts a `datetime.date` object into a formatted string using the
day/month/year representation:

```text
DD/MM/YYYY
```

The function always uses two digits for the day and month.

### Parameters

| Parameter | Type   | Description     |
| --------- | ------ | --------------- |
| `dates`   | `date` | Date to format. |

### Returns

`str`

A string formatted as:

```text
DD/MM/YYYY
```

### Exceptions

Raises `TypeError` if `dates` is not a `datetime.date` object.

### Algorithm

The function uses `strftime()` with the format:

```text
%d/%m/%Y
```

The format components are:

| Directive | Meaning            |
| --------- | ------------------ |
| `%d`      | Day, zero-padded   |
| `%m`      | Month, zero-padded |
| `%Y`      | Four-digit year    |

### Complexity

* **Time:** `O(1)`
* **Space:** `O(1)`

### Examples

```python
from datetime import date
from pyutils.date_utils import format_date

format_date(date(2026, 8, 8))
# "08/08/2026"
```

Single-digit values are zero-padded:

```python
format_date(date(2026, 1, 5))
# "05/01/2026"
```

---

# Input Validation

The functions in this module explicitly validate their input types.

Examples:

```python
from pyutils.date_utils import (
    days_between_dates,
    add_days,
    is_weekend,
    format_date,
)

days_between_dates("2026-08-10", "2026-08-15")
# TypeError

add_days("2026-08-10", 5)
# TypeError

add_days(date(2026, 8, 10), "5")
# TypeError

is_weekend("2026-08-08")
# TypeError

format_date("2026-08-08")
# TypeError
```

The module expects actual `datetime.date` objects rather than strings
representing dates.

For example:

```python
from datetime import date

format_date(date(2026, 8, 8))
# "08/08/2026"
```

---

# Design Notes

The implementations favor:

* explicit input validation;
* Python's standard `datetime` library;
* simple and readable algorithms;
* constant time and auxiliary space for the provided operations;
* immutable date calculations;
* behavior that can be verified through automated tests.

The module intentionally provides a small set of focused operations.
It does not attempt to implement a complete date/time framework.

---

# Complexity Summary

| Function               | Time   | Space  | Main technique      |
| ---------------------- | ------ | ------ | ------------------- |
| `days_between_dates()` | `O(1)` | `O(1)` | `date` subtraction  |
| `add_days()`           | `O(1)` | `O(1)` | `timedelta`         |
| `is_weekend()`         | `O(1)` | `O(1)` | weekday calculation |
| `format_date()`        | `O(1)` | `O(1)` | `strftime()`        |

---

# Verification

The behavior of the module is covered by automated tests.

From the project root:

```powershell
python -m pytest
```

The date utilities are tested together with the other modules of the
`pyutils` package.

The expected project test suite currently covers:

* valid dates;
* identical dates;
* dates in reverse order;
* positive and negative day offsets;
* weekend and weekday detection;
* date formatting;
* invalid input types;
* edge cases relevant to each function.

```