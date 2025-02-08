class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        for i, c in enumerate(s):
            if c in ['(', ')']:
                if stack and stack[-1][0] == '(' and c == ')':
                    stack.pop()
                else:
                    stack.append((c, i))
        
        res = ''
        skip = [i for _, i in stack]
        for i, c in enumerate(s):
            if i in skip:
                continue
            res += c
        
        return res
            