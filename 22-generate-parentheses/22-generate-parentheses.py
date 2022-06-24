class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        res = []
        
        def backtrack(opening, closing):
            if len(stack) == 2*n:
                res.append("".join(stack))
                return
            if opening < n:
                stack.append('(')
                backtrack(opening+1, closing)
                stack.pop()
                
            if closing < opening:
                stack.append(')')
                backtrack(opening, closing+1)
                stack.pop()
        
        backtrack(0, 0)
        return res