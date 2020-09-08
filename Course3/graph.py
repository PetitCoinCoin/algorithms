# A utility function to update the chain of parenting
def update_parent(dict_parent: dict, newp: int):
    while dict_parent[newp] != newp:
        newp = dict_parent[newp]
    return newp

class Graph: 
  
    def __init__(self,vertices): 
        self.V = vertices #No. of vertices 
        self.graph = list()
   
    # function to add an edge to graph 
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w])
  
    # A utility function to find set of an element i 
    # (uses path compression technique) 
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 

    # A function that does union of two sets of x and y 
    # (uses union by rank) 
    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 
  
        # Attach smaller rank tree under root of  
        # high rank tree (Union by Rank) 
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = update_parent(parent, yroot)
            children = [node for node, upnode in parent.items() if upnode == xroot]
            for node in children:
                parent[node] = parent[xroot]
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = update_parent(parent, xroot)
            children = [node for node, upnode in parent.items() if upnode == yroot]
            for node in children:
                parent[node] = parent[yroot]
  
        # If ranks are same, then make one as root  
        # and increment its rank by one 
        else : 
            parent[yroot] = update_parent(parent, xroot)
            children = [node for node, upnode in parent.items() if upnode == yroot]
            for node in children:
                parent[node] = parent[yroot]
            rank[xroot] += 1