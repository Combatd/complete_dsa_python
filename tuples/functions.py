myTuple = (1, 4, 3, 2, 5)
myTuple1 = (1, 2, 6, 9, 8, 7)

print(myTuple + myTuple1)

# We cannot multiply sequence of tuples with other tuples ex: myTuple * myTuple1
print(myTuple * 4)

print(4 in myTuple)

# Tuples are immutable, so we cannot change them by adding or removing

print(myTuple.count(2))

print(len(myTuple))
print(max(myTuple))
print(min(myTuple))

print(tuple([1, 2, 3, 4, 5])) # converted list to tuple