class Stack:
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)