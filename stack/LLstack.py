class Node:
  def __init__(self, value = None):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  
  def __iter__(self):
    curNode = self.head
    while curNode:
      yield curNode
      curNode = curNode.next

class Stack:
  def __init__(self):
    self.LinkedList = LinkedList()

  def __str__(self):
    values = [str(x.value) for x in self.LinkedList]
    return '\n'.join(values)

  # isEmpty
  def isEmpty(self):
    if self.LinkedList.head == None:
      return True
    else:
      return False

  # push
  def push(self, value):
    node = Node(value)
    node.next = self.LinkedList.head
    self.LinkedList.head = node

  # pop
  def pop(self):
    if self.isEmpty():
      return 'There is not any element in the stack'
    else:
      nodeValue = self.LinkedList.head.value
      self.LinkedList.head = self.LinkedList.head.next
      return nodeValue

  # peek
  def peek(self):
    pass

  # delete
  def delete(self):
    self.list = None



# Test the class
customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
print("------")
print(customStack.pop())
print('------')
print(customStack)