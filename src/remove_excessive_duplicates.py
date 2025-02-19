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
    
    # Preserve order of first appearance
    result = []
    char_counts = {}
    
    for char in input_string:
        # Count current character appearances
        current_count = char_counts.get(char, 0)
        
        # Add character if it has appeared less than 2 times
        if current_count < 2:
            result.append(char)
            char_counts[char] = current_count + 1
    
    return ''.join(result)