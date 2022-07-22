def factorial(n): # M(n)
    if n < 0:
        return -1 # O(1)
    elif n == 0:
        return 1 # O(1)
    else:
        return n * factorial(n-1) # M(n - 1)

    # We need to measure the recursive algorithm here
    # n! = 1 * 2 * 3..... * n
    #  3! = 1 * 2 * 3 = 6
    # M(n-1) = O(1) + M((n-1))-1  
    # M(n-2) = O(1) + M((n-2))-1
    # a + M(n-a)
    # n + M(n - n)  
    # n + 1
    # n
    # The time complexity is O(n)