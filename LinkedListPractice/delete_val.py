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

    def delete_at_head(self):
        first_element = self.get_head()
        if first_element is not None:
            self.head_node = first_element.next_node
            first_element.next_node = None
        return


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


def delete_by_val(lst, val):
    deleted = False
    current_node = lst.get_head()
    previous_node = None
    if current_node.data == val:
        lst.delete_at_head()
        deleted = True
        return deleted

    while current_node is not None:
        if val == current_node.data:
            previous_node.next_node = current_node.next_node
            current_node.next_node = None
            deleted = True
            break
        previous_node = current_node
        current_node = current_node.next_node

    return deleted


def length_list(lst):
    temp = lst.get_head()
    i = 0
    while temp is not None:
        temp = temp.next_node
        i += 1

    return i


list_ = LinkedList()

val_ = 5
insert_at_tail(list_, 0)
insert_at_tail(list_, 1)
insert_at_tail(list_, 2)
insert_at_tail(list_, 81)
insert_at_tail(list_, 4)
insert_at_tail(list_, 5)
insert_at_tail(list_, 6)

delete_by_val(list_, 81)
list_.print_node()

print(length_list(list_))
