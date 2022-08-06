
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
# Size: O(1)
def sizeOfHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize

newBinaryHeap = Heap(5)
print(sizeOfHeap(newBinaryHeap))