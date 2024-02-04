class TwoStack:

    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.top1 = -1
        self.top2 = capacity

    def push1(self, item):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.array[self.top1] = item
        else:
            raise IndexError("Stack 1 OverFlow Error")
        
    def push2(self, item):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.array[self.top2] = item
        else:
            raise IndexError("Stack 2 Overflow Error")
        
    def pop1(self):
        if self.top1 >= 0:
            popped = self.array[self.top1]
            self.top1 -= 1
            return popped
        else:
            raise IndexError("Stack 1 Underflow")
        
    def pop2(self):
        if self.top2 < self.capacity - 1:
            popped = self.array[self.top2]
            self.top2 += 1
            return popped
        else:
            raise IndexError("Stack 2 Underflow")
        
    def peek1(self):
        if self.top1 == -1:
            raise IndexError("Stack 1 Underflow")
        else:
            return self.array[self.top1]
        
    def peek2(self):
        if self.top2 == -1:
            raise IndexError("Stack 1 Underflow")
        else:
            return self.array[self.top2]
        


tstack = TwoStack(6)
tstack.push1(32)
tstack.push2(4)
tstack.push1(72)
tstack.push2(9)
tstack.push1(2)
tstack.push2(912)

print(tstack.peek1())
print(tstack.peek2())

print(tstack.array)
