class Youtube:
  def __init__(self, username, subscribers = 0):
    self.username = username
    self.subscribers = subscribers

print(Youtube.__dict__)

user1 = Youtube('Nephilim', 15)
print(user1.__dict__)
print(user1.username)
print(user1.subscribers)

user2 = Youtube("detective", 16)
print(user2.__dict__)
print(user2.username)
print(user2.subscribers)