class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        curr_num = 0
        prev_num = 0
        op = '+'

        for i in range(len(s)):
            if s[i].isdigit():
                curr_num = curr_num * 10 + int(s[i])
            
            if i == len(s)-1 or s[i] in "+-/*":
                if op == '+':
                    res += prev_num
                    prev_num = curr_num
                elif op == '-':
                    res += prev_num
                    prev_num = -curr_num
                elif op == "*":
                    prev_num *= curr_num
                elif op == "/":
                    prev_num = int(prev_num / curr_num)
            
                curr_num = 0
                op = s[i]
        
        res += prev_num
        return res