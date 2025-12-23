"""
Bubble Sort Implementation
==========================

A simple comparison-based sorting algorithm.

Time Complexity:
    - Best:    O(n) - when array is already sorted
    - Average: O(n²)
    - Worst:   O(n²)

Space Complexity: O(1) - in-place sorting

Stable: Yes
"""

from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    """
    Sort an array using bubble sort algorithm.
    
    Args:
        arr: List of integers to sort
        
    Returns:
        Sorted list in ascending order
    """
    n = len(arr)
    result = arr.copy()  # Don't modify original
    
    for i in range(n):
        # Track if any swaps occurred
        swapped = False
        
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        
        # If no swaps, array is sorted
        if not swapped:
            break
    
    return result


def test_bubble_sort():
    """Test cases for bubble sort."""
    # Test case 1: Normal array
    assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
    
    # Test case 2: Already sorted
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    # Test case 3: Reverse sorted
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    
    # Test case 4: Empty array
    assert bubble_sort([]) == []
    
    # Test case 5: Single element
    assert bubble_sort([42]) == [42]
    
    # Test case 6: Duplicates
    assert bubble_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]
    
    print("✅ All bubble sort tests passed!")


if __name__ == "__main__":
    test_bubble_sort()
    
    # Example usage
    sample = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {sample}")
    print(f"Sorted:   {bubble_sort(sample)}")
