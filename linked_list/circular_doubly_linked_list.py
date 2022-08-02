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

    # Insertion method for Circular Doubly Linked List
    # Time Complexity: O(n) Space Complexity: O(1)
    def insertCDLL(self, value, location):
        if self.head is None:
            return "The Circular Doubly Linked List does not exist"
        else:
            newNode = Node(value)
            if location == 0: # O(1)
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == -1: # O(1)
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1: # O(n)
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
        return "The node has been sucessfully inserted"

circularDLL = CircularDoublyLinkedList()
print(circularDLL.createCDLL(5))
print(circularDLL.insertCDLL(0,0))
print(circularDLL.insertCDLL(1, -1))
print(circularDLL.insertCDLL(2, 2))

print([node.value for node in circularDLL])