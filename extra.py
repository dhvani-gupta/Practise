# # def noOfCheckMultiple(n):
# #     for i in range(0,n):
# #         checkMultiple(n):
# def checkMultiple(m):
#     for num in range(1, 11):
#         if num % m == 0:
#             print(num, "-", m, "-")
#         else:
#             print(num)
#
#
# n = int(input("Enter Number of numbers for which you want to check multiples:"))
# listOfNumber = []
# for i in range(0, n):
#     number = int(input("Enter Number"))
#     #checkMultiple(number)
#     listOfNumber.append(number)
# for i in range(0, n):
#     checkMultiple(listOfNumber[i])


# n = int(input("Enter limit."))
# for i in range(1, n + 1):
#     if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
#         print(i, "-3,5,7-")
#     elif i % 3 == 0 and i % 5 == 0:
#         print(i, "-3,5-")
#     elif i % 3 == 0 and i % 7 == 0:
#         print(i, "-3,7-")
#     elif i % 5 == 0 and i % 7 == 0:
#         print(i, "-5,7-")
#     elif i % 3 == 0:
#         print(i, "-3-")
#     elif i % 5 == 0:
#         print(i, "-5-")
#     elif i % 7 == 0:
#         print(i, "-7-")
#     else:
#         print(i)
