import time
import re
from collections import defaultdict
import math

import networkx as nx
import heapq


def bellman_ford(graph, n: int):
    result = [[0] + [math.inf] * n]
    for i in range(1, n + 1):
        for v in range(0, n + 1):
            hops = [result[i - 1][w] + graph[w][v]['weight'] for w in graph.predecessors(v)]
            if len(hops) == 0:
                hops.append(result[i - 1][v])
            try:
                result[i].append(min(result[i - 1][v], min(hops)))
            except IndexError:
                result.append([min(result[i - 1][v], min(hops))])
        if result[i] == result[i - 1]:
            return result[i]
        
    if result[n] == result[n - 1]:
        return result[n]
    else:
        return False


def reweighting(graph, weights: list):
    graph.remove_node(0)
    for u, v, wt in graph.edges.data('weight'):
        graph[u][v]['weight'] = wt + weights[u] - weights[v]
    return graph


def dijkstra(graph, start: int):
    # Init
    distances = defaultdict(lambda : math.inf)
    remaining = [(distances[v], v) for v in list(graph.nodes) if v != start]
    heapq.heapify(remaining)
    for v in graph.successors(start):
        remaining.remove((distances[v], v))
        distances[v] = graph[start][v]['weight']
        heapq.heappush(remaining, (distances[v], v))

    # Main
    while len(remaining) > 0:
        new_vertex = heapq.heappop(remaining)
        new_v = new_vertex[1]
        distances[new_v] = new_vertex[0]
        # Update keys
        for v in graph.successors(new_v):
            if (distances[v], v) in remaining:
                remaining.remove((distances[v], v))
                distances[v] = min(distances[v], graph[new_v][v]['weight'] + distances[new_v])
                heapq.heappush(remaining, (distances[v], v))
    return distances


def pipeline(data: list, n: int):
    # Graph construction
    G = nx.DiGraph()
    for tail, head, wt in data:
        # Graph can't handle parallel edges so we keep the shortest
        try: 
            G[tail][head]['weight'] = min(G[tail][head]['weight'], wt)
        except KeyError:
            G.add_edge(tail, head, weight=wt)
    new_vertex = [(0, i, 0) for i in range(1, n + 1)]
    G.add_weighted_edges_from(new_vertex)

    # Pipeline
    weights = bellman_ford(G, n)
    print('BF done')
    if weights == False:
        return "This graph contains a negative cycle"
    else:
        G_reweighted = reweighting(G, weights)
        print('Reweighting done')
        shortest_dist = list()
        cpt = 1
        for s in list(G_reweighted.nodes):
            dist = dijkstra(G_reweighted, s)
            for key, val in dist.items():
                dist[key] = val - weights[s] + weights[key]
            shortest_dist.append(min(dist.values()))
        return min(shortest_dist)


if __name__ == '__main__':
    for file in ['g1.txt', 'g2.txt','g3.txt']: 

        # Get clean input data
        with open(file, 'r') as f:
            data = f.readlines()
        n = int(data[0].split(' ')[0])
        m = int(data[0].split(' ')[1][:-1])
        data = [tuple([int(a) for a in re.split(' |\n', x)[:-1]]) for x in data[1:]]
        
        # Pipeline
        start_time = time.time()
        print('Result for', file, ':', pipeline(data, n))
        print("--- %s seconds ---" % (time.time() - start_time))

    