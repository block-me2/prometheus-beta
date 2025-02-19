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
    
    # Track first two unique occurrences carefully
    result = []
    char_counts = {}
    unique_chars = set()
    
    for char in input_string:
        # First time seeing this character
        if char not in char_counts:
            result.append(char)
            char_counts[char] = 1
            unique_chars.add(char)
        # Second time seeing this character
        elif char_counts[char] == 1:
            result.append(char)
            char_counts[char] = 2
        # Implicit third time and beyond: ignore
    
    return ''.join(result)