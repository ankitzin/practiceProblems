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
        if self.get_head() is None:
            return True
        return False

    def insert_head(self, val):
        new_node = Node(val)
        if self.is_empty():
            self.head_node = new_node
            return self.head_node

        new_node.next_node = self.head_node
        self.head_node = new_node

        return self.head_node

    def insert_tail(self, val):
        new_node = Node(val)

        if self.is_empty():
            self.head_node = new_node
            return self.head_node

        temp_node = self.get_head()
        while temp_node.next_node is not None:
            temp_node = temp_node.next_node

        temp_node.next_node = new_node

        return self.head_node

    def delete_head(self):
        pass

    def delete(self):
        pass

    def length(self):
        pass

    def print_list(self):
        pass

    def insert_at_position(self):
        pass

    def mid_value(self):
        pass

    def remove_duplicates(self):
        pass


ll = LinkedList()
ll.insert_head(5)
ll.insert_head(8)
ll.insert_head(9)
ll.insert_tail(90)
