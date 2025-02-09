#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_so_far = float("inf")

        for price in prices:
            min_so_far = min(min_so_far, price)
            res = max(res, price - min_so_far)
        
        return res
# @lc code=end

