
import random
import pandas as pd

pd.options.mode.chained_assignment = None 


def minCut():
    # Get clean input array
    with open('kargerMinCut.txt', 'r') as f:
        data = f.readlines()
    data = [row.split('\t') for row in data]
    data = [[int(r[0]), [int(x) for x in r[1:-1]]] for r in data]
    graph = pd.DataFrame(data, columns=['vertex', 'links'])

    while len(graph)>2:
        # Randomly choose an edge
        u_idx = random.choice(range(len(graph)))
        u = graph.iloc[u_idx,0]
        v = random.choice(graph.iloc[u_idx,1])

        # Merge vertices u + v > u
        v_idx = list(graph.vertex).index(v)
        graph.links = [[u if x == v else x for x in edges] for edges in graph.links]
        new_links = graph.iloc[u_idx,1] + graph.iloc[v_idx,1]
        new_links = [x for x in new_links if x != u]
        graph.iat[u_idx, 1] = new_links
        graph = graph[graph.vertex != v]

    # print(graph)
    return len(graph.iloc[0,1])



if __name__ == '__main__':
    result = list()
    for i in range(200):
        result.append(minCut())
    print(result)
    print('Minimum is:', min(result))