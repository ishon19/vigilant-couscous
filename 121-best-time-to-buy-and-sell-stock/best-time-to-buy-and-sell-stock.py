class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_seen = float("inf")
        max_profit = 0

        for price in prices:
            min_seen = min(min_seen, price)
            max_profit = max(max_profit, price - min_seen)
        
        return max_profit