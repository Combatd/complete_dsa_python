newTuple = ('a', 'b', 'c', 'd', 'e')

print(newTuple[1])
print(newTuple[-1])

print(newTuple[1:])

# Traverse Tuple
for i in newTuple: # Time: O(n) Space: O(1)
    print(i) # O(1)

for i in range(len(newTuple)):
    print(newTuple[i])