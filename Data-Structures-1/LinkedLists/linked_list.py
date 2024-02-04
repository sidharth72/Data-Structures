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
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def is_empty(self):
        return self.head is None
        

    def display(self):
        current = self.head
        while current:
            print(current.data, end = " -> ")
            current = current.next
        print()


# list = LinkedList()
# list.append(5)
# list.append(3)
# list.display()