# Time: O(n)
# Space: O(1)

# Create function with 2 parameters which are an array and a value
# Loop through the array and check if the current array element is equal to the value
# If it exists, return the index at which the element is found
# If the value is never found, return -1

def linearSearch(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    
    return -1


print(linearSearch([20, 40, 30, 50, 90], 50), " <- linearSearch")
print(linearSearch([20, 40, 30, 50, 90], 100), " <- linearSearch")