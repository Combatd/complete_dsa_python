from array import *

arr1 = array('i', [1,2,3,4,5,6])
arr2 = array('d', [1.3, 1.5, 1.6])

# print(arr1)
# print(arr2)

# arr1.insert(0, 0) # O(n) worst case
# print(arr1)

def traverseArray(array): # Space Complexity = O(1)
    for i in array: # O(n)
        print(i) # O(1)

traverseArray(arr1)