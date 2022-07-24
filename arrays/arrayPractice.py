from array import *

# 1. Create an array and traverse

my_array = array('i', [1, 2, 3, 4, 5])

for i in my_array:
    print(i, ' <- traverse and printing out elements one by one')

# 2. Access individual eleemnts through indees
print("Step 2")
print(my_array[0])
print(my_array[3])

# 3. Append any value to the array using append() method

print("Step 3")
my_array.append(6)
print(my_array)

# 4. Insert value in an array using insert() method

print("Step 4")
my_array.insert(3, 11)
print(my_array)

# 5. Extend python array using extend() method

my_array1 = array('i', [10, 11, 12])
my_array.extend(my_array1)
print(my_array)