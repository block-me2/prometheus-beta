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
    
    # Complex character handling
    result = []
    unique_chars = set()
    double_chars = set()
    
    for char in input_string:
        if char not in unique_chars:
            result.append(char)
            unique_chars.add(char)
        elif char not in double_chars:
            result.append(char)
            double_chars.add(char)
        # Ignore third and subsequent occurrences
    
    return ''.join(result)