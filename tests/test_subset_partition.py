import pytest
from src.subset_partition import count_equal_sum_partitions

def test_basic_partition():
    """Test a simple scenario with a clear partition"""
    numbers = [1, 2, 3, 4, 5, 7]
    # This is a constraint check - can be adjusted based on actual implementation
    assert count_equal_sum_partitions(numbers) >= 1

def test_no_partition():
    """Test a scenario with no possible equal sum partitions"""
    numbers = [1, 2, 3, 4, 5]
    assert count_equal_sum_partitions(numbers) == 0

def test_multiple_partitions():
    """Test a scenario with multiple possible partitions"""
    numbers = [1, 2, 3, 4, 5, 6]
    assert count_equal_sum_partitions(numbers) >= 1

def test_single_element_list():
    """Test handling of a single-element list"""
    numbers = [10]
    assert count_equal_sum_partitions(numbers) == 0

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        count_equal_sum_partitions([])

def test_large_list():
    """Test a larger list to ensure performance and correctness"""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert count_equal_sum_partitions(numbers) >= 1

def test_all_zero_elements():
    """Test a list of multiple zeros"""
    numbers = [0, 0, 0]
    assert count_equal_sum_partitions(numbers) == 1

def test_negative_numbers():
    """Test partitioning with negative numbers"""
    numbers = [-1, 1, 2, 3, 4, 5]
    assert count_equal_sum_partitions(numbers) >= 1