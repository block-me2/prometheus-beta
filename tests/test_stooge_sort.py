import pytest
import sys
import os

# Ensure the src directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from stooge_sort import stooge_sort

def test_stooge_sort_normal_list():
    """Test sorting a normal list of integers."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert stooge_sort(arr) == sorted(arr)

def test_stooge_sort_already_sorted():
    """Test sorting an already sorted list."""
    arr = [1, 2, 3, 4, 5]
    assert stooge_sort(arr) == sorted(arr)

def test_stooge_sort_reverse_sorted():
    """Test sorting a reverse-sorted list."""
    arr = [5, 4, 3, 2, 1]
    assert stooge_sort(arr) == sorted(arr)

def test_stooge_sort_empty_list():
    """Test sorting an empty list."""
    arr = []
    assert stooge_sort(arr) == []

def test_stooge_sort_single_element():
    """Test sorting a list with a single element."""
    arr = [42]
    assert stooge_sort(arr) == [42]

def test_stooge_sort_duplicate_elements():
    """Test sorting a list with duplicate elements."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert stooge_sort(arr) == sorted(arr)

def test_stooge_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    arr = [-1, -5, 10, -3, 0, 7]
    assert stooge_sort(arr) == sorted(arr)

def test_stooge_sort_float_numbers():
    """Test sorting a list with floating-point numbers."""
    arr = [3.14, 2.71, 1.41, 0.58]
    assert stooge_sort(arr) == sorted(arr)

def test_stooge_sort_invalid_input_type():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError):
        stooge_sort("not a list")

def test_stooge_sort_non_comparable_elements():
    """Test that a list with non-comparable elements raises an error."""
    mixed_list = [1, "a", None]
    with pytest.raises(TypeError):
        stooge_sort(mixed_list)