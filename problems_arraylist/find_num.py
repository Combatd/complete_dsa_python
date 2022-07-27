# Check if an array contains a number and return the index
import numpy as np

myArray = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

# Linear Search
def findNumber(array, number):
    for i in range(len(array)):
        if array[i] == number:
            return i
    return "Number is not in the array"

print(findNumber(myArray, 13))