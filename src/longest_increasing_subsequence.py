def longest_continuous_increasing_subsequence(arr):
    """
    Find the length of the longest continuous increasing subsequence in an array.
    
    Args:
        arr (list): An array of integers
    
    Returns:
        int: Length of the longest continuous increasing subsequence
    
    Examples:
        - [1, 3, 5, 4, 7] returns 3 (subsequence: [1, 3, 5])
        - [2, 2, 2, 2] returns 1
        - [] returns 0
    """
    if not arr:
        return 0
    
    max_length = 1
    current_length = 1
    
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1
    
    return max_length