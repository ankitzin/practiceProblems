arr = [5, 5, 7, 6, 3, 4, 8, 6]
# arr = [3, 7, 4, 5]


count = 0
for i in range(0, len(arr)-1):
    if (arr[i] >= arr[i+1]) and arr[i+1] >= arr[i+2]:
        arr[i+1] = arr[i+2] - 1
        count += 1

print(count)
