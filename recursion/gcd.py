    # Greatest Common Divisor is the largest positive integer that divideds the numbers without a remainder
    # gcd(8, 12)
    #  8 = 2 * 2 * 2
    #  12 = 2 * 2 * 3

def gcd(a, b):
    assert int(a) == a and int(b) == b, "The numbers a and b must be integer only!"
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        # recursive case - gcd(a, 0) = a and gcd(a, b) = gcd(b, a mod b)
        return gcd(b, a % b) # euclidiean algorithm

print(gcd(48, 18))
print(gcd(48, -18))
print(gcd(48, 1.8)) # will hit assertion
