import pytest
from src.string_utils import replace_spaces_with_underscores

def test_replace_spaces_with_underscores():
    # Test normal case with multiple spaces
    assert replace_spaces_with_underscores("hello world") == "hello_world"
    
    # Test case with leading/trailing spaces
    assert replace_spaces_with_underscores(" hello world ") == "_hello_world_"
    
    # Test case with multiple consecutive spaces
    assert replace_spaces_with_underscores("hello  world") == "hello__world"
    
    # Test empty string
    assert replace_spaces_with_underscores("") == ""
    
    # Test string with no spaces
    assert replace_spaces_with_underscores("helloworld") == "helloworld"
    
    # Test error case: non-string input
    with pytest.raises(TypeError, match="Input must be a string"):
        replace_spaces_with_underscores(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        replace_spaces_with_underscores(None)