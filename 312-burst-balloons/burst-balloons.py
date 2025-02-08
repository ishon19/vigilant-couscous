class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # we know for sure that when we burst the lone balloon
        # the neighbors are gonna be 1, 1 both sides - that's our
        # base case
        padded = [1] + nums + [1]
        n = len(padded)

        dp = [[0] * n for _ in range(n)]

        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + padded[i] * padded[k] * padded[j])
        
        return dp[0][n-1]