class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    # Time Complexity: Amortized O(1) - has to reserve more memory
    # Space Complexity: O(1)
    def enqueue(self, value):
        self.items.append(value)
        return "The element is inserted at the end of Queue"

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def dequeue(self):
        if self.isEmpty():
            return "There are no elements in the queue"
        else:
            return self.items.pop(0)

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def peek(self):
        if self.isEmpty():
            return "There are no elements in the queue"
        else:
            return self.items[0]

    def delete(self):
        self.items = None

customQueue = Queue()
print(customQueue.isEmpty())
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.dequeue())
print(customQueue.peek())
customQueue.delete()