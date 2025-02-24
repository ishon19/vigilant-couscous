#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for char in s:
            if char in bracketMap:
                if not stack or stack[-1] != bracketMap[char]:
                    return False
                stack.pop() 
            else:
                stack.append(char)
        
        return len(stack) == 0
# @lc code=end

