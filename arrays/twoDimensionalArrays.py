import numpy as np

twoDArray = np.array([ [11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9] ]) # Time Complexity O(MN) m columns and n rows
print(twoDArray)

# newTwoDArray = np.insert(twoDArray, 0, [[1, 2, 3, 4]], axis=0)
# print(newTwoDArray)

# newTwoDArray = np.append(twoDArray, [[1, 2, 3, 4]], axis=0)
# print(newTwoDArray)

def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print("Incorrect index")
    else:
        print(array[rowIndex][colIndex])

accessElements(twoDArray, 2, 3)