class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def dfs(idx, opening, closing):
            if idx == 2*n:
                res.append(''.join(path))
                return
            
            if opening!=n:
                path.append('(')
                dfs(idx+1, opening + 1, closing)
                path.pop()
            
            if closing < opening:
                path.append(')')
                dfs(idx+1, opening, closing+1)
                path.pop()
        
        dfs(0, 0, 0)
        return res