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

    # Traversal of Circular Doubly Linked List
    # Time Complexity: O(n) Space Complexity: O(1)
    def traversalCDLL(self):
        if self.head is None: # O(1)
            print("There are no nodes for traversal")
        else:
            tempNode = self.head # O(1)
            while tempNode: # O(n)
                print(tempNode.value) # O(1)
                if tempNode == self.tail: # O(1)
                    break # O(1)
                tempNode = tempNode.next # O(1)

    # Reverse Traversal of Circular Doubly Linked List
    # Time Complexity: O(n) Space Complexity: O(1)
    def reverseTraversalCDLL(self):
        if self.head is None: # O(1)
            print("There are no nodes for reverse traversal")
        else:
            tempNode = self.tail # O(1)
            while tempNode: # O(n)
                print(tempNode.value) # O(1)
                if tempNode == self.head: # O(1)
                    break
                tempNode = tempNode.prev # O(1)

    # Search Circular Doubly Linked List
    # Time Complexity: O(n) Space Complexity: O(1)
    def searchCDLL(self, nodeValue):
        if self.head is None:
            return "There are no nodes in the Circular Doubly Linked List" # O(1)
        else:
            tempNode = self.head # O(1)
            while tempNode: # O(n)
                if tempNode.value == nodeValue:
                    return tempNode.value # O(1)
                if tempNode == self.tail:
                    return "The value does not exist in Circular Doubly Linked List" # O(1)
                tempNode = tempNode.next # O(1)

    # Delete a node in Circular Doubly Linked List
    # Time Complexity: O(n) Space Complexity: O(1)
    def deleteNode(self, location):
        if self.head is None: # O(1)
            print('There are no nodes to delete in the Circular Doubly Linked List')
        else:
            if location == 0: # O(1)
                if self.head == self.tail: # O(1)
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else: # O(1)
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == -1: # O(1)
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else: # O(1)
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                currentNode = self.head # O(1)
                index = 0 # O(1)
                while index < location - 1: # O(n)
                    currentNode = currentNode.next
                    index += 1
                currentNode.next = currentNode.next.next # O(1)
                currentNode.next.prev = currentNode # O(1)
            print("The node has been successfully deleted")

    # Delete entire Circular Doubly Linked List
    # Time Complexity: O(n) Space Complexity: O(1)
    def deleteCDLL(self):
        if self.head is None:
            print("There are no nodes to delete") # O(1)
        else:
            self.tail.next = None # O(1)
            tempNode = self.head # O(1)
            while tempNode: # will stop on a falsy value, O(n)
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None # O(1)
            self.tail = None # O(1)
            print("The Circular Doubly Linked List has been successfully deleted") # O(1)


circularDLL = CircularDoublyLinkedList()
print(circularDLL.createCDLL(5))
print(circularDLL.insertCDLL(0,0))
print(circularDLL.insertCDLL(1, -1))
print(circularDLL.insertCDLL(2, 2))

print([node.value for node in circularDLL])
circularDLL.traversalCDLL()
print([node.value for node in circularDLL])
circularDLL.reverseTraversalCDLL()

print([node.value for node in circularDLL])
print(circularDLL.searchCDLL(2))
print(circularDLL.searchCDLL(6))

circularDLL.deleteNode(1)
print([node.value for node in circularDLL])

circularDLL.deleteCDLL()
print([node.value for node in circularDLL])