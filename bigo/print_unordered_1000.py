def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(0, 100000):
                print(str(arrayA[i] + "," + str(arrayB(j))))

# 2 separate arrays being iterated so O(a) and O(b)
# k loop will always print a constant 100000, but 1000000 is still constant like 1
# O(a) * O(b) * O(100000) = O(ab) + O(1) = O(ab)