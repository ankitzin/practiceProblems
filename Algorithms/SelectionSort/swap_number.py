from typing import List


def swap(lst: List[int], fir, sec):
    temp = lst[fir]
    lst[fir] = lst[sec]
    lst[sec] = temp

