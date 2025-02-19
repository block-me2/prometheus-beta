import pytest
from src.remove_excessive_duplicates import remove_excessive_duplicates

def test_remove_excessive_duplicates():
    # Test cases with different scenarios
    assert remove_excessive_duplicates('aabbbccc') == 'aabb'
    assert remove_excessive_duplicates('abcde') == 'abcde'
    assert remove_excessive_duplicates('aaaaabbbbbccccc') == 'ab'
    assert remove_excessive_duplicates('') == ''
    assert remove_excessive_duplicates('aaa') == 'aa'
    assert remove_excessive_duplicates('aabbccddeeee') == 'aabbccdd'

def test_remove_excessive_duplicates_mixed_chars():
    assert remove_excessive_duplicates('hello world') == 'hel word'
    assert remove_excessive_duplicates('programming') == 'programing'

def test_remove_excessive_duplicates_edge_cases():
    assert remove_excessive_duplicates('!!!@@@###') == '!!@#'
    assert remove_excessive_duplicates('123444555') == '1234'

def test_input_types():
    # Test with non-string input should raise TypeError
    with pytest.raises(TypeError):
        remove_excessive_duplicates(None)
    with pytest.raises(TypeError):
        remove_excessive_duplicates(123)