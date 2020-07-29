import time
from bisect import bisect_left, bisect_right


def two_sum_hash(hash_arr: dict, target: int):
    for a in hash_arr.keys():
        try:
            hash_arr[target - a]
            return True
        except KeyError:
            pass
    return False


def two_sum_sorted(data: set):
    data = list(data)
    data.sort()
    output = list()
    for val in data:
        lower_idx = bisect_left(data, -10000-val)
        upper_idx = bisect_right(data, 10000-val)
        output.extend([x + val for x in data[lower_idx:upper_idx]])
    output = set(output)
    return len(output)


if __name__ == '__main__':
    
    start_time = time.time()
    
    # Get clean input data: order list of unique elements
    with open('prob-2sum.txt', 'r') as f:
        data = f.readlines()
    data = [int(x[:-1]) for x in data]
    data = set(data)
    
    print("--- %s seconds ---" % (time.time() - start_time))

    # data_dict = dict()
    # for a in data:
    #     data_dict[a] = a

    # print("--- %s seconds ---" % (time.time() - start_time))

    # result = list()
    # for t in range(-10000, 10001):
    #     result.append(two_sum_hash(data_dict, t))
    # print(sum(result))

    print(two_sum_sorted(data))
    print("--- %s seconds ---" % (time.time() - start_time))
