from typing import List


class Solution:

    def common_string(self, str1, str2):
        i = 0
        j = 0
        result = ""
        while i < len(str1) and j < len(str2):
            if str1[i] != str2[j]:
                break

            result += str1[i]
            i += 1
            j += 1

        return result

    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        word = strs[0]

        for i in range(1, len(strs)):
            word = self.common_string(word, strs[i])

        return word


s = Solution()
arr = ["flower", "flow", "flight"]

print(s.longestCommonPrefix(arr))
