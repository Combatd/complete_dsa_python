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



doublyLL = DoublyLinkedList()
doublyLL.createDLL(5)

print([node.value for node in doublyLL])

doublyLL.insertNode(0,0)
doublyLL.insertNode(2,-1)
doublyLL.insertNode(6,2)

print([node.value for node in doublyLL])
doublyLL.traversalDLL()