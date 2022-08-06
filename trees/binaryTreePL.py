class BinaryTree:
    # Time: O(1)
    # Space: O(n)
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size


newBT = BinaryTree(8)