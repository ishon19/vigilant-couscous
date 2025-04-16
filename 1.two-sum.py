#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        seen = {}
        
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target-num], i]
            seen[num] = i

        return res
# @lc code=end

