"""  
Write a function that takes a tuple and a value, 
and returns a new tuple with the value inserted at the beginning of the original tuple.

"""

def insert_value_front(input_tuple, value_to_insert):
  return (value_to_insert,) + input_tuple # concatenation



"""  
Time Complexity: O(n)
In order to create a new tuple, we iterate through the elements of the old tuple
in order to copy them over with our new value to insert as the first element.


Space Complexity: O(n)
We are creating a new tuple which requires memory to store n + 1 number of elements.

"""