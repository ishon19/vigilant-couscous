class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # memo = {}

        # def helper(index, remaining):
        #     if remaining == 0:
        #         return 1
        #     if remaining < 0 or index == len(coins):
        #         return 0
                
        #     if (index, remaining) in memo:
        #         return memo[(index, remaining)]
            
        #     memo[(index, remaining)] = helper(index, remaining - coins[index]) + helper(index + 1, remaining)
        #     return memo[(index, remaining)]
        
        # return helper(0, amount)
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

        for i in range(len(coins) + 1):
            dp[i][0] = 1

        for i in range(1, len(coins) + 1):
            for j in range(amount + 1):
                # exclude coin
                dp[i][j] = dp[i-1][j]
                if j >= coins[i-1]:
                    # include the coin
                    dp[i][j] += dp[i][j - coins[i-1]]
        
        return dp[len(coins)][amount]