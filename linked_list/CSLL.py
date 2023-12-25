class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class CSLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def __str__(self):
    temp_node = self.head
    result = ''
    while temp_node is not None:
      result += str(temp_node.value)
      temp_node = temp_node.next
      if temp_node == self.head:
        break
      result += ' -> '
    return result

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

  def prepend(self, value):
    new_node = Node(value)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
      new_node.next = new_node
    else:
      new_node.next = self.head
      self.head = new_node
      self.tail.next = new_node
    self.length += 1

csLinkedList = CSLinkedList()

csLinkedList.append(10)
csLinkedList.append(20)
print(csLinkedList)
csLinkedList.prepend(30)
csLinkedList.prepend(40)
print(csLinkedList)