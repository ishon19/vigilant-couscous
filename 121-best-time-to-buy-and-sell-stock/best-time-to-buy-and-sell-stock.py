class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_price = prices[0]

        for price in prices[1:]:
            if price < lowest_price:
                lowest_price = price
            else:
                max_profit = max(max_profit, price - lowest_price)
        
        return max_profit