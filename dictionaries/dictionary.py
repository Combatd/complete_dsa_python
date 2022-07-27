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

def traverseDict(dict): # Time Complexity: O(n), Space Compleixty: O(1)
    for key in dict: # O(n)
        print(key, dict[key]) # O(1)

traverseDict(myDict)

# Linear Search
def searchDict(dict, value): # Time Complexity: O(n), Space Complexity: O(1)
    for key in dict: # O(n)
        if dict[key] == value: # O(1)
            return key, value # O(1)
    return 'The value does not exist' # O(1)

print(searchDict(myDict, 27))
print(searchDict(myDict, 26))