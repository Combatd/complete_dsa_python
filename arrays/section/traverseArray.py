import array

my_array1 = array.array('i', [1,2,3,4])
print(my_array1)
# my_array1.insert(2, 9)
# print(my_array1)

my_array2 = array.array('d', [1.3, 1.5, 1.6])

def traverseArray(array):
  for i in array:
    print(i)

traverseArray(my_array1)

""" 
Time Complexity: O(n)
A traversal visits every element once.


Space Complexity: O(1)
We don't need to allocate any new memory

 """