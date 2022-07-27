newTuple = ('a', 'b', 'c', 'd', 'e')

print(newTuple[1])
print(newTuple[-1])

print(newTuple[1:])

# Traverse Tuple
for i in newTuple: # Time: O(n) Space: O(1)
    print(i) # O(1)

for i in range(len(newTuple)):
    print(newTuple[i])

print('b' in newTuple) # True
print('f' in newTuple) # False

# Linear Search
# Time Complexity: O(n)
# Space Complexity: O(1)
def searchTuple(pTuple, element):
    for i in pTuple: # O(n)
        if i == element: # O(1)
            return pTuple.index(i) # you can also return i, O(1)
    return 'The element does not exist'

print(searchTuple(newTuple, 'c'))