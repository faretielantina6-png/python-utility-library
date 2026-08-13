"""Examples of the list utilities provided by pyutils.list_utils."""

from pyutils.list_utils import (
    chunk_list,
    find_max,
    flatten_list,
    remove_duplicates,
)


def main() -> None:
    """Run examples for all list utility functions."""

    # ------------------------------------------------------------------
    # remove_duplicates
    # ------------------------------------------------------------------
    print("Remove duplicates:")

    numbers = [1, 2, 2, 3, 1, 4, 3]

    print(f"Input: {numbers}")
    print(f"remove_duplicates(numbers) -> {remove_duplicates(numbers)}")

    # ------------------------------------------------------------------
    # flatten_list
    # ------------------------------------------------------------------
    print("\nFlatten list:")

    nested_numbers = [[1, 2], [3, 4], [5]]

    print(f"Input: {nested_numbers}")
    print(f"flatten_list(nested_numbers) -> {flatten_list(nested_numbers)}")

    # ------------------------------------------------------------------
    # find_max
    # ------------------------------------------------------------------
    print("\nFind maximum:")

    values = [12, 5, 27, 8, 19]

    print(f"Input: {values}")
    print(f"find_max(values) -> {find_max(values)}")

    # ------------------------------------------------------------------
    # chunk_list
    # ------------------------------------------------------------------
    print("\nChunk list:")

    items = [1, 2, 3, 4, 5, 6, 7]

    print(f"Input: {items}")
    print(f"chunk_list(items, 3) -> {chunk_list(items, 3)}")


if __name__ == "__main__":
    main()