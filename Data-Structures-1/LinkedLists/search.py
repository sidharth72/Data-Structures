from linked_list import LinkedList, Node

def search(linked_list, element):
    count = 0
    current = linked_list.head
    while current:
        if current.data == element:
            count+=1
        current = current.next
    
    return count

list = LinkedList()
list.append(3)
list.append(2)
list.append(8)
list.append(4)
list.append(9)
index = search(list, 4)
if index:
    print(f"Found")
else:
    print("Not Found")