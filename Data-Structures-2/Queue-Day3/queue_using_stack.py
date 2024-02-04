class Queue:

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
    

queue = Queue()
queue.enqueue(5)
queue.enqueue(3)
queue.enqueue(9)
queue.enqueue(1)
queue.enqueue(9)
queue.enqueue(12)
queue.enqueue(19)

print(queue.dequeue())