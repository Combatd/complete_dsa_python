# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 16, 12, 8
# Day 4 - 15, 10, 14, 9

import numpy as np

twoDArray = np.array([ [1, 15, 10, 6], [10, 14, 11, 5], [12, 16, 12, 8], [15, 10, 14, 9] ])

print(twoDArray)



""" 
Time Complexity: O(n)
We initialize all values within a created array

Space Complexity: O(n)
We have n number of rows and n number of columns
We are going to need to allocate all the space for it in memory.

"""