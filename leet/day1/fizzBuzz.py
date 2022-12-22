"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

"""


def fizzbuzzs(n):
    lists = [i for i in range(1,n,1)]
    for i in range(0, len(lists),1):

        if lists[i] % 3 == 0 and lists[i] % 5 == 0:
            lists[i] = 'FizzBuzz'
        elif lists[i] % 3 == 0:
            lists[i] = 'Fizz'
        elif lists[i] % 5 == 0:
            lists[i] = 'Buzz'
        else:
            lists[i] = lists[i]

    return lists

n = 20
print(fizzbuzzs(n))