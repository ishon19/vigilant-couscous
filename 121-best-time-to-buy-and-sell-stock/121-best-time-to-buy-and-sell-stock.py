class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = float("inf")
        profit = 0
        
        for i in range(len(prices)):
            if prices[i]<smallest: smallest = prices[i]
            else: profit = max(profit, prices[i] - smallest)
        
        return profit