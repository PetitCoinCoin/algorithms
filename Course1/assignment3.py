def partition(data: list, beg: int, end: int):
    # Pivot definition
    p = data[beg]
    # Partition
    i = beg + 1
    for j in range(beg + 1, end):
        if data[j] < p:
            data[i], data[j] = data[j], data[i]
            i += 1
    data[i-1], data[beg] = data[beg], data[i-1]
    return i-1, end - beg - 1


def place_pivot(data: list, case: int, beg: int, end: int):
    if case == 1: # pivot = first element
        pass
    elif case == 2: # pivot = last element
        data[beg], data[end-1] = data[end-1], data[beg]
    elif case == 3: # pivot = median
        m = (end - 1 + beg) // 2
        if data[beg] < data[m]:
            if data[m] < data[end-1]:
                data[beg], data[m] = data[m], data[beg]
            elif data[beg] < data[end-1]:
                data[beg], data[end-1] = data[end-1], data[beg]
            else:
                pass
        else:
            if data[beg] < data[end-1]:
                pass
            elif data[m] < data[end-1]:
                data[beg], data[end-1] = data[end-1], data[beg]
            else: 
                data[beg], data[m] = data[m], data[beg]


def quickSort(data: list, beg: int, end: int, case: int):
    count = 0
    if beg < end - 1 :
        place_pivot(data, case, beg, end)
        pi, count = partition(data, beg, end)
        count = count + quickSort(data, beg, pi, case)
        count = count + quickSort(data, pi + 1, end, case)
    return count


if __name__ == '__main__':
    
    # Get clean input array
    with open('QuickSort.txt', 'r') as f:
        data = f.readlines()
    data = [int(x) for x in data]
    data_length = len(data)

    print(quickSort(data, 0, data_length, 3))
