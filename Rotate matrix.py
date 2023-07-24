import numpy as np

def rotates(arr, n):
    arr = np.transpose(arr)

def reverse(arr1, n):
    for x in range(len(arr1)):
        i = 0
        j = len(arr1[0]) - 1
        while i < j:
            temp = arr1[x][i]
            arr1[x][i] = arr1[x][j]
            arr1[x][j] = temp
            i += 1
            j -= 1

n = int(input())
arr = []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

rotates(arr, n)
reverse(arr, n)

for value in arr:
    print(value)
