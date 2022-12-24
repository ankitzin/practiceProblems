"""
Given an integer x, return true if x is a
palindrome
, and false otherwise.

"""


def palindrome(num:int):
    if num < 0:
        return False
    return num == int(str(num)[::-1])


print(palindrome(121    ))
