import pytest
from src.decimal_to_hex import decimal_to_hex

def test_decimal_to_hex_zero():
    """Test conversion of zero."""
    assert decimal_to_hex(0) == "0"

def test_decimal_to_hex_single_digit():
    """Test conversion of single-digit decimal numbers."""
    assert decimal_to_hex(9) == "9"
    assert decimal_to_hex(10) == "A"
    assert decimal_to_hex(15) == "F"

def test_decimal_to_hex_multiple_digits():
    """Test conversion of multi-digit decimal numbers."""
    assert decimal_to_hex(16) == "10"
    assert decimal_to_hex(255) == "FF"
    assert decimal_to_hex(4096) == "1000"

def test_decimal_to_hex_large_number():
    """Test conversion of large decimal numbers."""
    assert decimal_to_hex(1048575) == "FFFFF"

def test_decimal_to_hex_invalid_input_type():
    """Test error handling for non-integer inputs."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        decimal_to_hex("100")
    with pytest.raises(TypeError, match="Input must be an integer"):
        decimal_to_hex(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        decimal_to_hex(None)

def test_decimal_to_hex_negative_number():
    """Test error handling for negative numbers."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        decimal_to_hex(-1)
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        decimal_to_hex(-100)