# Find Unique values from the array

arr = [3, 7, 1, 8, 3, 8, 9, 2]

for i in range(len(arr)):
    is_unique = True
    for j in range(len(arr)):
        if i != j and arr[i] == arr[j]:
            is_unique = False
    if is_unique:
        print(arr[i])