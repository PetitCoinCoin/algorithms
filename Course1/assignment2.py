def inversion_count(data: list):
    n = len(data)
    # base case
    if n == 0:
        return print("error with data: ", data)
    elif n == 1:
        return (data, 0)
    # general case
    else:
        left = inversion_count(data[:int(n/2)])
        right = inversion_count(data[int(n/2):])
        split_count = 0
        split_sort = [None] * n
        i = 0
        j = 0
        nl = len(left[0])
        nr = len(right[0])
        for k in range(n):
            if i > nl-1:
                split_sort[k] = right[0][j]
                j += 1
            elif j > nr-1:
                split_sort[k] = left[0][i]
                i += 1
            elif left[0][i] < right[0][j]:
                split_sort[k] = left[0][i]
                i += 1
            else:
                split_sort[k] = right[0][j]
                j += 1
                split_count = split_count + nl - i
        inv_count = split_count + left[1] + right[1]
        return (split_sort, inv_count)        


if __name__ == '__main__':
    
    # Get clean input array
    with open('IntegerArray.txt', 'r') as f:
        data = f.readlines()
    data = [int(x) for x in data]

    print(inversion_count(data)[1])