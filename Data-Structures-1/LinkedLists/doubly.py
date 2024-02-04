class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next

        new_node.prev = current
        current.next = new_node

    def display_forward(self):
        current = self.head

        while current:
            print(current.data, end = " <-> ")
            current = current.next

    def display_backward(self):
        current = self.head
        while current.next:
            current = current.next

        while current:
            print(current.data, end = " <-> ")
            current = current.prev
        print("None")



def insert(linked_list, data, pos):
    new_node = Node(data)
    current = linked_list.head

    for _ in range(pos - 1):
        if current.next is None:
            print("Out of bound Error")
        current = current.next

    new_node.next = current.next
    new_node.prev = current
    if current.next:
        current.next.prev = new_node
    current.next = new_node

def delete(linked_list, pos):
    current = linked_list.head

    for _ in range(pos - 1):
        if current.next is None:
            print("Out of bound error")
            return
        current = current.next

    if current.next:
        current.next = current.next.next
        if current.next:
            current.next.prev = current
        else:
            print("Out of bound Error")


dlist = DoublyLinkedList()
dlist.append(4)
dlist.append(6)
dlist.append(7)
dlist.append(1)
dlist.append(9)

insert(dlist, 500, 1)

delete(dlist, 1)

dlist.display_forward()
print()
dlist.display_backward()



        

    