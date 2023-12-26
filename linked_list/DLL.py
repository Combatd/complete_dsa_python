class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None
  
  def __str__(self):
    return f"{self.prev} <- {self.value} -> {self.next}"

new_node = Node(10)
print(new_node)

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def __str__(self):
    temp_node = self.head
    result = ''
    while temp_node:
      result += str(temp_node.value)
      if temp_node.next is not None:
        result += ' <-> '
      temp_node = temp_node.next
    return result

  def append(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
    self.length += 1

  def prepend(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node
    self.length += 1

  def traverse(self):
    current_node = self.head
    while current_node:
      print(current_node.value)
      current_node = current_node.next

  def reverse_traverse(self):
    current_node = self.tail
    while current_node:
      print(current_node.value)
      current_node = current_node.prev

  def search(self, target):
    current_node = self.head
    index = 0
    while current_node:
      if current_node.value == target:
        return index
      current_node = current_node.next
      index += 1
    return -1

newDLL= DoublyLinkedList()
newDLL.append(10)
newDLL.append(20)
newDLL.append(30)
print(newDLL)
newDLL.prepend(50)
newDLL.prepend(60)
print(newDLL)
newDLL.traverse()
newDLL.reverse_traverse()
print(newDLL.search(30))
print(newDLL.search(999))