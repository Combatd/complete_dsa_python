def power(base, exp):
    # unintentional case
    assert exp >= 0 and int(exp) == exp, 'exponent must be positive integer' # unintentional case
    # base case
    if (exp == 0):
        return 1
    elif (exp == 1):
        return base
    else:
        # recursive case : 2^4 = 2*2*2*2 , x^a * x^b = x^a+b
        return base * power(base, exp - 1)

print(power(2, 4))
print(power(1, 0))
print(power(3.2, 2))
print(power(2, 1.2))
print(power(2, -1))