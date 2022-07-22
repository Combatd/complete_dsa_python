from array import *

arr1 = array('i', [1,2,3,4,5,6])
arr2 = array('d', [1.3, 1.5, 1.6])

# print(arr1)
# print(arr2)

# arr1.insert(0, 0) # O(n) worst case
# print(arr1)

def traverseArray(array): # Space Complexity = O(1)
    for i in array: # O(n) Time
        print(i) # O(1) Time

traverseArray(arr1)

def accessElement(array, index): # Space Complexity: O1()
    if index >= len(array): # negative indexes for access from end are supported in python
        print("There is not any element in this index") # O(1) Time
    else:
        print(array[index]) # O(1) Time

accessElement(arr1, 6)

def searchInArray(array, value): # Space Complexity = O(1)
    for i in array: # O(n) Time
        if i == value: # O(1) Time
            return array.index(value) # O(n) Time as it will search for the index containing the atching i and value
    return "The element does not exist in this array" # O(n)

print(searchInArray(arr1, 3))


print(arr1)
arr1.remove(4) # Space Complexity: O(1), Time Complexity: O(n)

print(arr1)