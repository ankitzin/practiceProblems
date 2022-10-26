
class Node():
    def __init__(self, data):
        self.data = data
        self.next_element = None


class LinkedList():
    def __init__(self):
        self.head_node = None

    def insert_head(self,data):
        temp_node = Node(data)
        temp_node.next_element = self.head_node
        self.head_node = temp_node
        return self.head_node

    def is_empty(self):
        if self.head_node is None:
            return True
        else:
            return False

    def print_node(self):
        if self.is_empty():
            print("list is empty.")
            return False

        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end='->')
            temp = temp.next_element
        print(temp.data, '->None')


list_ = LinkedList()
list_.print_node()

for i in range(10):
    list_.insert_head(i)

list_.print_node()


