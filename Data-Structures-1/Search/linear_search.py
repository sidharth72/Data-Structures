
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
    return -1


arr = [2, 5, 9, 15, 22, 34, 59]
index = linear_search(arr, 34)

if index != -1:
    print(f"Found at: {index}")
else:
    print("Not Found")