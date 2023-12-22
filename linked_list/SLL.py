class Node:
  def __init__(self, value):
    self.value = value
    self.next = None



class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def __str__(self):
    temp_node = self.head
    result = ''
    while temp_node is not None:
      result += str(temp_node.value)
      if temp_node.next is not None:
        result += ' -> '
      temp_node = temp_node.next
    return result

  def append(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.length += 1

  def prepend(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head = new_node
    self.length += 1
  
  def insert(self, index, value):
    new_node = Node(value)
    if index < 0 or index > self.length:
      return False
    elif self.length == 0:
      self.head = new_node
      self.tail = new_node
    elif index == 0:
      new_node.next = self.head
      self.head = new_node
    else:
      new_node = Node(value)
      temp_node = self.head
      for _ in range(index - 1):
        temp_node = temp_node.next
      new_node.next = temp_node.next
      temp_node.next = new_node
    self.length += 1
    return True
  
  def traverse(self):
    current = self.head
    while current:
      print(current.value)
      current = current.next

  def search(self, target):
    current = self.head
    index = 0
    while current:
      if current.value == target:
        return index
      current = current.next
      index += 1
    return -1

    

new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
print(new_linked_list)
new_linked_list.prepend(40)
print(new_linked_list)
new_linked_list.insert(0, 50)
new_linked_list.insert(7, 99999) # out of bounds, returns false
new_linked_list.traverse()
print(new_linked_list.search(30)) # 4
print(new_linked_list.search(99999)) # -1