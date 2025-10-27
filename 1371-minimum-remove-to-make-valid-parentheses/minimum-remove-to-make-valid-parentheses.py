class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for idx, c in enumerate(s):
            if c in ['(', ')']:
                if stack:
                    if c == ')' and stack[-1][0] == '(':
                        stack.pop()
                    else:
                        stack.append((c, idx))
                else:
                    stack.append((c, idx))
        
        skipIdx = [idx for _, idx in stack]
        res = ''
        for idx, c in enumerate(s):
            if idx not in skipIdx:
                res += c
        return res
                