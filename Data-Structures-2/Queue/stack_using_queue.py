# Creating stack using Queue
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class Queue:

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
            raise IndexError("Queue is empty")
        removed = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
        return removed


class StackUsingQueue:

    def __init__(self):
        self.queue = Queue()

    def push(self, item):
        self.queue.enqueue(item)

    def pop(self):
        if self.queue.is_empty():
            raise None
        while self.queue.front:
            self.queue.enqueue(self.queue.dequeue())
        return self.queue.dequeue()
    

stack = StackUsingQueue()

stack.push(3)
stack.push(2)
stack.push(11)

print(stack.pop())


            
