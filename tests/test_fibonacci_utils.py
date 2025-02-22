import pytest
from src.fibonacci_utils import fibonacci, fibonacciSum

def test_fibonacci_basic():
    assert fibonacci(0) == []
    assert fibonacci(1) == [1, 1]
    assert fibonacci(5) == [1, 1, 2, 3, 5]
    assert fibonacci(10) == [1, 1, 2, 3, 5, 8]
    assert fibonacci(20) == [1, 1, 2, 3, 5, 8, 13]

def test_fibonacci_edge_cases():
    with pytest.raises(ValueError):
        fibonacci(-1)
    with pytest.raises(ValueError):
        fibonacci("not a number")

def test_fibonacci_sum_basic():
    assert fibonacciSum([5]) == 15  # 1+1+2+3+5
    assert fibonacciSum([10]) == 32  # 1+1+2+3+5+8
    assert fibonacciSum([20]) == 62  # 1+1+2+3+5+8+13
    assert fibonacciSum([3, 7]) == 32  # up to 7: 1+1+2+3+5+8

def test_fibonacci_sum_edge_cases():
    assert fibonacciSum([]) == 0
    
    with pytest.raises(ValueError):
        fibonacciSum([-1, 5])
    
    with pytest.raises(ValueError):
        fibonacciSum(["not", "a", "number"])

def test_fibonacci_sum_multiple_inputs():
    assert fibonacciSum([2, 4, 6]) == 22  # up to 6: 1+1+2+3+5
    assert fibonacciSum([1, 100]) == 188  # up to 100: 1+1+2+3+5+8+13+21+34+55