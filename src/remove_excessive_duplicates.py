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
    
    # Track character counts and store sequences in order
    seen_chars = {}
    result = []
    
    for char in input_string:
        if char not in seen_chars:
            seen_chars[char] = 1
            result.append(char)
        elif seen_chars[char] == 1:
            seen_chars[char] += 1
            result.append(char)
        # Do nothing for third and subsequent occurrences
    
    return ''.join(result)