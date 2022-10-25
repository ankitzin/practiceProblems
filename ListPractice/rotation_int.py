from typing import List

list_ = [10, 20, 30, 40, 50]


def right_rotation(arr: List[int], k: int):
    k = k % len(arr)

    return arr[-k:] + arr[:-k]
