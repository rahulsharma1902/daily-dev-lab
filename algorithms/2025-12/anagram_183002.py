"""
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
