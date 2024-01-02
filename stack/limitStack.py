class Stack:
  def __init__(self, masSize):
    self.maxSize = masSize
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
    pass

  # pop
  def pop(self):
    pass

  # peek
  def peek(self):
    pass

  # delete
  def delete(self):
    pass