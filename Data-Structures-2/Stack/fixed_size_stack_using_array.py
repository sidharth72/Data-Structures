class Stack:

    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.top = -1

    def push(self, item):
        if self.top < self.capacity - 1:
            self.top += 1
            self.array[self.top] = item
        else:
            raise IndexError("Stack Overflow")
        
    def pop(self):
        if self.top < self.capacity - 1:
            popped = self.array[-1]
            self.top -= 1
            return popped
        else:
            raise IndexError("Stack Underflow")
        
    def peek(self):
        if not self.array is None:
            return self.array[-1]
        else:
            raise IndexError("Stack is empty")
        

stack = Stack(6)
stack.push(4)
stack.push(3)
stack.push(7)
stack.push(10)
stack.push(14)
stack.push(72)

print(stack.peek())
print(stack.array)
            
