class Stack():
    def __init__(self):
        self.array=[]
        self.t=-1
        
    def pop(self):
        a=self.array.pop(self.t)
        self.t=self.t-1
        return a
    
    def push(self,x):
        self.array.append(x)
        self.t=self.t+1

    def peek(self):
        return self.array[self.t]

    def isEmpty(self):
        if self.t==-1:
            return True
        else:
            return False