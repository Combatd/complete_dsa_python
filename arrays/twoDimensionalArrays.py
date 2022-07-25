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

def traverse2DArray(array): # Time Complexity: O(n^2), Space Complexity: O(1) 
    for i in range(len(array)): # O(mn) as it is rows and columns
        for j in range(len(array[0])): # 0(n) to access columns
            print(array[i][j]) # O(1)

traverse2DArray(twoDArray)

# Linear Search
def search2DArray(array, value): # Time Complexity: O(n^2) , Space Complexity: O(1)
    for i in range(len(array)): # O(mn)
        for j in range(len(array[0])): # O(n)
            if array[i][j] == value: # O(1)
                return "The value is located at index " + str(i) + " " + str(j) # O(n)
    return "The element is not found" # O(1)

print(search2DArray(twoDArray, 14))

new2DArray = np.delete(twoDArray, 1, axis = 1) # 0 axis for deleting rows and 1 for deleting columns
print(new2DArray)