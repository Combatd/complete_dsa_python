my_dict = {'name': 'Eddy', 'age': 26, 'address': 'London', 'education': 'master'}

# my_dict.clear()

dict = my_dict.copy()

new_dict = {}.fromkeys([1, 2, 3])



print(my_dict)
print(dict)
print(new_dict)

print(my_dict.get('age', 27))
print(my_dict.get('city', 27))
print(my_dict.items())
print(my_dict.keys())

print(my_dict.setdefault('name', 'added'))
print(my_dict.setdefault('name1', 'added'))
print(my_dict)

print(my_dict.popitem())
print(my_dict)

print(my_dict.pop('name1', 'not exist'))

print(my_dict.values())

new_dict = {'a': 1, 'b': 2, 'c': 3}

my_dict.update(new_dict)

print(my_dict)