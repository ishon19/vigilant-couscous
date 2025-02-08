#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0

        memo = {}

        def climb(step):
            if step in memo:
                return memo[step]
            if step <= 1:
                return 1
            memo[step] = climb(step-1) + climb(step-2)
            return memo[step]
       
        return climb(n)

# @lc code=end

