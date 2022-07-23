class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFar = float("inf")
        maxProfit = 0
        
        for i in range(len(prices)):
            minSoFar = min(minSoFar, prices[i])
            maxProfit = max(maxProfit, prices[i] - minSoFar)
        
        return max(maxProfit, 0)