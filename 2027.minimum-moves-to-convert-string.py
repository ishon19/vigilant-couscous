#
# @lc app=leetcode id=2027 lang=python3
#
# [2027] Minimum Moves to Convert String
#

# @lc code=start
class Solution:
    def minimumMoves(self, s: str) -> int:
        if len(s) < 3:
            return 1
        
        start = 0
        res = 0

        for end in range(2, len(s)):
            if not all(ch == 'O' for ch in s[start:end+1]):
                
                res += 1
            start += 1
        
        return res
# @lc code=end

