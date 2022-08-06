
from lib2to3.pytree import Node


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    # Time: O(1)
    # Space: O(1) - Empty Trie Data Structure
    def __init__(self):
        self.root = TrieNode()

    # Time: O(m) - m is number of characters
    # Space: O(m)
    def insertString(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch: node})
            current = node
        current.endOfString = True
        print("Successfully inserted " + str(word))

    # Time: O(m) - where m is the number of characters
    # Space: O(1)
    def searchString(self, word):
        currentNode = self.root
        for i in word: # O(m)
            node = currentNode.children.get(i)
            if node == None:
                return False
            currentNode = node

        if currentNode.endOfString == True:
            return True
        else:
            return False
    


newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Appl")
print(newTrie.searchString("App"))
print(newTrie.searchString("Ap"))