import numpy as np

myArray = np.array([1, 20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 14, 35, 16, 27, 50, 19, 21])
dupArr = np.array([3,3,3])

# Create an empty list
# Loop through each given list
# In each visit, check if the visited element is in our newly created list and save the visited element in the newly created list
# In other langauges, we might use hash, object instead of the Python list to store....

def isUnique(array):
    visited = list()
    for i in range(len(array)):
        if array[i] in visited:
            return False
        else:
            visited.append(array[i])
    return True

print(isUnique(myArray))
print(isUnique(dupArr))