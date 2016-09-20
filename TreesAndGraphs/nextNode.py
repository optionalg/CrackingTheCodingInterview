##4.6 Write an algorithm to find the 'next'node (i.e., in-order successor) of a given node
##in a binary search tree. You may assume that each node has a link to its parent.
def next_node(node):
    if node==None:
        return
    if node.right:
        return fetchLeftMost(node.right)
    cur=node
    par=cur.parent
    while par!=None and par.right==cur:
        cur=par
        par=par.parent
    return par

def fetchLeftMost(node):
    if node==None:
        return
    while node.left:
        node=node.left
    return node