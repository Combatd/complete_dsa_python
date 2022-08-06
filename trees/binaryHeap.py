
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


newBinaryHeap = Heap(5)
print(sizeOfHeap(newBinaryHeap))