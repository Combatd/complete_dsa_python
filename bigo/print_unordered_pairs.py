def printUnorderedPairs(array):
    for i in range(0, len(array)): # O(n-1) -> O(n) with i index
        for j in range(i + 1, len(array)): # O(n-2) -> O(n) with j index
            print(array[i], + "," + array[j]) # O(1)

# It has O(n) * O(n - 1) = O(n^2)