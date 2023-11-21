# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 16, 12, 8
# Day 4 - 15, 10, 14, 9

import numpy as np

twoDArray = np.array([ [1, 15, 10, 6], [10, 14, 11, 5], [12, 16, 12, 8], [15, 10, 14, 9] ])
print(twoDArray)

# newTwoDArray = np.insert(twoDArray, 0, [1, 2, 3, 4], axis=1)
# newTwoDArray = np.insert(twoDArray, 0, [1, 2, 3, 4], axis=0)

newTwoDArray = np.append(twoDArray, [[1, 2, 3, 4]], axis=0)
print(newTwoDArray)

""" 
Time Complexity: O(mn)
M is the number of column elements.
N is the nmber of row elements.
We will need to shift all elements in the rows and columns as we insert a new element.


Space Complexity: O(mn)
Moving all row and column elements over involves swapping element positions and transposing entire
matrices, so we need to allocate space for rows and columns.

"""