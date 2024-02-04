from linked_list import Node, LinkedList

def delete(linked_list, pos):
    current = linked_list.head

    if pos == 0:
        linked_list.head = current.next
        return
    
    for _ in range(pos - 1):
        if current.next is None:
            print("Out of bound error")
            return
        current = current.next
    current.next = current.next.next


list = LinkedList()

for i in range(6):
    list.append(i)

delete(list, 3)
list.display()