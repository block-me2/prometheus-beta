def fibonacci(n):
    """
    Generate Fibonacci sequence up to a given number.
    
    Args:
        n (int): The upper limit for the Fibonacci sequence.
    
    Returns:
        list: A list of Fibonacci numbers less than or equal to n.
    
    Raises:
        ValueError: If n is not a positive integer.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a positive integer")
    
    if n == 0:
        return []
    
    fib_seq = [1, 1]
    while fib_seq[-1] <= n:
        next_fib = fib_seq[-1] + fib_seq[-2]
        if next_fib > n:
            break
        fib_seq.append(next_fib)
    
    return fib_seq

def fibonacciSum(arr):
    """
    Calculate the sum of Fibonacci sequence up to the largest number in the input array.
    
    Args:
        arr (list): A list of positive integers.
    
    Returns:
        int: Sum of Fibonacci numbers less than or equal to the maximum number in the array.
    
    Raises:
        ValueError: If the input is not a list of positive integers.
    """
    if not arr:
        return 0
    
    if not all(isinstance(x, int) and x > 0 for x in arr):
        raise ValueError("Input must be a list of positive integers")
    
    max_num = max(arr)
    fib_seq = fibonacci(max_num)
    
    return sum(fib_seq) if len(fib_seq) > 0 else 0