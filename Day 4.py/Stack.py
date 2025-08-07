#Stack implementation in Python
class Stack:
    def __init__(self,capacity):
        self.stack = [0] * capacity
        self.top = -1
        self.capacity = capacity

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity -1
    
    def push(self,element):
        if self.top == self.capacity-1:
            print("Stack is overflow")
            return
        self.top += 1
        self.stack[self.top] = element

    def pop(self):
        if self.is_empty():
            print("Stack is underflow")
            return None
        element = self.stack[self.top]
        self.top -= 1
        return element
    
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.stack[self.top]
    
    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        for i in range(self.top,-1,-1):
            print(self.stack[i],end=' ')
        print()

#Example
s = Stack(5)
s.push(10)
s.push(20)
s.push(30)
s.display()
print(s.pop())
print(s.peek())
s.display()

















