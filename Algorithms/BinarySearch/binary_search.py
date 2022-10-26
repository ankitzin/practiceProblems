from typing import List


def binary_search_algo(arr: List[int], val: int):
    """
    Time complexity for searching the element in the sorted list is O(log n).

    :param arr: List of sorted array
    :param val: value to be search in the list
    :return: return the position in list for the available value
    """
    left = 0
    right = len(arr) - 1
    found = False
    while left < right:
        mid = (left + right)//2
        if val == arr[mid]:
            found = True
            print(f"Found at {mid + 1}")
            return mid + 1
        elif val > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1

    if not found:
        print(f"{val} not available in list")
        return None
