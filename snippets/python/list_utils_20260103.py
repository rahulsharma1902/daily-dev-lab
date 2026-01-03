"""
List Utility Functions
"""

def flatten(nested_list):
    """Flatten nested list."""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

def chunk(lst, size):
    """Split list into chunks."""
    return [lst[i:i + size] for i in range(0, len(lst), size)]

def unique(lst):
    """Remove duplicates preserving order."""
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

def find_duplicates(lst):
    """Find duplicate items."""
    seen = set()
    return list({x for x in lst if x in seen or seen.add(x)})

# Examples
if __name__ == "__main__":
    print(flatten([[1, 2], [3, [4, 5]]]))  # [1, 2, 3, 4, 5]
    print(chunk([1, 2, 3, 4, 5], 2))  # [[1, 2], [3, 4], [5]]
    print(unique([1, 2, 2, 3, 3, 3]))  # [1, 2, 3]
