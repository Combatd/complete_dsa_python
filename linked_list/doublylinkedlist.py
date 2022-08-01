# We need to create head and tail references
# Then we create blank node in memory, assing a value to the node
# Connect head and tail to the node

class Node:
    def __init__(self, value = None): # Time: O(1)
        self.value = value
        self.next = None
        self.prev = None

