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
            arr[j], arr[i] = arr[i], arr[j]

    arr[high], arr[i + 1] = arr[i + 1], arr[high]

    return i + 1

arr = [4, 1, 6, 8, 2, 3]
quick_sort(arr, 0, len(arr) - 1)

print(arr)