#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def minCost(i):
            if i in memo:
                return memo[i]
            if i in [0, 1]:
                return cost[i]
            memo[i] = cost[i] + min(minCost(i-1), minCost(i-2))
            return memo[i]

        
            
# @lc code=end

