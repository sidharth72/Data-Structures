def heapify(arr, n, i):
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    largest = i

    if left_child < n and arr[largest] < arr[left_child]:
        largest = left_child

    if right_child < n and arr[largest] < arr[right_child]:
        largest = right_child

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

arr = [8, 9, 2, 6, 7, 1, 2]
heap_sort(arr)
print(arr)