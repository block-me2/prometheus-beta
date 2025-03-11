"""
Tests for the error logging functionality.
"""

import pytest
import io
import sys

from src.error_logger import log_error

def test_log_error_normal_message(capfd):
    """Test logging a normal error message."""
    log_error("Test error message")
    
    # Capture the output
    captured = capfd.readouterr()
    assert captured.out.strip() == "ERROR: Test error message"

def test_log_error_with_whitespace(capfd):
    """Test logging an error message with whitespace."""
    log_error("  Spaced error message  ")
    
    # Capture the output
    captured = capfd.readouterr()
    assert captured.out.strip() == "ERROR: Spaced error message"

def test_log_error_raises_type_error():
    """Test that logging non-string input raises a TypeError."""
    with pytest.raises(TypeError, match="Error message must be a string"):
        log_error(123)
    
    with pytest.raises(TypeError, match="Error message must be a string"):
        log_error(None)

def test_log_error_raises_value_error():
    """Test that logging an empty string raises a ValueError."""
    with pytest.raises(ValueError, match="Error message cannot be empty"):
        log_error("")
    
    with pytest.raises(ValueError, match="Error message cannot be empty"):
        log_error("   ")