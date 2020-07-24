from collections import defaultdict 
import time


def kosaraju(data: list):
    graph_ini = defaultdict(list)
    for k, *v in data:
        graph_ini[k].append(v[0])
    
    graph_rev = defaultdict(list)
    data_rev = [[x[1], x[0]] for x in data]
    for k, *v in data_rev:
        graph_rev[k].append(v[0])

    n = max(graph_ini.keys())
    explored = dict()
    for k in range(1, n + 1):
        explored[k] = False
    t = 0
    s = None
    ftime = dict()
    count_leader = defaultdict(lambda : 0)

    def dfs(graph: dict, start: int, fill_leader=False, compute_time=False):
        nonlocal explored
        nonlocal ftime
        nonlocal count_leader
        nonlocal t
        nonlocal s

        explored[start] = True
        stack = [start]
         
        while stack:
            node = stack[-1]
            if not explored[node]:
                explored[node] = True
            remove_from_stack = True
            try:
                next_nodes = graph[node]
            except KeyError:
                next_nodes = []
            for next_node in next_nodes:
                if not explored[next_node]:
                    stack.append(next_node)
                    remove_from_stack = False
                    break
            if remove_from_stack:
                if compute_time:
                    t += 1
                    ftime[t] = stack.pop()
                else:
                    stack.pop()
                if fill_leader:
                    count_leader[s] += 1

    print("--- %s seconds ---" % (time.time() - start_time))
    # DFS on G reversed
    for i in range(n, 0, -1):
        if not explored[i]:
            dfs(graph_rev, i, compute_time=True)
    
    print("--- %s seconds ---" % (time.time() - start_time))
    # DFS on G with new node numerotation
    for k in range(1, n + 1):
        explored[k] = False
    for i in range(n, 0, -1):
        j = ftime[i]
        if not explored[j]:
            s = j
            dfs(graph_ini, j, fill_leader=True)

    print("--- %s seconds ---" % (time.time() - start_time))
    return count_leader

if __name__ == '__main__':
    start_time = time.time()
    # Get clean input data
    with open('SCC.txt', 'r') as f:
        data = f.readlines()
    data = [[int(a) for a in x.split(' ')[:-1]] for x in data]

    scc_details = kosaraju(data)
    result = sorted(scc_details.values(), reverse=True)

    print(result[:10])
    print("--- %s seconds ---" % (time.time() - start_time))