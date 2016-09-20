##4.1 Implement a function to check if a binary tree is balanced. For the purposes of
##this question, a balanced tree is defined to be a tree such that the heights of the
##two subtrees of any node never differ by more than one.
def height(node):
    if node==None:
        return 0
    lh=height(node.left)
    if lh==-1:
        return -1

    rh=height(node.right)
    if rh==-1:
        return -1

    hdiff=abs(lh-rh)
    if hdiff>1:
        return -1
    else:
        return max(lh, rh)

def isBalanced(treeNode):
    if height(treeNode)==-1:
        return False
    return True