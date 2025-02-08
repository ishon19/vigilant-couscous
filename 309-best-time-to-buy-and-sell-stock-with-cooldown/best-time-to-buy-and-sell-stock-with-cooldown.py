class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def helper(day, holding):
            if day >= len(prices):
                return 0
            
            if (day, holding) in memo:
                return memo[(day, holding)]
            
            if holding:
                # sell or hold
                memo[(day, holding)] = max(helper(day+2, False) + prices[day], helper(day+1, True))
            else:
                # buy or cooldown
                memo[(day, holding)] = max(helper(day+1, True) - prices[day], helper(day+1, False))
            
            return memo[(day, holding)]
        
        return helper(0, False)