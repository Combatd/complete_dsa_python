import numpy as np

twoDArray = np.array([ [11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9] ]) # Time Complexity O(MN) m columns and n rows
print(twoDArray)

# newTwoDArray = np.insert(twoDArray, 0, [[1, 2, 3, 4]], axis=0)
# print(newTwoDArray)

# newTwoDArray = np.append(twoDArray, [[1, 2, 3, 4]], axis=0)
# print(newTwoDArray)

def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]): # O(1)
        print("Incorrect index") # O(1)
    else:
        print(array[rowIndex][colIndex]) # O(1)

accessElements(twoDArray, 2, 3)

def traverse2DArray(array): # Space Complexity: O(1) Time Complexity: O(n^2)
    for i in range(len(array)): # O(mn) as it is rows and columns
        for j in range(len(array[0])): # 0(n) to access columns
            print(array[i][j]) # O(1)

traverse2DArray(twoDArray)