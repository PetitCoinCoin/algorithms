import time
import re
from itertools import chain, combinations
from collections import defaultdict
import math

import matplotlib.pyplot as plt
import networkx as nx


def graph_construction(data: list, n: int):
    edges = list()
    for i in range(0, n):
        for j in range(i + 1, n):
            distance = math.sqrt((data[i][0] - data[j][0])**2 + (data[i][1] - data[j][1])**2)
            edges.append((i, j, {'weight': distance}))
    G = nx.Graph()
    G.add_edges_from(edges)
    return G


def powerset(iterable):
    s = list(iterable)
    result = list(chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1)))
    result = [a for a in result if 0 in a]
    return result


def tsp(graph, n: int):
    subsets = powerset(range(n))
    temp = defaultdict(lambda : [math.inf] * n)
    temp[subsets[0]] = [0] + [math.inf] * (n - 1)
    for i in range(2, n + 1):
        for sub in [subs for subs in subsets if len(subs) == i]:
            for v in sub:
                if v != 0:
                    prev_sub = tuple(x for x in sub if x!= v)
                    values = [temp[prev_sub][k] + graph[k][v]['weight'] for k in prev_sub]
                    temp[sub][v] = min(values)
    return min([temp[tuple(range(n))][k] + graph[k][0]['weight'] for k in range(1, n)])


if __name__ == '__main__':
    # Get clean input data
    with open('tsp.txt', 'r') as f:
        data = f.readlines()
    n = int(data[0])
    data = [tuple([float(a) for a in re.split(' |\n', x)[:-1]]) for x in data[1:]]
    
    # Plot data
    x = [a[0] for a in data]
    y = [a[1] for a in data]
    labels = [i for i in range(len(x))]
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    for i, txt in enumerate(labels):
        ax.annotate(txt, (x[i], y[i]))
    plt.show()

    # After plot we can consider two sets of data with common edge 11-12

    # Result
    start_time = time.time()
    graph_left = graph_construction(data[:13], 13)
    graph_right = graph_construction(data[11:], n - 11)
    print("--- %s seconds ---" % (time.time() - start_time))
    left_val = tsp(graph_left, 13)
    print("--- %s seconds ---" % (time.time() - start_time))
    right_val = tsp(graph_right, n - 11)
    print("--- %s seconds ---" % (time.time() - start_time))
    print('Result :', left_val + right_val - 2 * graph_left[11][12]['weight'])

