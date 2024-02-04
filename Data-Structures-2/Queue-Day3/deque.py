class Deque:

    def __init__(self):
        self.queue = []

    def enqueue_front(self, item):
        self.queue.insert(0, item)

    def enqueue_back(self, item):
        self.queue.append(item)

    def pop_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            popped = self.queue.pop(0)
            return popped
        
    def pop_back(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            popped = self.queue.pop()
            return popped
        
        