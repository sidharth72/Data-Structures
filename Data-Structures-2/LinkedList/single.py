class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

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
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end = " -> ")
            current = current.next
        print(None)
    


list = LinkedList()
list.append(4)
list.append(5)
list.append(1)
list.append(9)
list.append(12)
list.append(23)
list.append(65)
list.append(934)

list.display()