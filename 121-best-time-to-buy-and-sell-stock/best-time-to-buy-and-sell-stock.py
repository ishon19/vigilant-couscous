class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        profit = 0
        for i in range(len(prices)):
            min_so_far = min(min_so_far, prices[i])
            profit = max(profit, prices[i]-min_so_far)
        return profit

        """
            # brute force
            # res = float("-inf")
            # for i in range(len(prices)):
            #     for j in range(i+1, len(prices)):
            #         res = max(res, prices[j]-prices[i])
            # return res if res>0 else 0        
            # keep track of the min price encountered and the max profit so far
            # res = 0
            # minSoFar = float("inf")
            # for price in prices:
            #     if price < minSoFar:
            #         minSoFar = price
            #     elif price - minSoFar > res:
            #         res = price - minSoFar
            # return res
        """