# wap to find the sum of a digits recursively


def sum_of_digits(number):
    assert 0 <= number and int(number) == number, "Invalid Number "
    if number == 0:
        return 0
    else:
        return int(number % 10) + sum_of_digits(int(number / 10))


if __name__ == '__main__':
    n = int(input("Enter a number:"))
    print("Sum of digits of", n, "is", sum_of_digits(n))

