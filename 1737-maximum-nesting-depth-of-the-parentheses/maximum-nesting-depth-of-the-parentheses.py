class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        res = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
            res = max(res, count)

        return res