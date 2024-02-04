class Queue:

    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == self.rear == None
    
    def is_full(self):
        return (self.rear + 1) % self.capacity

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("Queue is full")
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity

        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        if self.front == self.rear:
            self.front = self.rear = 0
        else:
            self.front = (self.front + 1) % self.capacity

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.queue[self.front]
        

