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

  def push(self, value):
    self.list.append(value)
    return "The element has been successfully inserted"

customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)