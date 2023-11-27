my_dict = dict()
print(my_dict)
my_dict2 = {}
print(my_dict2)

# Empty Dictionary Time and Space: O(1)

eng_sp = dict(one='uno', two='dos', three='tres')
print(eng_sp)

eng_sp_2 = {'one':'uno', 'two':'dos', 'three':'tres'}
print(eng_sp_2)

eng_sp_list = [('one','uno'), ('two','dos'), ('three','tres')]
eng_sp3 = dict(eng_sp_list)
print(eng_sp3)

""" 
Time Complexity: O(n)

Each key and value pair needs to be inserted in the dictionary one by one.

Space Complexity: O(n)

The dictionary will need to store each key and value pair in memory.

 """