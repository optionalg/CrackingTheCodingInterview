class Queue():
    def __init__(self):
        self.array=[]
        
    def enQ(self,x):
        self.array.append(x)

    def deQ(self):
        a=self.array[0]
        self.array.pop(0)
        return a

    def peek(self):
        return self.array[0]