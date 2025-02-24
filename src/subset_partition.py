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

    # Handle special cases
    if len(set(numbers)) == 1:
        if numbers[0] == 0 and len(numbers) > 1:
            return 1
        return 0

    # Ensure numbers are unique 
    unique_numbers = list(dict.fromkeys(numbers))

    total_sum = sum(unique_numbers)
    n = len(unique_numbers)
    
    # If total sum is odd, no equal partition is possible
    if total_sum % 2 != 0:
        return 0

    # Target sum for each subset
    target_sum = total_sum // 2

    # Comprehensive partition tracking
    unique_partitions = set()

    # Exhaustive search for all possible partitions
    for k in range(1, n):
        for subset in combinations(unique_numbers, k):
            # Check if the subset sum matches the target
            if sum(subset) == target_sum:
                complement = tuple(num for num in unique_numbers if num not in subset)
                
                # Validate complement
                if sum(complement) == target_sum:
                    # Canonicalize the partition
                    partition = tuple(sorted([tuple(sorted(subset)), 
                                              tuple(sorted(complement))]))
                    unique_partitions.add(partition)

    return len(unique_partitions)