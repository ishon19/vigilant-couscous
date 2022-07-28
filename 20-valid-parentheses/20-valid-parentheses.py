class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        stack = []
        opening = ['(','[','{']
        closing = [')',']','}']
        
        for i, c in enumerate(s):
            if c in opening:
                stack.append(c)
            else:
                if not len(stack): return False
                if c == ']' and stack.pop() != '[': return False
                if c == '}' and stack.pop() != '{': return False
                if c == ')' and stack.pop() != '(': return False
        
        return len(stack) == 0
                    
        
                    