"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""
from functools import reduce
from typing import List


def lcp(str1, str2):
    i = 0
    while (i < len(str1) and i < len(str2)):
        if str1[i] == str2[i]:
            i = i + 1
        else:
            break
    return str1[:i]


def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ''
    else:
        return reduce(lcp, strs)

print(longestCommonPrefix(["cir","car","gcc"]))

