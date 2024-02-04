class Node:

    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class Doubly:

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
        new_node = Node(data)
        current = self.head

        for _ in range(pos - 1):
            if current.next is None:
                print("Out of bound Error")
            current = current.next

        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node

    def delete(self, pos):
        current = self.head

        for i in range(pos - 1):
            if current.next is None:
                print("Out of bound")
                return
            current = current.next
        if current.next:
            current.next = current.next.next
            if current.next:
                current.next.prev = current
            else:
                print("Index Out of bounds")

        
list = Doubly()
list.insert(4)
list.insert(2)
list.insert(9)
list.insert(6)
list.insert(3)
list.insert(2)

list.display_forward()
print()
list.display_backward()