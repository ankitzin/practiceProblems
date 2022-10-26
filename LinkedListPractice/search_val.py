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
            print("List is Empty")

        temp = self.head_node
        while temp.next_node is not None:
            print(temp.data, end='->')
            temp = temp.next_node
        print(temp.data, '->None')


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


def search_element(lst, val):
    new_node = Node(val)

    if lst.get_head() is None:
        lst.head_node = new_node
        return 0 + 1

    temp = lst.head_node
    i = 0
    while temp.next_node is not None:
        temp = temp.next_node
        i += 1
        if temp.data == val:
            return i + 1

    return 'Not available'


list_ = LinkedList()
val_ = 5
insert_at_tail(list_, 0)
insert_at_tail(list_, 1)
insert_at_tail(list_, 2)
insert_at_tail(list_, 81)
insert_at_tail(list_, 4)
insert_at_tail(list_, 5)
insert_at_tail(list_, 6)

list_.print_node()

print(search_element(list_, val_))



