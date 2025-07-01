#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        sign = 1
        i = 0

        while i < len(s) and s[i] == ' ':
            i += 1

        if i == len(s):
            return 0
        
        if s[i] in ['-', '+']:
            sign = -1 if s[i] == "-" else 1
            i += 1

        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
        
        res *= sign

        return min(max(res, -2**31), (2 ** 31) -1)
# @lc code=end

