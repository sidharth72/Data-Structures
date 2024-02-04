class QueueStack:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            if not self.stack1:
                return None
            
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        return self.stack2.pop()
    


queue = QueueStack()
queue.enqueue(4)
queue.enqueue(2)
queue.enqueue(1)
queue.enqueue(8)
queue.enqueue(9)

print(queue.dequeue())
print(queue.dequeue())