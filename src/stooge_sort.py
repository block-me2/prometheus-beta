def stooge_sort(arr):
    """
    Implement the Stooge Sort algorithm.
    
    Stooge sort is a recursive sorting algorithm with a time complexity of O(n^(log 3 / log 1.5)) ≈ O(n^2.7095).
    
    Args:
        arr (list): The input list to be sorted in-place.
    
    Returns:
        list: The sorted list.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains elements that cannot be compared.
    """
    # Type checking
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr
    
    def _stooge_sort(arr, i, j):
        """
        Recursive helper function for stooge sort.
        
        Args:
            arr (list): The list to be sorted.
            i (int): Starting index of the sublist.
            j (int): Ending index of the sublist.
        """
        # If the first element is larger than the last, swap them
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        
        # If more than 2 elements, recursively sort
        if j - i + 1 > 2:
            t = (j - i + 1) // 3
            
            # Recursively sort first 2/3
            _stooge_sort(arr, i, j - t)
            
            # Recursively sort last 2/3
            _stooge_sort(arr, i + t, j)
            
            # Recursively sort first 2/3 again
            _stooge_sort(arr, i, j - t)
        
        return arr
    
    # Call the recursive helper function on the entire list
    return _stooge_sort(arr, 0, len(arr) - 1)