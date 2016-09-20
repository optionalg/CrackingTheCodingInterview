class Node():
    def __init__(self, data=None, next_node=None):
        self.data=data
        self.next_node=next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node
    '''
    def set_next(self, new_next):
        self.next_node=new_next
    '''

#Implementation of a linked list

class LinkedList():
    def __init__(self, x=None):
        self.head=Node(x)

    #Inserts next to head
    def insert(self, data):
        temp=Node(data, self.head.next_node)
        self.head.next_node=temp

    def insertToLast(self, data):
        temp=Node(data, None)
        temp2=self.head
        while temp2.next_node!=None:
            temp2=temp2.next_node
        temp2.next_node=temp
        
    def size(self):
        count=0
        temp=self.head
        while temp:
            count=count+1
            temp=temp.next_node
        return count

    def printList(self):
        temp=self.head
        print "Contents of linked list"
        while temp:
            data=temp.get_data()
            print data
            temp=temp.get_next()

    #head=1
    def delete(self, node_number):
        size=self.size()
        if node_number>size:
            return
        if node_number==1:
            temp=self.head
            self.head=self.head.next_node
            temp.next_node=None
        else:
            count=0
            temp=self.head
            while count<(node_number-2):
                temp=temp.next_node
                count=count+1
            temp.next_node=temp.next_node.next_node
   