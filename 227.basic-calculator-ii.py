#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:        
        if not s:
            return 0

        stack = []
        cur_num = 0
        op = '+'

        for i, c in enumerate(s):
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)
            
            if (c != ' ' and not c.isdigit()) or i == len(s) - 1:
                if op == '+':
                    stack.append(cur_num)
                elif op == '-':
                    stack.append(-cur_num)
                elif op == '*':
                    stack.append(stack.pop() * cur_num)
                elif op == '/':
                    stack.append(int(stack.pop() / cur_num))
                
                cur_num = 0
                op = c

        return sum(stack)
# @lc code=end

