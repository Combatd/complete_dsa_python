class Node:
    def __init__(self, value = None): # Time: O(1)
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
            node = node.next
            if node.next == self.tail.next:
                break
            

    # Creation of Circular Singly Linked List
    # Time Complexity: O(1) Space Complexity: O(1)
    def createCSLL(self, nodeValue):
        node = Node(nodeValue) # O(1)
        node.next = node # O(1)
        self.head = node # O(1)
        self.tail = node # O(1)
        return "The Circular Singly Linked List has been created" # O(1)

    # Insertion of a node in Circular Singly Linked List
    # Time Complexity: O(n) Space Complexity: O(1)
    def insertCSLL(self, value, location):
        if self.head is None:
            return "The head reference is None"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode # Circles around
            elif location == -1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1: # O(n)
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return "The node has been successfully inserted"

    # Traversal of a node in Circular Singly Linked List
    # Time Complexity: O(n) Space Complexity: O(1)
    def traversalCSLL(self):
        if self.head is None:
            print("There is no element for traversal")
        else:
            tempNode = self.head
            while tempNode: # O(n)
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    # Linear Search of a node in Circular Singly Linked List
    # Time Complexity: O(n) Space Complexity: O(1)
    def searchCSLL(self, nodeValue):
        if self.head is None: # O(1)
            return "There is not any node in this Circular Singly Linked List"
        else:
            tempNode = self.head # O(1)
            while tempNode: # O(1)
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return "The node does not exist in this Circular Singly Linked List"
    
    # Delete a node from Circularl Singly Linked List
    # Time Complexity: O(n) Space Complexity: O(1)
    def deleteNode(self, location):
        if self.head is None: # O(1)
            print("There is not any node in the Circular Singly Linked List")
        else:
            if location == 0: # O(1)
                if self.head == self.tail: # O(1)
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else: # O(1)
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == 1: # O(1)
                if self.head == self.tail: # O(1)
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else: # O(1)
                    node = self.head
                    while node is not None: # O(n)
                        if node.next == self.tail: # O(n)
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else: # O(1)
                tempNode = self.head
                index = 0
                while index < location - 1: # O(n)
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next


circularSLL = CircularSinglyLinkedList()
print(circularSLL.createCSLL(0))

print(circularSLL.insertCSLL(0, 0)) # insert at head
print(circularSLL.insertCSLL(2, 1)) # insert at tail
print(circularSLL.insertCSLL(3, 1))
print(circularSLL.insertCSLL(4, 1))

print(circularSLL.traversalCSLL())
print(circularSLL.searchCSLL(3))

print([node.value for node in circularSLL])

circularSLL.deleteNode(0)
print([node.value for node in circularSLL])