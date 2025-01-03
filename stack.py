# size of the stack
SIZE = 5

class Stack:
    def __init__(self):
        self.stack = [None] * 5
        self.top = -1
    
    def push(self, item):
        if self.is_full():
            print("Overflow!")
        else:
            self.top += 1
            self.stack[self.top] = item
    
    def pop(self):
        if self.is_empty():
            print("Underflow!")
        else:
            self.stack[self.top] = None
            self.top -= 1

    def is_full(self):
        return self.top >= SIZE-1

    def is_empty(self):
        return self.top < 1
    
    def display(self):
        print("----")
        # itterating from top of the stack
        for i in range(self.top, -1, -1):
            print(self.stack[i])
        print("----")
    
if __name__ == "__main__":
    s = Stack()
    s.display()
    s.pop()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    s.display()
    s.pop()
    s.display()