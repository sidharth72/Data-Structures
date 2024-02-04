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
            new_node.next = self.rear
            self.rear = new_node
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("The Queue is already empty")
        removed = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
        return removed

    def peek(self):
        if self.is_empty():
            raise IndexError("The Queue is already empty")
        else:
            return self.front.data
    

q = QueueList()
q.enqueue(4)
q.enqueue(5)
q.enqueue(8)
q.enqueue(9)
q.enqueue(1)
q.enqueue(10)

print(q.peek())