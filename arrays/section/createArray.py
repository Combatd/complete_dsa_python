import array

my_array = array.array('i')
print(my_array) # array('i')

my_array1 = array.array('i', [1, 2, 3, 4])
print(my_array1) # array('i', [1, 2, 3, 4])

# array model is homogenous, so all elements are the same type

import numpy as np

np_array = np.array([], dtype=int)
print(np_array) # []

np_array1 = np.array([1, 2, 3, 4], dtype=int)
print(np_array1) # [1 2 3 4]

# numpy array model has a feature rich high performance array object, with many operations and functions

""" 
Creating a new array

Time Complexity: O(1)
it requires minimal data operations, with array metadata, and allocating minimal memory
for array operations

Space Complexity: O(1)
An empty array has no elements. The memory allocated for the elements is minimal or none depending on the model used.
The memory used for array metadata is constant and does not depend on the number of elmeents.


An array with elements
Time Complexity: O(n) linear
The process of creating an array with elements involves copying elements from the input iterable
(python List) to the new array. It increases by each new element proportionally

Space Complexity: O(n)
As the number of elements increases, the memory needed to store those elements also increases proportionally.

Both the time taken to copy elements and memory allocation for elements are based on the number of elements.
If there are no elements, then it is constant.

 """