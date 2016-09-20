##4.2 Given a directed graph, design an algorithm to find out whether there is a route
##between two nodes.
def yepRoute(node1,node2):
    """
    Idea is to do a BFS from node1, if we run into node2, return True. False otherwise
    Structure of directed graph:
    - each node has attributes -(1) visited (bool) and (2)list, edges, containing other nodes that
    the node is connected to
    - all nodes contained in array, G
    - NEEDS SOME TWEAKING. ASSUMING GRAPH IS IN FORM OF ADJACENCY LIST BUT CODE READS LIKE GRAPH IS
    A N-NARY TREE OR SOMETHING!
    """
    for node in G:
        node.visited=False
    Q=[node1]
    while len(Q)!=0:
        n=Q.pop()
        n.visited=True
        for node in n.edges:
            if node==node2:
                return True
            else:
                if node.visited==False:      #gets added to Q only if it hasn't been visited.
                    Q.insert(0,node)
    return False