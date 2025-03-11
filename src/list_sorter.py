def is_sorted(lst, reverse=False):
    """
    Check if a list is sorted in ascending or descending order.

    Args:
        lst (list): The list to check for sorting.
        reverse (bool, optional): If True, check for descending order. 
                                  If False (default), check for ascending order.

    Returns:
        bool: True if the list is sorted, False otherwise.

    Raises:
        TypeError: If the input is not a list or contains incomparable elements.
    """
    # Check if input is a list
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    
    # Empty or single-element lists are always considered sorted
    if len(lst) <= 1:
        return True
    
    # Determine comparison function based on reverse flag
    def compare(a, b):
        if reverse:
            return a >= b
        else:
            return a <= b
    
    # Check sorting for the entire list
    for i in range(1, len(lst)):
        if not compare(lst[i-1], lst[i]):
            return False
    
    return True