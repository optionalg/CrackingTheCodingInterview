##4.8 You have two very large binary trees: Tl, with millions of nodes, and T2, with
##hundreds of nodes. Create an algorithm to decide ifT2 is a subtree of Tl.
##A tree T2 is a subtree of Tl if there exists a node n in Tl such that the subtree of
##n is identical to T2. That is, if you cut off the tree at node n, the two trees would
##be identical.
def containsTree(treeNode1, treeNode2):
    if treeNode1==None:
        return False
    if treeNode2==None:
        return True
    return subTree(treeNode1, treeNode2)

def subTree(tn1, tn2):
    if tn1==None:
        return False
    if tn1.data==tn2.data:
        return match(tn1, tn2)
    else:
        return subTree(tn1.left, tn2) or subTree(tn1.right, tn2)

def match(node1, node2):
    if node1==None and node2==None:
        return True
    if node1==None or node2==None:
        return False
    if node1.data!=node2.data:
        return False
    return match(node1.left, node2.left) and match(node1.right, node2.right)
