class BinaryTree:
    # Time: O(1)
    # Space: O(n)
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    # Time: O(1)
    # Space: O(1)
    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The Binary Tree is Full"
        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return "The value has been successfully inserted"

    # Time: O(n)
    # Space: O(1)
    def searchNode(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Success -> " + str(nodeValue)
        return "Not found"

    # Time: O(n)
    # Space: O(n)
    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index * 2) # left child 2x, recursive O(n / 2)
        self.preOrderTraversal(index * 2 + 1) # right child 2x + 1, recursive O(n / 2)

    # Time: O(n)
    # Space: O(n)
    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index * 2)
        print(self.customList[index])
        self.inOrderTraversal(index * 2 + 1)

    # Time: O(n)
    # Space: O(n)
    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index * 2)
        self.postOrderTraversal(index * 2 + 1)
        print(self.customList[index])


newBT = BinaryTree(8)
print(newBT.insertNode("Drinks"))
newBT.insertNode("Hot")
newBT.insertNode("Cold")
newBT.insertNode("Tea")
newBT.insertNode("Coffee")

print(newBT.searchNode("Tea"))
print(newBT.searchNode("Hot"))

newBT.preOrderTraversal(1)
newBT.inOrderTraversal(1)
newBT.postOrderTraversal(1)