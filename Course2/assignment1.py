from collections import defaultdict 
import sys
sys.setrecursionlimit(1500)


def kosaraju(data: list):
    graph_ini = defaultdict(list)
    for k, *v in data:
        graph_ini[k].append(v[0])
    
    graph_rev = defaultdict(list)
    data_rev = [[x[1], x[0]] for x in data]
    for k, *v in data_rev:
        graph_rev[k].append(v[0])

    n = max(graph_ini.keys())
    explored = list()
    t = 0
    s = None
    ftime = dict()
    leader = list()

    def dfs(graph: dict, start: int, fill_leader=False, compute_time=False):
        nonlocal explored
        nonlocal ftime
        nonlocal leader
        nonlocal t
        nonlocal s

        explored.append(start)
        if fill_leader:
            leader.append(s)

        try:
            next_nodes = graph[start]
        except KeyError:
            next_nodes = []
        for node in next_nodes:
            if node not in explored:
                dfs(graph, node, fill_leader, compute_time)
        if compute_time:
            t += 1
            ftime[t] = start
    
    # DFS on G reversed
    for i in range(n, 0, -1):
        if i not in explored:
            dfs(graph_rev, i, compute_time=True)
    
    # DFS on G with new node numerotation
    explored.clear()
    for i in range(n, 0, -1):
        j = ftime[i]
        if j not in explored:
            s = j
            dfs(graph_ini, j, fill_leader=True)

    return leader

if __name__ == '__main__':
    # Get clean input data
    with open('test_case_1.5.txt', 'r') as f:
        data = f.readlines()
    data = [[int(a) for a in x.split(' ')[:-1]] for x in data]

    scc_details = kosaraju(data)
    unique_leaders = set(scc_details)
    result = sorted([scc_details.count(x) for x in unique_leaders], reverse=True)

    print(result)