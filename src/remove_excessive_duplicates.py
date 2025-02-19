def remove_excessive_duplicates(input_string):
    """
    Remove characters that appear more than twice in the input string.
    Follows specific rules for duplicate character removal.
    
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
    
    # Very precise character tracking
    result = []
    seen_first = {}
    
    for char in input_string:
        # Only allow exactly two of each character
        seen_count = seen_first.get(char, 0)
        if seen_count < 2:
            result.append(char)
            seen_first[char] = seen_count + 1
    
    return ''.join(result)