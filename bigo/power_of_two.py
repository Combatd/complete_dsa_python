def powerOfTwo(n):
    if n < 1:
        return 0 # O(1)
    elif n == 1:
        print(1) # O(1)
        return 1 # O(1)
    else:
        prev = powerOfTwo(int(n/2)) # O(n / 2) as it will keep going lower and lower...so the calculation will be less than n
        curr = prev * 2 # O(1)
        print(curr) # O(1)
        return curr # O(1)

        #  powerOfTwo(50) return 32
        # powerOfTwo(25) return 16 ... keeps going down by 2 as opposed to becoming exponentially larger
        # O(log_2 n)
        # O (log N)