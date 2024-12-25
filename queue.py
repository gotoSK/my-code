SIZE = 5

class Queue:
    def __init__(self):
        self.queue = [0] * SIZE
        self.front = 0
        self.rare = -1
    
    def enqueue(self, item):
        if self.is_full():
            print("Overflow")
        else:
            self.rare += 1
            self.queue[self.rare] = item

    def dequeue(self):
        if self.is_empty():
            print("Underflow!")
        else:
            self.queue[self.front] = 0
            self.front += 1
    
    def is_full(self):
        return self.rare == SIZE-1
    
    def is_empty(self):
        return self.rare < self.front
    
    def display(self):
        print("----")
        # traversing queue
        i = self.front
        while True:
            if i <= self.rare:
                print(self.queue[i])
                i += 1
            else:
                break
        print("----")


    
if __name__ == "__main__":
    q = Queue()
    q.display()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.display()
    q.dequeue()
    q.dequeue()
    q.display()
