# Create buckets and distribute elements of array into buckets
# Sort buckets individually
# Merge buckets after sorting

import math

from numpy import number

from insertionSort import insertionSort

# Time: O(n^2)
# Space: O(n) - created temporary array
def bucketSort(customList):
    numberOfBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []

    for i in range(numberOfBuckets):
        arr.append([])
    for j in customList:
        index_b = math.ceil(j * numberOfBuckets / maxValue)
        arr[index_b - 1].append(j)

    for i in range(numberOfBuckets):
        arr[i] = insertionSort(arr[i])

    k = 0
    for i in range(numberOfBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList




cList = [2, 1, 7, 6, 5, 3, 4, 9, 8]
bucketSort(cList)