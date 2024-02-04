from linked_list import LinkedList, Node

def delete_value(linked_list, value):
    current = linked_list.head
    if current and current.data == value:
        linked_list.head = current.next
        return
    prev = None
    while current and current.data != value:
        prev = current
        current = current.next
    if current is None:
        print("Value not found...")
        return
    prev.next = current.next

list = LinkedList()
list.append(2)
list.append(3)
list.append(4)
list.append(4)
list.append(7)
delete_value(list, 7)
list.display()