class Stack:
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []
        
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    # isEmpty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # isFull
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    # push
    # Time Complexity: Amortized O(1)
    # Space Complexity: O(1)
    def push(self, value):
        if self.isFull:
            return "The stack is full"
        else:
            self.list.append(value)

customStack = Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
