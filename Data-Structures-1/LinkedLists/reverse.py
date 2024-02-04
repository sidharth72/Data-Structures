from linked_list import LinkedList, Node


def reverse_list(linked_list):
    current = linked_list.head
    prev = None

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    linked_list.head = prev

list = LinkedList()
list.append(3)
list.append(7)
list.append(4)
list.append(2)
list.append(1)
list.append(99)

list.display()

reverse_list(list)

list.display()

