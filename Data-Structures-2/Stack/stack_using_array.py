class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items is None:
            return self.items.pop()
        else:
            raise IndexError('Pop from an empty stack')
        
    def peek(self):
        if not self.items is None:
            return self.items[-1]
        else:
            raise IndexError('Peek from an empty Stack')
        
    def size(self):
        return len(self.items)
    

stack = Stack()
stack.push(3)
stack.push(2)
stack.push(6)
stack.push(8)
stack.push(1)
stack.push(9)
stack.push(12)
stack.push(0)

# popped_value = stack.pop()
# print(popped_value)

print(stack.peek())
