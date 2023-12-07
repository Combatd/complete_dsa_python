"""  
Define a function which takes as a parameter dictionary 
and returns a dictionary in which everse the key-value pairs are reversed.
"""

def reverse_dict(my_dict):
  new_dict = {}

  for key, value in my_dict.items():
    new_dict[value] = key

  return new_dict

# Time Complexity: O(n) iterate through each key value pair to add each one to the new dictionary reversed
# Space Complexity: O(n) each key value pair will be added to a new dictionary relative to the amount of key value pairs in the original dictionary

"""  
def reverse_dict(my_dict):
    return {value: key for key, value in my_dict.items()}
"""

""" 
Time complexity:

The overall time complexity of this function is O(n), where n is the number of elements in the dictionary my_dict. This is determined by the dictionary comprehension, which iterates through all the key-value pairs in the input dictionary.

Space complexity:

The space complexity of this function is O(n), where n is the number of elements in the dictionary my_dict. This is because the function creates a new dictionary with the same number of elements as the input dictionary but with reversed key-value pairs.


 """