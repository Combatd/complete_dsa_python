# Time: O(n^2)
# Space: O(1)

def bubbleSort(customList):
    for i in range(len(customList) - 1): # O(n)
        for j in range(len(customList) - i - 1): # O(n)
            if customList[j] > customList[j + 1]: # O(1)
                temp = customList[j] # O(1)
                customList[j] = customList[j + 1] # O(1)
                customList[j + 1] = temp # O(1)
                # shorthand : customList[j], customList[j + 1] = customList[j + 1], customList[j]
    print(customList)

cList = [2, 1, 7, 6, 5, 3, 4, 9, 8]
bubbleSort(cList)