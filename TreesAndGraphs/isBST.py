##4.5 Implement a function to check if a binary tree is a binary search tree.
import sys
def isBST(tree):
    maxi=sys.maxint
    mini=-maxi-1
    return isBST_(tree, mini, maxi)

def isBST_(node, mini, maxi):
    if node==None:
        return True
    if node.val<mini or node.val>=maxi:
        return False
    return isBST_(node.left, mini, node.val) and isBST_(node.right, node.val, maxi)
   