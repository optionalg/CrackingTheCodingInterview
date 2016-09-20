#Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore,
#in real life, we would likely start a new stack when the previous stack exceeds some threshold.
#Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of
#several stacks and should create a new stack once the previous one exceeds capacity.
#SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack (that is,
#popO should return the same values as it would if there were just a single stack).
#FOLLOW UP
#Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.
class SetofStacksArray():
    def __init__(self, threshold):
        self.stack=[]
        self.stack.append(Stack())
        self.threshold=threshold
        self.stackcounter=0
        
    def push(self, x):
        if len(self.stack[self.stackcounter].array)<self.threshold:
            self.stack[self.stackcounter].push(x)
            return
        if len(self.stack[self.stackcounter].array)==self.threshold:
            self.stack.append(Stack())
            self.stackcounter=self.stackcounter+1
            self.stack[self.stackcounter].push(x)
            return

    def pop(self):
        self.stack[self.stackcounter].pop()
        if len(self.stack[self.stackcounter].array)==0:
            del self.stack[self.stackcounter]
            self.stackcounter=self.stackcounter-1
            
    def popAt(self, x):
        if x>self.stackcounter:
            raise IndexError
        self.stack[x].pop()
    #havent moved from successing stacks to fill the gap