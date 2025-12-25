"""
Quick Sort Implementation
Time: O(n log n) avg | Space: O(log n)
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Test
if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2, 1]
    print(f"Sorted: {quick_sort(arr)}")
