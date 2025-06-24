class Stack:
    def __init__(self,max):
        self.max=max
        self.stack=[]

    def push(self,added):
        if len(self.stack)< self.max:
            self.stack.append(added)
        else:
            print("Stack is full... :(")   
        
