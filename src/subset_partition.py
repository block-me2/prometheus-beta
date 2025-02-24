from typing import List, Set
from itertools import combinations

def count_equal_sum_partitions(numbers: List[int]) -> int:
    """
    Calculate the number of ways a group of distinct numbers can be 
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

    total_sum = sum(numbers)
    n = len(numbers)
    count = 0

    # If total sum is odd, no equal partition is possible
    if total_sum % 2 != 0:
        return 0

    # Target sum for each subset
    target_sum = total_sum // 2

    # Special case for all zeros
    if all(num == 0 for num in numbers):
        return 1 if len(numbers) > 1 else 0

    # Try all possible combinations 
    for r in range(1, n // 2 + 1):
        for subset in combinations(numbers, r):
            # Check if this subset has the target sum
            if sum(subset) == target_sum:
                # Check the complementary subset
                complement = [num for num in numbers if num not in subset]
                
                # Ensure the complement has the same sum 
                # and that it's not the same as the original subset
                if sum(complement) == target_sum:
                    # Include the combination only if they're not equivalent
                    if sorted(subset) < sorted(complement):
                        count += 1

    return count