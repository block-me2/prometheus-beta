from typing import List, Set
from itertools import combinations

def count_equal_sum_partitions(numbers: List[int]) -> int:
    """
    Calculate the number of ways a group of distinct numbers can be 
    partitioned into two subsets with equal sums.

    Args:
        numbers (List[int]): A list of distinct integers to partition.

    Returns:
        int: The number of ways the list can be partitioned into two 
             subsets with equal total sums.

    Raises:
        ValueError: If the input list is empty or contains duplicates.
    """
    # Validate input
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    if len(set(numbers)) != len(numbers):
        raise ValueError("Input list must contain distinct numbers")

    total_sum = sum(numbers)
    n = len(numbers)
    count = 0

    # If total sum is odd, no equal partition is possible
    if total_sum % 2 != 0:
        return 0

    # Target sum for each subset
    target_sum = total_sum // 2

    # Try all possible combinations 
    for r in range(1, n // 2 + 1):
        for subset in combinations(numbers, r):
            # Check if this subset has the target sum
            if sum(subset) == target_sum:
                # Check the complementary subset
                complement = [num for num in numbers if num not in subset]
                
                # Ensure the complement has the same sum and doesn't duplicate the subset
                if sum(complement) == target_sum and sorted(subset) != sorted(complement):
                    count += 1

    # Divide by 2 to avoid double counting symmetric partitions
    return count // 2