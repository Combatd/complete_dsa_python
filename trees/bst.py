from queueLinkedList import Queue

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

# Time: O(n)
# Space: O(1)
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

# Time: O(n)
# Space: O(n)
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

# Time: O(n)
# Space: O(n)
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

# Time: O(n)
# Space: O(n)
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

# Time: O(log n) - will always be less than n in divide and conquer algorithm
# Space: O(log n)
def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print('The value is found ', str(nodeValue))
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print('The value is found ', str(nodeValue))
        else:      
            searchNode(rootNode.leftChild, nodeValue) # O(n / 2)
    else:
        if rootNode.rightChild.data == nodeValue:
            print('The value is found ', str(nodeValue))
        else:      
            searchNode(rootNode.rightChild, nodeValue) # O(n / 2)





newBST = BSTNode(None)
print(insertNode(newBST, 70))
print(insertNode(newBST, 50))
print(insertNode(newBST, 90))
print(insertNode(newBST, 30))
print(insertNode(newBST, 60))
print(insertNode(newBST, 80))
print(insertNode(newBST, 100))
print(insertNode(newBST, 20))
print(insertNode(newBST, 40))
preOrderTraversal(newBST)
inOrderTraversal(newBST)
postOrderTraversal(newBST)
levelOrderTraversal(newBST)
searchNode(newBST, 60)