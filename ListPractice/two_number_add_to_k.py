from typing import List

_lst = [1, 21, 3, 14, 5, 60, 7, 8]
_k = 81


def two_number_list_sum_k(lst, k):
    index = 0
    sec_index = 0
    val = 0

    while index < len(lst):
        for val in lst:
            if val + lst[index] == k:
                return [val, lst[index]]

        index += 1


def two_number_list_sum_k_index(lst: List[int], k):
    """
    Time complexity for this is O(nlogn) bcz for sorting O(nlogn) + O(n)(for finding the number)
    :param lst: List of integers
    :param k: Sum should be equal to this number
    :return: list of two integer that is equal to
    """
    left_i = 0
    right_i = len(lst)-1
    val = 0
    lst.sort()
    while left_i < right_i:
        if lst[left_i] + lst[right_i] > k:
            val = lst[left_i] + lst[right_i]
            right_i -= 1
        elif lst[left_i] + lst[right_i] < k:
            val = lst[left_i] + lst[right_i]
            left_i += 1
        else:
            if lst[left_i]+lst[right_i] == k:
                return [lst[left_i],lst[right_i]]


print(two_number_list_sum_k(_lst, _k))
print(two_number_list_sum_k_index(_lst, _k))
