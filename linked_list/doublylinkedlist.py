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

    # Insertion Method in Doubly Linked List
    # Time Complexity: O(n) Space Complexity: O(1)
    def insertNode(self, nodeValue, location):
        if self.head is None: # O(1)
            print("The node cannot be inserted") # O(1)
        else:
            newNode = Node(nodeValue) # O(1)
            if location == 0: # O(1)
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == -1: # O(1)
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head # O(1)
                index = 0 # O(1)
                while index < location - 1: # O(n)
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next # O(1)
                newNode.prev = tempNode # O(n)
                newNode.next.prev = newNode # O(n)
                tempNode.next = newNode # O(n)

    # Traversal Method in Doubly Linked List
    # Time Complexity: O(n) Space Complexity: O(1)
    def traversalDLL(self):
        if self.head is None: # O(1)
            print("There is not any element to traverse") # O(1)
        else: # O(1)
            tempNode = self.head # O(1)
            while tempNode: # O(n)
                print("Value of tempNode: ", tempNode.value) # O(1)
                tempNode = tempNode.next # O(1)

    # Reverse Traversal Method in Doubly Linked List
    # Time Complexity: O(n) Space Complexity: O(1)
    def reverseTraversalDLL(self):
        if self.head is None:
            print("There is not one node in the Doubly Linked List to traverse") # O(1)
        else:
            tempNode = self.tail # O(1)
            while tempNode: # O(n)
                print("Value of tempNode: ", tempNode.value) #O(1)
                tempNode = tempNode.prev # O(1)

    # Search Method in Doubly Linked List
    # Time Complexity: O(n) Space Complexity: O(1)
    def searchDLL(self, nodeValue):
        if self.head is None: # O(1)
            return "There are no nodes in the Doubly Linked List" # O(1)
        else:
            tempNode = self.head # O(1)
            while tempNode: # O(n)
                if tempNode.value == nodeValue: # O(1)
                    return tempNode.value # O(1)
                tempNode = tempNode.next # O(1)
            return "The node does not exist in this list" # O(1)

    # Delete a node from Doubly Linked List
    # Time Complexity: O(n) Space Complexity: O(1)
    def deleteNode(self, location):
        if self.head is None: # O(1)
            print("There is not any element in DLL")
        else:
            if location == 0: # O(1)
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1: # O(1)
                if self.head == self.tail: # O(1)
                    self.head = None
                    self.tail = None
                else: # O (1)
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                currentNode = self.head
                index = 0
                while index < location - 1: # O(n) Reach the node that is before the location
                    currentNode = currentNode.next
                    index += 1
                currentNode.next = currentNode.next.next
                currentNode.next.prev = currentNode
            print("The node was successfully deleted")



doublyLL = DoublyLinkedList()
doublyLL.createDLL(5)

print([node.value for node in doublyLL])

doublyLL.insertNode(0,0)
doublyLL.insertNode(2,-1)
doublyLL.insertNode(6,2)

print([node.value for node in doublyLL])
doublyLL.traversalDLL()
doublyLL.reverseTraversalDLL()

print(doublyLL.searchDLL(6))
print(doublyLL.searchDLL(7))

doublyLL.deleteNode(1)
print([node.value for node in doublyLL])