##4.7 Design an algorithm and write code to find the first common ancestor of two
##nodes in a binary tree. Avoid storing additional nodes in a data structure.
##NOTE: This is not necessarily a binary search tree.
def covers(root, node):
    if root==None:
        return False
    if root==Node:
        return True
    return covers(root.left, node) or covers(root.right, node)

def commonAncestorHelper(node, p, q):
    if node==None:
        return
    if node==left or node==right:
        return node
    pOnLeft=covers(node, left)
    qOnLeft=covers(node, left)
    if pOnLeft!=qOnLeft:
        return node
    if pOnLeft:
        return commonAncestorHelper(node.left, p, q)
    else:
        return commonAncestorHelper(node.right, p, q)

def commonAncestor(root, p, q):
    if covers(root, p)==False or covers(root, q)==False:
        return None
    return commonAncestorHelper(root, p, q)