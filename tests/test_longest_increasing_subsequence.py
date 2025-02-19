import pytest
from src.longest_increasing_subsequence import longest_continuous_increasing_subsequence

def test_typical_case():
    assert longest_continuous_increasing_subsequence([1, 3, 5, 4, 7]) == 3

def test_decreasing_sequence():
    assert longest_continuous_increasing_subsequence([7, 5, 3, 1]) == 1

def test_equal_elements():
    assert longest_continuous_increasing_subsequence([2, 2, 2, 2]) == 1

def test_empty_array():
    assert longest_continuous_increasing_subsequence([]) == 0

def test_single_element():
    assert longest_continuous_increasing_subsequence([42]) == 1

def test_all_increasing():
    assert longest_continuous_increasing_subsequence([1, 2, 3, 4, 5, 6]) == 6

def test_multiple_subsequences():
    assert longest_continuous_increasing_subsequence([1, 3, 5, 2, 4, 6, 7, 8]) == 4