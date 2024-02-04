# Insertion Sorting

arr = [3, 9, 1, 2, 0, 1, 4, 18, 12]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j = j - 1

    arr[j + 1] = key


print(arr)