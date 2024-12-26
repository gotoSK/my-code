class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLL:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            print("Stack Underflow!")
            return
        node = self.top
        self.top = node.next
        node = None

    def display(self):
        if self.is_empty():
            print("Stack Underflow!")
            return
        node = self.top
        print()
        while node:
            print(" -> ", node.data, end="")
            node = node.next
        print("\ntop\n")

    def is_empty(self):
        return self.top is None
    
if __name__ == "__main__":
    stack = StackLL()
    stack.display()
    stack.pop()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.display()
    stack.pop()
    stack.pop()
    stack.display()