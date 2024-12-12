class Solution:
    def isValid(self, s: str) -> bool:
        # check if it is valid parentheses
        stack = []

        for c in s:
            if stack:
                if c == ')' and stack[-1] == '(':
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)  
    
        return len(stack) == 0