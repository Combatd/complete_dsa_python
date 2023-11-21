# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 16, 12, 8
# Day 4 - 15, 10, 14, 9

import numpy as np

twoDArray = np.array([ [1, 15, 10, 6], [10, 14, 11, 5], [12, 16, 12, 8], [15, 10, 14, 9] ])
print(twoDArray)

def accessElements(array, rowIndex, colIndex):
  if rowIndex >= len(array) and colIndex >= len(array[0]):
    print("Incorrect index")
  else:
    print(array[rowIndex][colIndex])

accessElements(twoDArray, 2, 3)

""" 
a[i][j] i is row index, j is column index

Time Complexity: O(1)
Checking to make sure the index is not out of bounds and accessing an element by index and printing out are very fast operations.


Space Complexity: O(1)
We don't need to allocate more memory when we are accessing an element

"""