class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end = " -> ")
            current = current.next
        print(None)

    def delete(self, pos):
        current = self.head
        if pos == 0:
            self.head = current.next
            return
        for _ in range(pos - 1):
            if current.next is None:
                print("Out of bound error")
                return

            current = current.next
        current.next = current.next.next


list = LinkedList()
list.insert(6)
list.insert(8)
list.insert(1)
list.insert(3)
list.insert(5)
list.insert(18)

list.delete(1)

list.display()

