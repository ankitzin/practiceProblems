name = int(input())                  # Reading input from STDIN

factorial = 1
number = int(name)
for val in range(1, number+1, 1):
    factorial = factorial * val

name = factorial
print('Hi, %s.' % name)         # Writing output to STDOUT
