arr = [1, 9, 2, 0, 5, 7, 1, 3]


# The loop need to go until n, so the time complexity is O(n)
for i in range(1, len(arr)):
    j = i - 1
    key = arr[i]
    # The time complexity is according to the working of while 
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j = j - 1

    arr[j + 1] = key
print(arr)