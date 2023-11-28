myDict = {'name': 'Eddy', 'age': 26}
myDict['age'] = 27
print(myDict)


""" 
Time Complexity: O(1)
We can access the attribute straight away without looping through elements.

Space Complexity: O(1)
No additional memory is allocated to update an existing value for a key.
"""

myDict['address'] = 'London'
print(myDict)

"""  
Time Complexity: O(1)
We can access the attribute straight away without looping through elements.

Space Complexity: amortized O(1)
If the existing capacity for space is reached from adding additional key-value pairs,
the amount of memory space will double to accept more key-value pairs.

"""