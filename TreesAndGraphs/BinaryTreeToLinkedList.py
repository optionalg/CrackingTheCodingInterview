##4.4 Given a binary tree, design an algorithm which creates a linked list of all the
##nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked
##lists).
def BTtoLL(node):
    if node==None:
        return
    LL=[]
    current=LinkedList(node)
    while current.size()!=0:
        LL.append(current)
        parent=current
        temp=parent
        current=LinkedList()
        while temp:
            if temp.left:
                current.insert(temp.left)
            if temp.right:
                current.insert(temp.right)
            temp=temp.next
            toDel=current
            current=current.next
            toDel.next=None
    return LL