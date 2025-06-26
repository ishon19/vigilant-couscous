#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0

        for i in range(len(nums)):
            if i > furthest:
                return False 
            
            furthest = max(furthest, nums[i] + i)

            if furthest >= len(nums) - 1:
                return True
        return True
# @lc code=end

