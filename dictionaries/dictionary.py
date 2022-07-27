# myDict = dict()
# print(myDict)

# secondDict = {}
# print(secondDict)

# myDict = {1: 'one', 2: 'two'}
# engToSp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
# print(engToSp)
# print(engToSp['one']) # Time Complexity: O(1)

myDict = {'name': 'Eddy', 'age': 26}
myDict['age'] = 27 # Time Complexity: O(1) Space Complexity: O(1)
myDict['address'] = 'London' # Time Complexity: O(1) Space Complexity: amortized O(1) - underlying linked list needs to grow
print(myDict)