class Queue:
    def __init__(self,max):
        self.items = []
        self.max=max

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        if self.size() < self.max:
            self.items.insert(0,item)
        else:
            print("Queue Overlflowed")    

    def dequeue(self):
        if self.size() != 0:
            return self.items.pop()
        else:
            print("Underflowed")
    def size(self):
        return len(self.items)
    def display(self):
        print(self.items)
    def front(self):
        return self.items[-1]
    def rear (self):
        return self.items[0]
    
q=Queue(3)
q.enqueue("dhanyata")
q.display()
q.enqueue("sam")
q.display()
q.enqueue("ron")
print(q.front())
print(q.rear())
q.display()
q.enqueue("fred")
q.display()
q.dequeue()
q.display()
print(q.front())
print(q.rear())
q.dequeue()
q.display()
q.dequeue()
q.display()
q.dequeue()
