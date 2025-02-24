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
    numbers = list(dict.fromkeys(numbers))

    total_sum = sum(numbers)
    n = len(numbers)
    
    # If total sum is odd, no equal partition is possible
    if total_sum % 2 != 0:
        return 0

    # Target sum for each subset
    target_sum = total_sum // 2

    unique_partitions = set()

    # Comprehensive subset search
    for r in range(1, n):
        for subset in combinations(numbers, r):
            # Check if the subset sum matches the target
            if sum(subset) == target_sum:
                # Find the complement subset
                complement = tuple(num for num in numbers if num not in subset)
                
                # Ensure the complement sums match
                if sum(complement) == target_sum:
                    # Sort both subset and complement to avoid duplicates
                    subset = tuple(sorted(subset))
                    complement = tuple(sorted(complement))
                    
                    # Use a unique representation for the partition
                    partition = tuple(sorted([subset, complement]))
                    
                    # Only count unique valid partitions 
                    if partition not in unique_partitions:
                        unique_partitions.add(partition)

    return len(unique_partitions)