def allFib(n):
    for i in range(n):
        print(str(i) + ":, " + str(fib(i)))

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    return fib(n - 1) + fib(n - 2)

    # F1(n - 1) + f(n - 2)
    # F(n) + F(n)
    # n + n
    # 2^n
    # branches^depth -> O(2^N)
    # fib(1) = 2^1
    # fib(4) = 2^4
    # fib(n) = 2^n
    # 2^n+1-2
    # O(2^n)