from platform import node
from turtle import circle


class Node:
    def __init__(self, value = None): # Time: O(1)
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    # Creation of Circular Doubly Linked List
    # Time Complexity: O(1) Space Complexity: O(1)
    def createCDLL(self, nodeValue):
        newNode = Node(nodeValue) # O(1)
        self.head = newNode # O(1)
        self.tail = newNode # O(1)
        newNode.prev = newNode # O(1)
        newNode.next = newNode # O(1)
        return "The Circular Doubly Linked List is created successfully" # O(1)




circularDLL = CircularDoublyLinkedList()
print(circularDLL.createCDLL(5))
print([node.value for node in circularDLL])