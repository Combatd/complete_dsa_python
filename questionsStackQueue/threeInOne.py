# Three in ONe
# Describe how you could use a single Python list to implement three stacks.

#  [0, 1, 2, 3, 4, 5, 6, 7, 8]

# For Stack 1 - [0], [1], [2] 0, n/3
# For Stack 2 - [3], [4], [5] n/3, 2n / 3
# For Stack 3 - [7], [8], [9] 2n / 3, n

class MultiStack:
    def __init__(self, stackSize):
        self.numberOfStacks = 3
        self.customList = [0] * (stackSize * self.numberOfStacks)
        self.sizes = [0] * self.numberOfStacks
        self.stackSize = stackSize

    # stackNumber identifies which of the 3 stacks to use
    def isFull(self, stackNumber):
        if self.sizes[stackNumber] == self.stackSize:
            return True
        else:
            return False

    def isEmpty(self, stackNumber):
        if self.sizes[stackNumber] == 0:
            return True
        else:
            return False

    # helper method
    def indexOfTop(self, stackNumber):
        offset = stackNumber * self.stackSize
        return offset + self.sizes[stackNumber] - 1

    def push(self, item, stackNumber):
        if self.isFull(stackNumber):
            return "The stack is full"
        else:
            self.sizes[stackNumber] += 1
            self.customList[self.indexOfTop(stackNumber)] = item

    def pop(self, stackNumber):
        if self.isEmpty(stackNumber):
            return "The stack is empty"
        else:
            value = self.customList[self.indexOfTop(stackNumber)]
            self.customList[self.indexOfTop(stackNumber)] = 0
            self.sizes = [0] * self.numberOfStacks

    def peek(self, stackNumber):
        if self.isEmpty(stackNumber):
            return "The stack is empty"
        else:
            print(self.customList)
            value = self.customList[self.indexOfTop(stackNumber)]
            return value

customStack = MultiStack(6)
print(customStack.isFull(0))
print(customStack.isEmpty(1))
customStack.push(1, 0)
customStack.push(2, 0)
customStack.push(3, 2)
print(customStack.peek(0))
print(customStack.pop(0))
