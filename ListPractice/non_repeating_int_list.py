from collections import defaultdict

list_ = [9, 2, 3, 2, 6, 6]


def non_repeat_int_list(arr):
    index = 0
    for index in range(arr):
        index_1 = 0

        while index_1 < len(arr):
            if index_1 != index and arr[index_1] == arr[index]:
                break
            index_1 += 1

        if index_1 == len(arr):
            return arr[index]
    return None


def non_repeat_int_logic(arr):
    mp = defaultdict(lambda : 0)

    for i in range(len(arr)):
        mp[arr[i]] += 1

    for i in range(len(arr)):
        if mp[arr[i]] == 1:
            return arr[i]
    return -1


print(non_repeat_int_logic(list_))
