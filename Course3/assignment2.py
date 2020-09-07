import time
from graph import *

def kclustering(k: int, g: Graph):
    # Sort graph
    g.graph = sorted(g.graph,key=lambda item: item[2])

    # Init
    # mst = list() 
    parent = dict()
    rank = dict()

    for node in range(1, g.V+1): 
        parent[node] = node # Each node is its own parent
        rank[node] = 0

    result = 0, 0, 0
    idx = 0
    
    # Number of edges to be taken is equal to V-1 
    while len(set(parent.values())) >= k : 

        # Pick next cheapest edge
        if idx == 124750:
            print(parent)
        u,v,w =  g.graph[idx]
        idx += 1
        x = g.find(parent, u) 
        y = g.find(parent, v) 

        # If edge doesn't create a cycle
        if x != y: 
            # mst.append([u,v,w]) 
            g.union(parent, rank, x, y)
            result = u, v, w
        if len(set(parent.values()))<10:
            print(set(parent.values()))
    return result

def hamming_distance(ch1: str, ch2: str):
    return sum([a != b for a,b in zip(ch1, ch2)])

def graph_construction(nodes: list):
    for node in nodes

if __name__ == '__main__':
    # Get clean input data for 1st problem
    with open('clustering1.txt', 'r') as f:
        data = f.readlines()
    n = int(data[0])
    data = [[int(a) for a in x[:-1].split(' ')] for x in data[1:]]
    graph_data = Graph(n)
    for d in data:
        graph_data.addEdge(d[0], d[1], d[2])

    # Problem 1
    start_time = time.time()
    print('Result for 1st problem:', kclustering(4, graph_data))
    print("--- %s seconds ---" % (time.time() - start_time))

    # Get clean input data for 2nd problem
    with open('clustering_big.txt', 'r') as f:
        data_big = f.readlines()
    data_big = [x.replace(' ', '') for x in data_big[1:]]

    # Problem 1
    start_time = time.time()
    print('Result for 2nd problem:', hamming_clustering(data_big))
    print("--- %s seconds ---" % (time.time() - start_time))

