# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")

"""

ALO WIA QL
OLAAIWQL

step1:
create the list with three chars

"""
a = "ALOWIA"
li = []
val = []

def reverse(val):
    res = "".join(val)
    return res[::-1]

# def reverseAlternet(a):
if len(a) % 3 != 0:
    last = len(a) % 3

for i in range(len(a)):
    val.append(a[i])
    if len(val) == 3:
        li.append(reverse(val))
        val = []
while last != 0:
    li.append(a[-(last)])
    last -= 1

print("".join(li))
