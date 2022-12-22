from typing import Optional

head_ = [1, 2, 3, 4, 5, 6]


def work(head):
    if len(head) % 2 == 0:
        mid = len(head)//2 + 1
    else:
        mid = len(head)//2 + 1

    return head[mid-1:]


print(work(head_))

