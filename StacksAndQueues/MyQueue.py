#Implement a MyQueue class which implements a queue using two stacks.
#reference: http://www.geeksforgeeks.org/queue-using-stacks/
#Used Method 1. Stack 2 basically temp buffer
class MyQueue():
    def __init__(self):
        self.stack1=Stack()
        self.stack2=Stack()

    def enQ(self,x):
        #pop everything one-by-one from stack1 and push to stack2
        while not self.stack1.isEmpty():
            a=self.stack1.pop()
            self.stack2.push(a)
        #push x to stack 1
        self.stack1.push(x)
        #pop everything one-by-one from stack2 and push to stack1
        while not self.stack2.isEmpty():
            a=self.stack2.pop()
            self.stack1.push(a)

    def deQ(self):
        self.stack1.pop()