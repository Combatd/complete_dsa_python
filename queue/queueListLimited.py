from tracemalloc import start

from numpy import true_divide


class Queue:
    # Time: O(1)
    # Space: O(n)
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    # Time: O(1)
    # Space: O(1)
    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False

    # Time: O(1)
    # Space: O(1)
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    # Time: O(1)
    # Space: O(1)
    def enqueue(self, value):
        if self.isFull():
            return "The queue is full"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "The element is inserted at end of the Queue"

    # Time: O(1)
    # Space: O(1)
    def dequeue(self):
        if self.isEmpty():
            return "There are no elements in the Queue"
        else:
            firstElement = self.items[self.start] # We will save the element before removing to return it
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start
            else:
                self.start += 1
            self.items[start] = None
            return firstElement

    # Time: O(1)
    # Space: O(1)
    def peek(self):
        if self.isEmpty():
            return "There are no elements in the Queue"
        else:
            return self.items[self.start]  

    # Time:
    # Space:
    def delete(self):
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1



customQueue = Queue(3)
print(customQueue.isFull())
print(customQueue.isEmpty())
print(customQueue.enqueue(1))
print(customQueue.enqueue(2))
print(customQueue.enqueue(3))
print(customQueue)
print(customQueue.isFull())
print(customQueue.dequeue())
print(customQueue.peek(), " <-- Peek")
customQueue.delete()
print(customQueue)