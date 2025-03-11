import pytest
from src.edit_distance import edit_distance

def test_same_string():
    """Test edit distance between identical strings is 0"""
    assert edit_distance('hello', 'hello') == 0

def test_empty_strings():
    """Test edit distance with empty strings"""
    assert edit_distance('', '') == 0
    assert edit_distance('', 'abc') == 3
    assert edit_distance('abc', '') == 3

def test_different_strings():
    """Test edit distance for strings requiring multiple edits"""
    assert edit_distance('kitten', 'sitting') == 3
    assert edit_distance('sunday', 'saturday') == 3

def test_case_sensitivity():
    """Test edit distance is case-sensitive"""
    assert edit_distance('Hello', 'hello') == 1

def test_unicode_strings():
    """Test edit distance with unicode characters"""
    assert edit_distance('café', 'cafe') == 1

def test_long_strings():
    """Test edit distance with longer strings"""
    assert edit_distance('algorithm', 'logarithm') == 3

def test_none_input():
    """Test that None input raises a ValueError"""
    with pytest.raises(ValueError, match="Input strings cannot be None"):
        edit_distance(None, 'test')
    with pytest.raises(ValueError, match="Input strings cannot be None"):
        edit_distance('test', None)
    with pytest.raises(ValueError, match="Input strings cannot be None"):
        edit_distance(None, None)

def test_one_character_different():
    """Test edit distance for strings with one character difference"""
    assert edit_distance('cat', 'cut') == 1
    assert edit_distance('cat', 'car') == 1
    assert edit_distance('cat', 'at') == 1