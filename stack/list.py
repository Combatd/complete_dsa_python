class Stack:
  def __init__(self):
    self.list = []

  def __str__(self):
    values = self.list.reverse()
    values = [str(x) for x in self.list]
    return '\n'.join(values)

  # isEmpty
  def isEmpty(self):
    if self.list == []:
      return True
    else:
      return False

  # push
  def push(self, value):
    self.list.append(value)
    return "The element has been successfully inserted"

  # pop
  def pop(self):
    if self.isEmpty():
      return 'There is not any element in the list'
    else:
      return self.list.pop()

customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)

print(customStack.pop())