class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_val = float('inf')
        for i in range(len(prices)):
            if prices[i]<min_val:
                min_val = prices[i]
            elif prices[i] - min_val > ans:
                ans = prices[i] - min_val
        return ans
                
                