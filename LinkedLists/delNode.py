##Implement an algorithm to delete a node in the middle of a singly linked list,
##given only access to that node.
#Note: works for all but the tail node
def delNode(node):
    """
    type node: Node
    retType: None
    Time: O(1)
    """
    node.data=node.next.data
    node.next=node.next.next
