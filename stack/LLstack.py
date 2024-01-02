class Node:
  def __init__(self, value = None):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

class Stack:
  def __init__(self):
    self.LinkedList = LinkedList()
    self.length = 0

  # isEmpty
  def isEmpty(self):
    if self.LinkedList.head == None:
      return True
    else:
      return False


  # isFull
  def isFull(self):
    pass

  # push
  def push(self, value):
    pass

  # pop
  def pop(self):
    pass

  # peek
  def peek(self):
    pass

  # delete
  def delete(self):
    self.list = None



# Test the class
customStack = Stack()
print(customStack.isEmpty())