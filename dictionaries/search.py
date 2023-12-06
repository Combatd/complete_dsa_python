
myDict = {'name': 'Eddy', 'age': 26, 'address': 'London'}

def searchDict(dict, value):
  for key in dict:
    if dict[key] == value:
      return key, value
  return 'The value does not exist'


print(searchDict(myDict, 26))
print(searchDict(myDict, 27))

"""  
Time Complexity: O(n)
We have to visit each key value pair in the dictionary, and return it if
it matches the value argument.


Space Complexity: O(1)
We don't need to allocate additional memory to perform a search by key
"""