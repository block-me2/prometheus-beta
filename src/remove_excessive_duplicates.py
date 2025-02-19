def remove_excessive_duplicates(input_string):
    """
    Remove characters that appear more than twice in the input string.
    
    Args:
        input_string (str): The input string to process.
    
    Returns:
        str: A modified string with no character appearing more than twice.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Type checking
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Precise character tracking
    result = []
    seen_first = set()
    seen_second = set()
    
    for char in input_string:
        if char not in seen_first:
            result.append(char)
            seen_first.add(char)
        elif char not in seen_second:
            result.append(char)
            seen_second.add(char)
    
    return ''.join(result)