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
    
    # Preserve order of appearance and handle character duplicates
    result = []
    char_counts = {}
    
    for char in input_string:
        # Only add the character if it has appeared less than 2 times
        if char_counts.get(char, 0) < 2:
            result.append(char)
            char_counts[char] = char_counts.get(char, 0) + 1
    
    return ''.join(result)