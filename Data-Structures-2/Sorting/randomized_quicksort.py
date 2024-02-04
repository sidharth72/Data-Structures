import random

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr

    # Randomly choose a pivot
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    # Partition the array around the pivot
    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort the subarrays
    return randomized_quicksort(left) + equal + randomized_quicksort(right)

# Example usage:
my_list = [38, 27, 43, 3, 9, 82, 10]
print("Original List:", my_list)

# Perform Randomized Quicksort
sorted_list = randomized_quicksort(my_list)
print("Sorted List:", sorted_list)