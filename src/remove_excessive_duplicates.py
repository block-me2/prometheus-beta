def remove_excessive_duplicates(input_string):
    """
    Remove characters that appear more than twice in the input string.
    
    Args:
        input_string (str): The input string to process.
    
    Returns:
        str: A modified string with characters appearing more than twice removed.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Type checking
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Count the occurrences of each character
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Create a new string with characters appearing twice or less
    result = []
    used_char_count = {}
    
    for char in input_string:
        # If the character appears more than twice in total, skip
        if char_count[char] > 2:
            # But allow up to two instances of such a character
            if used_char_count.get(char, 0) < 2:
                result.append(char)
                used_char_count[char] = used_char_count.get(char, 0) + 1
    
    return ''.join(result)