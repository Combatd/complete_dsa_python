class Node:
    def __init__(self, value): # Time: O(1)
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self): # Time: O(1) Space: O(1)
        self.head = None # Time: O(1)
        self.tail = None # Time: O(1)
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Insert in Linked List
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0: # start of Linked List
                newNode.next = self.head
                self.head = newNode
            elif location == 1: # node after start of Linked List
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode

    # Traverse Singly Linked List
    # Time Complexity: O(n) Space Complexity: O(1)
    def traverseSLL(self):
        if self.head is None: # Time: O(1)
            print("The Singly Linked List does not exist") # Time: O(1)
        else:
            node = self.head # Time: O(1)
            while node is not None: # Time: O(n)
                print(node.value) # Time: O(1)
                node = node.next # Time: O(1)

singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(4, 1)

singlyLinkedList.insertSLL(0, 0)
singlyLinkedList.insertSLL(0, 4)
print([node.value for node in singlyLinkedList])
singlyLinkedList.traverseSLL()