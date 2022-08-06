
class Heap:
    # Time: O(1)
    # Space: O(n) - initalizing list with a fixed size
    def __init__(self, size):
        self.customList = (size + 1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1

# Time: O(1)
# Space: O(1)
def peekOfHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1]

# Time: O(1)
# Space: O(1)
def sizeOfHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize

# Time: O(n)
# Space: O(1) - no additional memory was allocated
def levelOrderTraversal(rootNode):
    if not rootNode: # O(1)
        return
    else:
        for i in range(1, rootNode.heapSize + 1): # O(n)
            print(rootNode.customList[i]) # O(1)

# Time: O(log n)
# Space: O(log n)
def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = int(index / 2) # O(1)
    if index <= 1: # O(1)
        return
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType) # O(log n) to left child
    elif heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType) # O(log n) to righ child

# Time: O(log n)
# Space: O(log n)
def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize: # O(1)
        return "The Binary Heap is full"
    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType) # O(log n)
    return "The value has been successfully inserted" 

def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0

    if rootNode.heapSize < leftIndex: # if it has no children
        return
    elif rootNode.heapSize == leftIndex:
        if heapType == "Min": # root is smaller than child
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
    
    else:
        if heapType == "Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
    heapifyTreeExtract(rootNode, swapChild, heapType)

# Time: O(log n)
# Space: O(log n)
def extractNode(rootNode, heapType):
    if rootNode.heapSize == 0: # O(1)
        return
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyTreeExtract(rootNode, 1, heapType) # O(log n)
        return extractedNode # O(1)

# Time: O(1)
# Space: O(1)
def deleteEntireBP(rootNode):
    rootNode.customList = None

newHeap = Heap(5)
# print(sizeOfHeap(newHeap))
insertNode(newHeap, 4, "Max")
insertNode(newHeap, 5, "Max")
insertNode(newHeap, 2, "Max")
insertNode(newHeap, 1, "Max")
print(extractNode(newHeap, "Max"), " <-- extractNode")
levelOrderTraversal(newHeap)
deleteEntireBP(newHeap)