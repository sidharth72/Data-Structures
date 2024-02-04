def binary_search(arr, low, high, target):

    if low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return f"Found at {mid}"
        elif arr[mid] < target:
            # Passing sub array to the same function, recursion happens
            return binary_search(arr, mid + 1, high, target)
        else:
            # Passing sub array to the same function, recursion happens
            return binary_search(arr, low, mid - 1, target)

    return -1

arr = [2, 5, 9, 15, 22, 34, 59]
index = binary_search(arr, 0, len(arr) - 1, 22)
print(index)
