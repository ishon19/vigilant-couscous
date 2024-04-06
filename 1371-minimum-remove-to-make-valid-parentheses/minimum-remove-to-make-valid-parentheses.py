class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        
        for i, c in enumerate(s):
            if c in ['(',')']:
                if not stack:
                    stack.append((c, i))
                else:
                    if stack[-1][0] == '(' and c == ')':
                        stack.pop()
                    else:
                        stack.append((c, i))
        
        res = ''
        idx = [i for c, i in stack]

        for i, c in enumerate(s):
            if i in idx:
                continue
            res += c

        return res