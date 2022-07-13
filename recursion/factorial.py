def factorial(n):
    assert n >= 0 and int(n) ==  n, 'The number must be positive integer only!' # unintentional case
    if n in [0,1]:
        return 1 # base case will return as final invocation
    else:
        return n * factorial(n - 1) # recursive case

print(factorial(3))
print(factorial(2))
print(factorial(10))
print(factorial(-1)) # should hit our assertion