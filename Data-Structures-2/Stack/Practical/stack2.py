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
            popped = self.array[self.top]
            self.top -= 1
            return popped
        else:
            raise IndexError("Stack Underflow")
        
    def peek(self):
        if self.top == -1:
            raise IndexError("Stack Underflow")
        else:
            return self.array[self.top]
        

stack = Stack(6)
stack.push(4)
stack.push(9)
stack.push(12)
stack.push(9)

stack.pop()

print(stack.peek())
