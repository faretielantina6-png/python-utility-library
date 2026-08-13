````markdown
# python-utility-library

A small Python utility library providing reusable functions for common
mathematical, string, list, and date operations.

## Features

The library currently provides four utility modules:

- `math_utils` — mathematical utilities
- `string_utils` — string manipulation utilities
- `list_utils` — list processing utilities
- `date_utils` — date manipulation utilities

Each module provides simple, reusable functions with explicit input
validation and documented behavior.

## Requirements

- Python 3.12+
- pytest (for running the test suite)

## Installation

Clone the repository:

```bash
git clone https://github.com/faretielantina6-png/python-utility-library.git
cd python-utility-library
````

Create a virtual environment:

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the test dependency:
The library itself currently has no external runtime dependencies.
'pytest' is required only for running the test suite.

```bash
python -m pip install pytest
```

## Usage

The utility functions can be imported directly from the `pyutils`
package.

### Mathematical utilities

```python
from pyutils.math_utils import factorial, gcd, is_prime, lcm

is_prime(17)
# True

factorial(5)
# 120

gcd(48, 18)
# 6

lcm(12, 18)
# 36
```

### String utilities

```python
from pyutils.string_utils import (
    reverse_string,
    is_palindrome,
    count_vowels,
    word_count,
)

reverse_string("Python")
# "nohtyP"

is_palindrome("radar")
# True

count_vowels("Python")
# 1

word_count("Python is powerful")
# 3
```

### List utilities

```python
from pyutils.list_utils import (
    remove_duplicates,
    flatten_list,
    find_max,
    chunk_list,
)

remove_duplicates([1, 2, 2, 3, 1])
# [1, 2, 3]

flatten_list([[1, 2], [3, 4]])
# [1, 2, 3, 4]

find_max([12, 5, 27, 8])
# 27

chunk_list([1, 2, 3, 4, 5], 2)
# [[1, 2], [3, 4], [5]]
```

### Date utilities

```python
from datetime import date

from pyutils.date_utils import (
    days_between_dates,
    add_days,
    is_weekend,
    format_date,
)

start = date(2026, 8, 10)
end = date(2026, 8, 15)

days_between_dates(start, end)
# 5

add_days(start, 5)
# datetime.date(2026, 8, 15)

is_weekend(date(2026, 8, 8))
# True

format_date(start)
# "10/08/2026"
```

## Running the tests

The project uses `pytest` for automated testing.

Run the complete test suite from the project root:

```bash
python -m pytest
```

The current test suite covers all four utility modules.

Expected result:

```text
66 passed
```

## Running the examples

Example programs are provided in the `examples/` package.

Run them from the project root with:

```bash
python -m examples.math_example
python -m examples.string_example
python -m examples.list_example
python -m examples.date_example
```

The examples demonstrate the basic usage and expected behavior of the
library functions.

## Project structure

```text
python-utility-library/
├── pyutils/
│   ├── __init__.py
│   ├── math_utils.py
│   ├── string_utils.py
│   ├── list_utils.py
│   └── date_utils.py
│
├── tests/
│   ├── test_math_utils.py
│   ├── test_string_utils.py
│   ├── test_list_utils.py
│   └── test_date_utils.py
│
├── docs/
│   ├── math_utils.md
│   ├── string_utils.md
│   ├── list_utils.md
│   └── date_utils.md
│
├── examples/
│   ├── __init__.py
│   ├── math_example.py
│   ├── string_example.py
│   ├── list_example.py
│   └── date_example.py
│
├── .gitignore
├── LICENSE
└── README.md
```

## Documentation

Detailed technical documentation is available for each module:

* [`docs/math_utils.md`](docs/math_utils.md)
* [`docs/string_utils.md`](docs/string_utils.md)
* [`docs/list_utils.md`](docs/list_utils.md)
* [`docs/date_utils.md`](docs/date_utils.md)

The module documentation describes:

* function contracts;
* parameters and return values;
* input validation;
* exceptions;
* algorithms;
* time and space complexity;
* usage examples.

## Testing workflow

The project follows a test-first development workflow:

1. Define the function contract.
2. Write tests describing the expected behavior.
3. Implement the function.
4. Run the test suite.
5. Fix implementation errors.
6. Validate the final implementation with formatting and test checks.

All implemented functions are covered by automated tests.

## Design principles

The project intentionally favors:

* simple and readable implementations;
* explicit input validation;
* reusable utility functions;
* well-defined contracts;
* appropriate algorithmic complexity;
* automated testing;
* documentation close to the implementation;
* minimal unnecessary abstraction.

The goal is not to build a large framework, but to develop a small,
maintainable Python package while applying professional software
engineering practices.

## License

This project is distributed under the license included in the
`LICENSE` file.

````