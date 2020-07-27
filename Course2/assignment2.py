import warnings
warnings.filterwarnings("ignore")

from collections import defaultdict 
import pandas as pd
import time

def dijkstra_naive(graph, start=1, n=200):

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
    
    return distances

if __name__ == '__main__':
    start_time = time.time()
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

    print("--- %s seconds ---" % (time.time() - start_time))
    dist = dijkstra_naive(graph_df)
    print("--- %s seconds ---" % (time.time() - start_time))
    result = [dist[x] for x in [7,37,59,82,99,115,133,165,188,197]]
    print(result)
    