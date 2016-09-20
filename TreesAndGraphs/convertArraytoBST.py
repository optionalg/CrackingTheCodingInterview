##4.3 Given a sorted (increasing order) array with unique integer elements, write an
##algorithm to create a binary search tree with minimal height.
class TreeNode():
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None
        
def convertListToTree(nums):
    """
    nums is the sorted array
    Initially thought of using insert method of Class BinarySearchTree, but then each insert will
    go tru root and complexity will be O(NlogN)
    """
    return convertListToTree_(nums, 0, len(nums)-1)

def convertListToTree_(nums, start, end):
    if end<start:
        return
    mid=(start+end)/2
    n=TreeNode(nums[mid])
    n.left=convertListToTree_(nums,start,mid-1)
    n.right=convertListToTree_(nums,mid+1,end)
    return n