# myList = [1, 2, 3, 4, 5, 6, 7]
# print(myList)

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

# myList = ['a', 'b', 'c', 'd', 'e', 'f']

# myList[0:2] = ['x', 'y']
# print(myList[:]) # slice is exclusive of end index

# myList.pop(2) # second element in the list - Time Complexity: O(n)
# print(myList.pop()) # last element in the list - Time Complexity: O(1)
# print(myList)

# del myList[2:4] # Time Complexity O(n)
# print(myList)

# myList.remove('e') # Time Complexity: O(n)
# print(myList)

myList = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# IN operator
if 20 in myList:
    print(myList.index(20)) # Time Complexity: O(n)
else:
    print("The value does not exist in the list")

# Linear Search
def searchInList(list, value): # Time Complexity: O(n) Space Complexity: O(1)
    for i in list: # O(n)
        if i == value: # O(1)
            return list.index(value) # O(1)
    return "The value does not exist in the list" # O(1)

print(searchInList(myList, 50))