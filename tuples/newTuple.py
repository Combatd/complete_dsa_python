newTuple = (
  'a',
  'b',
  'c',
  'd',
  'e'
)
newTuple1 = ('a',)
newTuple2 = tuple('abcde')

print(newTuple)
print(newTuple1)
print(newTuple2)

""" 
Time Complexity: O(1)
A tuple declares all the elements upfront, a very quick way to create a collection

Space Complexity: O(n)
A tuple grows by the amount of elements inside of it.

"""