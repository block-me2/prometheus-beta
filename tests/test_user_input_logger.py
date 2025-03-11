import os
import pytest
import logging
import sys
from io import StringIO
from src.user_input_logger import log_user_input

def test_log_user_input_console(monkeypatch, caplog):
    """Test logging user input to console"""
    # Simulate user input
    monkeypatch.setattr('builtins.input', lambda _: "Test input")
    
    # Capture logging
    caplog.set_level(logging.INFO)
    
    # Call the function
    result = log_user_input()
    
    # Assertions
    assert result == "Test input"
    assert "Test input" in caplog.text

def test_log_user_input_file(monkeypatch, tmp_path):
    """Test logging user input to a file"""
    # Create a temporary log file
    log_file = tmp_path / "test_log.txt"
    
    # Simulate user input
    monkeypatch.setattr('builtins.input', lambda _: "File logging test")
    
    # Call the function with log file
    result = log_user_input(str(log_file))
    
    # Read log file contents
    with open(log_file, 'r') as f:
        log_contents = f.read()
    
    # Assertions
    assert result == "File logging test"
    assert "File logging test" in log_contents

def test_log_user_input_empty(monkeypatch):
    """Test that empty input raises a ValueError"""
    # Simulate empty input
    monkeypatch.setattr('builtins.input', lambda _: "")
    
    # Expect ValueError
    with pytest.raises(ValueError, match="Input cannot be empty"):
        log_user_input()

def test_log_user_input_whitespace(monkeypatch):
    """Test that whitespace-only input raises a ValueError"""
    # Simulate whitespace input
    monkeypatch.setattr('builtins.input', lambda _: "   \t\n")
    
    # Expect ValueError
    with pytest.raises(ValueError, match="Input cannot be empty"):
        log_user_input()