import time
from collections import defaultdict


def graph_construction(data: list):
    output = list()
    for clause in data:
        output.append((-clause[0], clause[1]))
        output.append((-clause[1], clause[0]))
    output = list(set(output))
    return output


def kosaraju(data: list):
    graph_ini = defaultdict(list)
    for k, *v in data:
        graph_ini[k].append(v[0])
    
    graph_rev = defaultdict(list)
    data_rev = [[x[1], x[0]] for x in data]
    for k, *v in data_rev:
        graph_rev[k].append(v[0])

    key_range = list(set(list(graph_ini.keys()) + list(graph_rev.keys())))
    explored = dict()
    for k in key_range:
        explored[k] = False
    t = 0
    s = None
    ftime = dict()
    id_leader = defaultdict(lambda : 0)

    def dfs(graph: dict, start: int, fill_leader=False, compute_time=False):
        nonlocal explored
        nonlocal ftime
        nonlocal id_leader
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
                    id_leader[node] = s

    # DFS on G reversed
    for i in sorted(key_range, reverse=True):
        if not explored[i]:
            dfs(graph_rev, i, compute_time=True)
    
    # DFS on G with new node numerotation
    for k in key_range:
        explored[k] = False
    for i in sorted(ftime.keys(), reverse=True):
        j = ftime[i]
        if not explored[j]:
            s = j
            dfs(graph_ini, j, fill_leader=True)

    return id_leader


def faisability_check(leaders: dict):
    for k in leaders.keys():
        if leaders[k] == leaders[-k]:
            return 'Insatisfiable'
    return 'Satisfiable'


if __name__ == '__main__':
    for file in ['2sat1.txt', '2sat2.txt','2sat3.txt', '2sat4.txt', '2sat5.txt', '2sat6.txt']: 

        # Get clean input data
        with open(file, 'r') as f:
            data = f.readlines()
        n = int(data[0])
        data = [[int(a) for a in x.split(' ')] for x in data[1:]]
        
        # Pipeline
        print("***")
        start_time = time.time()
        graph = graph_construction(data)
        print("Graph construction done --- %s seconds ---" % (time.time() - start_time))
        scc_leaders = kosaraju(graph)
        print("KOSARAJU done --- %s seconds ---" % (time.time() - start_time))
        print('Result for', file, ':', faisability_check(scc_leaders))
        print("TOTAL TIME --- %s seconds ---" % (time.time() - start_time))
