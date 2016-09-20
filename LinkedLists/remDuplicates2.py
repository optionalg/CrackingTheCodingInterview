
##FOLLOW UP
##COME BACK TO THIS
##How would you solve this problem if a temporary buffer is not allowed?
def remDuplicates2(ll):
    """
    type ll: LinkedList
    retType: LinkedList
    Time: O(n^2)
    Space: O(1)
    """
    temp1=ll.head
    while temp1.next!=None:
        check=temp1.data
        temp2=temp1.next
        if temp2==None:
            break
        while temp2.next!=None:
            if check==temp2.data:
                temp1.next=temp2.next
                temp2.next=None
                temp2=temp1.next
            else:
                temp2=temp2.next
        temp1=temp1.next
    return ll
