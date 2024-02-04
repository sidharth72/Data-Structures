class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackList:

    def __init__(self):
        self.top = None


    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top is None:
            popped = self.top.data
            self.top = self.top.next
            return popped
        else:
            raise IndexError("Stack underflow")
        
    def peek(self):
        if not self.top is None:
            return self.top.data
        else:
            raise IndexError("Stack Underflow")
        


stacklist = StackList()
stacklist.push(5)
stacklist.push(7)
stacklist.push(9)
stacklist.push(12)

print(stacklist.peek())
        