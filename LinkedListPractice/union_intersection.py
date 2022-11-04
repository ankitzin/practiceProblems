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
        if self.is_empty():
            print("List is empty Nothing to delete")
            return None
        else:
            if self.length() == 1:
                print("deleted ")
                self.head_node = None
                return self.head_node

        temp_node = self.get_head()
        temp_node = temp_node.next_node
        self.head_node = None
        self.head_node = temp_node
        return self.head_node

    def delete(self, val):
        deleted = False
        prev_node = None
        curr_node = self.head_node

        if self.is_empty():
            print("List is None")
            return None

        while curr_node:
            if curr_node.data == val:
                prev_node.next_node = curr_node.next_node
                curr_node.next_node = None
                deleted = True
                break

            prev_node = curr_node
            curr_node = curr_node.next_node

        return deleted

    def length(self):
        temp_node = self.head_node
        len_ = 0
        while temp_node:
            temp_node = temp_node.next_node
            len_ += 1

        return len_

    def print_list(self):
        temp_node = self.get_head()
        print(temp_node)
        while temp_node is not None:
            print(temp_node.data, end='->')
            temp_node = temp_node.next_node
        print(None)

    def insert_at_position(self):
        pass

    def mid_value(self):
        pass

    def remove_duplicates(self):
        prev_node = None
        curr_node = self.get_head()

        while curr_node:
            prev_node = curr_node
            while prev_node:
                if prev_node.next_node:
                    if curr_node.data == prev_node.next_node.data:
                        new_next_node = prev_node.next_node.next_node
                        prev_node.next_node = new_next_node
                    else:
                        prev_node = prev_node.next_node
                else:
                    prev_node = prev_node.next_node

            curr_node = curr_node.next_node

        return self.head_node

ll = LinkedList()
ll.insert_head(5)
ll.insert_head(8)
ll.insert_head(9)
ll.insert_head(9)
ll.insert_tail(90)
print(ll.length())
# ll.delete_head()
# ll.delete(8)
ll.remove_duplicates()
ll.print_list()

l2 = LinkedList()
l2.insert_head(33)
l2.insert_head(36)
l2.insert_head(5)


def remove_duplicates(lst: LinkedList):
    if lst.is_empty():
        return None

    if lst.get_head().next_node is None:
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


def join_ll_union(l1:LinkedList, l2: LinkedList):
    if l1.is_empty() and l2.is_empty():
        return None
    if l1.is_empty():
        return l2
    if l2.is_empty():
        return l1

    if not l1.is_empty():
        curr_list = l1.head_node
        next_list = l2.head_node
        while curr_list:
            curr_list = curr_list.next_node
            if curr_list.next_node == None:
                curr_list.next_node = next_list
                break
        return l1


fin = join_ll_union(ll, l2)
remove_duplicates(fin)
fin.print_list()
print("lets see how it goes")


