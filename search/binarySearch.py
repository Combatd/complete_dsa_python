# Create function with 2 parameters which are a sorted array and a value
# Create 2 pointers: a left pointer at the start of the array and a right pointer at the end of the array
# Based on left and right pointers calculate middle pointer
# While middle is not equal to the value and start <= end loop:
    # if the middle is greater than the value move the right pointer down
    # if the midle is less than  the value move the left pointer up
# If the value is never found return -1
import math
def binarySearch(array, value):
    start = 0
    end = len(array) - 1
    middle = math.floor((start + end) / 2)
    # print(start, middle, end)
    while not (array[middle] == value) and start <= end:
        if value < array[middle]:
            end = middle - 1 # move the right pointer down
        else:
            start = middle + 1 # move the left pointer up
        middle = math.floor((start + end) / 2)
        # print(start, middle, end)
    if array[middle] == value:
        return middle
    else:
        return -1

custArray = [8, 9, 12, 15, 17, 19, 20, 21, 28]
print(binarySearch(custArray, 15))