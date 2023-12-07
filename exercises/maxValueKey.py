"""  
Define a function which takes a dictionary as a parameter 
and returns the key with the highest value in a dictionary.
"""

def max_value_key(my_dict):
  max_pair = ['key', 0]
  
  for key, value in my_dict.items():
    if value > max_pair[1]:
      max_pair = [key, value]

  return max_pair[0]

my_dict = {'a': 5, 'b': 9, 'c': 2}
print(max_value_key(my_dict))

"""  
def max_value_key(my_dict):
    return max(my_dict, key=my_dict.get)
"""

""" 
Time complexity:

The overall time complexity of this function is O(n), where n is the number of elements in the dictionary my_dict. 
This is determined by the max() function, which iterates through all the keys in the dictionary.

Space complexity:

The space complexity of this function is O(1), 
as it does not create any additional data structures or store any intermediate values. 
The max() function only keeps track of the current maximum value and its corresponding key, which requires constant space

 """