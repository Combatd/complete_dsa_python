newTuple = (
  'a',
  'b',
  'c',
  'd',
  'e'
)

print('a' in newTuple) # => True
# Time: O(n) linear search through tuple elements one by one
# Space: O(1) no memory required for a search

print(newTuple.index('c')) # => 2
# Time: O(n) linear search through tuple elements one by one
# Space: O(1) no memory required for a search

def searchTuple(p_tuple, element):
  for i in range(0, len(p_tuple)):
    if p_tuple[i] == element:
      return f"The {element} is found at {i} index"
  
  return "The element is not found"

print(searchTuple(newTuple, 'b'))

""" 
Time Complexity: O(n)
We loop through each element of the tuple to find the element and element index

Space Complexity: O(1)
We don't require more memory to perform a search of a Tuple's elements

"""