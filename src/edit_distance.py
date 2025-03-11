def edit_distance(str1: str, str2: str) -> int:
    """
    Calculate the Levenshtein (Edit) Distance between two strings.
    
    The Edit Distance is the minimum number of single-character edits 
    (insertions, deletions, or substitutions) required to change one string into another.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        int: Minimum number of edits required to transform str1 into str2
    
    Time Complexity: O(m*n), where m and n are lengths of str1 and str2
    Space Complexity: O(m*n)
    
    Examples:
        >>> edit_distance('kitten', 'sitting')
        3
        >>> edit_distance('', 'abc')
        3
        >>> edit_distance('abc', 'abc')
        0
    """
    # Handle edge cases
    if str1 is None or str2 is None:
        raise ValueError("Input strings cannot be None")
    
    # Get lengths of input strings
    m, n = len(str1), len(str2)
    
    # Create a matrix to store results of subproblems
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill first row and column for base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill the matrix using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If characters are same, no operation needed
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # Choose minimum of insert, delete, or replace
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # Delete
                    dp[i][j-1],    # Insert
                    dp[i-1][j-1]   # Replace
                )
    
    return dp[m][n]