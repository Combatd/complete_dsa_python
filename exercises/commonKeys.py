"""  
Define a function with takes two dictionaries as parameters and merge them 
and sum the values of common keys.
"""


def merge_dicts(dict1, dict2):
  merged_dict = dict1.copy()
  for key, value in dict2.items():
    if key in dict1.keys():
      merged_dict[key] += value
    else:
      merged_dict[key] = value

  return merged_dict
      
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

print(merge_dicts(dict1, dict2))


""" 
def merge_dicts(dict1, dict2):
  merged_dict = dict1.copy()
  for key, value in dict2.items():
    merge_dict[key] = merged_dict.get(key, 0) + value

  return merged_dict
 """