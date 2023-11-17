import array

my_array1 = array.array('i', [1,2,3,4,5,6])
print(my_array1)

def accessElement(array, index):
  if index > len(array):
    print('There is not any element in this index')
  else:
    print(array[index])

accessElement(my_array1, 1)
accessElement(my_array1, 8) # out of bounds




""" 
Time Complexity: O(1)
We have an index to access an array element directly without
touching any other element, so it will always be constant time.

Space Complexity: O(1)
We access an already existing element in the array. No additional
memory needs to be allocated.
"""