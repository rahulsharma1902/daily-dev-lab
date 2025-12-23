"""
Binary Search Implementation
============================

An efficient search algorithm for sorted arrays.

Time Complexity:
    - Best:    O(1)
    - Average: O(log n)
    - Worst:   O(log n)

Space Complexity: 
    - Iterative: O(1)
    - Recursive: O(log n) due to call stack

Prerequisites: Array must be sorted
"""

from typing import List, Optional


def binary_search_iterative(arr: List[int], target: int) -> int:
    """
    Find target in sorted array using iterative binary search.
    
    Args:
        arr: Sorted list of integers
        target: Value to find
        
    Returns:
        Index of target if found, -1 otherwise
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_recursive(arr: List[int], target: int, 
                           left: int = None, right: int = None) -> int:
    """
    Find target in sorted array using recursive binary search.
    
    Args:
        arr: Sorted list of integers
        target: Value to find
        left: Left boundary (optional)
        right: Right boundary (optional)
        
    Returns:
        Index of target if found, -1 otherwise
    """
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def test_binary_search():
    """Test cases for binary search."""
    sorted_arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
    # Test iterative version
    assert binary_search_iterative(sorted_arr, 7) == 3
    assert binary_search_iterative(sorted_arr, 1) == 0
    assert binary_search_iterative(sorted_arr, 19) == 9
    assert binary_search_iterative(sorted_arr, 8) == -1
    assert binary_search_iterative([], 5) == -1
    
    # Test recursive version
    assert binary_search_recursive(sorted_arr, 7) == 3
    assert binary_search_recursive(sorted_arr, 1) == 0
    assert binary_search_recursive(sorted_arr, 19) == 9
    assert binary_search_recursive(sorted_arr, 8) == -1
    
    print("✅ All binary search tests passed!")


if __name__ == "__main__":
    test_binary_search()
    
    # Example usage
    sample = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target = 23
    
    result = binary_search_iterative(sample, target)
    print(f"Array: {sample}")
    print(f"Searching for {target}: found at index {result}")
