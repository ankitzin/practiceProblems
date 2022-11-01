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

    def insert_tail(self, val):
        new_node = Node(val)
        temp_node = self.get_head()

        if temp_node :
            temp_node = temp_node.next_node

        temp_node.next_node = new_node
        self.head_node = temp_node

        return self.head_node

    def print_list(self):
        temp = self.get_head()
        if temp:
            print(temp.data, end='->')
            temp = temp.next_node

        print(temp.data, 'None')

    def length(self):
        temp = self.get_head()
        len_ = 0

        while temp:
            temp = temp.next_node
            len_ += 1
        return len_

    def search(self, val):
        temp = self.get_head()
        while temp:
            if temp.data == val:
                return True
            temp = temp.next_node

        return False

    def delete_head(self):
        temp = self.get_head()
        temp = temp.next_node
        self.head_node = temp
        temp.next_node = None

        return self.head_node

    def delete(self, val):
        prev = None
        current = self.get_head()
        deleted = False
        if self.is_empty():
            print("List is None")
            return
        if current.data == val:
            self.delete_head()
            deleted = True
            return deleted

        while current is not None:
            if current.data == val:
                prev.next_node = current.next_node
                current.next_node = None
                deleted = True
                break

            prev = current
            current = current.next_node

        return deleted


def remove_duplicates(lst: LinkedList):
    if lst.is_empty():
        return None

    if lst.get_head().next_element is None:
        return lst

    first_node = lst.get_head()

    while first_node:
        sec_node = first_node
        while sec_node:
            if sec_node.next_node:
                if first_node.data == sec_node.next_node.data:
                    new_next_node = sec_node.next_node.next_node
                    sec_node.next_node = new_next_node
                else:
                    sec_node = sec_node.next_node
            else:
                sec_node = sec_node.next_node

        first_node = first_node.next_node
    
    return lst






