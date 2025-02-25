from typing import List, TypeVar, Any, Callable
from functools import cmp_to_key

T = TypeVar('T')

def patience_sort(arr: List[T], key: Callable[[T], Any] = None) -> List[T]:
    """
    Implement the Patience Sorting algorithm.
    
    Patience Sort is a sorting algorithm inspired by the card game patience (solitaire).
    It works by creating 'piles' of cards (elements) and then merging them.
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    Args:
        arr (List[T]): The input list to be sorted
        key (Optional[Callable[[T], Any]]): Optional key function for custom sorting
    
    Returns:
        List[T]: A new sorted list
    
    Raises:
        TypeError: If the input is not a list
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create piles (each pile is a sorted sublist)
    piles = []
    
    for item in arr:
        # Determine which pile to place the item in
        suitable_pile = None
        for pile in piles:
            # If pile is empty or item is less/equal to top of pile
            if not pile or key_compare(item, pile[-1], key) <= 0:
                suitable_pile = pile
                break
        
        # If no suitable existing pile, create a new pile
        if suitable_pile is None:
            piles.append([])
            suitable_pile = piles[-1]
        
        # Add item to the suitable pile
        suitable_pile.append(item)
    
    # Merge piles
    result = []
    heap = []
    
    # Add last items from each pile to heap
    for i, pile in enumerate(piles):
        if pile:
            heap.append((pile[-1], i, 1))
    
    import heapq
    # Heapify requires a custom comparison to handle complex types with key
    def heap_compare(a, b):
        return key_compare(a[0], b[0], key)
    
    heap.sort(key=cmp_to_key(heap_compare))
    
    while heap:
        val, pile_index, pile_length = heap[0]
        result.append(val)
        heap.pop(0)
        
        # If more items in the pile, add the next one
        remaining_pile = piles[pile_index][:-pile_length]
        if remaining_pile:
            new_item = remaining_pile[-1]
            heap.append((new_item, pile_index, 1))
            heap.sort(key=cmp_to_key(heap_compare))
    
    return result

def key_compare(a: T, b: T, key: Callable[[T], Any] = None) -> int:
    """
    Compare two elements using an optional key function.
    
    Args:
        a (T): First element to compare
        b (T): Second element to compare
        key (Optional[Callable[[T], Any]]): Optional key function
    
    Returns:
        int: Negative if a < b, 0 if a == b, positive if a > b
    """
    # If key function is provided, use it for comparison
    if key:
        a_val = key(a)
        b_val = key(b)
        return (a_val > b_val) - (a_val < b_val)
    
    # Try standard comparison methods
    try:
        return (a > b) - (a < b)
    except TypeError:
        # Fallback to string representation comparison
        return (str(a) > str(b)) - (str(a) < str(b))