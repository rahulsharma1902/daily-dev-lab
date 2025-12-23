"""
Singly Linked List Implementation
=================================

A basic linked list with common operations.

Operations and Time Complexity:
    - Insert at head:  O(1)
    - Insert at tail:  O(n) or O(1) with tail pointer
    - Delete:          O(n)
    - Search:          O(n)
    - Access by index: O(n)

Space Complexity: O(n)
"""

from typing import Any, Optional


class Node:
    """A node in the linked list."""
    
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional['Node'] = None
    
    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:
    """Singly linked list implementation."""
    
    def __init__(self):
        self.head: Optional[Node] = None
        self._size = 0
    
    def __len__(self) -> int:
        return self._size
    
    def __repr__(self) -> str:
        if not self.head:
            return "LinkedList(empty)"
        
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        
        return "LinkedList(" + " -> ".join(nodes) + ")"
    
    def is_empty(self) -> bool:
        """Check if the list is empty."""
        return self.head is None
    
    def insert_at_head(self, data: Any) -> None:
        """Insert a new node at the beginning. O(1)"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1
    
    def insert_at_tail(self, data: Any) -> None:
        """Insert a new node at the end. O(n)"""
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        self._size += 1
    
    def delete(self, data: Any) -> bool:
        """Delete first occurrence of data. Returns True if found."""
        if not self.head:
            return False
        
        # Special case: delete head
        if self.head.data == data:
            self.head = self.head.next
            self._size -= 1
            return True
        
        # Search for the node
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next
        
        return False
    
    def search(self, data: Any) -> Optional[Node]:
        """Search for a node with given data. O(n)"""
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None
    
    def to_list(self) -> list:
        """Convert linked list to Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def reverse(self) -> None:
        """Reverse the linked list in place. O(n)"""
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev


def test_linked_list():
    """Test cases for linked list."""
    ll = LinkedList()
    
    # Test empty list
    assert ll.is_empty()
    assert len(ll) == 0
    
    # Test insertions
    ll.insert_at_head(3)
    ll.insert_at_head(2)
    ll.insert_at_head(1)
    assert ll.to_list() == [1, 2, 3]
    
    ll.insert_at_tail(4)
    ll.insert_at_tail(5)
    assert ll.to_list() == [1, 2, 3, 4, 5]
    
    # Test search
    assert ll.search(3) is not None
    assert ll.search(10) is None
    
    # Test delete
    assert ll.delete(3) is True
    assert ll.to_list() == [1, 2, 4, 5]
    assert ll.delete(1) is True  # Delete head
    assert ll.to_list() == [2, 4, 5]
    
    # Test reverse
    ll.reverse()
    assert ll.to_list() == [5, 4, 2]
    
    print("✅ All linked list tests passed!")


if __name__ == "__main__":
    test_linked_list()
    
    # Example usage
    ll = LinkedList()
    for i in range(1, 6):
        ll.insert_at_tail(i)
    
    print(f"Original: {ll}")
    ll.reverse()
    print(f"Reversed: {ll}")
