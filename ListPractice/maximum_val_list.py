from typing import List

arr_ = [9, 2, 3, 6, -3]


def find_minimum_easy(arr: List[int]):
    """
    Sorted the list then find the lowest value . O(nlogn) time complexity
    :param arr: List of integers
    :return: minimum value in list
    """
    arr.sort()
    return arr[0]


def find_minimum_logic(arr: List[int]):
    """
    Used the logic to solve this using O(n) so better than above solution
    :param arr: Array of integers
    :return: minimum value in the integers
    """
    min_val = 999

    for val in arr:
        if min_val > val:
            min_val = val

    return min


print(find_minimum_logic(arr_))
