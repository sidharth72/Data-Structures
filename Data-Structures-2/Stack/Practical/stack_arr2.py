class Stack:

    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items is None:
            removed = self.items.pop()
            return removed
        else:
            raise IndexError("Index out of bound")
        
    def peek(self):
        if not self.items is None:
            return self.items[-1]
        else:
            raise IndexError("Index out of bound")


stack = Stack()
stack.push(324)
stack.push(6)
stack.push(9)
stack.push(5)

print(stack.peek())
        
