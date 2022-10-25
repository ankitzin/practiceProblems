"""
Both methods take the O(n) time complexity.
one using list comprehension and other using auxilary list ( extra lists)
"""

list_ = [10, -1, 20, 4, 0, 5, -9, -6]


def rearrange(arr):
    neg_lis = []
    pos_lis = []
    zer_lis = []
    for val in arr:
        if val < 0:
            neg_lis.append(val)
        elif val == 0:
            zer_lis.append(val)
        else:
            pos_lis.append(val)

    return neg_lis+zer_lis+pos_lis


def rearrange_com(arr):
    return [i for i in arr if i < 0] + [i for i in arr if i >= 0]


print(rearrange(list_))
print(rearrange_com(list_))