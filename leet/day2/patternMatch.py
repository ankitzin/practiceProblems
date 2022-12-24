"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == p:
            return True