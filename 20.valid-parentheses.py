#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketPairs = {'(': ')', '{': '}', '[': ']'}
        
        for char in s:
            if stack:
                if stack[-1] in bracketPairs.keys() and char == bracketPairs[stack[-1]]:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        
        return len(stack) == 0
# @lc code=end

