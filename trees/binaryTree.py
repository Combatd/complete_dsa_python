from queueLinkedList import Queue


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

# Time: O(n)
# Space: O(n)
def postOrderTraversal(rootNode):
    if not rootNode: # O(1)
        return

    postOrderTraversal(rootNode.leftChild) # O(n / 2)
    postOrderTraversal(rootNode.rightChild) # O(n / 2)
    print(rootNode.data) # O(1)

# Time: O(n)
# Space: O(n) - need to create a queue and go through all elements
def levelOrderTraversal(rootNode):
    if not rootNode: # O(1)
        return
    else:
        customQueue = Queue() # O(1)
        customQueue.enqueue(rootNode) # O(1)
        while not(customQueue.isEmpty()): # O(n)
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)

            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

preOrderTraversal(newBT)
inOrderTraversal(newBT)
postOrderTraversal(newBT)
levelOrderTraversal(newBT)