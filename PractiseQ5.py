# WAP to convert a number from Decimal to binary


def decimal_to_binary(n):
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimal_to_binary(n / 2)

decimal_to_binary(10)
