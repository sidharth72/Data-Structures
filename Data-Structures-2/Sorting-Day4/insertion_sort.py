arr = [1, 7, 2, 9, 8, 3]

for i in range(len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key


print(arr)