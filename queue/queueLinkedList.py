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