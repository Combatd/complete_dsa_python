
from logging import root


class BSTNode:
    # Time: O(1)
    # Space: O(1)
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


# Time: O(log n) - Recursion through binary tree will always take less than n nodes
# Space: O(log n)
def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue) # O(n / 2)
        
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue) # O(n / 2)
        else:
            insertNode(rootNode.rightChild, nodeValue) # O(n / 2)
    return "The node has been successfully inserteds"

newBST = BSTNode(None)
print(insertNode(newBST, 70))
print(insertNode(newBST, 60))
print(newBST.data)
print(newBST.leftChild.data)