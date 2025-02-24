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
        ValueError: If the input list is empty or has duplicate elements.
    """
    # Validate input
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Check for duplicate elements
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

    # Special case for all zeros
    if all(num == 0 for num in numbers):
        return 1 if len(numbers) > 1 else 0

    # Keep track of processed subset combinations to avoid duplicates
    processed_subsets = set()

    # Try all possible combinations 
    for r in range(1, n // 2 + 1):
        for subset in combinations(numbers, r):
            # Skip processed or redundant subsets
            subset_key = tuple(sorted(subset))
            if subset_key in processed_subsets:
                continue

            # Check if this subset has the target sum
            if sum(subset) == target_sum:
                # Find the complementary subset 
                complement = [num for num in numbers if num not in subset]
                
                # Verify complement sum
                if sum(complement) == target_sum:
                    # Ensure each subset is unique
                    complement_key = tuple(sorted(complement))
                    subset_key = tuple(sorted(subset))
                    
                    # Only count if this is a new unique pairing
                    if subset_key < complement_key:
                        count += 1
                        processed_subsets.add(subset_key)
                        processed_subsets.add(complement_key)

    return count