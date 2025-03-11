import pytest
from src.array_reversal import reverse_array

def test_reverse_normal_array():
    """Test reversing a standard list of integers."""
    input_array = [1, 2, 3, 4, 5]
    expected = [5, 4, 3, 2, 1]
    assert reverse_array(input_array) == expected

def test_reverse_empty_array():
    """Test reversing an empty list."""
    assert reverse_array([]) == []

def test_reverse_single_element_array():
    """Test reversing a list with a single element."""
    input_array = [42]
    assert reverse_array(input_array) == [42]

def test_reverse_mixed_type_array():
    """Test reversing an array with mixed types."""
    input_array = [1, 'a', True, 3.14]
    expected = [3.14, True, 'a', 1]
    assert reverse_array(input_array) == expected

def test_input_type_error():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_array("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_array(123)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_array(None)