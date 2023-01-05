class Stack():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, val):
        return self.items.append(val)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


if __name__ == '__main__':
    s = Stack()
    s.is_empty()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s)
    s.pop()
    s.pop()
    print(s)