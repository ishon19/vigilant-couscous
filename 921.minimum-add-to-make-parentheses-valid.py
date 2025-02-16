#
# @lc app=leetcode id=921 lang=python3
#
# [921] Minimum Add to Make Parentheses Valid
#

# @lc code=start
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        need = 0

        for c in s:
            if c == '(':
                balance += 1
            else:
                if balance > 0:
                    balance -= 1
                else:
                    need += 1
        
        return balance + need
# @lc code=end

