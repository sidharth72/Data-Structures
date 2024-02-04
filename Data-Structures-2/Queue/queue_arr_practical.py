class Queue:

    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def is_empty(self):
        return self.front == self.rear == -1

    def enqueue(self, data):
        if self.is_full():
            raise IndexError("Queue is full")
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        popped = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return popped
    

    def show_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.queue[self.front]
        

q = Queue(6)

q.enqueue(8)
q.enqueue(33)
q.enqueue(2)
q.enqueue(9)
q.enqueue(6)
q.enqueue(1)

q.dequeue()

print(q.show_front())