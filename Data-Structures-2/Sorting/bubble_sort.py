
arr = [5, 4, 9, 1]

for i in range(len(arr)):
    for j in range(0, len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j + 1], arr[j] = arr[j], arr[j + 1]

print(arr)