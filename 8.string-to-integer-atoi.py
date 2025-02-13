#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s: return 0

        i = 0
        sign = 1
        res = 0

        if s[i] in ['-', '+']:
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        while i < len(s) and s[i].isdigit():
            res += res * 10 + int(s[i])
            i += 1
        
        res = sign * res
        res = max(min(res, 2 ** 31 -1), -2**31)

        return res
# @lc code=end

