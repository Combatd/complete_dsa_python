def decimalToBinary(n):
    # unintentional case
    assert int(n) == n, 'The number must be an integer only'
    # base case
    if n == 0:
        return 0
    else:
    # recursive case : f(n) = n % 2 + 10 * f(n/2)
        return n % 2 + 10 * decimalToBinary(int(n / 2))

print(decimalToBinary(10))
print(decimalToBinary(13))
print(decimalToBinary(-13))