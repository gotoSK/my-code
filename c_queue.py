SIZE = 3

class CQueue:
    def __init__(self):
        self.queue = [None] * 5
        self.front = -1
        self.rare = -1
    
    def enqueue(self, item):
        if self.is_full():
            print("Overflow!")
        else:
            if self.front == -1:
                self.front += 1
            self.rare = (self.rare + 1) % SIZE
            self.queue[self.rare] = item

    def dequeue(self):
        if self.is_empty():
            print("Underflow!")
        else:
            if self.front == self.rare:
                self.queue[self.front] = None
                self.front = -1
                self.rare =-1
            else:
                self.queue[self.front] = None
                self.front = (self.front + 1) % SIZE
    
    def is_full(self):
        return (self.rare + 1) % SIZE == self.front

    def is_empty(self):
        return self.front == -1
    
    def __str__(self):
        display = []
        i = self.front
        while i != self.rare:
            display.append(self.queue[i])
            i = (i+1) % SIZE
        display.append(self.queue[i])
        return str(display)

if __name__ == "__main__":
    cq = CQueue()
    print(cq)
    cq.enqueue(1)
    cq.enqueue(2)
    print(cq)
    cq.dequeue()
    print(cq)
    cq.enqueue(3)
    cq.enqueue(4)
    print(cq)
    cq.enqueue(5)
    cq.dequeue()
    cq.dequeue()
    cq.dequeue()
    print(cq)