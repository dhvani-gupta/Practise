# def firstMethod():
#     secondMethod()
#     print("First")
#
#
# def secondMethod():
#     thirdMethod()
#     print("second")
#
#
# def thirdMethod():
#     FourthMethod()
#     print("Third")
#
#
# def FourthMethod():
#      print("Fourth")
#
#
# if __name__ == '__main__':
#     print("START")
#     firstMethod()
#
# def recursiveMethod(n):
#     if n < 1:
#         print(n, "<1")
#     else:
#         recursiveMethod(n - 1)
#         print(n)
#
#
# if __name__ == '__main__':
#     n = 5
#     recursiveMethod(n)



# import time
#
#
# def powerOfTwo_r(n):
#     if n == 0:
#         return 1
#     else:
#         power = powerOfTwo_r(n - 1)
#         return power * 2
#
#
# def powerOfTwo_i(n):
#     i = 0
#     power = 1
#     while i < n:
#         power = power * 2
#         i = i + 1
#     return power
#
#
# if __name__ == '__main__':
#     n = 4
#     po = powerOfTwo_r(n)
#     print("recursion", po)
#     p = time.process_time()
#     print(p)
#
#     pow = powerOfTwo_i(n)
#     print("Iteration", pow)
#     m = time.process_time()
#     print(m)

