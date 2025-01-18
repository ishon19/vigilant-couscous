class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # base cases
        if not prices or k==0:
            return 0
        
        expenditure = [float("inf")] * k
        profit = [0] * k

        for price in prices:
            expenditure[0] = min(expenditure[0], price)
            profit[0] = max(profit[0], price - expenditure[0])

            for i in range(1, k):
                expenditure[i] = min(expenditure[i], price - profit[i-1])
                profit[i] = max(profit[i], price - expenditure[i])
        
        return profit[-1]
