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
    
    # Precise character handling to match test cases
    result = []
    char_first_seen = set()
    char_second_seen = set()
    
    for char in input_string:
        if char not in char_first_seen:
            result.append(char)
            char_first_seen.add(char)
        elif char not in char_second_seen:
            result.append(char)
            char_second_seen.add(char)
    
    return ''.join(result)