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
            return None
        removed = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
        return removed
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.front.data
        
queue = QueueList()
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(1)
queue.enqueue(8)
queue.enqueue(9)

queue.dequeue()

print(queue.peek())
