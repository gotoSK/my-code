class Node:
    def __init__(self, data):
        self.data = data
        self. next = None

class QueueLL:
    def __init__(self):
        self.front = None
        self.rare = None

    def enqueue(self, data):
        node = Node(data)
        if self.underflow(): # when empty queue
            self.front = self.rare = node
        else:
            self.rare.next = node
            self.rare = node

    def dequeue(self):
        if self.underflow():
            print("Queue is empty!")
            return
        self.front = self.front.next
        if not self.front:
            self.rare = None
            
    def underflow(self):
        return not self.front
    
    def display(self):
        if self.underflow():
            print("Queue is qmpty!")
            return
        node = self.front
        print("front", end="")
        while node:
            print(" -> ", node.data, end="")
            node = node.next
        print(" <- rare")
    
if __name__ == "__main__":
    queue = QueueLL()

    queue.display()
    queue.dequeue()
    
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.display()

    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.display()