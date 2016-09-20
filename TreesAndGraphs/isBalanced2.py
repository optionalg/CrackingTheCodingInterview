"""
Not optimized.
Time: O(N^2)
def balanced(tree):
    if tree==None:
        return True
    lh=maxHeight(tree.left)
    rh=maxHeight(tree.right)
    if abs(lh-rh)>1:
        return False
    else:
        return balanced(tree.left) and balanced(tree.right)
    
def maxHeight(root):
    if node==None:
        return 0
    depth=1
    def maxH(root,d):
        if node==None:
            return
        if d>depth:
            depth=d
        maxH(root.left, d+1)
        maxH(root.right, d+1)
    maxH(root, 1)
    return depth
"""