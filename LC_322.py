class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # define the dp array
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        coins.sort()
        
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], 1 + dp[i-coin])
        return dp[amount] if dp[amount]!=amount+1 else -1