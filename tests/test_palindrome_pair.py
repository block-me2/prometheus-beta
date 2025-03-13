import pytest
from src.palindrome_pair import palindrome_pair, is_palindrome

def test_is_palindrome():
    """Test the is_palindrome helper function."""
    assert is_palindrome(121) == True
    assert is_palindrome(123) == False
    assert is_palindrome(11) == True
    assert is_palindrome(0) == True

def test_palindrome_pair_basic_cases():
    """Test basic scenarios for palindrome_pair."""
    # Palindrome difference exists
    assert palindrome_pair([10, 20, 30, 40]) == True  # 30 - 10 = 20 (palindrome)
    assert palindrome_pair([5, 15, 25, 35]) == True  # 35 - 15 = 20 (palindrome)
    
    # No palindrome difference
    assert palindrome_pair([1, 2, 3, 4]) == False
    assert palindrome_pair([11, 22, 33, 44]) == False

def test_palindrome_pair_edge_cases():
    """Test edge cases for palindrome_pair."""
    # Empty list
    assert palindrome_pair([]) == False
    
    # Single element list
    assert palindrome_pair([5]) == False
    
    # Negative numbers
    assert palindrome_pair([-10, 0, 10]) == True  # 10 - 0 = 10 (palindrome)

def test_palindrome_pair_input_validation():
    """Test input validation for palindrome_pair."""
    # Non-list input
    with pytest.raises(TypeError):
        palindrome_pair(123)
    
    # List with non-numeric elements
    with pytest.raises(ValueError):
        palindrome_pair([1, 2, 'a', 3])

def test_palindrome_pair_floating_point():
    """Test palindrome_pair with floating point numbers."""
    assert palindrome_pair([10.5, 20.5, 30.5]) == False
    assert palindrome_pair([10.1, 20.9, 30.3]) == False