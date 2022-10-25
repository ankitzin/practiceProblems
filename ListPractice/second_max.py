list_ = [9, 2, 3, 6, 80, 200]


def second_max_int(arr):
    arr.sort()
    return arr[-2]


def second_max_int_logic(arr):
    first = 0
    second = 0
    index = 0
    for i, val in enumerate(arr):
        if first < val:
            first = val
            index = i
    arr[index] = 0
    for val in arr:
        if second < val:
            second = val

    return second


print(second_max_int_logic(list_))
