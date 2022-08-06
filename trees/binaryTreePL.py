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

newBT = BinaryTree(8)
print(newBT.insertNode("Drinks"))
newBT.insertNode("Hot")
newBT.insertNode("Cold")

print(newBT.searchNode("Tea"))
print(newBT.searchNode("Hot"))