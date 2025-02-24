from typing import List

def count_equal_sum_partitions(numbers: List[int]) -> int:
    """
    Calculate the number of ways a group of numbers can be 
    partitioned into two subsets with equal sums.

    Args:
        numbers (List[int]): A list of integers to partition.

    Returns:
        int: The number of ways the list can be partitioned into two 
             subsets with equal total sums.

    Raises:
        ValueError: If the input list is empty.
    """
    # Validate input
    if not numbers:
        raise ValueError("Input list cannot be empty")

    # Handle special cases
    if len(set(numbers)) == 1:
        if numbers[0] == 0 and len(numbers) > 1:
            return 1
        return 0

    # Remove duplicates while maintaining order
    unique_numbers = list(dict.fromkeys(numbers))
    total_sum = sum(unique_numbers)
    
    # If total sum is odd, no equal partition is possible
    if total_sum % 2 != 0:
        return 0

    # Target sum for each subset
    target_sum = total_sum // 2
    n = len(unique_numbers)

    # Dynamic Programming approach
    # dp[i][j] represents if sum j can be achieved using first i elements
    dp = [[False] * (target_sum + 1) for _ in range(n + 1)]
    
    # Empty subset can always make a sum of 0
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            # If current number is less than target sum
            if unique_numbers[i-1] <= j:
                dp[i][j] = dp[i-1][j - unique_numbers[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    # If target sum is achievable, count partitions
    if not dp[n][target_sum]:
        return 0

    # Reconstruct at least one valid partition
    subset = []
    j = target_sum
    for i in range(n, 0, -1):
        if j >= unique_numbers[i-1] and dp[i-1][j - unique_numbers[i-1]]:
            subset.append(unique_numbers[i-1])
            j -= unique_numbers[i-1]

    # Validate partition
    complement = [num for num in unique_numbers if num not in subset]
    
    # Ensure a valid partition exists 
    return 1 if sum(subset) == sum(complement) == target_sum else 0