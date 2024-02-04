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
        else:
            removed = self.front.data
            self.front = self.front.next
            return removed
        
    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.front.data
        

class Stack:

    def __init__(self):
        self.queue = Queue()

    def push(self, item):
        self.queue.enqueue(item)

    def pop(self):
        if self.queue.is_empty():
            return None
        # Move all elements except the last one to the front
        while self.queue.front.next:
            self.queue.enqueue(self.queue.dequeue())
        # Retrieve and remove the last element (original front)
        removed = self.queue.dequeue()
        return removed

    

stack = Stack()
stack.push(3)
stack.push(2)
stack.push(1)

print(stack.pop())
        