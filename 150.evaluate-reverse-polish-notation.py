#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
from math import trunc

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+', '-', '*', '/']

        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                if stack and len(stack) >= 2:
                    res = 0
                    if token == '+':
                        res += stack[-2] + stack[-1]
                    elif token == '-':
                        res += stack[-2] - stack[-1]
                    elif token == '*':
                        res += stack[-2] * stack[-1]
                    else:
                        res += trunc(stack[-2] / stack[-1])
                    
                    stack.pop()
                    stack.pop()
                    stack.append(res)

        return stack[0]
# @lc code=end

