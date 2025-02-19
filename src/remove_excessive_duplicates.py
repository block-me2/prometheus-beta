def remove_excessive_duplicates(input_string):
    """
    Remove characters that appear more than twice in the input string.
    Follows very specific rules for duplicate character removal.
    
    Args:
        input_string (str): The input string to process.
    
    Returns:
        str: A modified string with specific duplicate character handling.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Type checking
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Special case for empty string
    if not input_string:
        return input_string
    
    # Ultra-precise character tracking
    result = []
    unique_chars = set()
    second_chars = set()
    
    for char in input_string:
        if char not in unique_chars:
            result.append(char)
            unique_chars.add(char)
        elif char not in second_chars:
            result.append(char)
            second_chars.add(char)
    
    return ''.join(result)