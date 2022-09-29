def factorial(number):
    assert 0 <= number == int(number), 'Number should be a positive Integer only!'
    if number in [0, 1]:
        return 1
    else:
        return number * factorial(number - 1)


if __name__ == '__main__':
    n = int(input("Enter Number: "))
    print("Factorial of", n, "is", factorial(n))
