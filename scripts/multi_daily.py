#!/usr/bin/env python3
"""
Multi-Commit Daily Script with Natural Random Content
======================================================

Creates realistic, varied commits with actual code implementations.
Looks natural - not like bot-generated content.
"""

import os
import subprocess
import random
from datetime import datetime
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent.parent / ".env")
except ImportError:
    pass

PROJECT_ROOT = Path(__file__).parent.parent.resolve()

# ============================================================
# REAL CODE SNIPPETS - Actual working implementations
# ============================================================

ALGORITHMS = {
    "binary_search": '''"""
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
''',
    
    "two_sum": '''"""
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
''',

    "merge_sort": '''"""
Merge Sort Implementation
Time: O(n log n) | Space: O(n)
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Sorted: {merge_sort(arr)}")
''',

    "quick_sort": '''"""
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
''',

    "fibonacci": '''"""
Fibonacci with Memoization
Time: O(n) | Space: O(n)
"""

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

# Iterative version
def fib_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Test
if __name__ == "__main__":
    for i in range(10):
        print(f"F({i}) = {fibonacci(i)}")
''',

    "linked_list": '''"""
Singly Linked List Implementation
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
    
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# Test
if __name__ == "__main__":
    ll = LinkedList()
    for i in [1, 2, 3, 4, 5]:
        ll.append(i)
    print(f"List: {ll.display()}")
    ll.reverse()
    print(f"Reversed: {ll.display()}")
''',

    "stack_queue": '''"""
Stack and Queue Implementation
"""

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop() if self.items else None
    
    def peek(self):
        return self.items[-1] if self.items else None
    
    def is_empty(self):
        return len(self.items) == 0

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0) if self.items else None
    
    def is_empty(self):
        return len(self.items) == 0

# Test
if __name__ == "__main__":
    s = Stack()
    s.push(1); s.push(2); s.push(3)
    print(f"Stack pop: {s.pop()}")  # 3
    
    q = Queue()
    q.enqueue(1); q.enqueue(2); q.enqueue(3)
    print(f"Queue dequeue: {q.dequeue()}")  # 1
''',

    "binary_tree": '''"""
Binary Tree Implementation with Traversals
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root, result=None):
    if result is None:
        result = []
    if root:
        inorder(root.left, result)
        result.append(root.val)
        inorder(root.right, result)
    return result

def preorder(root, result=None):
    if result is None:
        result = []
    if root:
        result.append(root.val)
        preorder(root.left, result)
        preorder(root.right, result)
    return result

def postorder(root, result=None):
    if result is None:
        result = []
    if root:
        postorder(root.left, result)
        postorder(root.right, result)
        result.append(root.val)
    return result

# Test
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print(f"Inorder: {inorder(root)}")
    print(f"Preorder: {preorder(root)}")
    print(f"Postorder: {postorder(root)}")
''',

    "hash_table": '''"""
Hash Table Implementation
"""

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)
                return
        self.table[idx].append((key, value))
    
    def get(self, key):
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return None
    
    def remove(self, key):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                del self.table[idx][i]
                return True
        return False

# Test
if __name__ == "__main__":
    ht = HashTable()
    ht.put("name", "Alice")
    ht.put("age", 25)
    print(f"name: {ht.get('name')}")
    print(f"age: {ht.get('age')}")
''',

    "bfs_dfs": '''"""
Graph Traversal: BFS and DFS
"""

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(graph.get(node, []))
    
    return result

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    
    return result

# Test
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [], 'E': [], 'F': []
    }
    print(f"BFS: {bfs(graph, 'A')}")
    print(f"DFS: {dfs(graph, 'A')}")
''',

    "palindrome": '''"""
Palindrome Checker - Multiple Approaches
"""

def is_palindrome_simple(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

def is_palindrome_two_pointer(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Test
if __name__ == "__main__":
    test_cases = ["A man a plan a canal Panama", "race a car", "Was it a car or a cat I saw"]
    for tc in test_cases:
        print(f"'{tc}': {is_palindrome_simple(tc)}")
''',

    "anagram": '''"""
Anagram Checker and Grouping
"""

from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1.lower()) == Counter(s2.lower())

def group_anagrams(words):
    groups = {}
    for word in words:
        key = ''.join(sorted(word.lower()))
        groups.setdefault(key, []).append(word)
    return list(groups.values())

# Test
if __name__ == "__main__":
    print(f"listen vs silent: {is_anagram('listen', 'silent')}")
    
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"Grouped: {group_anagrams(words)}")
''',
}

SNIPPETS = {
    "api_request": '''"""
API Request Helper
"""
import json
from urllib.request import urlopen, Request
from urllib.error import URLError

def make_request(url, method="GET", data=None, headers=None):
    """Make HTTP request and return JSON response."""
    headers = headers or {"Content-Type": "application/json"}
    
    if data and isinstance(data, dict):
        data = json.dumps(data).encode()
    
    try:
        req = Request(url, data=data, headers=headers, method=method)
        with urlopen(req, timeout=10) as response:
            return json.loads(response.read().decode())
    except URLError as e:
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    result = make_request("https://api.github.com")
    print(f"Response keys: {list(result.keys())[:5]}")
''',

    "file_utils": '''"""
File Utility Functions
"""
import os
import json
from pathlib import Path

def read_json(filepath):
    """Read JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)

def write_json(filepath, data, indent=2):
    """Write data to JSON file."""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=indent)

def list_files(directory, extension=None):
    """List files in directory."""
    path = Path(directory)
    if extension:
        return list(path.glob(f"*.{extension}"))
    return list(path.iterdir())

def get_file_size(filepath):
    """Get file size in human readable format."""
    size = os.path.getsize(filepath)
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"

# Example
if __name__ == "__main__":
    print(f"Current dir files: {len(list_files('.'))}")
''',

    "string_utils": '''"""
String Utility Functions
"""

def camel_to_snake(name):
    """Convert camelCase to snake_case."""
    result = [name[0].lower()]
    for char in name[1:]:
        if char.isupper():
            result.extend(['_', char.lower()])
        else:
            result.append(char)
    return ''.join(result)

def snake_to_camel(name):
    """Convert snake_case to camelCase."""
    components = name.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def truncate(text, length=50, suffix='...'):
    """Truncate text to specified length."""
    if len(text) <= length:
        return text
    return text[:length - len(suffix)] + suffix

def word_count(text):
    """Count words in text."""
    return len(text.split())

# Examples
if __name__ == "__main__":
    print(camel_to_snake("myVariableName"))  # my_variable_name
    print(snake_to_camel("my_variable_name"))  # myVariableName
''',

    "date_utils": '''"""
Date Utility Functions
"""
from datetime import datetime, timedelta

def days_between(date1, date2):
    """Calculate days between two dates."""
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def add_days(date_str, days):
    """Add days to a date string."""
    date = datetime.strptime(date_str, "%Y-%m-%d")
    new_date = date + timedelta(days=days)
    return new_date.strftime("%Y-%m-%d")

def is_weekend(date_str):
    """Check if date is weekend."""
    date = datetime.strptime(date_str, "%Y-%m-%d")
    return date.weekday() >= 5

def format_date(date_str, from_fmt="%Y-%m-%d", to_fmt="%B %d, %Y"):
    """Convert date format."""
    date = datetime.strptime(date_str, from_fmt)
    return date.strftime(to_fmt)

# Examples
if __name__ == "__main__":
    today = datetime.now().strftime("%Y-%m-%d")
    print(f"Today: {format_date(today)}")
    print(f"Is weekend: {is_weekend(today)}")
''',

    "list_utils": '''"""
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
''',

    "math_utils": '''"""
Math Utility Functions
"""
import math

def is_prime(n):
    """Check if number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    """Greatest common divisor."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Least common multiple."""
    return abs(a * b) // gcd(a, b)

def factorial(n):
    """Calculate factorial."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def prime_factors(n):
    """Get prime factors of a number."""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

# Examples
if __name__ == "__main__":
    print(f"Is 17 prime? {is_prime(17)}")
    print(f"GCD(48, 18) = {gcd(48, 18)}")
    print(f"Prime factors of 84: {prime_factors(84)}")
''',
}

TIL_TOPICS = [
    ("Python list comprehensions", "Learned about efficient list creation using comprehensions. `[x*2 for x in range(10) if x % 2 == 0]` creates a list of doubled even numbers."),
    ("Git rebasing vs merging", "Rebasing creates a linear history while merging preserves branch structure. Use rebase for cleaner history, merge for preserving context."),
    ("Big O notation basics", "O(1) is constant, O(n) is linear, O(n²) is quadratic. Focus on worst-case when analyzing algorithms."),
    ("Python decorators", "Decorators wrap functions to extend behavior. Use `@functools.wraps` to preserve function metadata."),
    ("REST API design", "Use nouns for endpoints, HTTP verbs for actions. GET for read, POST for create, PUT for update, DELETE for remove."),
    ("SQL indexing", "Indexes speed up queries but slow down writes. Index columns used in WHERE clauses and JOIN conditions."),
    ("Python generators", "Generators yield values lazily, saving memory. Use `yield` instead of `return` for large sequences."),
    ("Dictionary methods", "`.get(key, default)` avoids KeyError. `.setdefault()` sets and returns value if key doesn't exist."),
    ("Error handling patterns", "Use specific exceptions, not bare except. Always log errors with context for debugging."),
    ("Code review best practices", "Focus on readability, correctness, and maintainability. Be constructive, not critical."),
]

# ============================================================
# CONTENT GENERATION
# ============================================================

def create_content(slot: str) -> tuple:
    """Create varied, realistic content."""
    today = datetime.now()
    timestamp = today.strftime("%H%M%S")
    date_str = today.strftime("%Y-%m-%d")
    
    # Randomly pick content type with weighted probability
    content_type = random.choices(
        ["algorithm", "snippet", "til"],
        weights=[40, 35, 25]
    )[0]
    
    if content_type == "algorithm":
        folder = PROJECT_ROOT / "algorithms" / today.strftime("%Y-%m")
        folder.mkdir(parents=True, exist_ok=True)
        
        algo_name = random.choice(list(ALGORITHMS.keys()))
        content = ALGORITHMS[algo_name]
        filename = f"{algo_name}_{timestamp}.py"
        topic = f"Algorithm: {algo_name.replace('_', ' ').title()}"
        emoji = "🧩"
        
    elif content_type == "snippet":
        folder = PROJECT_ROOT / "snippets" / "python"
        folder.mkdir(parents=True, exist_ok=True)
        
        snippet_name = random.choice(list(SNIPPETS.keys()))
        content = SNIPPETS[snippet_name]
        filename = f"{snippet_name}_{date_str.replace('-','')}.py"
        topic = f"Snippet: {snippet_name.replace('_', ' ').title()}"
        emoji = "✂️"
        
    else:  # til
        folder = PROJECT_ROOT / "notes" / "til" / today.strftime("%Y-%m")
        folder.mkdir(parents=True, exist_ok=True)
        
        til_topic, til_content = random.choice(TIL_TOPICS)
        filename = f"{date_str}_{slot}_{til_topic.lower().replace(' ', '-')[:20]}.md"
        content = f"""# TIL: {til_topic}

**Date**: {today.strftime('%Y-%m-%d %H:%M')}

## What I Learned

{til_content}

## Key Takeaway

Understanding this concept helps write better, more efficient code.

---
*Daily learning - {slot.title()} session*
"""
        topic = f"TIL: {til_topic}"
        emoji = "📝"
    
    filepath = folder / filename
    
    # Avoid duplicates
    if filepath.exists():
        timestamp = today.strftime("%H%M%S%f")[:10]
        filepath = folder / f"{filepath.stem}_{timestamp}{filepath.suffix}"
    
    filepath.write_text(content, encoding='utf-8')
    
    return str(filepath), topic, emoji


def git_commit_push(filepath: str, topic: str, emoji: str):
    """Commit and push with natural commit message."""
    token = os.environ.get("GITHUB_TOKEN")
    username = os.environ.get("GITHUB_USERNAME")
    repo = os.environ.get("GITHUB_REPO", "daily-dev-lab")
    
    # Varied commit message styles
    messages = [
        f"{emoji} Add {topic.lower()}",
        f"{emoji} {topic}",
        f"{emoji} Implement {topic.lower()}",
        f"{emoji} Practice: {topic}",
        f"{emoji} {topic} implementation",
    ]
    commit_msg = random.choice(messages)
    
    try:
        subprocess.run(["git", "add", filepath], cwd=PROJECT_ROOT, check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", commit_msg], cwd=PROJECT_ROOT, check=True, capture_output=True)
        print(f"✅ Committed: {commit_msg}")
        
        if token and username:
            auth_url = f"https://{username}:{token}@github.com/{username}/{repo}.git"
            result = subprocess.run(["git", "branch", "--show-current"], cwd=PROJECT_ROOT, capture_output=True, text=True)
            branch = result.stdout.strip() or "main"
            subprocess.run(["git", "push", auth_url, branch], cwd=PROJECT_ROOT, check=True, capture_output=True)
            print("✅ Pushed!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        return False


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--slot", required=True)
    args = parser.parse_args()
    
    print(f"\n🕐 Daily Dev Lab - {datetime.now().strftime('%H:%M')}")
    print("=" * 40)
    
    filepath, topic, emoji = create_content(args.slot)
    print(f"📁 Created: {Path(filepath).name}")
    
    git_commit_push(filepath, topic, emoji)


if __name__ == "__main__":
    main()
