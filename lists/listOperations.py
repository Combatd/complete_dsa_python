myList = [1, 2, 3, 4, 5, 6, 7]
print(myList)

# myList[2] = 33 # Space Complexity: O(1)
# print(myList)

# myList[4] = 55 # Time Complexlity: O(1)
# print(myList)

# myList.insert(4, 15) # Time Complexity: O(n)
# print(myList)

# myList.append(55) # Time Complexity: O(1)
# print(myList)

# newList = [11, 12, 13, 14]
# myList.extend(newList) # Time Complexity: O(n) Space Complexity: O(n)
# print(myList)

myList = ['a', 'b', 'c', 'd', 'e', 'f']

# myList[0:2] = ['x', 'y']
# print(myList[:]) # slice is exclusive of end index

# myList.pop(2) # second element in the list - Time Complexity: O(n)
# print(myList.pop()) # last element in the list - Time Complexity: O(1)
# print(myList)

# del myList[2:4] # Time Complexity O(n)
# print(myList)

myList.remove('e') # Time Complexity: O(n)
print(myList)