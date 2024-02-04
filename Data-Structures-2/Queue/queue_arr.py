class Queue:

    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1
        
    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Oueue is Full")
        if self.is_empty():
            # Set to the first index of the array if the Queue is empty
            self.front = self.rear = 0
        else:
            # Increment the rear to enqueue
            self.rear = (self.rear + 1) % self.capacity
        # Insert the element
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        # Storing the removing item from the array
        removed_item = self.queue[self.front]

        # Incase if there is only one value
        # Then the front and rear are equal
        # So we need to make it -1 to delete the element
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            # Icrementing the front-one my one for removing elements
            self.front = (self.front + 1) % self.capacity
        return removed_item
    
    def front_value(self):
        if self.is_empty():
            return None
        return self.queue[self.front]
    
    def is_empty(self):
        return self.front == self.rear == -1
    
    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def size(self):
        if self.is_empty():
            return 0
        return ((self.rear - self.front + self.capacity) % self.capacity) + 1

queue = Queue(6)
queue.enqueue(5)
queue.enqueue(9)
queue.enqueue(12)
queue.enqueue(3)


en_item = queue.dequeue()
print(queue.front_value())
print(queue.size())



