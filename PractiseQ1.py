import sys


def get_ints():
    return map(int, input().strip().split())


def func(N):
    if N == 0:
        return "a"
    elif N == 1:
        return "b"
    elif N == 2:
        return "c"
    else:
        return func(N - 1) + func(N - 2) + func(N - 3)


def findChar(k, N):
    if len(N) < k:
        return -1
    else:
        return N[k - 1]


while True:
    try:
        n, c = get_ints()
    except EOFError:
        break
    # stringObtained = str(func(n))
    # print(stringObtained)
    # print(type(stringObtained))
    print(findChar(c, func(n)))

    sys.exit()
