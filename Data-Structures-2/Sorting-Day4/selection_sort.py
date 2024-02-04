arr = [3, 11, 2, 5, 9]

for i in range(len(arr)):
    minpos = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[minpos]:
            minpos = j

    arr[minpos], arr[i] = arr[i], arr[minpos]

print(arr)