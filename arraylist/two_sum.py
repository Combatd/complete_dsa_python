# Write a program to find all pairs of integers whose sum is equal to a given number.

# Does array contain only positive / negative numbers?
# What if the same pair repeats, do we print them every time?
# If the reverse of the pair is acceptable, can we print both (4, 1) amd (1,4) if sum is 5?
# Do we need to print only distinct pairs? Does (3, 3) count as a valid pair of 6?
# How big is the array?

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]: # numbers must be distinct for pairs
                continue
            if nums[i] + nums[j] == target:
                print(i, j)

myList = [1, 2, 3, 2, 3, 4, 5, 6]

two_sum(myList, 6)