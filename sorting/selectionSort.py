
# Time: O(n^2)
# Space: O(1)
def selectionSort(customList):
    for i in range(len(customList)): # O(n)
        min_index = i
        for j in range(i + 1, len(customList)): # O(n)
            if customList[min_index] > customList[j]:
                min_index = j
        temp = customList[i]
        customList[i] = customList[min_index] # O(1)
        customList[min_index] = temp
        # shorthand: customList[i], customList[min_index] = customList[min_index], customList[i]
    print(customList)

cList = [2, 1, 7, 6, 5, 3, 4, 9, 8]
selectionSort(cList)