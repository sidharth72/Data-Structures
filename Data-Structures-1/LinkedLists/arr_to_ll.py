from linked_list import LinkedList, Node
# Convert array to linked list
arr = [4, 5, 6, 2, 7]

list = LinkedList()

for i in range(len(arr)):
    list.append(arr[i])


print(arr)
list.display()