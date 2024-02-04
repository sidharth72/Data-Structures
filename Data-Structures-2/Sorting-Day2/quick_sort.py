
def quick_sort(arr, low, high):
    if low <= high:
        pivot_index = partition(arr, low, high)

        quick_sort(arr, pivot_index+1, high)
        quick_sort(arr, low, pivot_index - 1)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


arr = [3, 5, 1, 8, 2, 3, 4]

quick_sort(arr, 0, len(arr) - 1)

print(arr)