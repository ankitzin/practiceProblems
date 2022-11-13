from stack import Stack

string = "Ankit is King remember that"
s = Stack()


def reverse(word):
    reverse_str = ""
    for char in word:
        s.push(char)

    while not s.is_empty():
        reverse_str += str(s.peek())
        s.pop()

    return reverse_str


print(reverse(string))
