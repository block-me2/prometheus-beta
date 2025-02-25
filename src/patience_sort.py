from typing import List, TypeVar, Any

T = TypeVar('T')

def patience_sort(arr: List[T]) -> List[T]:
    """
    Implement the Patience Sorting algorithm.
    
    Patience Sort is a sorting algorithm inspired by the card game patience (solitaire).
    It works by creating 'piles' of cards (elements) and then merging them.
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    Args:
        arr (List[T]): The input list to be sorted
    
    Returns:
        List[T]: A new sorted list
    
    Raises:
        TypeError: If the input is not a list
        TypeError: If list elements cannot be compared
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
        # Find the rightmost pile where we can place the item
        suitable_pile = None
        for pile in piles:
            # If pile is empty or item is less than/equal to top of pile
            if not pile or try_less_than_or_equal(item, pile[-1]):
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
    heap = [(pile[-1], i) for i, pile in enumerate(piles)]
    
    # Use Python's heapq for efficient min-heap operations
    import heapq
    heapq.heapify(heap)
    
    while heap:
        val, pile_index = heapq.heappop(heap)
        result.append(val)
        
        # Remove the top element from its pile
        piles[pile_index].pop()
        
        # If pile is not empty, add its new top to the heap
        if piles[pile_index]:
            heapq.heappush(heap, (piles[pile_index][-1], pile_index))
    
    return result

def try_less_than_or_equal(a: T, b: T) -> bool:
    """
    Try to compare two elements safely, raising TypeError if not comparable.
    
    Args:
        a (T): First element to compare
        b (T): Second element to compare
    
    Returns:
        bool: True if a <= b, False otherwise
    
    Raises:
        TypeError: If elements cannot be compared
    """
    try:
        return a <= b
    except TypeError:
        raise TypeError(f"Cannot compare {type(a)} and {type(b)}")