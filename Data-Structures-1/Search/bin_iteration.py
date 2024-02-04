def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (high + low) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr = [2, 5, 9, 15, 22, 34, 59]
index = binary_search(arr, 34)

if index != -1:
    print(f"Found at: {index}")
else:
    print("Not Found")