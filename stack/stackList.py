class Stack:
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    # isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # push
    # Time Complexity: Amortized O(1) - allocates a few times more memory on each call
    # Space Complexity: O(1) - appending one element at a time
    def push(self, value):
        self.list.append(value)
        return "The element has been successfully inserted"


customStack = Stack()
print(customStack.isEmpty())
print(customStack.push(1))
print(customStack.push(2))
print(customStack.push(3))
print(customStack)