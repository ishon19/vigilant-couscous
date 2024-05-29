class Solution:
    def numSteps(self, s: str) -> int:
        num = lambda x: int(x, 2)
        res = 0

        while not num(s) == 1:
            val = num(s)
            if val % 2 != 0:
                val += 1
            else:
                val //= 2
            s = format(val, 'b')
            res += 1
        
        return res