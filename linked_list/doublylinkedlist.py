# We need to create head and tail references
# Then we create blank node in memory, assing a value to the node
# Connect head and tail to the node

class Node:
    def __init__(self, value = None): # Time: O(1)
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Creation of Doubly Linked List
    # Time Complexity; O(1) Space Complexity: O(1)
    def createDLL(self, nodeValue):
        node = Node(nodeValue) # O(1)
        node.prev = None # O(1)
        node.next = None # O(1)
        self.head = node # O(1)
        self.tail = node # O(1)
        return 'The Doubly Linked List is created successfully'



doublyLL = DoublyLinkedList()
doublyLL.createDLL(5)

print([node.value for node in doublyLL])