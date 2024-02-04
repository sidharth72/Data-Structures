class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class QueueList:

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
            raise IndexError("Queue contains nothing")
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            removed = self.front.data
            self.front = self.front.next
            return removed
        
    def peek(self):
        if self.is_empty():
            raise IndexError("Queue contains nothing to peek")
        else:
            return self.front.data
        

queue = QueueList()
queue.enqueue(4)
queue.enqueue(2)
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(8)

queue.dequeue()

print(queue.peek())