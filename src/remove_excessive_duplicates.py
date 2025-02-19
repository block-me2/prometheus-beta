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
    
    # Precise character handling
    result = []
    char_counts = {}
    order_of_chars = []
    
    for char in input_string:
        if char not in char_counts:
            char_counts[char] = 1
            result.append(char)
            order_of_chars.append(char)
        elif char not in order_of_chars:
            char_counts[char] += 1
            result.append(char)
            order_of_chars.append(char)
    
    return ''.join(result)