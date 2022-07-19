def printUnorderedPairs(array):
    for i in range(0, len(array)): # O(n) with i index
        for j in range(i + 1, len(array)): # O(n - 1) with i index
            print(array[i], + "," + array[j]) # O(1)

