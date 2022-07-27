myDict = {'one': 'uno', 'two': 'dos', 'three': 'tres', 'four': 'quarto'}

print('one' in myDict)
print('uno' in myDict.values()) # Time: O(1)

for key in myDict: # Time: O(n)
    print(key, myDict[key])

print(all(myDict)) # All values are truthy or dictionary is empty iterable

falseDict = {0: False, 1: True}
print(all(falseDict))

print(any(myDict))
print(any(falseDict)) # if any key has truthy value, return True
print(any({})) # empty iterable is false

print(len(myDict))
print(sorted(myDict))

alphaDict = {'e': 1, 'a': 2, 'u': 3, 'o': 4, 'i': 5}
betaDict = {'eee': 1, 'aaaaa': 2, 'uu': 3, 'ooooooo': 4, 'i': 5}
print(sorted(alphaDict))
print(sorted(betaDict, key=len))