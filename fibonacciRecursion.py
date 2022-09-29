def fib(n):
    assert 0 <= n == int(n), 'Fibonacci numbers cannot be -ve and non Integer'
    if n in [0, 1]:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    number = int(input("Enter Number:"))
    for i in range(0, number + 1):
        print(fib(i), end=" ")
    print("\nFibonacci series value for", number, "th index is", fib(number))
