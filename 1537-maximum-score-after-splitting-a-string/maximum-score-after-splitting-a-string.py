class Solution:
    def maxScore(self, s: str) -> int:
        ones = zeros = 0
        res = -inf

        for i in range(len(s)-1):
            if s[i] == '1':
                ones += 1
            else:
                zeros += 1
            
            res = max(res, zeros - ones)
        
        if s[-1] == '1':
            ones += 1
        
        return res + ones