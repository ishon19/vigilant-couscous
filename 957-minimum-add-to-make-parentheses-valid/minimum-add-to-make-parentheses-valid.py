class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for c in s:
            if not stack:
                stack.append(c)
            else:
                if c == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(c)
        
        return len(stack)