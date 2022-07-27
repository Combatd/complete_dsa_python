myDict = {'name': 'Eddy', 'age': 26, 'address': 'London', 'education': 'master'}

dict = myDict.copy()
print(myDict)
print(dict)

newDict = {}.fromkeys([1,2,3], 0)
print(newDict)

print(myDict.get('city', 27)) # will return the value 27 if key doesn't exist
print(myDict.get('city'))

print(myDict.items())
print(myDict.keys())

print(myDict.popitem())
print(myDict)

myDict.setdefault('name', 'added') # will still return "Eddy" for name
myDict.setdefault('name1', 'added') # name1 key now has value of "added"

myDict.pop('name1')
print(myDict)

print(myDict.values())

someDict = {'a': 1, 'b': 2, 'c': 3}
myDict.update(someDict)
print(myDict)