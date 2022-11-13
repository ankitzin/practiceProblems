"""
Stack : LIFO
Last inserted values into the list will be first element to come out
methods:
    is_empty()
    peek()
    size()
    push()
    pop()
    size()
"""


class Stack:
    def __init__(self):
        self.stack_list = []
        self.stack_size = 0

    def is_empty(self):
        return not self.stack_list

    def size(self):
        return self.stack_size

    def peek(self):
        return self.stack_list[-1]

    def push(self, item):
        self.stack_size += 1
        self.stack_list.append(item)

    def pop(self):
        self.stack_size -= 1
        self.stack_list.pop()

    def __str__(self):
        return str(self.stack_list)


s = Stack()
s.push(4)
s.push(5)
s.push(6)
print(s)
print(s.size())
s.pop()
print(s.size())
print(s)
