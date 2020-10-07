import time
import re
from collections import defaultdict
import math
import matplotlib.pyplot as plt

import heapq


def euclidean_dist(x: tuple, y: tuple):
    return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)


def heuristic_tsp(data: list, n: int):
    # Init
    visited = defaultdict(lambda: False)
    visited[0] = True
    path = [0]
    distance = 0
    city = 0
    neighbors = [(euclidean_dist(data[0], data[i]), i) for i in range(1, n)]
    heapq.heapify(neighbors)

    # Run
    while len(path) < n:
        new_city = heapq.heappop(neighbors)
        while visited[new_city[1]]:
            new_city = heapq.heappop(neighbors)
        distance = distance + new_city[0]
        path.append(new_city[1])
        visited[new_city[1]] = True
        city = new_city[1]
        neighbors =  [(euclidean_dist(data[city], data[i]), i) for i in range(1, n) if not visited[i]]
        heapq.heapify(neighbors)
        
    distance = distance + (euclidean_dist(data[city], data[0]))
    return distance


if __name__ == '__main__':
    # Get clean input data
    with open('nn.txt', 'r') as f:
        data = f.readlines()
    n = int(data[0])
    data = [tuple([float(a) for a in re.split(' |\n', x)[1:-1]]) for x in data[1:]] 
    
    # Plot data
    x = [a[0] for a in data]
    y = [a[1] for a in data]
    labels = [i for i in range(len(x))]
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    for i, txt in enumerate(labels):
        ax.annotate(txt, (x[i], y[i]))
    # plt.show()

    # Result
    start_time = time.time()
    print('Result :', heuristic_tsp(data, n))
    print("--- %s seconds ---" % (time.time() - start_time))