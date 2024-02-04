# Bubble Sort

arr = [3, 9, 1, 2, 0, 1, 4, 18, 12]


for i in range(len(arr)):
    for j in range(0, len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]


print(arr) 
