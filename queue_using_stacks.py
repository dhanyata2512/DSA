import StackDS
class Queue:
    def __init__(self,max):
        self.queue=StackDS.Stack(max)
        self.temporary=StackDS.Stack(max)
        self.max=max
    def enqueue(self,value):
        if self.queue.size() < self.max:
            self.queue.push(value)
        else:
            print('no space...')    
    def dequeue(self):
        while self.queue.size() != 1:
            self.temporary.push(self.queue.pop())
        last=self.queue.pop()
        while self.temporary.size() !=  0:
            self.queue.push(self.temporary.pop())
        return last
    def display(self):
        print(self.queue.show())

q=Queue(4)
q.enqueue(14)
q.display()
q.enqueue(13)
q.display()
q.enqueue(34)
q.display()
q.enqueue(33)
q.display()
q.dequeue()
q.display()
q.dequeue()
q.display()                    
                

        