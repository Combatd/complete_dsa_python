def fibonacci(n):
    assert n >= 0 and int(n) ==  n, 'Fibonacci number must be positive integer only!' # unintentional case
    if n in [0, 1]:
        return n
    else:
        # recursive case is f(n) = f(n - 1) + f(n - 2)
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))
print(fibonacci(2))
print(fibonacci(7))
print(fibonacci(-1))