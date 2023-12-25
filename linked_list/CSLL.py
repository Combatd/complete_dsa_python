class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class CSLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def append(self, value):
    new_node = Node(value)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
      new_node.next = new_node
    else:
      self.tail.next = new_node
      new_node.next = self.head
      self.tail = new_node
    self.length += 1

csLinkedList = CSLinkedList()

print(csLinkedList.append(10))
print(csLinkedList.append(20))
print(csLinkedList.head.value)
print(csLinkedList.tail.value)