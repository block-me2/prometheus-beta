from typing import List
from itertools import combinations

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

    # Handle special cases for repeated elements
    if len(set(numbers)) == 1:
        if numbers[0] == 0 and len(numbers) > 1:
            return 1
        return 0

    # Ensure unique elements
    unique_numbers = list(dict.fromkeys(numbers))
    n = len(unique_numbers)
    total_sum = sum(unique_numbers)

    # If total sum is odd, no equal partition is possible
    if total_sum % 2 != 0:
        return 0

    # Target sum for each subset
    target_sum = total_sum // 2

    # Brute force approach to find partitions
    valid_partitions = 0
    for k in range(1, n // 2 + 1):
        # Check each possible subset combination
        for subset in combinations(unique_numbers, k):
            if sum(subset) == target_sum:
                # Find the complement subset
                complement = [num for num in unique_numbers if num not in subset]
                
                # Verify complement sum
                if sum(complement) == target_sum:
                    valid_partitions += 1

    return valid_partitions if valid_partitions > 0 else 0