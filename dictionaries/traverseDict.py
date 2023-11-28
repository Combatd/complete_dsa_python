myDict = {'name': 'Eddy', 'age': 26, 'address': 'London'}

def traverseDict(dict):
  for key in dict: # Time: O(n) - it will iterate through the collection one by one
    print(key, dict[key]) # prints key and value - Time: O(1)

traverseDict(myDict)

""" 
Time Complexity: O(n)
We have to loop through and check each key value pair one by one

Space Complexity: O(1)
No additional memory is allocated to access existing values of a dictionary.

"""