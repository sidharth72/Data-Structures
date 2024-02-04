arr = [6, 1, 2, 3, 8, 1, 2]

for i in range(len(arr)):
    minpos = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[minpos]:
            minpos = j

    arr[i], arr[minpos] = arr[minpos], arr[i]

print(arr)