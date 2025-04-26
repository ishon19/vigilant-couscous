class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(path, opening, closing):
            if len(path) == 2 * n:
                res.append(path)
                return 
            
            if opening < n:
                dfs(path + '(', opening + 1, closing)
            
            if closing < opening:
                dfs(path + ')', opening, closing + 1)

        dfs("", 0, 0)
        return res