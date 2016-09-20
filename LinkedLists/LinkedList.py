class Node ():
    def __init__(self,data=None):
        self.data=data
        self.next=None

class LinkedList():
    def __init__(self,data=None):
        self.head=Node(data)
        self.size=1
        
    def insert(self,data=None):
        temp=Node(data)
        temp.next=self.head.next
        self.head.next=temp
        self.size+=1
        
    def printList(self):
        print "Contents of linked list"
        temp=self.head
        while temp!=None:
            print temp.data
            temp=temp.next