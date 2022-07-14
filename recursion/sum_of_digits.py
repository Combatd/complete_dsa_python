def sum_of_digits(n):
    assert n >= 0 and int(n) ==  n, 'The number must be positive integer only!' # unintentional case
    # base case
    if (n == 0):
        return 0
    else:
    # recursive case
    # If we take 10, we can divide 10/10 to get 1 with remainder 0, 54 / 10 as 5 and remainder 4
    # 112/10 = 11 and remainder 2, but 11/10 = 1 and remainder 1
    # f(n) = n % 10 + f(n / 10)
        return int(n % 10) + sum_of_digits(int(n / 10))

print(sum_of_digits(112))
print(sum_of_digits(4))
print(sum_of_digits(11))
print(sum_of_digits(1234))
print(sum_of_digits(11111))
print(sum_of_digits(-299))