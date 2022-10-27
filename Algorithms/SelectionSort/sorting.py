from typing import List


def select_sort(arr: List[int]):
    i = 0
    if len(arr)== 1:
        return arr
    elif len(arr) == 0:
        return None
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index] , arr[i]

    return arr