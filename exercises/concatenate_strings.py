"""  
Write a function that takes a tuple of strings and concatenates them, 
separating each string with a space
"""

def concatenate_strings(input_tuple):
  new_string = ""
  for i in range(len(input_tuple) - 1):
    new_string += input_tuple[i] + ' '
  new_string = new_string + input_tuple[-1]
  return new_string


""" 
Time Compleixty: O(n)
We have to iterate through each string element in the input tuple to create the new string.


Space Complexity: O(n)
We create a new string with n elements and spaces in between, so we allocate memory accrordingly.
"""