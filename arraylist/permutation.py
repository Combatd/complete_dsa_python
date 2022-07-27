def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    return list1 == list2

listOne = [1,2,3]
listTwo = [1,3,2]
aList = ['a', 'c', 'd']
bList = ['c', 'a', 'b']

[print(permutation(listOne, listTwo))]
[print(permutation(aList, bList))]