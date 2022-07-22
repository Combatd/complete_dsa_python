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