import array

my_array1 = array.array('i', [1,2,3,4])
print(my_array1)
my_array1.insert(5, 6)
print(my_array1)

""" 
Time Complexity: O(n)
It depends on how many elements we need to shift over.

If we have to shift all our elements to the right, such as when we place
our new element at the beginning, we get the worst case based on the total
number of elements.

Space Complexity: O(1)
We need only one place in memory to insert the element.
"""