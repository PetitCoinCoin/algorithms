import time
from networkx.utils.union_find import UnionFind
from graph import *


def kclustering(k: int, g: Graph):
    # Sort graph
    g.graph = sorted(g.graph,key=lambda item: item[2])

    # Init
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
        u,v,w =  g.graph[idx]
        idx += 1
        x = g.find(parent, u) 
        y = g.find(parent, v) 

        # If edge doesn't create a cycle
        if x != y: 
            g.union(parent, rank, x, y)
            result = u, v, w
    return result[2]

def hamming_clustering(nodes: list, n_nodes:int, n_bits: int):
    # Init
    nodes_int = [int(n, 2) for n in nodes]
    nodes_map = dict()
    for i in range(n_nodes):
        try:
            nodes_map[nodes_int[i]].append(i)
        except KeyError:
            nodes_map[nodes_int[i]] = [i]
    uf = UnionFind(range(n_nodes))

    # Bit masks
    dist1 = [1 << i for i in range(n_bits)]
    dist2 = list()
    for i in range(n_bits):
        for j in range(i, n_bits):
            dist2.append(2**i + 2**j)
    bit_masks = list(set(dist1 + dist2))

    # Union if identical vertices
    for eq_list in nodes_map.values():
        if len(eq_list) > 1:
            for item in eq_list[1:]:
                uf.union(eq_list[0], item)

    # Calculation
    for k in nodes_map.keys():
        for d in bit_masks:
            try:
                uf.union(nodes_map[k][0], nodes_map[k ^ d][0])
            except KeyError:
                pass
    return len(list(map(sorted, uf.to_sets())))


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
    n_nodes = int(data_big[0].split(' ')[0])
    n_bits = int(data_big[0][:-1].split(' ')[1])
    data_big = [x.replace(' ', '') for x in data_big[1:]]

    # Problem 2
    start_time = time.time()
    print('Result for 2nd problem:',hamming_clustering(data_big, n_nodes, n_bits))
    print("--- %s seconds ---" % (time.time() - start_time))

