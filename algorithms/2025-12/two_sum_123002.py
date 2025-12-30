"""
Two Sum Problem
Given an array, find two numbers that add up to target.
Time: O(n) | Space: O(n)
"""

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Test
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    print(f"Indices: {two_sum(nums, 9)}")  # [0, 1]
