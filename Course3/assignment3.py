import time
from anytree import Node, RenderTree
from heapq import heappush, heappop
from collections import defaultdict 


def huffman_code(data, levels: dict, n: int):
    while n>1:
        # get minimum frequencies
        leaf1 = heappop(data)
        leaf2 = heappop(data)
        nodes = leaf1[1] + '+' + leaf2[1]
        nodes = nodes.split('+')
        # update heap with new node
        parent = (leaf1[0] + leaf2[0], leaf1[1] + '+' + leaf2[1])
        heappush(data, parent)
        n = len(data)
        # build tree
        for node in nodes:
            levels[node] += 1
    return levels


def max_weight_is(weights: list, n: int):
    max_weights = [0, weights[0]]
    for i in range(2, n+1):
        max_weights.append(max(max_weights[i-1], max_weights[i-2] + weights[i-1]))
    return max_weights


def reconstruction(weights: list, n: int):
    max_weights = max_weight_is(weights, n)
    indep_set = list()
    i = n
    while i > 0:
        if max_weights[i-1] >= max_weights[i-2] + weights[i-1]:
            i -= 1
        else:
            indep_set.append(i-1)
            i -= 2
    return indep_set


if __name__ == '__main__':
    # Get clean input data for Problem 1-2
    with open('huffman.txt', 'r') as f:
        data12 = f.readlines()
    n = int(data12[0])
    data12 = [int(x[:-1]) for x in data12[1:]]
    heap_data = list()
    for idx, value in enumerate(data12, start=1):
        heappush(heap_data, (value, str(idx)))
    levels_dict = defaultdict(lambda: 0)

    # Problem 1
    start_time = time.time()
    levels_dict = huffman_code(heap_data, levels_dict, n)
    max_depth = max(levels_dict.values())
    min_depth = min(levels_dict.values())
    print('Result for 1st problem:', max_depth)
    print('Result for 2nd problem:', min_depth)
    print("--- %s seconds ---" % (time.time() - start_time))

    # Get clean input data for 3rd problem
    with open('mwis.txt', 'r') as f:
        data3 = f.readlines()
    n = int(data3[0])
    data3 = [int(x[:-1]) for x in data3[1:]]

    # Problem 3
    start_time = time.time()
    result_nodes = reconstruction(data3, n)
    qst_nodes = [1, 2, 3, 4, 17, 117, 517, 997]
    answer = ''
    for node in qst_nodes:
        if node in result_nodes:
            answer = answer + '0'
        else:
            answer = answer + '1'
    print('Result for 3rd problem:', answer)
    print("--- %s seconds ---" % (time.time() - start_time))

