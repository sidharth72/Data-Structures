class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top is None:
            popped_item = self.top.data
            self.top = self.top.next
            return popped_item
        else:
            raise IndexError("Pop from an empty stack is not possible")
        
    def peek(self):
        if not self.top is None:
            return self.top.data
        else:
            raise IndexError("Stack is empty")
        
    def size(self):
        current = self.top
        count = 0

        while current:
            count += 1
            current = current.next
        return count
            

stack = Stack()
stack.push(4)
stack.push(9)
stack.push(11)
stack.push(29)
stack.push(54)
stack.push(323)
stack.push(123)

del_item = stack.pop()
print(del_item)
print(stack.peek())