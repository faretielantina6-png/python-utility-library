from pyutils.list_utils import (remove_duplicates, flatten_list, find_max, chunk_list)

def test_remove_duplicates():
    assert remove_duplicates([1, 2,2,3,1]) == [1, 2, 3]

def test_remove_duplicates_empty():
    assert remove_duplicates([]) == []

def test_remove_duplicates_preserved_order():
    assert remove_duplicates([3, 1, 2, 3, 2]) == [3, 1, 2] 

def test_duplicate_invalid_type():
    try:
        remove_duplicates("123") # type: ignore[arg-type]
    except TypeError:
        pass
    else:
        assert False

def test_duplicates_unhashable_items():
    try:
        remove_duplicates([[1], [2],[1]]) # type: ignore[arg-type]
    except TypeError:
        pass
    else:
        assert False

def test_flatten_list():
    assert flatten_list([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]

def test_flatten_list_empty():
    assert flatten_list([]) == []

def test_flatten_list_empty_sublists():
    assert flatten_list([[1],[], [2, 3]]) == [1, 2, 3]

def test_flatten_list_invalid_type():
    try:
        flatten_list("123") # type: ignore[arg-type]
    except TypeError:
        pass
    else:
        assert False


def test_find_max():
    assert find_max([1, 2, 3, 4, 5]) == 5

def test_find_max_negative():
    assert find_max([-1, -2, -3]) == -1

def test_find_single_element():
    assert find_max([7]) == 7

def test_find_max_empty():
    try:
        find_max([])
    except ValueError:
        pass
    else:
        assert False 

def test_chunk_list():
    assert chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]

def test_chunk_list_exact_size():
    assert chunk_list([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]

def test_chunk_list_size():
    assert chunk_list([1, 2, 3], 10) == [[1, 2, 3]]

def test_chunk_list_empty():
    assert chunk_list([], 3) == []

def test_chunk_list_invalid_size():
    try:
        chunk_list([1, 2, 3], 0)
    except ValueError:
        pass
    else:
        assert False
