import array

my_array1 = array.array('i', [1,2,3,4,5,6])

# We can't just target an element and delete it directly or we lose our indexes.
# We have to remove an element and move the existing elements in memory.

my_array1.remove(4) # [1, 2, 3, 5, 6]
print(my_array1)

""" 
Time Complexity: O(1)
After we access the element and remove it, we must move all the subsequent elements to fill the empty space.

Space Complexity: O(1)
We don't allocate additional memory than what is already in the array if we are just moving elements after removing one.

"""