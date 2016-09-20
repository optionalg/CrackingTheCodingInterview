##Write code to partition a linked list around a value x, such that all
##nodes less than x come before all nodes greater than or equal to x.
def partition(ll, x):
    """
    type ll: LinkedList
    type x: int
    retType: None
    Time: O(1)
    """
    larger=LinkedList()
    dH=Node
    dH.next=ll.head
    temp=dH
    while temp.next!=None:
        if temp.next.data<x:
            temp=temp.next
        else:
            toDel=temp.next
            temp.next=toDel.next
            toDel.next=None
            larger.insert(toDel.data)
    temp.next=larger.head.next
    return ll