#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        for i, c in enumerate(s):
            if c in ['(', ')']:
                if not stack:
                    stack.append((i, c))
                else:
                    if stack[-1][-1] == '(' and c ==')':
                        stack.pop()
                    else:
                        stack.append((i, c))
        
        res = ''
        indices = set([i for i,c in stack])
        for i, c in enumerate(s):
            if i in indices:
                continue
            res += c

        return res
        
# @lc code=end

