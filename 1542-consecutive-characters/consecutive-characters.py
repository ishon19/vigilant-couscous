class Solution:
    def maxPower(self, s: str) -> int:
        stack = []
        res = 1

        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][-1] += 1
                res = max(res, stack[-1][-1])
            else:
                stack.append([c, 1])
        
        return res
