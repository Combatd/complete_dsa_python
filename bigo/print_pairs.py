def printPairs(array):
    for i in array: # O(n)
        for i in array: # O(n) at every iteration
            print(str(i) + "," + str(j)) # O(1)

# In a for loop of O(n), each n iteration has an O(n) for loop that runs. n(n) = O(n^2) quadratic