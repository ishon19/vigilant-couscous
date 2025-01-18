class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        # first step remove the whitespaces
        i = 0
        res = 0
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31 
        sign = 1

        while i < len(s) and s[i] == ' ':
            i += 1
        
        # find the sign
        if i<len(s) and s[i] in ['+', '-']:
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        # now construct the number
        while i < len(s):
            if s[i].isdigit():
                res = res * 10 + int(s[i])
            else:
                break
            i += 1
        
        res = -res if sign == -1 else res

        if res > INT_MAX:
            return INT_MAX
        elif res < INT_MIN:
            return INT_MIN

        return res