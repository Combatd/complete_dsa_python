import numpy as np

myArray = np.array([1, 20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 14, 35, 16, 27, 50, 19, 21])

def maxProductSimple(array): # can use built in numpy methods here, but this is bad Space Complexity
    sortedArr = np.sort(array)
    return sortedArr[-1] * sortedArr[-2]

print(maxProductSimple(myArray))

def findMaxProduct(array):
    maxProduct = 0
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] * array[j] > maxProduct:
                maxProduct = array[i] * array[j]
    return maxProduct

print(findMaxProduct(myArray))