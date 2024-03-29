# Queue using Linked List

# Create a Queue
# Create an object of Linked List class
# #enqueue
# #dequeue
# so on...

from multiprocessing.sharedctypes import Value


class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Queue:
    # Time: O(1)
    # Space: O(1)
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.LinkedList]
        return " ".join(values)

    # Time: O(1)
    # Space: O(1)
    def enqueue(self, value):
        newNode = Node(value)
        if self.LinkedList.head == None:
            self.LinkedList.head = newNode
            self.LinkedList.tail = newNode
        else:
            self.LinkedList.tail.next = newNode
            self.LinkedList.tail = newNode

    # Time: O(1)
    # Space: O(1)
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    # Time: O(1)
    # Space: O(1)
    def dequeue(self):
        if self.isEmpty():
            return "There are no nodes in the queue"
        else:
            tempNode = self.LinkedList.head
            if self.LinkedList.head == self.LinkedList.tail:
                self.LinkedList.head = None
                self.LinkedList.tail = None
            else:
                self.LinkedList.head = self.LinkedList.head.next
            return tempNode
    
    # Time: O(1)
    # Space: O(1)
    def peek(self):
        if self.isEmpty():
            return "There are no nodes in the queue"
        else:
            return self.LinkedList.head

    # Time: O(1)
    # Space: O(1)
    def delete(self): # Singly Linked List you only have to set head and tail to None
        self.LinkedList.head = None 
        self.LinkedList.tail = None


custQueue = Queue()
custQueue.enqueue(1)
custQueue.enqueue(2)
custQueue.enqueue(3)
print(custQueue)
print(custQueue.dequeue(), " <- deque")
print(custQueue)
print(custQueue.peek(), "<- peek")