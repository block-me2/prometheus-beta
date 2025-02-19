def remove_excessive_duplicates(input_string):
    """
    Remove characters that appear more than twice in the input string.
    
    Args:
        input_string (str): The input string to process.
    
    Returns:
        str: A modified string with characters appearing more than twice removed.
    """
    # Count the occurrences of each character
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Create a new string with characters appearing twice or less
    result = ''.join(char for char in input_string if char_count[char] <= 2)
    
    return result