import array

my_array1 = array.array('i', [1,2,3,4,5,6])

def linear_search(array, target):
  for i in range(len(array)):
    if array[i] == target:
      return i
  return -1

print(linear_search(my_array1, 5)) # => 4



""" 
Time Complexity: O(n)
It will loop through each and every element of the array until it finds the target value.

Space Complexity: O(1)
Accessing attributes like length of the array or creating a range for iterating does
not require allocating a huge amount of memory.

"""