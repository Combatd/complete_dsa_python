my_dict = {'name': 'Eddy', 'age': 26, 'address': 'London', 'education': 'master'}

# del my_dict['age']

# removed_element = my_dict.pop('name', None)
removed_element = my_dict.popitem() # remove last inserted key value pair

print(removed_element)
print(my_dict)


""" 
Time Complexity: O(1)
This is a hash table deletion, we find the element by key and delete the value in the memory location

Space Complexity: O(1)
No additional space needs to be allocated to the dictionary when a value is removed

 """

my_dict.clear()

print(my_dict)

""" 
Time Complexity: O(n)
Every key and value pair has to be found and removed from memory one by one

Space Complexity: O(1)
No additional space needs to be allocated to the dictionary when values are removed

 """
