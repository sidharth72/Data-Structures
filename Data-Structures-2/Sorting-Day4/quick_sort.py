def quick_sort(arr, low, high):
    if low <= high:

        pivot_index = partition(arr, low, high)

        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[high], arr[i + 1] = arr[i+1], arr[high]

    return i + 1


arr = [3, 14, 7, 2, 8, 1, 2]
quick_sort(arr, 0, len(arr) - 1)
print(arr)