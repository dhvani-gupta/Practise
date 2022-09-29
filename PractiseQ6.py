arr = []
arr1 = []
count = 0
count1 = 0
n = int(input("Enter Size of array:"))

print("Enter first array:")
for i in range(0, n):
    ele = int(input())
    arr.append(ele)
print("Enter second array:", )
for j in range(0, n):
    ele2 = int(input())
    arr1.append(ele2)

# print(arr, arr1)

for i in range(0, n):
    for j in range(0, n):
        if arr[i] == arr1[j]:
            count1 += 1
    if arr[i] == arr1[i]:
        count += 1
print("Perfect", count)
print("imperfect", count1-count)
