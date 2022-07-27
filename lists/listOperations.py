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

newList = [11, 12, 13, 14]
myList.extend(newList) # Time Complexity: O(n) Space Complexity: O(n)
print(myList)