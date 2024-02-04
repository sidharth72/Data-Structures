from linked_list import Node
from linked_list import LinkedList


def insert(linked_list, data, pos):
    new_node = Node(data)
    if pos == 0:
        new_node.next = linked_list.head
        linked_list.head = new_node
        return
    
    current = linked_list.head
    for _ in range(pos - 1):
        if current.next is None:
            print("Out of bound error")
            return
        current = current.next
    new_node.next = current.next
    current.next = new_node
