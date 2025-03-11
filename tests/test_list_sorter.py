import pytest
from src.list_sorter import is_sorted

def test_empty_list():
    """Test that an empty list is considered sorted."""
    assert is_sorted([]) == True

def test_single_element_list():
    """Test that a single-element list is considered sorted."""
    assert is_sorted([42]) == True

def test_sorted_list_ascending():
    """Test a sorted list in ascending order."""
    assert is_sorted([1, 2, 3, 4, 5]) == True

def test_sorted_list_descending():
    """Test a sorted list in descending order with reverse flag."""
    assert is_sorted([5, 4, 3, 2, 1], reverse=True) == True

def test_unsorted_list_ascending():
    """Test an unsorted list in non-ascending order."""
    assert is_sorted([1, 3, 2, 4, 5]) == False

def test_unsorted_list_descending():
    """Test an unsorted list in non-descending order with reverse flag."""
    assert is_sorted([5, 3, 4, 2, 1], reverse=True) == False

def test_list_with_duplicates_ascending():
    """Test a sorted list with duplicate elements in ascending order."""
    assert is_sorted([1, 2, 2, 3, 4]) == True

def test_list_with_duplicates_descending():
    """Test a sorted list with duplicate elements in descending order."""
    assert is_sorted([5, 4, 4, 3, 2], reverse=True) == True

def test_list_with_mixed_types():
    """Test sorting with comparable mixed types."""
    assert is_sorted([1, 2.0, 3]) == True

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError):
        is_sorted("not a list")

def test_list_with_uncomparable_types():
    """Test behavior with uncomparable types."""
    with pytest.raises(TypeError):
        is_sorted([1, "a", 3])