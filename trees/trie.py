
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    # Time: O(1)
    # Space: O(1) - Empty Trie Data Structure
    def __init__(self):
        self.root = TrieNode()

newTrie = Trie()