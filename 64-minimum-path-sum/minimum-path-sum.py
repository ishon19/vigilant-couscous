class Solution:
    def minPathSum(self, grid):
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        dp = [[0] * cols for _ in range(rows)]
        
        # Initialize the first cell
        dp[0][0] = grid[0][0]
        
        # Initialize the first row and first column
        for i in range(1, rows):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, cols):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        # Fill the DP table
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[-1][-1]

