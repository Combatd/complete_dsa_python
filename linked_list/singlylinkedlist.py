class Node:
    def __init__(self, value): # Time: O(1)
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self): # Time: O(1) Space: O(1)
        self.head = None # Time: O(1)
        self.tail = None # Time: O(1)

singlyLinkedList = SLinkedList()
node1 = Node(1)
node2 = Node(2)

# Time: O(1)
singlyLinkedList.head = node1
singlyLinkedList.head.next = node2
singlyLinkedList.tail = node2