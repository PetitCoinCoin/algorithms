import warnings
warnings.filterwarnings("ignore")

from collections import defaultdict 
import pandas as pd
import time
import heapq

def dijkstra_naive(graph, start=1, n=200):
    start_time = time.time()

    # Init
    processed = [start]
    distances = defaultdict(lambda : 1000000)
    distances[start] = 0

    # Main
    while len(processed) < n:
        df = graph[graph['tail'].isin(processed) & ~graph['head'].isin(processed)]
        df['dijkstra'] = df.apply(lambda row: distances[row['tail']] + row['weight'], axis=1)
        idx_min = df[df.dijkstra == df.dijkstra.min()].index

        new_vertex = df.loc[idx_min[0],'head']
        processed.append(new_vertex)
        distances[new_vertex] = df.loc[idx_min[0],'dijkstra']
    
    print("--- %s seconds ---" % (time.time() - start_time))
    return distances


def dijkstra_heap(graph, start=1, n=200):
    start_time = time.time()
    
    # Init
    distances = defaultdict(lambda : 1000000)
    distances[start] = 0

    remaining = []
    df = graph[graph['tail'] == start]
    for i in range(1, n+1):
        if i != start:
            idx = df[df['head'] == i].index
            try:
                dijkstra = df.loc[idx[0], 'weight']
                distances[df.loc[idx[0], 'head']] = dijkstra
            except IndexError:
                pass
            heapq.heappush(remaining, (distances[i], i))
        

    # Main
    while len(remaining) > 0:
        new_vertex = heapq.heappop(remaining)
        distances[new_vertex[1]] = new_vertex[0]
        # Update keys
        df = graph[graph['tail'] == new_vertex[1]]
        for idx in df.index:
            h = df.loc[idx, 'head']
            if (distances[h], h) in remaining:
                remaining.remove((distances[h], h))
                w = df.loc[idx, 'weight']
                distances[h] = min(distances[h], distances[new_vertex[1]] + w)
                heapq.heappush(remaining, (distances[h], h))

    print("--- %s seconds ---" % (time.time() - start_time))
    return distances

if __name__ == '__main__':
    
    # Get clean input data
    with open('dijkstraData.txt', 'r') as f:
        data = f.readlines()
    data = [x.split('\t')[:-1] for x in data]
    tails = list()
    heads = list()
    weights = list()
    for d in data:
        linked_vertices = [[int(a) for a in x.split(',')] for x in d[1:]]
        for v in linked_vertices:
            tails.append(int(d[0]))
            heads.append(v[0])
            weights.append(v[1])
    graph_df = pd.DataFrame({'tail': tails, 'head': heads, 'weight': weights})

    print("__________Naïve approach___________")
    dist = dijkstra_naive(graph_df)
    result = [dist[x] for x in [7,37,59,82,99,115,133,165,188,197]]
    print(result)

    print("__________Using heap___________")
    dist = dijkstra_heap(graph_df)
    result = [dist[x] for x in [7,37,59,82,99,115,133,165,188,197]]
    print(result)
    