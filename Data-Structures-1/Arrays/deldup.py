# Delete Duplicates form the array

arr = [3, 7, 1, 8, 3, 8, 9, 2]
unique = []

for i in range(len(arr)):
    is_duplicate = False
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            is_duplicate = True
            break

    if not is_duplicate:
        unique.append(arr[i])

print(arr)
print(unique)