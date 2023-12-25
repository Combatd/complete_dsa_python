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
    if not self.head:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
    self.length += 1


newDLL= DoublyLinkedList()
newDLL.append(10)
newDLL.append(20)
print(newDLL)