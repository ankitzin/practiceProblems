import sys


class Solution:

    def convertor(self, ch):
        ch = ch.upper()
        con_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        if ch in con_dict.keys():
            return con_dict[ch]
        else:
            print('Please update the roman')
            sys.exit(1)

    def roman_to_int(self, s: str) -> int:
        symbol_to_value = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0
        i = 0
        while i < len(s):
            s1 = symbol_to_value[s[i]]
            if i+1 < len(s):
                s2 = symbol_to_value[s[i+1]]

                if s2 <= s1:
                    result = result + s1
                    i = i+1
                else:
                    result = result + s2 - s1
                    i = i+2
            else:
                result = result + s1
                i = i + 1

        return result


s = Solution()
print(s.roman_to_int("xxvi".upper()))
