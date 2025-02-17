import pytest
import time
from src.execution_timer import measure_execution_time

def test_measure_execution_time(capsys):
    @measure_execution_time
    def simple_function(x, y):
        return x + y
    
    # Test basic functionality
    result = simple_function(3, 4)
    assert result == 7
    
    # Check output format
    captured = capsys.readouterr()
    assert "Function simple_function took" in captured.out
    assert "seconds to execute." in captured.out

def test_measure_execution_time_with_sleep(capsys):
    @measure_execution_time
    def sleep_function(duration):
        time.sleep(duration)
    
    # Test sleep function
    sleep_function(0.1)
    
    # Check output capture
    captured = capsys.readouterr()
    assert "Function sleep_function took" in captured.out
    assert float(captured.out.split()[5]) >= 0.1

def test_measure_execution_time_with_exception(capsys):
    @measure_execution_time
    def exception_function():
        raise ValueError("Test exception")
    
    # Test exception handling
    with pytest.raises(ValueError):
        exception_function()
    
    # Check output capture
    captured = capsys.readouterr()
    assert "Function exception_function raised an exception" in captured.out