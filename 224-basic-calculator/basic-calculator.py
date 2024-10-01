class Solution:
    def calculate(self, s: str) -> int:
        # stack for managing parentheses
        stack = []
        res = 0
        sign = 1
        i = 0

        while i < len(s):
            # while we see number keep on calculating
            if s[i].isdigit():
                num = 0
                while i<len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                res += sign * num
                i-=1 # since it got incremented more
            elif s[i] == '+' or s[i] == '-':
                sign = 1 if s[i] == '+' else -1
            elif s[i] == '(':
                # prepare to calculate again
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif s[i] == ')':
                last_sign = stack.pop()
                last_res = stack.pop()
                res = last_res + res * last_sign
            
            i += 1
        
        return res
