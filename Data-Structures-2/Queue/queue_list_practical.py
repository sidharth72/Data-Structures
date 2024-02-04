class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueList:

    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front == self.rear == None

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        popitem = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
        return popitem
    
    def front_value(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.front.data
    

lqueue = QueueList()
lqueue.push(5)
lqueue.push(7)
lqueue.push(9)
lqueue.push(12)
lqueue.push(72)
lqueue.push(4)

print(lqueue.front_value())
    


