def del_odd(linked_list):
    current = linked_list.head
    prev = None

    while current:
        # If the first node data itself is odd
        if current.data % 2 == 0:
            if prev is None:
                linked_list.head = current.next
            else:
                # Where we assign the value of the previous to the current.next node
                prev.next = current.next

            # Iterating again through the list
            current = current.next
        else:
            # Else we set previous is current, and set current equals current.next
            prev = current
            current = current.next


