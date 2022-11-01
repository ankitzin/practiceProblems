class Node:
    def __init__(self,data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if self.head_node is None:
            return True

        return False

    def length(self):
        temp = self.get_head()
        len_ = 0

        while temp:
            temp = temp.next_node
            len_ += 1

        return len_


def find_mid(lst:LinkedList):
    if lst.is_empty():
        print("list is Empty")

    val = lst.length()
    if val % 2 == 0:
        val = val/2
    else:
        val = val/2 + 1

    node = lst.get_head()
    len = 0
    while node:
        node = node.next_node
        len += 1
        if len == val:
            return node.data
