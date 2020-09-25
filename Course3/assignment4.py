import time


def knapsack(capacity: int, sizes: list, values: int, n:int):
    result = [[0]*(capacity + 1), []]
    for i in range(1, n):
        for x in range(capacity + 1):
            if sizes[i] >= x:
                new_val = result[0][x]
            else:
                new_val = max(result[0][x], result[0][x - sizes[i]] + values[i])
            if x == 0:
                result[1] = [new_val]
            else:
                result[1].append(new_val)
            # try:
            #     result[i].append(new_val)
            # except IndexError:
            #     result.append([new_val])
        result[0], result[1] = result[1], result[0]
    return result[0][capacity]


if __name__ == '__main__':
    # Get clean input data for Problem 1
    start_time = time.time()
    with open('knapsack1.txt', 'r') as f:
        data= f.readlines()
    info = [int(x) for x in data[0].split(' ')]
    capa = info[0]
    nb = info[1]
    data = [[int(a) for a in x[:-1].split(' ')] for x in data[1:]]
    val = [x[0] for x in data]
    size = [x[1] for x in data]
    print("--- %s seconds ---" % (time.time() - start_time))
   
    # Problem 1
    start_time = time.time()
    print('Result for 1st problem:', knapsack(capa, size, val, nb))
    print("--- %s seconds ---" % (time.time() - start_time))

    # Get clean input data for Problem 2
    start_time = time.time()
    with open('knapsack_big.txt', 'r') as f:
        data= f.readlines()
    info = [int(x) for x in data[0].split(' ')]
    capa = info[0]
    nb = info[1]
    data = [[int(a) for a in x[:-1].split(' ')] for x in data[1:]]
    val = [x[0] for x in data]
    size = [x[1] for x in data]
    print("--- %s seconds ---" % (time.time() - start_time))
   
    # Problem 2
    start_time = time.time()
    print('Result for 2nd problem:', knapsack(capa, size, val, nb))
    print("--- %s seconds ---" % (time.time() - start_time))