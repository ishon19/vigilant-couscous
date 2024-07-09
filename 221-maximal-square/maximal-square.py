class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        res = 0
        
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0 for c in range(cols+1)] for r in range(rows+1)]
        
        # construct the dp table 
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "1":
                    dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1
                    res = max(res, dp[r+1][c+1])
        return res * res
