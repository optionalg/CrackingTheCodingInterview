#Write a program to sort a stack in ascending order (with biggest items on top). You may use at most one
#additional stack to hold items, but you may not copy the elements into any other data structure
#(such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.
def sort(self):
    for i in range(0, len(self.array)):
        small=self.array[i]
        minIndex=i
        for j in range(i+1, len(self.array)):
            if small>self.array[j]:
                small=self.array[j]
                minIndex=j
        temp=self.array[i]
        self.array[i]=self.array[minIndex]
        self.array[minIndex]=temp