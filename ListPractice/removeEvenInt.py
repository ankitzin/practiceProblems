from typing import List


def remove_even_integer(l1: List[int]):
    """
    Time complexity for this solution is O(n)
    this function to remove the even from list of integers
    :param l1: List of integers
    :return: output_l1 list of odd integers
    """
    output_l1 = []
    for i, val in enumerate(l1):
        if val % 2 != 0:
            output_l1.append(val)
    return output_l1


def remove_even_comp(l1: List[int]):
    """
        Time complexity for this solution is O(n)
        this function to remove the even from list of integers
        :param l1: List of integers
        :return: list of odd integers
    """
    return [number for number in l1 if number % 2 != 0]


challenge_1_list = [-108, 194, -37, -16]

res_c1_1 = remove_even_integer(challenge_1_list)
res_c1_2 = remove_even_comp(challenge_1_list)

print(res_c1_1, res_c1_2)

