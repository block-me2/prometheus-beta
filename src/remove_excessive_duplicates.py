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
    
    # Precisely track first two occurrences of each character
    result = []
    first_chars = {}
    
    for char in input_string:
        if char not in first_chars:
            result.append(char)
            first_chars[char] = 1
        elif first_chars[char] == 1:
            result.append(char)
            first_chars[char] = 2
    
    return ''.join(result)