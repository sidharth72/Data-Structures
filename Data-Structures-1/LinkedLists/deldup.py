from linked_list import Node, LinkedList
# Delete Duplicates from a Linked List
def delete_dup(linked_list):
    if linked_list.is_empty():
        return
    current = linked_list.head
    while current:
        runner = current
        while runner.next:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
        
list = LinkedList()

list.append(4)
list.append(4)
list.append(7)
list.append(2)
list.append(4)
list.append(5)
list.append(4)
list.append(5)
list.append(4)
list.append(10)

delete_dup(list)

list.display()