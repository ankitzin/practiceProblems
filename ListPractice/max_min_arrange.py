list_ = [1, 2, 3, 4, 5]


def max_min_arrange_list(arr):
    result = []
    for i in range(len(arr)//2):
        result.append(arr[-(i+1)])
        result.append(arr[i])

    if len(arr) % 2 == 1:
        result.append(arr[len(arr)//2])

    return result


print(max_min_arrange_list(list_))
