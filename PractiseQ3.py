# WAP to find power of a number

def power(base, exp):
    assert 0 <= exp == int(exp), "Invalid exponent"
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * power(base, exp - 1)


print(power(2, 2.5))
