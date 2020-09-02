import time
import pandas as pd


def greedy_difference(jobs):
    jobs['difference'] = jobs['weight'] - jobs['length'] 
    jobs.sort_values(['difference', 'weight'], ascending=[False, False], inplace=True)
    jobs['completion_time'] = jobs['length'].cumsum()
    jobs['weighted_completion_time'] = jobs['completion_time'] * jobs['weight']
    return jobs['weighted_completion_time'].sum()

def greedy_ratio(jobs):
    jobs['ratio'] = jobs['weight'] / jobs['length'] 
    jobs.sort_values(['ratio', 'weight'], ascending=[False, False], inplace=True)
    jobs['completion_time'] = jobs['length'].cumsum()
    jobs['weighted_completion_time'] = jobs['completion_time'] * jobs['weight']
    return jobs['weighted_completion_time'].sum()

def prim(edges):
    n = max(edges.start.max(), edges.end.max())
    # Init
    edges['start_scanned'] = len(edges.index) * [False]
    edges['end_scanned'] = len(edges.index) * [False]
    edges.loc[edges.start == 1, 'start_scanned'] = True
    edges.loc[edges.end == 1, 'end_scanned'] = True
    MST_cost = list() # Could just use an int and sum progressively for assignment
    while sum(edges['start_scanned'])<len(edges.index) and sum(edges['end_scanned'])<len(edges.index):
        temp = edges[(edges['start_scanned']) & (edges['end_scanned'] == False)]
        idx = temp['cost'].idxmin()
        # Append edge to MST
        MST_cost.append(edges.iloc[idx, 2])
        # Mark end vertex as scanned
        v = edges.iloc[idx, 1]
        edges.loc[edges.start == v, 'start_scanned'] = True
        edges.loc[edges.end == v, 'end_scanned'] = True
    return sum(MST_cost)

if __name__ == '__main__':
    # Get clean input data
    with open('jobs.txt', 'r') as f:
        data = f.readlines()
    data = [[int(a) for a in x[:-1].split(' ')] for x in data[1:]]
    df = pd.DataFrame({'weight': [d[0] for d in data], 'length': [d[1] for d in data]})

    # Problem 1
    start_time = time.time()
    print('Result for 1st problem:', greedy_difference(df))
    print("--- %s seconds ---" % (time.time() - start_time))

    # Problem 2
    start_time = time.time()
    print('Result for 2nd problem:', greedy_ratio(df))
    print("--- %s seconds ---" % (time.time() - start_time))

    # Get clean input data for Prim's algorithm
    with open('edges.txt', 'r') as f:
        data_3 = f.readlines()
    n = int(data_3[0][:-1].split(' ')[0])
    m = int(data_3[0][:-1].split(' ')[1])
    data_3 = [[int(a) for a in x[:-1].split(' ')] for x in data_3[1:]]
    # Need to double data because it is an undirected graph
    df_3 = pd.DataFrame({'start': [d[0] for d in data_3] + [d[1] for d in data_3], 
                        'end': [d[1] for d in data_3] + [d[0] for d in data_3],
                        'cost': [d[2] for d in data_3] + [d[2] for d in data_3]})

    # Problem 3
    start_time = time.time()
    print('Result for 3rd problem:', prim(df_3))
    print("--- %s seconds ---" % (time.time() - start_time))