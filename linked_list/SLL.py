class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

new_node = Node(10)
print(new_node)
# Time and Space O(1)

class LinkedList:
  def __init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1

new_linked_list = LinkedList(10)
print(new_linked_list)
print(new_linked_list.head.value)

""" 
Linked List Initialization with one node
Time Complexity: O(1)
Only one node needs to be initialized as the Linked List object is initialized.

Space Complexity: O(1)
Only one Node is created to be in one new LinkedList so it is a constant space usage.
"""