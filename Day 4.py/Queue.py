#Queue implementation in Python
class Queue:
    def __init__(self, capacity):
        self.queue = [0] * capacity
        self.front = 0
        self.rear = -1
        self.capacity = capacity
        

    def is_empty(self):
        return self.front > self.rear

    def is_full(self):
        return self.rear == self.capacity - 1

    def enqueue(self, element):
        if self.is_full():
            print("Queue is overflow")
            return
        self.rear += 1
        self.queue[self.rear] = element

    def dequeue(self):
        if self.is_empty():
            print("Queue is underflow")
            return None
        element = self.queue[self.front]
        self.front += 1
        return element

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        for i in range(self.front, self.rear + 1):
            print(self.queue[i], end=' ')
        print()

# Example usage
q = Queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
print(q.dequeue())
print(q.peek())
q.display()
