import time
from heapq import heappush, heappop, nsmallest, heapreplace


def median_maintenance(arr: list):
    start_time = time.time()

    heap_low = list()
    heappush(heap_low, (-arr[0], arr[0]))
    heap_high = list()
    median = [arr[0]]
    len_m = 1

    for elt in arr[1:]:
        if len_m % 2 == 1:
            if elt > median[-1]:
                heappush(heap_high, elt)
                median.append(median[-1])
            else:
                heappush(heap_high, heapreplace(heap_low, (-elt, elt))[1])
                median.append(nsmallest(1, heap_low)[0][1])
        else:
            if elt > median[-1]:
                heappush(heap_high, elt)                
                change_elt = heappop(heap_high)
                heappush(heap_low, (-change_elt, change_elt))
                median.append(change_elt)
            else:
                nsmallest(1, heap_low)[0][1]
                heappush(heap_low, (-elt, elt))
                median.append(median[-1])
        len_m += 1
    
    print("--- %s seconds ---" % (time.time() - start_time))
    return median


if __name__ == '__main__':
    
    # Get clean input data
    with open('Median.txt', 'r') as f:
        data = f.readlines()
    data = [int(x[:-1]) for x in data]

    result = median_maintenance(data)
    print(sum(result))
    print(sum(result) % 10000)
