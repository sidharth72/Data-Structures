class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListQueue:

    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front == self.rear == None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("List is empty")
        removed = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
        return removed
    
    def front_data(self):
        if self.is_empty():
            return None
        return self.front.data
    
    def size(self):
        count = 0
        current = self.front
        while current:
            count+=1
            current = current.next
        return count
    
lqueue = ListQueue()
lqueue.enqueue(4)
lqueue.enqueue(5)  
lqueue.enqueue(9)
lqueue.enqueue(12)
lqueue.enqueue(54)
lqueue.enqueue(8)

lqueue.dequeue()
lqueue.dequeue()
lqueue.dequeue()

print(lqueue.front_data())
