class Node:
    def __init__(self, data):
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
        else:
            return False

    def print_node(self):
        if self.is_empty():
            print("list is empty")
            return False
        temp = self.head_node
        while temp.next_node is not None:
            print(temp.data, end='->')
            temp = temp.next_node
        print(temp.data, '->None')
        return True


def insert_at_tail(lst, val):
    new_node = Node(val)

    if lst.get_head() is None:
        lst.head_node = new_node
        return

    temp = lst.get_head()
    while temp.next_node:
        temp = temp.next_node

    temp.next_node = new_node
    return


lst = LinkedList()
lst.print_node()

insert_at_tail(lst, 0)
lst.print_node()

insert_at_tail(lst, 1)
lst.print_node()

insert_at_tail(lst, 2)
lst.print_node()
