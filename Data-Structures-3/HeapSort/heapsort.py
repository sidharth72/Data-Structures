def heapify(arr, n, i):
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    largest = i
    
    if left_child < n and arr[largest] < arr[left_child]:
        largest = left_child

    if right_child < n and arr[largest] < arr[right_child]:
        largest = right_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    # First Heapifying, since the non leaf nodes just above the
    # leaf nodes are always be half the number of leaf nodes 
    # and we dont need to start from leaf nodes since they 
    # already follow the heap propert, 
    # We are giving the range in reverse from n // 2 - 1 to -1
    # In reverse order
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


    
array = [12, 11, 13, 5, 6, 7]
heap_sort(array)
print(array)
