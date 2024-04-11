class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items is None:
            popitem = self.items[-1]
            self.items.pop()
            return popitem
        else:
            raise IndexError("Stack is empty")
        
    def peek(self):
        if not self.items is None:
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")
        

string = "sidharth"
stack = Stack()

for c in string:
    stack.push(c)

reversed_string = ""
for i in range(len(string)):
    popitem = stack.pop()
    reversed_string+=popitem

print(reversed_string)

    

