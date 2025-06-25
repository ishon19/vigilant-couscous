#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:        
        s = s.strip()

        last_num = 0
        cur_num = 0
        total = 0
        op = "+"

        for i, c in enumerate(s):
            
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)
            
            if i == len(s) - 1 or c in "+-*/":
                if op == "+":
                    total += last_num
                    last_num = cur_num
                elif op == "-":
                    total += last_num
                    last_num = -cur_num
                elif op == "*":
                    last_num = last_num * cur_num
                elif op == "/":
                    last_num = int(last_num / cur_num) if last_num >=0 else -(-last_num // cur_num)
                
                op = c
                cur_num = 0

        return total + last_num
# @lc code=end

