class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        res = []
        
        def backtrack(opening, closing):
            if opening == closing == n:
                res.append("".join(stack))
                return
            if opening < n:
                stack.append('(')
                backtrack(opening+1, closing)
                stack.pop() # this is the backtrack
                
            if closing < opening:
                stack.append(')')
                backtrack(opening, closing+1)
                stack.pop() # this is the backtrack
        
        backtrack(0, 0)
        return res