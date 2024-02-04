from linked_list import LinkedList, Node

# Delete Duplicates from a sorted linked list
list = LinkedList()

def del_dup_sorted(linked_list):
    if linked_list.is_empty():
        return
    current = linked_list.head
    while current.next:
        if current.next.data == current.data:
            current.next = current.next.next
        else:
            current = current.next


list.append(2)
list.append(3)
list.append(4)
list.append(4)
list.append(7)


del_dup_sorted(list)

list.display()