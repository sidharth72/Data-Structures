class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == self.rear == -1
    
    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("Queue is already full")
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is already full")
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            removed = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
            return removed
        
    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.queue[self.front]
        

    
queue = Queue(6)
queue.enqueue(5)
queue.enqueue(8)
queue.enqueue(3)
queue.enqueue(11)
queue.enqueue(9)
queue.enqueue(7)

queue.dequeue()

print(queue.peek())


