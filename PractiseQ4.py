# WAP to find HCF/ GCD of 2 numbers

def gcd(n1, n2):
    assert n1 == int(n1) and n2 == int(n2), "Invalid Numbers"
    if n1 < 0:
        n1 = -1 * n1
    if n2 < 0:
        n2 = -1 * n2

    if n2 == 0:
        return n1
    else:
        return gcd(n2, n1 % n2)


n = int(input("Number1:"))
m = int(input("Number2:"))
print(gcd(n, m))
