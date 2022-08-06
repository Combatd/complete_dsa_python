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

tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
rightChild.rightChild = coffee
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

# Time; O(n)
# Space: O(n)
def searchBT(rootNode, nodeValue):
    if not rootNode:
        return "The Binary Tree does not exist"
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "Success -> " + str(nodeValue)

            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)

            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
    return "Not Found"

# Time: O(n)
# Space: O(n)
def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Successfully inserted"
            
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Successfully inserted"


# Time: O(n)
# Space:
def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)

            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
                
            deepestNode = root.value
            return deepestNode

# Time:
# Space:
def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value is dNode:
                root.value = None
                return
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)

            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)

# Time: O(n)
# Space: O(n)
def deleteNodeBT(rootNode, node):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "The node has been successfully deleted"

            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)

            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        return "Failed to delete"



deleteNodeBT(newBT, "Tea")
levelOrderTraversal(newBT)

# deepestNode = getDeepestNode(newBT)
# print(deepestNode.data, "<- deepestNode")
# newNode = getDeepestNode(newBT)
# deleteDeepestNode(newBT, newNode)
# levelOrderTraversal(newBT)

# preOrderTraversal(newBT)
# inOrderTraversal(newBT)
# postOrderTraversal(newBT)
# levelOrderTraversal(newBT)
# print(searchBT(newBT, "Tea"))

# newNode = TreeNode("Cola")
# print(insertNodeBT(newBT, newNode))
# levelOrderTraversal(newBT)

# newNode = getDeepestNode(newBT)
# deleteDeepestNode(newBT, newNode)
# levelOrderTraversal(newBT)