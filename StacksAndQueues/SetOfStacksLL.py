#Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore,
#in real life, we would likely start a new stack when the previous stack exceeds some threshold.
#Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of
#several stacks and should create a new stack once the previous one exceeds capacity.
#SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack (that is,
#popO should return the same values as it would if there were just a single stack).
#FOLLOW UP
#Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.        
#(a linked list where each node is a stack)

import LLforStack as LL

class SetOfStacksLL():
    def __init__(self, threshold):
        self.list=LL.LinkedList(Stack())
        #self.list.data=Stack()
        self.threshold=threshold
        self.temp=self.list.head
        
    def push(self,x):
        if len(self.temp.data.array)<self.threshold:
            self.temp.data.push(x)
            return
        if len(self.temp.data.array)==self.threshold:
            self.list.insertToLast(Stack())
            self.temp=self.temp.next_node
            self.temp.data.push(x)
            return

    def pop(self):
        self.temp.data.pop()
        if len(self.temp.data.array)==0:
            prev=self.list.head
            while prev.next_node!=self.temp:
                prev=prev.next_node
            self.temp=prev
           
    def popAt(self, x):
        if x>self.list.size():
            return
        temp2=self.list.head
        i=0
        while i<x:
            temp2=temp2.next_node
            i=i+1
        temp2.data.pop()