integers = [1, 2, 3, 4]
print(integers)

stringList = ['Milk', 'Cheese', 'Butter']
print(stringList)

mixList = [1, 1.5, 'spam']
print(mixList)

nestedList = [1, 2, 4, 5, [1.5, 1.6], ['test']]
print(nestedList)

# Accessing/Traversing the List

shoppingList = ['Milk', 'Cheese', 'Butter'] 
print(shoppingList[0]) # access the first element
print(shoppingList[-1]) # last element
# Mapping, each index maps to one of the elements

print('Milk' in shoppingList)

for i in shoppingList:
    print(i)

for idx in range(len(shoppingList)):
    shoppingList[idx] = shoppingList[idx] + '+'
    print(shoppingList[idx])