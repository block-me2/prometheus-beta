import pytest
from src.patience_sort import patience_sort

def test_patience_sort_basic():
    """Test sorting a basic list of integers"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    assert patience_sort(arr) == sorted(arr)

def test_patience_sort_already_sorted():
    """Test sorting an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert patience_sort(arr) == arr

def test_patience_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert patience_sort(arr) == sorted(arr)

def test_patience_sort_empty_list():
    """Test sorting an empty list"""
    arr = []
    assert patience_sort(arr) == []

def test_patience_sort_single_element():
    """Test sorting a single-element list"""
    arr = [42]
    assert patience_sort(arr) == [42]

def test_patience_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    assert patience_sort(arr) == sorted(arr)

def test_patience_sort_with_strings():
    """Test sorting a list of strings"""
    arr = ['banana', 'apple', 'cherry', 'date']
    assert patience_sort(arr) == sorted(arr)

def test_patience_sort_with_mixed_types():
    """Test sorting a list with comparable mixed types"""
    class ComparableClass:
        def __init__(self, value):
            self.value = value
        
        def __repr__(self):
            return f"ComparableClass({self.value})"
    
    arr = [
        ComparableClass(3), 
        ComparableClass(1), 
        ComparableClass(4), 
        ComparableClass(1)
    ]
    sorted_arr = sorted(arr, key=lambda x: x.value)
    result = patience_sort(arr, key=lambda x: x.value)
    
    assert len(result) == len(sorted_arr)
    assert all(x.value == y.value for x, y in zip(result, sorted_arr))

def test_patience_sort_invalid_input():
    """Test that invalid input raises appropriate exceptions"""
    with pytest.raises(TypeError):
        patience_sort(None)
    
    with pytest.raises(TypeError):
        patience_sort("not a list")
    
    with pytest.raises(TypeError):
        patience_sort(123)

def test_patience_sort_immutability():
    """Test that the original list is not modified"""
    original = [3, 1, 4, 1, 5]
    copied = original.copy()
    patience_sort(original)
    assert original == copied