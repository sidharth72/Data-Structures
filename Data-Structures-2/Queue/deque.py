# Implementation of double ended Queue
# Insertion and deletion can be happen in both ways
class Deque:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")
    
    def remove_rear(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Queue is empty")
        
    def size(self):
        return len(self.items)
    

deque = Deque()
deque.add_front(5)
deque.add_front(8)
deque.add_front(2)
deque.add_front(1)
deque.add_front(9)

print(deque.items)