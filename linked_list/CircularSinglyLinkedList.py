class Node:
    def __init__(self, value): # Time: O(1)
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self): # Time: O(1) Space: O(1)
        self.head = None # Time: O(1)
        self.tail = None # Time: O(1)
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    # Creation of Circular Singly Linked List
    # Time Complexity: O(1) Space Complexity: O(1)
    def createCSLL(self, nodeValue):
        node = Node(nodeValue) # O(1)
        node.next = node # O(1)
        self.head = node # O(1)
        self.tail = node # O(1)
        return "The Circular Singly Linked List has been created" # O(1)

circularSLL = CircularSinglyLinkedList()
circularSLL.createCSLL(1)

print([node.value for node in circularSLL])