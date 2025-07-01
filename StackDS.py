class Stack:
    def __init__(self,max):
        self.max=max
        self.stack=[]

    def push(self,added):
        if self.size()< self.max:
            self.stack.append(added)
        else:
            print("Stack is full... :(") 
    def pop(self):
        if not self.is_empty():
            return self.stack.pop(-1)
        else:
            print("stack is empty..:(") 
    def show(self):
        print(self.stack)
    def is_empty (self):
        if len(self.stack)==0:
           return True
        else:
           return False
    def size(self):
        return len(self.stack)
    def top(self):
        return self.stack[-1]
       


my_stack=Stack(3)
my_stack.show()
my_stack.push(4)
my_stack.show()
my_stack.push(3)
my_stack.show()
print(my_stack.top())
my_stack.push(2)
my_stack.show()
my_stack.push(1)
my_stack.show()
for i in range(4):
    i=my_stack.pop()
    print(i)
    my_stack.show()


 
        
