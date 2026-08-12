def remove_duplicates(items: list)-> list:
    """Removes duplicates from a list while preserving the order of elements."""

    if not isinstance(items,list):
        raise TypeError("Items must be a list.")
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def flatten_list(items: list) -> list:
    """Flattens a list of lists into a single list."""

    if not isinstance(items,list):
        raise TypeError("Items must be a list.")
    result = []
    for sublist in items:
        if isinstance(sublist, list):
            result.extend(sublist)
        else:
            raise TypeError("All elements of the input list must be lists.")
    return result

def find_max(items: list) ->int:
    """Finds the maximum value in a list."""

    if not isinstance(items,list):
        raise TypeError("Items must be a list.")
    if not items:
        raise ValueError("Cannot find max of an empty list.")
    max_value = items[0]
    for item in items:
        if item > max_value:
            max_value = item
    return max_value

def chunk_list(items: list, size: int) -> list:
    """Chunks a list into sublists of a specified size."""
    if not isinstance(items, list):
        raise TypeError("Items must be a list.")
    if not isinstance(size, int):
        raise TypeError("Size must be an integer.")
    if size <= 0:
        raise ValueError("Size must be a positive integer.")
    result = []
    for i in range(0, len(items), size):
        result.append(items[i:i + size])
    return result