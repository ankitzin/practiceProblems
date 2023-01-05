import stackswork

s = stackswork.Stack()
string = "gninrael nidekil htiw tol a nrael"
reversed_string = ""

for i in string:
    s.push(i)

while not s.is_empty():
    reversed_string += s.peek()
    s.pop()

print(reversed_string)