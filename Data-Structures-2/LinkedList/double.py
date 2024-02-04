class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
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
        print(None)

    def display_backward(self):
        current = self.head
        while current.next:
            current = current.next

        while current:
            print(current.data, end = " <-> ")
            current = current.prev
        print(None)


    def insert(self, data, pos):
        current = self.head
        new_node = Node(data)

        for _ in range(pos - 1):
            if current.next is None:
                return "Out of bound error"
            current = current.next

        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node

    def delete(self, pos):
        current = self.head
        for _ in range(pos - 1):
            if current.next is None:
                return "Out of bound Error"
            current = current.next

        if current.next:
            current.next = current.next.next
            if current.next:
                current.next.prev = current
            else:
                return "Out of bound error"
            

    

dlist = DoublyLinkedList()
dlist.append(23)
dlist.append(25)
dlist.append(632)
dlist.append(93)
dlist.append(12)
dlist.append(9)
dlist.insert(9023, 3)

dlist.delete(2)

dlist.display_backward()
dlist.display_forward()