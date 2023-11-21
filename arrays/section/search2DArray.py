# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 16, 12, 8
# Day 4 - 15, 10, 14, 9

import numpy as np

twoDArray = np.array([ [1, 15, 10, 6], [10, 14, 11, 5], [12, 16, 12, 8], [15, 10, 14, 9] ])
print(twoDArray)

def searchTwoDarray(array, value):
  # rows length, then columns length
  for i in range(len(array)):
    for j in range(len(array[0])):
      if array[i][j] == value:
        return 'The value is located at index ' + str(i) + ' ' + str(j)
  return 'The element is not found'

print(searchTwoDarray(twoDArray, 14))
print(searchTwoDarray(twoDArray, 55))

""" 
Time Complexity: O(mn)
We iteratively check each row element until we find the target element value.
We go through each element row starting with the element in the first column.
So we have O(mn), where m is number of orws, and n is numebr of columns.

Space Complexity: O(1)
We are searching for an element within an existing 2D array so we don't need to
allocate any more space for these operations.

"""