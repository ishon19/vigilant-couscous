#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        i = 0
        sign = 1
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31 

        while i < len(s) and s[i] == ' ':
            i += 1
        
        if i == len(s):
            return 0
        
        if s[i] in ['+', '-']:
            if s[i] == '-':
                sign = -1
            i += 1
        
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
        
        res = res * sign
        return min(INT_MAX, max(res, INT_MIN))

# @lc code=end

