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

    # Special cases 
    if numbers.count(0) > 1 and len(set(numbers)) == 1:
        return 1

    # Remove duplicates while maintaining order 
    unique_numbers = []
    seen = set()
    for num in numbers:
        if num not in seen:
            unique_numbers.append(num)
            seen.add(num)

    # Update numbers to unique list if duplicates existed 
    numbers = unique_numbers

    total_sum = sum(numbers)
    n = len(numbers)
    count = 0

    # If total sum is odd, no equal partition is possible
    if total_sum % 2 != 0:
        return 0

    # Target sum for each subset
    target_sum = total_sum // 2

    # Tracked subsets to avoid duplicates
    processed_subsets = set()

    # Try all possible combinations 
    for r in range(1, n // 2 + 1):
        for subset in combinations(numbers, r):
            # Hash the subset for tracking
            subset_key = tuple(sorted(subset))

            # Skip if we've already processed this subset combo
            if subset_key in processed_subsets:
                continue

            # Check subset sum
            if sum(subset) == target_sum:
                # Find complement and check its sum
                complement = [num for num in numbers if num not in subset]
                
                # Validate complement sum 
                if sum(complement) == target_sum:
                    # Create sorted keys to avoid duplicates
                    complement_key = tuple(sorted(complement))
                    
                    # Ensure unique subset pairing
                    if subset_key < complement_key:
                        count += 1
                        processed_subsets.add(subset_key)
                        processed_subsets.add(complement_key)

    return count