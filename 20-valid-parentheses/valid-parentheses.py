class Solution:
    def isValid(self, s: str) -> bool:
        # stack based approach should work for this problem
        stack = []

        for c in s:
            if not stack:
                stack.append(c)
            else:
                if stack[-1] == '(' and c == ')':
                    stack.pop()
                elif stack[-1] == '{' and c == '}':
                    stack.pop()
                elif stack[-1] == '[' and c == ']':
                    stack.pop()
                else:
                    stack.append(c)
        
        return not stack