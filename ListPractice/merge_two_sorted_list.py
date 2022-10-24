from typing import List

list1_ = [1, 2, 3, 5]
list2_ = [2, 6, 7, 8]


def merge_lists_time(list1: List[int], list2: List[int]):
    """
    Time complexity for this is O(mn) that means O(m^2) or O(n^2)
    :param list1: List of sorted integer
    :param list2: List of sorted integer
    :return: Single list with sorted integer
    """

    index_1 = 0
    index_2 = 0

    while index_1 < len(list1) and index_2 < len(list2):
        if list1[index_1] > list2[index_2]:
            list1.insert(index_1, list2[index_2])
            index_2 += 1
            index_1 += 1
        else:
            index_1 += 1

    if index_2 < len(list2):
        list1.extend(list2[index_2:])

    return list1


def merge_lists_space(list1: List[int], list2: List[int]):
    """
        Time complexity for this is O(m+n) that means O(m+n) or O(n+M)
        both are good but we need to select which is efficient for our requirement. Because one is for space and other is
        for time, its trade off.
        :param list1: List of sorted integer
        :param list2: List of sorted integer
        :return: Single list with sorted integer
    """

    index_1 = 0
    index_2 = 0
    index_result = 0
    result = []
    for i in range(len(list2)+len(list1)):
        result.append(i)

    while index_1 < len(list1) and index_2 < len(list2):
        if list1[index_1] < list2[index_2]:
            result[index_result] = list1[index_1]
            index_1 += 1
            index_result += 1
        else:
            result[index_result] = list2[index_2]
            index_2 += 1
            index_result += 1

    while index_1 < len(list1):
        result[index_result] = list1[index_1]
        index_1 += 1
        index_result += 1

    while index_2 < len(list2):
        result[index_result] = list2[index_2]
        index_2 += 1
        index_result += 1

    return result


print(merge_lists_time(list1_, list2_))
list1_ = [1, 2, 3, 5]
list2_ = [2, 6, 7, 8]

print(merge_lists_space(list1_, list2_))