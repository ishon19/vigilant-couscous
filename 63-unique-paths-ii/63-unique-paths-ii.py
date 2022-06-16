class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r,c = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(c+1)] for j in range(r+1)]            
        dp[0][1] = 1
        for i in range(1, r+1):
            for j in range(1, c+1):                
                if not obstacleGrid[i-1][j-1]:
                    waysUp = dp[i-1][j]
                    waysLeft = dp[i][j-1]
                    dp[i][j] = waysUp + waysLeft          
        return dp[-1][-1]