class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None


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

    def insert_at_head(self, dt):
        new_node = Node(dt)

        if self.is_empty():
            self.head_node = new_node
            return self.head_node

        new_node.next_node = self.head_node
        self.head_node.previous_node = new_node
        self.head_node = new_node

        return self.head_node

    def insert_at_tail(self,dt):
        new_node = Node(dt)

        if self.is_empty():
            self.head_node = new_node
            return self.head_node

        temp = self.get_head()
        while temp.next_node is not None:
            temp = temp.next_node

        temp.next_node = new_node

        return

    def reverse_list(self):
        previous = None
        current_node = self.get_head()
        next_node = None

        while current_node:
            next_node = current_node.next_node
            current_node.next_node = previous
            previous = current_node
            current_node = next_node

            self.head_node = previous

        return self.head_node

    def print_list(self):
        curr = self.get_head()
        while curr:
            print(curr.data, end='->')
            curr = curr.next_node


lst = LinkedList()
lst.insert_at_head(6)
lst.insert_at_head(5)
lst.insert_at_head(4)

lst.reverse_list()
lst.print_list()
