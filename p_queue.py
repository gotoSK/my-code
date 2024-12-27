import math

SIZE = 5

class PQueue:
    def __init__(self):
        self.queue = [] # [value, priority]

    def enqueue(self, item, priority):
        self.queue.append([item, priority])

    def dequeue(self):
        if self.is_empty():
            print("Priority Queue empty!")
        else:
            ind = self.peek()
            del self.queue[ind]

    def is_empty(self):
        return len(self.queue) == 0
    
    def peek(self):
        hi_pri = - math.inf
        ind = None
        for idx, i in enumerate(self.queue):
            if i[1] > hi_pri:
                hi_pri = i[1]
                ind = idx
        return ind
    
    def __str__(self):
        return str(self.queue)
    
if __name__ == "__main__":
    pp = PQueue();
    print(pp)
    pp.dequeue()
    pp.enqueue(1, 4)
    pp.enqueue(2, 1)
    pp.enqueue(3, 3)
    pp.enqueue(4, 2)
    print(pp)
    pp.dequeue()
    print(pp)