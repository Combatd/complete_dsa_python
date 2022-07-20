def printUnorderedPairs(array):
    for i in range(0, len(array)): # O(n-1) -> O(n) with i index
        for j in range(i + 1, len(array)): # O(n-2) -> O(n) with j index
            print(array[i], + "," + array[j]) # O(1)

# It has O(n) + O(n) which could be O(a) and O(b) due to 2 different arrays so O(ab)
# where the length of one array is a and the other length is b