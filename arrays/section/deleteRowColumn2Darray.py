# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 16, 12, 8
# Day 4 - 15, 10, 14, 9

import numpy as np

twoDArray = np.array([ [1, 15, 10, 6], [10, 14, 11, 5], [12, 16, 12, 8], [15, 10, 14, 9] ])
print(twoDArray)

newTDarray = np.delete(twoDArray, 1, axis = 1)
print(newTDarray)




""" 
Time Complexity: O(mn)
You must copy every over every element excluding the deleted target element.

Space Compelxity: O(mn)
Space must be allocated for all the rows and columns of elements minus the deleted element.

"""