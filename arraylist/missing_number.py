# How to find the missing number in an integer array of 1 to 100?
# One number will be 0 instead of the correct number!
# 1+2+3+...+n = n(n+1) / 2

def find_missing_number(array):
    sum1 = len(array) * (len(array) + 1) / 2
    sum2 = sum(array)
    if sum1 >= sum2:
        return sum1 - sum2
    else:
        return sum2 - sum1
    
myList = [1, 2, 3, 4, 5, 6, 7, 8, 0, 10]
print(find_missing_number(myList))