class Stack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, item):
        self.stack.append(item)
        if not self.minstack or item <= self.minstack[-1]:
            self.minstack.append(item)

    def pop(self):
        if not self.stack:
            return None
        popped = self.stack.pop()
        if popped == self.minstack[-1]:
            self.minstack.pop()
        else:
            raise IndexError("Stack Underflow")
        
    def get_min(self):
        if not self.stack:
            return None
        return self.minstack[-1]
    

stack = Stack()
stack.push(10)
stack.push(6)
stack.push(9)
stack.push(2)
stack.push(213)

print(stack.get_min())