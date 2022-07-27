# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b 
# print(c)

# a = [0, 1]
# a = a * 4
# print(a) # Multiple copies of list a

a = [0, 1, 2, 3, 4, 5, 6]
print(len(a))
print(max(a))
print(min(a))
print(sum(a))
print(sum(a) / len(a))

list = []
while True:
    inp = input('Enter a number: ')
    if (inp == 'done'): break
    value = float(inp)
    list.append(value)
    total = sum(list)
    count = len(list)
    average = total / count

print("Average: ", average)
    
