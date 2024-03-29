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

    # Time: O(n)
    # Space: O(n)
    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex + 1):
            print(self.customList[i])

    # Time: O(n)
    # Space: O(n)
    def deleteNode(self, value):
        if self.lastUsedIndex == 0: # O(1)
            return "There is not any node to delete"
        for i in range(1, self.lastUsedIndex + 1): # O(n)
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex] # Swap Location
                self.customList[self.lastUsedIndex] = None # Delete the Node
                self.lastUsedIndex -= 1
                return "The node has been successfully deleted"
    # Time: O(1)
    # Space: O(1)
    def deleteBT(self):
        self.customList = None
        return "The Binary Tree has been successfully deleted"


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
newBT.levelOrderTraversal(1)


print(newBT.deleteNode("Tea"))
newBT.levelOrderTraversal(1)

print(newBT.deleteBT())
newBT.levelOrderTraversal(1) # This will throw an error because there is no more list