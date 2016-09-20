      
##Write code to remove duplicates from an unsorted linked list.
def remDuplicates1(ll):
    """
    type ll: LinkedList
    retType: LinkedList
    Time: O(n)
    Space: O(n)
    """
    buff=[]
    temp=ll.head
    buff.append(temp.data)
    while temp.next!=None:
        if temp.next.data in buff:
            delete=temp.next
            temp.next=delete.next
            delete.next=None
            ll.size-=1
        else:
            buff.append(temp.next.data)
            temp=temp.next
    return ll