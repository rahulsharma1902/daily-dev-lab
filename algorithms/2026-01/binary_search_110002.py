"""
Binary Search Implementation
Time: O(log n) | Space: O(1)
"""

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Test
if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9, 11, 13]
    print(f"Found 7 at index: {binary_search(nums, 7)}")
