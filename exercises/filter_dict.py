"""  
Define a function that takes a dictionary as a parameter 
and returns a dictionary with elements based on a condition.

"""

def filter_dict(my_dict, condition):
  filtered_dict = {}
  for key, value in my_dict.items():
    if condition(key, value):
      filtered_dict[key] = value

  return filtered_dict

# Time: O(n) as we will check each key value pair if it matches the lambda condition one by one
# Space: O(n) as potentially every single dicitonary key-value pair could match the condition as we put it into a new dictionary

""" 
def filter_dict(my_dict, condition):
    return {k: v for k, v in my_dict.items() if condition(k, v)}
"""

"""  
Time complexity:

The overall time complexity of this function is O(n), where n is the number of elements 
in the dictionary my_dict. This is determined by the dictionary comprehension, 
which iterates through all the key-value pairs in the input dictionary.

Space complexity:

The space complexity of this function depends on the number of elements in the filtered 
dictionary, which in turn depends on the condition function.
In the worst case, when all key-value pairs meet the condition, 
the space complexity is O(n), where n is the number of elements in the dictionary my_dict. In the best case, when no key-value pairs meet the condition, the space complexity is O(1) as the function creates an empty dictionary.s
"""