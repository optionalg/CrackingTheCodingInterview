
##Implement an algorithm to find the kth to last element of a singly linked list.
##Assumption: data values in linkedlist are of type int
def kthToLast(ll,k):
    """
    type ll: LinkedList
    type k: int
    retType: int
    Time: O(n^2)
    Space: O(1)
    """
    dH=Node()
    dH.next=ll.head
    fast=dH
    slow=dH
    while k!=0:
        fast=fast.next
        k-=1
    while fast.next!=None:
        fast=fast.next
        slow=slow.next
    return slow.data