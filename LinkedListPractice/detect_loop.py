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

    def delete_head(self):
        first_node = self.get_head()

        if first_node is not None:
            self.head_node = first_node.next_node
            first_node.next_node = None

        return

    def search(self, value):
        current_node = self.head_node
        available = False
        if current_node is not None:
            if current_node.data == value:
                available = True
                return available
            current_node = current_node.next_node

        return available

    def length(self):
        length = 0
        temp = self.head_node()
        while temp is not None:
            length += 1
            temp = temp.next_node
        return length

    def print_list(self):
        temp = self.head_node()
        if temp is not None:
            print(temp.data, end='->')
            temp = temp.next_node
        print('None')

    def insert_at_head(self,val):
        temp = Node(val)
        temp.next_node = self.head_node
        self.head_node = temp

        return self.head_node

    def insert_at_tail(self,val):
        new_node = Node(val)
        temp = self.head_node()

        while temp is not None:
            temp = temp.next_node

        temp.next_node = new_node
        self.head_node = temp
        return self.head_node


def detect_loop(node: LinkedList):
    first = node.get_head()
    second = node.get_head()

    while first and second and second.next_node:
        first = first.next_node
        second = second.next_node.next_node

        if first == second:
            return True

    return False


lst = LinkedList()

detect_loop(lst)
