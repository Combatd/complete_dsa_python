from logging import root


class TreeNode:
    # Time: O(1)
    # Space: O(1)
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None




newBT = TreeNode("Drinks")
leftChild = TreeNode('Hot')
rightChild = TreeNode('Cold')
newBT.leftChild = leftChild
newBT.rightChild = rightChild

# Time: O(n)
# Space: O(n)
def preOrderTraversal(rootNode):
    if not rootNode:
        return

    print(rootNode.data) # O(1)
    preOrderTraversal(rootNode.leftChild) # O(n / 2) recursion step
    preOrderTraversal(rootNode.rightChild) # O(n / 2) recursion step

# Time: O(n)
# Space: O(n)
def inOrderTraversal(rootNode):
    if not rootNode: # O(1)
        return

    inOrderTraversal(rootNode.leftChild) # O(n / 2)
    print(rootNode.data) # O(1)
    inOrderTraversal(rootNode.rightChild) # O(n / 2)


preOrderTraversal(newBT)
inOrderTraversal(newBT)